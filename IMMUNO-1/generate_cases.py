"""
IMMUNO-1/generate_cases.py
===========================
Generador de casos sintéticos SVperitus–IMMUNO-1 (n=25).

Usa el motor normativo (normative_engine.py) para etiquetar vectores.
La generación es por muestreo aleatorio + rechazo: genera campos clínicos
aleatorios hasta obtener la clase deseada.

ADVERTENCIA: dataset SINTÉTICO. Motor normativo v0.1.
Requiere validación clínica antes de cualquier uso en producción.

Autor: Juan Antonio Lloret Egea  |  ORCID: 0000-0002-6634-3351
ISSN 2695-641X  |  CC BY-NC-ND 4.0
"""

import sys
import random
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.io_utils import load_config, save_vectors_csv, ensure_dir
import normative_engine as engine

CONFIG_PATH = Path(__file__).parent / "config" / "imm_n25.yaml"
DATA_DIR    = Path(__file__).parent / "data"

PARAM_IDS = engine.PARAM_IDS
CLASSES   = list(engine.CLASSES)


def _random_case(rng: random.Random) -> dict:
    """
    Genera un diccionario de campos clínicos con valores aleatorios.
    Rangos clínicamente plausibles que cubren todo el espacio para
    garantizar diversidad en las tres clases.
    """
    def rbool():
        return rng.choice([True, False, None])

    def rfloat(lo, hi, none_prob=0.15):
        return None if rng.random() < none_prob else rng.uniform(lo, hi)

    def rint(lo, hi, none_prob=0.15):
        return None if rng.random() < none_prob else rng.randint(lo, hi)

    def rchoice(options, none_prob=0.15):
        return None if rng.random() < none_prob else rng.choice(options)

    return {
        # P01
        "anc_actual":                          rfloat(50, 2500),
        "anc_expected_nadir":                  rfloat(50, 2000),
        "neutropenia_duration_days_expected":  rint(0, 30),
        # P02
        "cd4_count":                           rfloat(50, 1200, none_prob=0.3),
        "lymphocyte_total":                    rfloat(100, 3000),
        "t_cell_depleting_therapy_12m":        rbool(),
        # P03
        "igg_mgdl":                            rfloat(100, 1400),
        "bacterial_infections_severe_12m":     rint(0, 5),
        # P04
        "anatomic_asplenia":                   rbool(),
        "functional_hyposplenism":             rbool(),
        "encapsulated_vaccines_complete":      rbool(),
        "asplenia_prophylaxis":                rbool(),
        # P05
        "mucositis_grade":                     rchoice([0, 1, 2, 3, 4]),
        "skin_ulcers_relevant":                rbool(),
        "cvc_present":                         rbool(),
        "cvc_complications":                   rbool(),
        # P06
        "hematology_phase":                    rchoice(
            ["induction", "consolidation", "relapse_high_risk",
             "maintenance", "chronic_stable"]
        ),
        # P07
        "chemo_intensity":                     rchoice(["high", "standard", "low"]),
        "days_since_last_chemo":               rint(0, 365),
        # P08
        "anti_cd20_12m":                       rbool(),
        "btk_inhibitor_12m":                   rbool(),
        "pi3k_inhibitor_12m":                  rbool(),
        "viral_screening_documented":          rbool(),
        # P09
        "hsct_allogeneic_years_ago":           rfloat(0.1, 5.0, none_prob=0.55),
        "hsct_autologous_years_ago":           rfloat(0.5, 6.0, none_prob=0.55),
        "cart_years_ago":                      rfloat(0.1, 3.0, none_prob=0.70),
        "gvhd_moderate_severe_active":         rbool(),
        "prophylaxis_revaccination_program":   rbool(),
        # P10
        "prednisone_equivalent_mgday":         rfloat(0, 60),
        "corticosteroid_duration_weeks":       rint(0, 26),
        "pjp_risk_assessed":                   rbool(),
        # P11
        "serious_bacterial_infections_12m":    rint(0, 4),
        "prophylaxis_plan_reviewed":           rbool(),
        # P12 / P23 (campos compartidos)
        "invasive_fungal_infection_history":   rbool(),
        "ifi_high_risk_context":               rbool(),
        "antifungal_prophylaxis_adequate":     rbool(),
        # P13
        "chronic_viral_infection_active":      rbool(),
        "hbv_carrier":                         rbool(),
        "viral_prophylaxis_monitoring_ok":     rbool(),
        # P14
        "mdr_colonization_known":              rbool(),
        "mdr_management_strategy":             rbool(),
        # P15
        "prolonged_hospitalization_recent":    rbool(),
        "icu_admission_recent":                rbool(),
        "prophylactic_plan_adjusted":          rbool(),
        # P16
        "flu_vaccine_current_season":          rbool(),
        "flu_vaccine_contraindicated":         rbool(),
        # P17
        "pneumococcal_sequence_complete":      rbool(),
        # P18
        "sars_cov2_boosters_current":          rbool(),
        "high_risk_hematologic_patient":       rbool(),
        # P19
        "hbv_vaccine_series_complete":         rbool(),
        "anti_hbs_protective":                 rbool(),
        "hbv_revaccinated_nonresponder":       rbool(),
        # P20
        "vaccine_calendar_adequate":           rbool(),
        "live_vaccine_contraindicated_given":  rng.choice([False, False, False, True, None]),
        # P21
        "pjp_prophylaxis_criteria_met":        rbool(),
        "pjp_prophylaxis_active":              rbool(),
        # P22
        "antiviral_prophylaxis_indicated":     rbool(),
        "antiviral_prophylaxis_active":        rbool(),
        "cmv_monitoring_active":               rbool(),
        # P24
        "high_risk_prolonged_neutropenia":     rbool(),
        "antibacterial_prophylaxis_policy_documented": rbool(),
        # P25
        "risk_reassessment_plan_explicit":     rbool(),
        "reassessment_periodicity_defined":    rbool(),
        "reassessment_includes_vaccines":      rbool(),
    }


def generate_synthetic_dataset(
    n_per_class: int = 1000,
    seed: int = 42,
    output_csv: Path = None,
    max_attempts_per_sample: int = 200_000,
) -> Tuple[List[List[str]], List[str]]:
    """
    Genera n_per_class vectores ternarios por clase (muestreo por rechazo).
    """
    rng = random.Random(seed)
    vectors = []
    labels  = []

    for cls in CLASSES:
        found    = 0
        attempts = 0
        print(f"  Generando {n_per_class} vectores clase {cls}…", flush=True)

        while found < n_per_class:
            attempts += 1
            if attempts > max_attempts_per_sample * n_per_class:
                raise RuntimeError(
                    f"Superado el límite de intentos para clase {cls}."
                )
            case = _random_case(rng)
            vector, global_class = engine.evaluate_and_classify(case)
            if global_class == cls:
                vectors.append(vector)
                labels.append(cls)
                found += 1

        print(f"    ✓ {cls}: {n_per_class} vectores ({attempts} intentos)")

    if output_csv is not None:
        save_vectors_csv(vectors, labels, output_csv, PARAM_IDS)
        print(f"  CSV guardado: {output_csv}")

    return vectors, labels


def split_dataset(
    vectors, labels,
    train_ratio=0.70, val_ratio=0.15, seed=42,
):
    rng = random.Random(seed)
    by_class = defaultdict(list)
    for i, lbl in enumerate(labels):
        by_class[lbl].append(i)

    splits = {"train": ([], []), "val": ([], []), "test": ([], [])}

    for cls, indices in by_class.items():
        rng.shuffle(indices)
        n_total = len(indices)
        n_train = int(n_total * train_ratio)
        n_val   = int(n_total * val_ratio)

        for split_name, idx_slice in [
            ("train", indices[:n_train]),
            ("val",   indices[n_train:n_train + n_val]),
            ("test",  indices[n_train + n_val:]),
        ]:
            for idx in idx_slice:
                splits[split_name][0].append(vectors[idx])
                splits[split_name][1].append(labels[idx])

    return splits


def main():
    parser = argparse.ArgumentParser(
        description="SVperitus IMMUNO-1 — Generador de casos sintéticos"
    )
    parser.add_argument("--n-per-class", type=int, default=1000)
    parser.add_argument("--seed",        type=int, default=42)
    parser.add_argument(
        "--output-dir", type=Path,
        default=Path(__file__).parent / "data" / "vectors",
    )
    args = parser.parse_args()

    cfg = load_config(CONFIG_PATH)
    print(f"\nSVperitus – IMMUNO-1  |  n={cfg['n']}  |  T(n)={cfg['threshold']}")
    print(f"Motor normativo v0.1  |  seed={args.seed}\n")

    ensure_dir(args.output_dir)
    vectors, labels = generate_synthetic_dataset(
        n_per_class=args.n_per_class,
        seed=args.seed,
        output_csv=args.output_dir / "all_vectors.csv",
    )

    splits = split_dataset(vectors, labels, seed=args.seed)
    for split_name, (vecs, lbls) in splits.items():
        csv_path = args.output_dir / f"{split_name}_vectors.csv"
        save_vectors_csv(vecs, lbls, csv_path, PARAM_IDS)
        counts = {c: lbls.count(c) for c in CLASSES}
        print(f"  {split_name}: {len(lbls)} vectores — {counts}")

    print(f"\n✓ Total: {len(vectors)} vectores generados.")
    print("⚠ Dataset SINTÉTICO — requiere validación clínica.")


if __name__ == "__main__":
    main()
