//! Cálculo auxiliar de una adjudicación humana. No evalúa medicina ni sustituye el núcleo SV.
use std::{env, fs, io, path::Path};

#[derive(Debug)]
struct Item { id: String, valor: char, fundamento: String, evidencia: String }
fn critica(i: usize) -> bool { (i + 1) % 5 != 0 }
fn leer(s: &str) -> Result<Vec<Item>, String> {
    let mut lineas = s.lines();
    if lineas.next() != Some("pregunta\tintegridad\tvalor\tfundamento\tevidencia") {
        return Err("Cabecera incorrecta".into());
    }
    let mut items = Vec::new();
    for (i, linea) in lineas.enumerate() {
        let c: Vec<_> = linea.split('\t').collect();
        if c.len() != 5 || c[0] != format!("P{:02}", i+1) || c[1] != "valida" {
            return Err(format!("Fila {} inválida: orden, columnas o integridad", i+1));
        }
        let valor = match c[2] { "0" => '0', "1" => '1', "U" => 'U', _ => return Err("Valor ajeno a la terna".into()) };
        if c[3].trim().is_empty() || c[4].trim().is_empty() { return Err("Falta fundamento o evidencia".into()); }
        items.push(Item{id:c[0].into(), valor, fundamento:c[3].into(), evidencia:c[4].into()});
    }
    if items.len() != 25 { return Err("Se exigen exactamente 25 adjudicaciones válidas".into()); }
    Ok(items)
}
fn calcular(v: &[Item]) -> ([usize;3], &'static str, &'static str) {
    let mut n = [0;3];
    for p in v { n[match p.valor {'0'=>0,'1'=>1,_=>2}] += 1; }
    let k = if n[1]>=19 {"NO_APTO"} else if n[0]>=19 {"APTO"} else {"INDETERMINADO"};
    let a = if v.iter().enumerate().any(|(i,p)|critica(i)&&p.valor=='1') {"NO_APTO"}
        else if v.iter().enumerate().any(|(i,p)|critica(i)&&p.valor=='U') {"U"}
        else if k=="APTO" {"APTO"} else {"U"};
    (n,k,a)
}
fn radio(c:char)->f64 { match c {'0'=>1.,'1'=>2.,_=>3.} }
fn punto(i:usize,c:char)->(f64,f64) {
    let t=std::f64::consts::TAU*i as f64/25.; (radio(c)*t.cos(),radio(c)*t.sin())
}
fn json(s:&str)->String {
    let mut o=String::from("\"");
    for c in s.chars() {match c {'"'=>o.push_str("\\\""),'\\'=>o.push_str("\\\\"),'\n'=>o.push_str("\\n"),'\r'=>o.push_str("\\r"),'\t'=>o.push_str("\\t"),c if c<' '=>o.push_str(&format!("\\u{:04x}",c as u32)),_=>o.push(c)}}
    o.push('"');o
}
fn resultados(v:&[Item], ejecucion_ref:&str)->(String,String) {
    let (n,k,a)=calcular(v);
    let mut f=format!("{{\n  \"instrumento\":\"EVAL-PDQ-HCL-25-20260929/r1\",\n  \"naturaleza\":\"calculo_auxiliar_sobre_adjudicacion_humana\",\n  \"corpus_sha256\":\"94024658204c0607c5879f8cf263d6238d639494b5d9c266396c20f3e848a45d\",\n  \"n\":25,\"b\":5,\"umbral\":19,\"N0\":{},\"N1\":{},\"NU\":{},\n  \"kappa\":\"{}\",\"dictamen_final\":\"{}\",\n  \"posiciones\":[\n",n[0],n[1],n[2],k,a);
    let mut svg=String::from("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 800 850\"><rect width=\"800\" height=\"850\" fill=\"white\"/><g font-family=\"sans-serif\" fill=\"#162b3d\"><text x=\"30\" y=\"32\" font-size=\"20\">EVAL-PDQ-HCL-25 · representación auxiliar</text><text x=\"30\" y=\"59\">Radios: 0 = 1; 1 = 2; U = 3. Orden P01–P25.</text>");
    for r in [90,180,270] {svg.push_str(&format!("<circle cx=\"400\" cy=\"420\" r=\"{r}\" fill=\"none\" stroke=\"#cad3da\"/>"));}
    let coords:Vec<_>=v.iter().enumerate().map(|(i,p)|punto(i,p.valor)).collect();
    let puntos=coords.iter().map(|(x,y)|format!("{:.4},{:.4}",400.+90.*x,420.-90.*y)).collect::<Vec<_>>().join(" ");
    svg.push_str(&format!("<polygon points=\"{puntos}\" fill=\"#39749d\" fill-opacity=\"0.12\" stroke=\"#285f85\" stroke-width=\"2\"/>"));
    for (i,p) in v.iter().enumerate() {
        let (x,y)=coords[i];let (lx,ly)=punto(i,'U');
        f.push_str(&format!("    {{\"id\":{},\"critica\":{},\"valor\":{},\"x\":{:.12},\"y\":{:.12},\"fundamento\":{},\"evidencia\":{}}}{}\n",json(&p.id),critica(i),json(&p.valor.to_string()),x,y,json(&p.fundamento),json(&p.evidencia),if i==24{""}else{","}));
        let color=match p.valor {'0'=>"#18734b",'1'=>"#ae2525",_=>"#a46300"};
        svg.push_str(&format!("<circle cx=\"{:.4}\" cy=\"{:.4}\" r=\"4\" fill=\"{color}\"/><text x=\"{:.4}\" y=\"{:.4}\" text-anchor=\"middle\" font-size=\"12\">{}:{}{}</text>",400.+90.*x,420.-90.*y,400.+105.*lx,424.-105.*ly,p.id,p.valor,if critica(i){"*"}else{""}));
    }
    f.push_str(&format!("  ],\n  \"ejecucion_ref\":{}\n}}\n",json(ejecucion_ref)));
    let dictamen = match a {"APTO"=>"Apto","NO_APTO"=>"No apto",_=>"U (indeterminación honesta)"};
    svg.push_str(&format!("<text x=\"30\" y=\"790\">κ = {k}; dictamen = {dictamen}. * Posición crítica.</text><text x=\"30\" y=\"818\">Resultado limitado al instrumento; no acredita aptitud clínica.</text></g></svg>\n"));
    (f,svg)
}
fn main()->io::Result<()> {
    let a:Vec<_>=env::args().skip(1).collect();
    if a.len()!=3 || a[2].trim().is_empty() {return Err(io::Error::other("Uso: evaluar adjudicaciones.tsv directorio_nuevo referencia_ejecucion"));}
    if fs::metadata(&a[0])?.len()>2_000_000 {return Err(io::Error::other("Entrada excesiva"));}
    let v=leer(&fs::read_to_string(&a[0])?).map_err(io::Error::other)?;
    let (f,s)=resultados(&v,&a[2]);let out=Path::new(&a[1]);
    fs::create_dir(out)?;
    fs::write(out.join("frame.json"),f)?;fs::write(out.join("poligono.svg"),s)?;
    println!("Resultado auxiliar escrito; requiere cotejo receptor con la evidencia original.");Ok(())
}
#[cfg(test)] mod pruebas {
    use super::*;
    fn entrada(v:&[char;25])->String {let mut s="pregunta\tintegridad\tvalor\tfundamento\tevidencia\n".to_owned();for(i,c)in v.iter().enumerate(){s+=&format!("P{:02}\tvalida\t{}\tCaso sintético de comprobación\tprueba-sintetica-{}\n",i+1,c,i+1)}s}
    #[test] fn critico_error_aunque_mayoria_favorable(){let mut a=['0';25];a[0]='1';assert_eq!(calcular(&leer(&entrada(&a)).unwrap()),([24,1,0],"APTO","NO_APTO"));}
    #[test] fn critico_u_no_se_convierte_en_error(){let mut a=['0';25];a[0]='U';assert_eq!(calcular(&leer(&entrada(&a)).unwrap()),([24,0,1],"APTO","U"));}
    #[test] fn cinco_no_criticos_erroneos(){let mut a=['0';25];for i in [4,9,14,19,24]{a[i]='1'}assert_eq!(calcular(&leer(&entrada(&a)).unwrap()),([20,5,0],"APTO","APTO"));}
    #[test] fn frontera_19_y_18(){let mut a=['1';25];a[..19].fill('0');assert_eq!(calcular(&leer(&entrada(&a)).unwrap()).1,"APTO");a[18]='U';assert_eq!(calcular(&leer(&entrada(&a)).unwrap()).1,"INDETERMINADO");}
    #[test] fn error_tecnico_no_es_u(){let s=entrada(&['U';25]).replacen("valida","fallo_tecnico",1);assert!(leer(&s).is_err());}
    #[test] fn dimension_y_orden(){let s=entrada(&['0';25]);assert!(leer(&s.replacen("P01","P02",1)).is_err());assert!(leer(&s.lines().take(25).collect::<Vec<_>>().join("\n")).is_err());assert!(leer(&(s+"\n")).is_err());}
    #[test] fn falta_evidencia(){let s=entrada(&['0';25]).replace("prueba-sintetica-1\n","\n");assert!(leer(&s).is_err());}
    #[test] fn radios_y_vertices(){assert_eq!(punto(0,'0'),(1.,0.));assert_eq!(punto(0,'1'),(2.,0.));assert_eq!(punto(0,'U'),(3.,0.));let(f,s)=resultados(&leer(&entrada(&['0';25])).unwrap(),"SINTETICO-NO-INFERENCIA");assert_eq!(f.matches("\"id\":").count(),25);assert!(f.contains("SINTETICO-NO-INFERENCIA"));assert_eq!(s.matches("<polygon ").count(),1);assert_eq!(s.matches("* Posición crítica").count(),1);}
    #[test] fn escapar_datos(){assert_eq!(json("a\"\\\n"),"\"a\\\"\\\\\\n\"");}
}
