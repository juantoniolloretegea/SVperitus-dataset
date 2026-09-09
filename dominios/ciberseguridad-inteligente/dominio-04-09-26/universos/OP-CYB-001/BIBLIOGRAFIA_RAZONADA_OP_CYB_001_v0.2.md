# Bibliografía razonada del primer universo y de la estimación del dominio

**Versión 0.2. Referencias y versiones consultadas hasta el 9 de septiembre de 2026.**

Se distinguen fuentes profesionales, documentación de implementación, estudios empíricos, guías educativas y documentos rectores del proyecto. Los originales anteriores conservan su identidad; las doce incorporaciones B01–B12 quedan identificadas por URL, tamaño y huella en el anexo. Las guías R001–R040 sostienen el catálogo curricular y el mapa de operaciones, no todas las proposiciones técnicas del primer universo. Las fuentes no afirman la atomicidad SV: esa adjudicación pertenece a este trabajo.

## T001

Souppaya, M.; Scarfone, K. (2022, abril). *Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology. NIST SP 800-40r4*. [Documento original](https://doi.org/10.6028/NIST.SP.800-40r4).

**Localización utilizada:** §§2.2–2.3, pp. 4–7; §§3.1–3.5.

**Función y límite:** Fundamento profesional del ciclo de actualización, de la verificación del efecto y del balance de recursos.

## F018

Scarfone, K.; Souppaya, M.; Cody, A.; Orebaugh, A. (2008, septiembre). *Technical Guide to Information Security Testing and Assessment. NIST SP 800-115*. [Documento original](https://doi.org/10.6028/NIST.SP.800-115).

**Localización utilizada:** §§3.4–3.6, 4.3, 6.5, 7.3–7.4.

**Función y límite:** Alcance y límites de las pruebas, resultados falsos y tratamiento de evidencia.

## B01

Johnson, A.; Dempsey, K.; Ross, R.; Gupta, S.; Bailey, D. (2011; actualización editorial de 10-10-2019). *Guide for Security-Focused Configuration Management of Information Systems. NIST SP 800-128*. [Documento original](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf).

**Localización utilizada:** §§3.2–3.4, pp. 30–44; apéndices E e I.

**Función y límite:** Configuración, efectos funcionales y de seguridad, autorización y cierre del cambio. La actualización de 2019 no introduce cambios técnicos.

## B02

Regenscheid, A. (2018, mayo). *Platform Firmware Resiliency Guidelines. NIST SP 800-193*. [Documento original](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-193.pdf).

**Localización utilizada:** §§3–4.

**Función y límite:** Contraste de plataforma y firmware. No acredita un método universal de medición del firmware activo.

## B03

Moran, B.; Tschofenig, H.; Birkholz, H. (2022, enero). *A Manifest Information Model for Firmware Updates in Internet of Things (IoT) Devices. RFC 9124*. [Documento original](https://www.rfc-editor.org/rfc/rfc9124.txt).

**Localización utilizada:** §§3.2–3.15, 3.19, 3.21, 3.25; §4.

**Función y límite:** Contraste informativo de identidad, autenticidad, precursor, selección y dependencias. No es una norma universal para todo activo IT.

## B04

The Linux Kernel development community (Linux 6.8.0). *Livepatch*. [Documento original](https://www.kernel.org/doc/html/v6.8/livepatch/livepatch.html).

**Localización utilizada:** §3, Consistency model; §§5.2–5.5.

**Función y límite:** Habilitación y transición por tarea, con semántica explícita del estado -1 y límites del mecanismo.

## B05

The Linux Kernel development community (Linux 6.8.0). *System State Changes*. [Documento original](https://www.kernel.org/doc/html/v6.8/livepatch/system-state.html).

**Localización utilizada:** §§1–4.

**Función y límite:** Compatibilidad entre parches y modificación de estado compartido; base para contrastar obligaciones adicionales.

## B06

Microsoft (Metadato ms.date=2018-12-05; captura de 09-09-2026). *FlushFileBuffers function (fileapi.h)*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers).

**Localización utilizada:** Return value; Remarks.

**Función y límite:** Resultado y alcance de una sincronización de archivo.

## B07

Microsoft (Metadato ms.date=2018-12-05; captura de 09-09-2026). *FlushViewOfFile function (memoryapi.h)*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile).

**Localización utilizada:** Remarks.

**Función y límite:** Contraejemplo a equiparar escritura de páginas, metadatos y persistencia en el dispositivo.

## B08

Dai, J.; Zhang, Y.; Jiang, Z.; Zhou, Y.; Chen, J.; Xing, X.; Zhang, X.; Tan, X.; Yang, M.; Yang, Z. (2020). *BScout: Direct Whole Patch Presence Test for Java Executables. 29th USENIX Security Symposium, pp. 1147–1164*. [Documento original](https://www.usenix.org/system/files/sec20-dai.pdf).

**Localización utilizada:** §1, pp. 1147–1148; §§4–6 para el alcance del estudio.

**Función y límite:** Estudio empírico sobre presencia íntegra de parches en ejecutables Java. Sus resultados no se transfieren a todas las plataformas ni validan este catálogo.

## B09

Sun, S.; Xing, Y.; Wang, X.; Wang, S.; Li, Q.; Sun, K. (2025). *DisPatch: Unraveling Security Patches from Entangled Code Changes. 34th USENIX Security Symposium*. [Documento original](https://www.usenix.org/system/files/usenixsecurity25-sun-shiyu.pdf).

**Localización utilizada:** §1, pp. 4521–4522; §7, evaluación; §8, discusión y límites.

**Función y límite:** Estudio sobre dependencias de modificaciones de código. Compilar un fragmento separado no acredita que resuelva íntegramente la vulnerabilidad. La delimitación de un parche individual también requiere juicio experto.

## B10

Swanson, M.; Bowen, P.; Phillips, A.; Gallup, D.; Lynes, D. (2010; actualización de 11-11-2010). *Contingency Planning Guide for Federal Information Systems. NIST SP 800-34 Rev. 1*. [Documento original](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf).

**Localización utilizada:** §3.2, pp. 15–19; §§3.4.1, 4.3.

**Función y límite:** Relación entre servicios, dependencias, impacto y recuperación. Un objetivo temporal no es un resultado medido.

## B11

Microsoft (Metadato ms.date=2018-05-31; captura de 09-09-2026). *File Caching*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching).

**Localización utilizada:** Texto principal.

**Función y límite:** Diferencia entre escrituras almacenadas en memoria y su sincronización; intercambio entre rendimiento y fiabilidad.

## B12

Microsoft (Metadato ms.date=2018-12-05; captura de 09-09-2026). *MoveFileExW function (winbase.h)*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-movefileexw).

**Localización utilizada:** MOVEFILE_DELAY_UNTIL_REBOOT; MOVEFILE_WRITE_THROUGH; Remarks.

**Función y límite:** Operaciones diferidas de archivo y límites de la confirmación de programación.

## T002

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *IUpdateInstallationResult::get_RebootRequired*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iupdateinstallationresult-get_rebootrequired).

**Localización utilizada:** Remarks.

**Función y límite:** Requisito individual de reinicio.

## T003

Microsoft (Captura de 08–09-09-2026). *InstallationRebootBehavior*. [Documento original](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-uamg/eee24bbd-0be7-4a81-bed5-bff1fbb1832b).

**Localización utilizada:** Enumeración.

**Función y límite:** Comportamiento previsto, distinto del resultado de instalación.

## T004

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *OperationResultCode*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-operationresultcode).

**Localización utilizada:** Constants.

**Función y límite:** Semántica de los resultados de operación.

## T005

Microsoft (Metadato ms.date=2018-05-31; captura de 08–09-09-2026). *IUpdateInstallationResult Properties*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/wua_sdk/iupdateinstallationresult-properties).

**Localización utilizada:** Properties.

**Función y límite:** Separación de ResultCode, HResult y RebootRequired.

## T006

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *IInstallationResult::GetUpdateResult*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nf-wuapi-iinstallationresult-getupdateresult).

**Localización utilizada:** Parameters; Remarks.

**Función y límite:** Correspondencia con el índice original de la colección.

## T007

Microsoft (Metadato ms.date=2026-02-12; captura de 08–09-09-2026). *Updates may not be installed with Fast Startup in Windows 10*. [Documento original](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/updates-not-install-with-fast-startup).

**Localización utilizada:** Summary; More information.

**Función y límite:** Diferencia entre inicio rápido y reinicio íntegro en ese perfil.

## T008

Microsoft (Metadato ms.date=2023-02-08; captura de 08–09-09-2026). *Dynamic-link library search order*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order).

**Localización utilizada:** Factors that affect searching.

**Función y límite:** Selección de bibliotecas y efectos del contexto de carga.

## T009

Microsoft (Metadato ms.date=2018-05-31; captura de 08–09-09-2026). *About Restart Manager*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/rstmgr/about-restart-manager).

**Localización utilizada:** Texto principal.

**Función y límite:** Gestión de programas que usan archivos afectados.

## T010

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *IUpdateHistoryEntry interface*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdatehistoryentry).

**Localización utilizada:** Methods.

**Función y límite:** Datos de historia de actualización; no prueba automática de cobertura.

## T011

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *UpdateOperation*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/wuapi/ne-wuapi-updateoperation).

**Localización utilizada:** Constants.

**Función y límite:** Distinción entre instalación y desinstalación.

## T012

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *GetModuleInformation*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/psapi/nf-psapi-getmoduleinformation).

**Localización utilizada:** Parameters; Remarks.

**Función y límite:** Información de módulo y permisos de observación.

## T013

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *MODULEINFO structure*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/psapi/ns-psapi-moduleinfo).

**Localización utilizada:** Members.

**Función y límite:** Dirección, tamaño y punto de entrada; no identidad criptográfica.

## T014

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *RM_UNIQUE_PROCESS*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/restartmanager/ns-restartmanager-rm_unique_process).

**Localización utilizada:** Members.

**Función y límite:** Identificación de proceso mediante PID y tiempo de creación.

## T015

Microsoft (Metadato ms.date=2018-12-05; captura de 08–09-09-2026). *CreateProcessW*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw).

**Localización utilizada:** Return value.

**Función y límite:** Creación anterior a la terminación de la inicialización.

## T016

Microsoft (Metadato ms.date=2025-07-14; captura de 08–09-09-2026). *Terminating a Process*. [Documento original](https://learn.microsoft.com/en-us/windows/win32/procthread/terminating-a-process).

**Localización utilizada:** How Processes are Terminated.

**Función y límite:** Procesos hijos y permanencia de objetos por referencias externas.

## R001

Universidad Rey Juan Carlos (Curso 2026–2027). *FUNDAMENTOS FISICOS DE LA INFORMATICA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285001&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R002

Universidad Rey Juan Carlos (Curso 2026–2027). *INTRODUCCION A LA CIBERSEGURIDAD. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285002&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R003

Universidad Rey Juan Carlos (Curso 2026–2027). *INTRODUCCION A LA PROGRAMACION. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285003&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R004

Universidad Rey Juan Carlos (Curso 2026–2027). *LOGICA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285004&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R005

Universidad Rey Juan Carlos (Curso 2026–2027). *MATEMATICA DISCRETA Y ALGEBRA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285005&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R006

Universidad Rey Juan Carlos (Curso 2026–2027). *CALCULO. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285006&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R007

Universidad Rey Juan Carlos (Curso 2026–2027). *CRIPTOGRAFIA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285007&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R008

Universidad Rey Juan Carlos (Curso 2026–2027). *DIMENSIONES Y MODELO DE LA SEGURIDAD. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285008&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R009

Universidad Rey Juan Carlos (Curso 2026–2027). *ESTADISTICA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285009&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R010

Universidad Rey Juan Carlos (Curso 2026–2027). *ESTRUCTURAS DE DATOS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285010&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R011

Universidad Rey Juan Carlos (Curso 2026–2027). *METODOS OPERATIVOS Y ESTADISTICOS DE GESTION. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285011&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R012

Universidad Rey Juan Carlos (Curso 2026–2027). *PRINCIPIOS JURIDICOS BASICOS APLICADOS A LA CIBERSEGURIDAD. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285012&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R013

Universidad Rey Juan Carlos (Curso 2026–2027). *PROGRAMACION AVANZADA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285013&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R014

Universidad Rey Juan Carlos (Curso 2026–2027). *REDES DE COMPUTADORES. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285014&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R015

Universidad Rey Juan Carlos (Curso 2026–2027). *TECNICAS DE HACKING. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285015&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R016

Universidad Rey Juan Carlos (Curso 2026–2027). *BASES DE DATOS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285016&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R017

Universidad Rey Juan Carlos (Curso 2026–2027). *DESARROLLO WEB SEGURO. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285017&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R018

Universidad Rey Juan Carlos (Curso 2026–2027). *ESTRUCTURA DE COMPUTADORES. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285018&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R019

Universidad Rey Juan Carlos (Curso 2026–2027). *SEGURIDAD EN REDES. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285019&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R020

Universidad Rey Juan Carlos (Curso 2026–2027). *IDIOMA MODERNO. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285020&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R021

Universidad Rey Juan Carlos (Curso 2026–2027). *ARQUITECTURA DE COMPUTADORES. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285021&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R022

Universidad Rey Juan Carlos (Curso 2026–2027). *DISEÑO Y ANALISIS DE ALGORITMOS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285022&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R023

Universidad Rey Juan Carlos (Curso 2026–2027). *INGENIERIA DEL SOFTWARE. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285023&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R024

Universidad Rey Juan Carlos (Curso 2026–2027). *SEGURIDAD EN BASES DE DATOS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285024&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R025

Universidad Rey Juan Carlos (Curso 2026–2027). *SISTEMAS OPERATIVOS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285025&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R026

Universidad Rey Juan Carlos (Curso 2026–2027). *INTELIGENCIA ARTIFICIAL. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285026&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R027

Universidad Rey Juan Carlos (Curso 2026–2027). *MALWARE Y AMENAZAS DIRIGIDAS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285027&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R028

Universidad Rey Juan Carlos (Curso 2026–2027). *METODOLOGIAS DE DESARROLLO SEGURO. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285028&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R029

Universidad Rey Juan Carlos (Curso 2026–2027). *REDES AVANZADAS Y COMPUTACION EN LA NUBE. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285029&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R030

Universidad Rey Juan Carlos (Curso 2026–2027). *SISTEMAS DE INFORMACION. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285030&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R031

Universidad Rey Juan Carlos (Curso 2026–2027). *VISION ARTIFICIAL APLICADA A LA CIBERSEGURIDAD. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285031&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R032

Universidad Rey Juan Carlos (Curso 2026–2027). *AUDITORIA. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285032&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R033

Universidad Rey Juan Carlos (Curso 2026–2027). *INTELIGENCIA DE LA SEGURIDAD. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285033&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R034

Universidad Rey Juan Carlos (Curso 2026–2027). *PENTESTING. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285034&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R035

Universidad Rey Juan Carlos (Curso 2026–2027). *ANALISIS Y GESTION DEL RIESGO. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285036&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R036

Universidad Rey Juan Carlos (Curso 2026–2027). *PROTECCION DE INFRAESTRUCTURAS CRITICAS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285037&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R037

Universidad Rey Juan Carlos (Curso 2026–2027). *REGULACION Y GOBERNANZA DE LA SEGURIDAD. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285038&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R038

Universidad Rey Juan Carlos (Curso 2026–2027). *PRACTICAS EXTERNAS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285039&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R039

Universidad Rey Juan Carlos (Curso 2026–2027). *RECONOCIMIENTO ACADEMICO DE CREDITOS. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285035&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## R040

Universidad Rey Juan Carlos (Curso 2026–2027). *TRABAJO FIN DE GRADO. Guía docente del Grado en Ingeniería de la Ciberseguridad*. [Documento original](https://gestion3.urjc.es/guiasdocentes/pdfGuia.jsp?txtAsignatura=2285040&txtTitulacion=2285&txtCursoAcademico=2026-27).

**Localización utilizada:** II. Presentación; III. Resultados de aprendizaje; IV. Contenido.

**Función y límite:** Base educativa. La ficha no constituye por sí sola un parámetro; su función se relaciona con la operación en el catálogo.

## M001

UNSW Canberra (Edición 2026 o 2026–2027 identificada en el catálogo). *Cyber Security Industry Project 1*. [Documento original](https://www.handbook.unsw.edu.au/undergraduate/courses/2026/ZSPS2119).

**Localización utilizada:** Descripción y resultados de aprendizaje del curso.

**Función y límite:** Complemento educativo selectivo; no equivalencia entre títulos o créditos de países distintos.

## M002

UNSW Canberra (Edición 2026 o 2026–2027 identificada en el catálogo). *Machine Learning for Cyber Security*. [Documento original](https://www.handbook.unsw.edu.au/undergraduate/courses/2026/ZSPS2118).

**Localización utilizada:** Descripción y resultados de aprendizaje del curso.

**Función y límite:** Complemento educativo selectivo; no equivalencia entre títulos o créditos de países distintos.

## M003

UNSW Canberra (Edición 2026 o 2026–2027 identificada en el catálogo). *Trustworthy AI for Cyber Security*. [Documento original](https://www.handbook.unsw.edu.au/undergraduate/courses/2026/ZSPS2122).

**Localización utilizada:** Descripción y resultados de aprendizaje del curso.

**Función y límite:** Complemento educativo selectivo; no equivalencia entre títulos o créditos de países distintos.

## M004

UNSW Canberra (Edición 2026 o 2026–2027 identificada en el catálogo). *Deep Learning for Cyber Security*. [Documento original](https://www.handbook.unsw.edu.au/undergraduate/courses/2026/ZSPS2121).

**Localización utilizada:** Descripción y resultados de aprendizaje del curso.

**Función y límite:** Complemento educativo selectivo; no equivalencia entre títulos o créditos de países distintos.

## W016

University of Warwick (Edición 2026 o 2026–2027 identificada en el catálogo). *W016*. [Documento original](https://courses.warwick.ac.uk/modules/2026/WM284-15).

**Localización utilizada:** Descripción y resultados de aprendizaje del curso.

**Función y límite:** Complemento educativo selectivo; no equivalencia entre títulos o créditos de países distintos.

## G009

University of Guelph (Consulta de 08-09-2026; calendario sin edición anual visible). *CIS*6580*. [Documento original](https://calendar.uoguelph.ca/search/?P=CIS*6580).

**Localización utilizada:** Descripción y resultados de aprendizaje del curso.

**Función y límite:** Complemento educativo selectivo; no equivalencia entre títulos o créditos de países distintos.

## SV-ES

Sistema Vectorial SV; decisión del Director (2026-09-07). *Acta de uso del español en todos los repositorios del Sistema Vectorial SV*. [Documento original](https://github.com/juantoniolloretegea/SV-lenguaje-de-computacion/blob/ab61d9bb7a2002d3a4a389e292c2a9b0a850d264/docs/calidad/ACTA_DE_USO_DEL_ESPANOL_EN_TODOS_LOS_REPOSITORIOS_SV_2026_09_07.md).

**Localización utilizada:** §§1–4.

**Función y límite:** Norma interna obligatoria de redacción y precisión; no fuente técnica de ciberseguridad.

## SV-AT

Sistema Vectorial SV (2026-09-02). *Contrato matemático de parámetro atómico, matriz y ruta. INMUNO v0.3*. [Documento original](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/fe8adf76aa030ba5ff4997be5772b5de5e4452f3/dominios/inmunologia/cambio-rumbo/03-base-documental-candidata/05-normalizacion-atomica-en-evaluacion/Contrato_matematico_parametro_atomico_matriz_ruta_INMUNO_v0.3_2026-09-02.md).

**Localización utilizada:** §§3–7.

**Función y límite:** Método de identidad, independencia y consecuencia. No se trasladan reglas clínicas, cantidades ni matrices.

## SV-IN

Sistema Vectorial SV; instrucción aprobada por el Director (2026-09-08). *Instrucción de relevo de ciberseguridad inteligente, revisión 1.2*. [Documento original](https://github.com/juantoniolloretegea/SVperitus-dataset/blob/47dc27aec9e7b517c27cfcf39b7ad1b186d36a4c/dominios/ciberseguridad-inteligente/dominio-04-09-26/watson-biblioteca-ciber/Aprobada_INSTRUCCION_RELEVO_CIBERSEGURIDAD_INTELIGENTE_2026_09_08.md).

**Localización utilizada:** §§5, 7–9 y 11; orden posterior del Director de 09-09-2026.

**Función y límite:** Marco de constitución, actualizado en la secuencia por la orden humana que exige terminar el primer universo antes de decidir el relevo.
