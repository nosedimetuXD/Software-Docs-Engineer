# Software Docs Engineer 🛠️📚

> **Agentic Engineering Skill for Software Architecture, API Contracts, and Technical Documentation.**  
> Built for AI Coding Assistants (Google Antigravity, Claude Code, Cursor, Codex, Windsurf, Copilot Workspace).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Standards: ISO/IEC/IEEE 42010](https://img.shields.io/badge/Standards-ISO%2FIEC%2FIEEE%2042010%3A2022-green.svg)](https://standards.ieee.org/)
[![Framework: Diátaxis](https://img.shields.io/badge/Framework-Diátaxis-purple.svg)](https://diataxis.fr/)
[![Architecture: arc42](https://img.shields.io/badge/Architecture-arc42-orange.svg)](https://arc42.org/)

---

## 🌟 Overview

**`software-docs-engineer`** transforms AI coding assistants from basic code commentators into senior technical documentation architects. Rooted in international standards and contemporary engineering workflows, it enforces:

- 🧭 **Diátaxis Framework:** Semantic segregation into Tutorials, How-To Guides, Reference, and Explanation, eliminating cognitive drift.
- 🏛️ **arc42 & C4 Modeling:** 12 architectural sections aligned with **ISO/IEC/IEEE 42010:2022** and **Mermaid.js Diagrams-as-Code (DaC)**.
- 📝 **Architectural Decision Records (ADR):** Standardized **MADR 3.x** format for logging non-reversible design choices.
- 🔌 **API Contracts (Sync & Async):** Rigorous **OpenAPI 3.1** (JSON Schema 2020-12 / RFC 9457 Problem Details) and **AsyncAPI 3.0+** specifications.
- ⚙️ **Docs-as-Code & Docs-as-Tests:** CI/CD quality gates, prose linting with **Vale**, structural linting with **markdownlint**, and verified executable snippets (Doc Detective).
- 📈 **Documentation Drift Prevention & DX Metrics:** Tracking **TTFHW (Time to First Hello World)**, Support Deflection Rates, and Pull Request quality gates.
- 🤖 **AI & Agent Optimization:** Native generation of [`/llms.txt`](https://llmstxt.org/) and [`/llms-full.txt`] for consumption by autonomous agents and RAG pipelines.

---

## 📁 Repository Structure

```text
software-docs-engineer/
├── SKILL.md                                  # Core skill instructions, decision trees, and playbooks
├── README.md                                 # Project documentation and installation guide
├── LICENSE                                   # MIT License
├── references/
│   ├── diataxis_framework.md                # Quadrant definitions and anti-pattern catalog
│   ├── arc42_and_c4.md                      # arc42 mapping to ISO 42010 & Mermaid C4 templates
│   ├── api_contracts_and_eda.md             # OpenAPI 3.1, AsyncAPI 3.0, and breaking change rules
│   ├── docs_as_code_and_tests.md            # CI/CD pipelines, Vale linting, and snippet tests
│   ├── drift_mitigation_and_metrics.md      # DX formulas (KaTeX), benchmarks, and PR checklists
│   └── llms_txt_and_agent_readability.md    # llms.txt standard and token-efficient formatting
└── examples/
    ├── madr_template.md                     # Markdown Architecture Decision Record (MADR) template
    └── arc42_starter.md                     # Production-ready arc42 starter template
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

### 2. Claude Code / Codex / Other Agentic Harnesses

Copy the contents of `SKILL.md` or mount the directory into your agent's custom instructions or `.agents/` folder.

---

## 🎯 How to Prompt Your Agent

Once installed, your agent will automatically activate the skill whenever you ask for documentation tasks:

```text
"Document the architecture of this microservice using arc42 and C4 diagrams."
"Create an ADR justifying our migration from REST to Kafka event streaming."
"Generate OpenAPI 3.1 specifications for the /v1/billing endpoints."
"Audit our docs repository to prevent documentation drift and add CI/CD linters."
"Write an llms.txt index for this repository so external agents can understand it."
```

---

## 📐 Key Frameworks & Standards

| Standard / Framework | Scope in this Skill |
| :--- | :--- |
| **ISO/IEC/IEEE 42010:2022** | System architecture descriptions, concerns, viewpoints, and views. |
| **ISO/IEC/IEEE 26500 Series** | Requirements for technical user information and agile documentation (26511 / 26515). |
| **Diátaxis** | Cognitive segregation: Tutorials, How-To Guides, Reference, Explanation. |
| **arc42 (v8.2)** | 12-section standardized architectural communication. |
| **C4 Model** | Context, Container, Component, and Dynamic sequence modeling in Mermaid.js. |
| **MADR 3.x** | Markdown Architectural Decision Records. |
| **OpenAPI 3.1 & AsyncAPI 3.0** | Machine-readable API contracts for synchronous and event-driven architectures. |
| **llms.txt** | Machine-readable markdown indices optimized for AI context windows. |

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE). Contributions and pull requests are welcome!
