# Atributos de Calidad (ISO/IEC 25000 SQuaRE) y Patrones de Diseño (Larman / GoF)

Este documento articula el modelo de calidad de producto software **ISO/IEC 25000 / ISO/IEC 25010** con las prácticas de diseño orientado a objetos de **Craig Larman** (patrones GRASP) y el catálogo de patrones del **GoF (Gang of Four)**.

---

## 1. Modelo de Calidad ISO/IEC 25010 (SQuaRE)

Para justificar técnicamente las decisiones de diseño arquitectónico y documentar los Requisitos No Funcionales, se deben emplear las 8 características de calidad:

| Característica | Subcaracterísticas Clave | Pregunta Guía de Ingeniería | Métricas Típicas |
| :--- | :--- | :--- | :--- |
| **1. Adecuación Funcional** | Completitud, corrección y pertinencia funcional. | ¿El software hace exactamente lo que el negocio requiere? | % de casos de uso cubiertos sin defectos. |
| **2. Eficiencia de Desempeño** | Comportamiento temporal, utilización de recursos, capacidad. | ¿Responde dentro de los límites de latencia bajo carga? | Tiempo de respuesta promedio (ms), concurrencia máx, TPS. |
| **3. Compatibilidad** | Coexistencia e interoperabilidad. | ¿Interopera con servicios externos sin conflictos? | Cumplimiento OpenAPI, soporte protocolos estándar. |
| **4. Capacidad de Uso (Usabilidad)** | Reconocibilidad, aprendizaje, operabilidad, protección contra errores de usuario, estética y accesibilidad. | ¿El usuario logra su cometido con bajo esfuerzo y sin frustración? | Tasa de éxito de tareas (>90%), tiempo de aprendizaje. |
| **5. Fiabilidad** | Madurez, disponibilidad, tolerancia a fallos y capacidad de recuperación. | ¿El sistema permanece operativo ante caídas o excepciones? | Uptime (99.9%), MTBF (Mean Time Between Failures), MTTR. |
| **6. Seguridad** | Confidencialidad, integridad, no repudio, autenticidad y responsabilidad. | ¿Los datos y endpoints están protegidos contra accesos no autorizados? | Cifrado AES-256/TLS 1.3, cero vulnerabilidades OWASP Top 10. |
| **7. Mantenibilidad** | Modularidad, reusabilidad, analizabilidad, modificabilidad y testeabilidad. | ¿Es fácil corregir errores y agregar nuevas características? | Cobertura de tests unitarios (>80%), complejidad ciclomática (<10). |
| **8. Portabilidad** | Adaptabilidad, instalabilidad y capacidad de ser reemplazado. | ¿Puede ejecutarse en múltiples plataformas o entornos de nube? | Docker containerization, configuración 12-Factor App. |

---

## 2. Asignación de Responsabilidades con Patrones GRASP (Craig Larman)

Al elaborar la **Vista Lógica** (Diagramas de Clases y Secuencia), la justificación de cómo interactúan los objetos debe apoyarse en los 9 principios GRASP:

1. **Information Expert (Experto en Información):** Asignar la responsabilidad a la clase que posee la información necesaria para cumplirla.
2. **Creator (Creador):** La clase `A` crea instancias de `B` si `A` contiene o agrega a `B`, o si registra a `B` de forma estrecha.
3. **Controller (Controlador):** Asignar la responsabilidad de recibir o gestionar un mensaje de evento del sistema a una clase que representa al sistema global o al caso de uso.
4. **Low Coupling (Bajo Acoplamiento):** Diseñar dependencias mínimas entre módulos para facilitar el mantenimiento y la reutilización.
5. **High Cohesion (Alta Cohesión):** Mantener las clases enfocadas en una sola responsabilidad estrechamente relacionada (Single Responsibility).
6. **Polymorphism (Polimorfismo):** Manejar comportamientos alternativos según el tipo mediante interfaces o jerarquías polimórficas, en lugar de condicionales `if/switch` excesivos.
7. **Pure Fabrication (Fabricación Pura):** Crear clases de servicio que no representan conceptos del dominio (ej. `DatabaseAdapter`, `ReportGenerator`) para mantener alta la cohesión.
8. **Indirection (Indirección):** Introducir un intermediario para evitar el acoplamiento directo entre dos componentes.
9. **Protected Variations (Variaciones Protegidas):** Diseñar interfaces estables para blindar el sistema contra la inestabilidad de cambios en subsistemas externos.

---

## 3. Patrones de Diseño GoF (Gang of Four)

Documentar formalmente en la sección de diseño arquitectónico la selección de patrones:
* **Creacionales:** Factory Method, Abstract Factory, Singleton, Builder.
* **Estructurales:** Adapter, Facade, Decorator, Composite, Proxy.
* **Comportamiento:** Strategy, Observer, Command, State, Template Method.
