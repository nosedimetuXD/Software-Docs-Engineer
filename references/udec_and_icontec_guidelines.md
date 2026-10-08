# Lineamientos Académicos de Ingeniería de Software (UdeC) y Normas ICONTEC

Esta guía condensa los requisitos de presentación, formato y sustentación definidos en los lineamientos de proyectos de la **Universidad de Cartagena** (Ing. Martín Monroy Ríos, MSc, PhD) y las normas **ICONTEC** aplicables a informes técnicos de ingeniería.

---

## 1. Estructura Oficial del Entregable (`Proyecto_ISw_X.zip`)

El entregable final debe ser un archivo `.zip` con el nombre `Proyecto_ISw_X` (donde `X` es el número del grupo asignado). Su contenido comprende exactamente 4 carpetas:

```text
Proyecto_ISw_X.zip/
├── Documentación/              # Formatos Word (.docx) y UML
│   ├── Informe.docx            # Informe general del proyecto
│   ├── Manual_del_Sistema.docx # Manual de arquitectura, requisitos y diseño (4+1)
│   ├── Especificacion_Req.docx # Documento ERS bajo ISO/IEC/IEEE 29148
│   ├── Manual_de_Usuario.docx  # Guía operativa para el usuario final
│   ├── Proyecto_UML.qea/.eap   # Archivo de modelado en Enterprise Architect
│   └── Presentacion.pptx       # Diapositivas para sustentación (máximo 30 minutos)
├── Código Fuente/              # Proyecto íntegro ejecutable del entorno de desarrollo
├── Instaladores/               # Binarios ejecutables, dependencias, variables de entorno
│   └── credenciales.txt        # Usuarios y contraseñas de prueba por cada rol
└── Anexos/                     # Soportes indispensables
    ├── script_bd.sql           # Script de creación y población de la base de datos
    └── evidencias/             # Actas de reuniones, fotografías, encuestas
```

---

## 2. Reglas Editoriales y Normas ICONTEC

Todos los documentos en la carpeta `Documentación/` deben cumplir estrictamente:
1. **Redacción Impersonal:** 
   - Prohibido el uso de primera persona (*"hicimos", "desarrollamos", "creamos"*).
   - Utilizar fórmulas impersonales: *"Se analizó", "se implementó", "el sistema permite", "se diseñó"*.
2. **Formato de Texto:**
   - Fuente: Arial o Times New Roman de 12 puntos.
   - Interlineado: 1.5 líneas (o según plantilla oficial).
   - Alineación: Justificada.
3. **Numeración Decimal:**
   - Jerarquía: `1.`, `1.1.`, `1.1.1.`. Máximo tres niveles de desglose numérico.
4. **Figuras y Tablas:**
   - Deben estar centradas, con rótulo superior (`Tabla 1. Matriz de Requisitos`), llamada en el texto (*"como se observa en la Tabla 1..."*) y fuente inferior (`Fuente: Elaboración propia, 2026`).
5. **Conclusiones Orientadas al Aprendizaje:**
   - Las conclusiones no deben resumir lo que hace el software; deben dar cuenta explícita del aprendizaje de ingeniería logrado frente a los objetivos planteados.

---

## 3. Rúbrica de Sustentación (30 Minutos)

Durante la presentación del proyecto se evalúan dos dimensiones críticas:

### A. Dimensión de Presentación
* Dominio conceptual y seguridad del equipo al exponer.
* Claridad visual (diapositivas sintetizadas, sin párrafos extensos de texto).
* Cohesión del equipo y distribución equitativa de intervenciones.
* Ajuste estricto al tiempo límite (30 minutos máximo).

### B. Dimensión de Revisión Técnica
* Coherencia absoluta entre el **Manual del Sistema**, el **Modelo UML en Enterprise Architect** y el **Código Fuente en ejecución**.
* Demostración en vivo de la aplicación funcionando.
* Respeto a los derechos de autor y citación bibliográfica formal.
