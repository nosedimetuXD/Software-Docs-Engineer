# Convergencia Arquitectónica: Modelo 4+1 de Kruchten, arc42 y C4 Model

Este documento establece la correspondencia formal entre el **Modelo de Vistas 4+1 de Philippe Kruchten**, la plantilla de arquitectura **arc42 (ISO/IEC/IEEE 42010:2022)**, el **C4 Model** de Simon Brown y las herramientas de modelado UML (*Enterprise Architect*, *Mermaid* y *PlantUML*).

---

## 1. Matriz de Mapeo y Correspondencia

| Vista 4+1 (Kruchten) | Propósito y Enfoque | Sección arc42 Correspondiente | Nivel C4 Model | Diagramas UML / Modelado Recomendados |
| :--- | :--- | :--- | :--- | :--- |
| **Vista de Escenarios (+1)** | Define el comportamiento del sistema desde el punto de vista de los actores externos. Valida y unifica las otras 4 vistas. | **1. Introducción y Metas**<br>**3. Contexto y Alcance** | **C4 Nivel 1: Contexto del Sistema** | • Diagrama de Casos de Uso (UML)<br>• C4 System Context (Mermaid)<br>• Prototipos y Wireframes de GUI |
| **Vista Lógica** | Organización abstracta del sistema y cumplimiento de requisitos funcionales. Estructura de dominio y responsabilidades. | **5. Bloques de Construcción (Nivel 2/3)** | **C4 Nivel 3: Componentes** | • Diagrama de Clases (con patrones GoF y GRASP)<br>• Diagrama de Paquetes Lógicos (Capas / Hexagonal)<br>• Diagrama de Objetos |
| **Vista de Procesos** | Aspectos dinámicos, concurrencia, rendimiento, sincronización de hilos y escalabilidad en tiempo de ejecución. | **6. Vista de Tiempo de Ejecución (Runtime View)** | Dinámico / Flujos de interacción | • Diagrama de Secuencia (UML - llamadas síncronas/asíncronas)<br>• Diagrama de Actividades (Workflows y bifurcaciones concurrentes)<br>• Diagrama de Estados (ciclo de vida de entidades reactivas) |
| **Vista de Desarrollo** | Organización física de los artefactos de software en el entorno de desarrollo y gestión de configuración. | **5. Bloques de Construcción (Nivel 1/2)** | **C4 Nivel 2: Contenedores** | • Diagrama de Componentes (módulos, librerías, APIs, microservicios)<br>• Diagrama de Paquetes físicos (árbol de directorios/código fuente)<br>• Matriz de Dependencias (gestores de paquetes: npm, pip, maven) |
| **Vista Física / Despliegue** | Asignación de los componentes de software sobre los nodos de hardware e infraestructura de red. | **7. Vista de Despliegue (Deployment View)** | **C4 Despliegue / Infraestructura** | • Diagrama de Despliegue (UML - Nodos, artefactos, dispositivos)<br>• Topología de Red (balanceadores, protocolos TCP/HTTP/gRPC, firewalls)<br>• Especificación de Infraestructura (Cloud, Docker, Kubernetes) |

---

## 2. Enriquecimiento Transversal provisto por arc42

El Modelo 4+1 tradicional se potencia enormemente incorporando las secciones transversales de **arc42**:

1. **Restricciones de Arquitectura (arc42 §2):** Limitaciones técnicas, normativas, presupuestarias o de hardware impuestas al sistema.
2. **Conceptos Transversales (arc42 §8):** Decisiones de arquitectura que afectan a todas las vistas:
   - Seguridad (Autenticación JWT, RBAC, cifrado en reposo y tránsito).
   - Persistencia y Transacciones (ACID, transacciones distribuidas, ORM).
   - Observabilidad (Métricas, Tracing distribuido, Logs estructurados).
   - Manejo de Errores y Resiliencia (Circuit Breaker, Retry, Failover).
3. **Decisiones de Arquitectura - ADRs (arc42 §9):** Registro formal en formato MADR de decisiones clave y alternativas descartadas.
4. **Requisitos de Calidad (arc42 §10):** Árbol de calidad fundamentado en la norma **ISO/IEC 25000 (SQuaRE)** y escenarios estímulo-respuesta.
5. **Riesgos y Deuda Técnica (arc42 §11):** Matriz de probabilidad e impacto para anticipar contingencias.

---

## 3. Estructura de Modelado en Enterprise Architect (.qea / .eap)

Para proyectos que requieren archivo de modelado UML institucional, el árbol de paquetes debe reflejar esta convergencia:

```text
Proyecto_UML_Raiz/
├── 1. Modelo de Negocio/
│   ├── Diagramas de Actividades (Procesos de Negocio)
│   ├── Casos de Uso del Mundo Real
│   └── Modelo de Dominio (Clases conceptuales)
├── 2. Requisitos del Sistema/
│   ├── Diagramas de Casos de Uso del Sistema
│   └── Especificación de Casos de Uso Tabulares
├── 3. Modelo de Diseño/
│   ├── 3.1 Vista de Escenarios (Casos de Uso de diseño + Wireframes)
│   ├── 3.2 Vista Lógica (Paquetes en capas, Clases de diseño GRASP/GoF)
│   └── 3.3 Vista de Procesos (Diagramas de Secuencia y Estados)
└── 4. Modelo de Implementación/
    ├── 4.1 Vista de Desarrollo (Diagrama de Componentes y librerías)
    └── 4.2 Vista Física (Diagrama de Despliegue en servidores/nodos)
```
