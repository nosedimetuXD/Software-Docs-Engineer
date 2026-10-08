# Especificación de Requisitos de Software bajo ISO/IEC/IEEE 29148:2018

Este documento establece el estándar para formular, clasificar, validar y rastrear requisitos de software de acuerdo con la norma internacional **ISO/IEC/IEEE 29148**, articulada con la taxonomía cognitiva del **Framework Diátaxis**.

---

## 1. Clasificación Formal de Requisitos

Todo sistema de software debe descomponer sus requisitos en cuatro categorías principales:

1. **Requisitos Funcionales (RF):**
   - Describen *qué* debe hacer el software en respuesta a entradas o estímulos específicos.
   - Sintaxis obligatoria: `El sistema DEBERÁ [verbo en infinitivo] [objeto/resultado esperado] cuando [condición/estímulo].`
   - Ejemplo: `RF-01: El sistema DEBERÁ autenticar al usuario mediante credenciales corporativas (OAuth 2.0 / JWT) antes de permitir el acceso al módulo de inventarios.`

2. **Requisitos No Funcionales / Atributos de Calidad (RNF):**
   - Fundamentados en la norma **ISO/IEC 25010 (SQuaRE)**: Eficiencia de desempeño, Usabilidad, Fiabilidad, Seguridad, Mantenibilidad, Portabilidad, Compatibilidad.
   - Deben formularse de manera **cuantitativa y medible**, nunca ambigua.
   - Ejemplo: `RNF-01 (Desempeño): El sistema DEBERÁ procesar el 95% de las transacciones de pago en un tiempo de respuesta inferior a 1.5 segundos con una concurrencia de hasta 500 usuarios simultáneos.`

3. **Restricciones de Diseño e Implementación (RES):**
   - Limitaciones tecnológicas, normativas, presupuestarias o de infraestructura impuestas por el entorno o el cliente.
   - Ejemplo: `RES-01: El backend DEBERÁ implementarse en Java 17 LTS utilizando Spring Boot 3 y la base de datos DEBERÁ ser PostgreSQL 15.`

4. **Requisitos de Transición y Despliegue:**
   - Procedimientos necesarios para poner el software en marcha (migración de datos históricos, capacitación, parametrización inicial).

---

## 2. Criterios de Calidad de Requisitos (Regla INCOSE / IEEE)

Cada requisito individual debe cumplir con los siguientes atributos:
* **Necesario:** Satisface una meta real del negocio o usuario.
* **No ambiguo:** Solo admite una interpretación técnica válida.
* **Completo:** Contiene toda la información necesaria para su implementación y verificación.
* **Consistente:** No entra en contradicción con ningún otro requisito del sistema.
* **Verificable:** Es posible diseñar una prueba objetiva (inspección, prueba, análisis o demostración) para comprobar su cumplimiento.
* **Rastreable:** Posee un identificador único persistente (`RF-01`, `RNF-02`) trazable a casos de uso, clases de diseño y casos de prueba.

---

## 3. Estructura Estándar de la ERS (ISO/IEC/IEEE 29148)

```text
1. Introducción
   1.1 Propósito
   1.2 Ámbito del Producto (Alcance, beneficios, metas)
   1.3 Visión General del Producto
       1.3.1 Perspectiva del producto (Interfaces con otros sistemas, hardware, software, red)
       1.3.2 Funciones principales del producto
       1.3.3 Características de los usuarios (Roles, experiencia técnica)
       1.3.4 Limitaciones y restricciones
   1.4 Definiciones, Acrónimos y Abreviaturas
2. Referencias Documentales
3. Requisitos Específicos
   3.1 Interfaces Externas (Usuario, Hardware, Software, Comunicaciones)
   3.2 Funciones del Software (Desglose detallado de Requisitos Funcionales)
   3.3 Requisitos de Capacidad de Uso (Usabilidad, accesibilidad)
   3.4 Requisitos de Desempeño (Concurrencia, latencia, throughput)
   3.5 Requisitos de Bases de Datos (Integridad, retención, volumen)
   3.6 Restricciones de Diseño
   3.7 Atributos de Calidad (Seguridad, Fiabilidad, Disponibilidad, Mantenibilidad)
   3.8 Información de Soporte
4. Matriz de Verificación (Requisito vs Método de Verificación)
5. Apéndices (Suposiciones y Dependencias)
```

---

## 4. Matriz de Trazabilidad Bidireccional

| ID Requisito | Descripción Resumida | Caso de Uso Asociado | Diagrama Secuencia / Clase | Caso de Prueba (QA) | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `RF-01` | Autenticación con OAuth 2.0 | `CU-01: Iniciar Sesión` | `AuthService.authenticate()` | `TC-AUTH-01` | Aprobado |
| `RF-02` | Registro de Transacción | `CU-05: Realizar Pago` | `PaymentProcessor.pay()` | `TC-PAY-03` | En Desarrollo |
| `RNF-01` | Cifrado de datos en tránsito | Transversal | Configuración TLS 1.3 / HTTPS | `TC-SEC-01` | Verificado |
