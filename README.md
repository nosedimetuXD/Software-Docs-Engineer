# Software Docs Engineer 🛠️📚

> **Agentic Engineering Skill for Software Architecture, Formal Requirements (ISO 29148), Kruchten 4+1 Views, API Contracts, and Technical Documentation.**  
> Built for AI Coding Assistants (Google Antigravity, Claude Code, Cursor, Codex, Windsurf, Copilot Workspace).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Standards: ISO/IEC/IEEE 29148](https://img.shields.io/badge/Standards-ISO%2FIEC%2FIEEE%2029148%3A2018-blue.svg)](https://standards.ieee.org/)
[![Standards: ISO/IEC/IEEE 42010](https://img.shields.io/badge/Standards-ISO%2FIEC%2FIEEE%2042010%3A2022-green.svg)](https://standards.ieee.org/)
[![Standards: ISO/IEC 25000](https://img.shields.io/badge/Standards-ISO%2FIEC%2025000%20SQuaRE-red.svg)](https://iso25000.com/)
[![Framework: Diátaxis](https://img.shields.io/badge/Framework-Diátaxis-purple.svg)](https://diataxis.fr/)
[![Architecture: Kruchten 4+1 & arc42](https://img.shields.io/badge/Architecture-4%2B1%20%7C%20arc42-orange.svg)](https://arc42.org/)

---

## 🌟 Overview

**`software-docs-engineer`** transforms AI coding assistants from basic code commentators into senior technical documentation architects. Rooted in international standards, formal academic engineering curricula, and contemporary cloud-native workflows, it enforces:

- 📋 **ISO/IEC/IEEE 29148:2018 Requirements Engineering:** Unambiguous functional and non-functional requirements specification (ERS/SRS), structured tabular use cases, and bidirectional traceability matrices.
- 📐 **Kruchten 4+1 Architecture Model & arc42 Convergence:** Harmonious synthesis between Kruchten's 5 views (Scenario, Logical, Process, Development, Physical) and **arc42 / C4 Model** with Enterprise Architect and Mermaid.js support.
- 💎 **ISO/IEC 25000 (SQuaRE) & Larman GRASP:** Formal quality attribute trees (performance, security, usability, maintainability) and object-oriented design grounded in Craig Larman's GRASP responsibilities and GoF patterns.
- 🏛️ **Academic & Institutional Standards (ICONTEC / UdeC):** Strict third-person impersonal styling, formal project reports, systems manuals, and automatic compliance audits for deliverables (`Proyecto_ISw_X.zip`).
- 🧭 **Diátaxis Framework:** Cognitive segregation of user manuals and developer portals into Tutorials, How-To Guides, Reference, and Explanation.
- 📝 **Architectural Decision Records (ADR):** Standardized **MADR 3.x** format for logging non-reversible design choices.
- 🔌 **API Contracts (Sync & Async):** Rigorous **OpenAPI 3.1** (JSON Schema 2020-12 / RFC 9457 Problem Details) and **AsyncAPI 3.0+** specifications.
- ⚙️ **Docs-as-Code & Docs-as-Tests:** CI/CD quality gates, prose linting with **Vale**, structural linting with **markdownlint**, and verified executable snippets.
- 🤖 **AI & Agent Optimization:** Native generation of [`/llms.txt`](https://llmstxt.org/) and [`/llms-full.txt`] for autonomous agent context consumption.
- 📊 **Office & Tabular Automation:** Python automation tools for compiling use cases into styled Excel sheets (`.xlsx`) and validating delivery structures.

---

## 📁 Repository Structure

```text
software-docs-engineer/
├── SKILL.md                                  # Core skill instructions, dual-track decision trees, and playbooks
├── README.md                                 # Project documentation and installation guide
├── LICENSE                                   # MIT License
├── references/
│   ├── kruchten_4plus1_convergence.md        # Kruchten 4+1 mapping to arc42, C4, and Enterprise Architect
│   ├── iso_29148_requirements_spec.md        # ISO/IEC/IEEE 29148 requirements guidelines and traceability
│   ├── iso25000_quality_attributes.md        # ISO 25000 SQuaRE quality attributes & Craig Larman GRASP/GoF
│   ├── udec_and_icontec_guidelines.md        # Formal academic reporting guidelines (UdeC & ICONTEC)
│   ├── diataxis_framework.md                 # Diátaxis quadrant definitions and anti-pattern catalog
│   ├── arc42_and_c4.md                       # arc42 mapping to ISO 42010 & Mermaid C4 templates
│   ├── api_contracts_and_eda.md              # OpenAPI 3.1, AsyncAPI 3.0, and breaking change rules
│   ├── docs_as_code_and_tests.md             # CI/CD pipelines, Vale linting, and snippet tests
│   ├── drift_mitigation_and_metrics.md       # DX formulas, benchmarks, and PR checklists
│   └── llms_txt_and_agent_readability.md     # llms.txt standard and token-efficient formatting
├── examples/
│   ├── iso_29148_ers_template.md             # Production-ready ERS template (ISO 29148)
│   ├── manual_sistema_4plus1_template.md     # Comprehensive Systems Manual template (Kruchten 4+1)
│   ├── manual_usuario_diataxis_template.md   # Role-based User Manual template (Diátaxis)
│   ├── informe_proyecto_icontec_template.md  # Formal Project Final Report template (ICONTEC)
│   ├── caso_de_uso_spec.yaml                 # Structured Use Case schema for automation
│   ├── madr_template.md                      # Markdown Architecture Decision Record (MADR) template
│   └── arc42_starter.md                      # Production-ready arc42 starter template
├── scripts/
│   ├── export_casos_uso_xlsx.py              # Generates styled Excel sheets from use case specs
│   └── audit_and_package_project.py          # Linter that validates delivery guidelines and zips project
└── templates/
    ├── plantilla_informe_proyecto.docx       # Official Word template for Project Report
    ├── plantilla_manual_sistema.docx         # Official Word template for Systems Manual
    └── plantilla_casos_uso.xlsx              # Official Excel template for Use Cases
```

---

## 🚀 Installation & Usage

### 1. Google Antigravity (AGY)

#### Global Installation (All Projects):
Clone or copy this repository into your global Antigravity skills directory:

```bash
# Windows PowerShell
git clone https://github.com/nosedimetuXD/Software-Docs-Engineer.git "$env:USERPROFILE\.gemini\config\skills\software-docs-engineer"

# macOS / Linux
git clone https://github.com/nosedimetuXD/Software-Docs-Engineer.git ~/.gemini/config/skills/software-docs-engineer
```

#### Project-Specific Installation:
Add it directly to your repository's workspace customizations:

```bash
mkdir -p .agents/skills/
git clone https://github.com/nosedimetuXD/Software-Docs-Engineer.git .agents/skills/software-docs-engineer
```

---

## 🎯 How to Prompt Your Agent

Once installed, your agent will automatically activate the skill whenever you ask for documentation tasks:

```text
"Redacta la Especificación de Requisitos de Software (ERS) para este módulo según ISO 29148."
"Estructura el Manual del Sistema aplicando el Modelo de Vistas 4+1 de Kruchten y patrones GRASP."
"Genera el libro de Casos de Uso en Excel a partir de nuestras especificaciones."
"Audita el paquete de entrega del proyecto antes de generar el archivo ZIP final."
"Document the architecture of this microservice using arc42 and C4 diagrams."
"Create an ADR justifying our migration from REST to Kafka event streaming."
```

---

## 📐 Key Frameworks & Standards

| Standard / Framework | Scope in this Skill |
| :--- | :--- |
| **ISO/IEC/IEEE 29148:2018** | Requirements engineering, functional and non-functional decomposition, bidirectional traceability. |
| **Kruchten 4+1 View Model** | Scenario, Logical, Process, Development, and Physical architectural views mapped to UML & EA. |
| **ISO/IEC 25000 (SQuaRE)** | Software product quality requirements and evaluation metrics. |
| **ISO/IEC/IEEE 42010:2022** | System architecture descriptions, concerns, viewpoints, and views. |
| **Normas ICONTEC** | Formal technical reporting, third-person impersonal styling, decimal hierarchy. |
| **Diátaxis** | Cognitive segregation: Tutorials, How-To Guides, Reference, Explanation. |
| **arc42 & C4 Model** | Standardized architectural communication and component modeling. |
| **MADR 3.x** | Markdown Architectural Decision Records. |
| **OpenAPI 3.1 & AsyncAPI 3.0** | Machine-readable API contracts for synchronous and event-driven architectures. |
| **llms.txt** | Machine-readable markdown indices optimized for AI context windows. |

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE). Contributions and pull requests are welcome!
