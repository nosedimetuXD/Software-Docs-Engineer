# The Diátaxis Framework: Systematic Architecture of Technical Documentation

The Diátaxis framework, developed by Daniele Procida, structures documentation according to four distinct user needs across two cognitive axes:
1. **Theory vs. Practice** (Axis of Thought vs. Action).
2. **Learning vs. Working** (Axis of Acquisition vs. Application).

```text
               PRACTICAL CRAFT
                      ▲
                      │
     How-To Guides    │    Tutorials
     (Problem-oriented)│    (Learning-oriented)
                      │
ACQUISITION ──────────┼────────── APPLICATION
OF SKILL              │          OF SKILL
                      │
     Reference        │    Explanation
     (Information-    │    (Understanding-
      oriented)       │     oriented)
                      │
                      ▼
              THEORETICAL KNOWLEDGE
```

---

## 1. The Four Quadrants

### Quadrant 1: Tutorials (Learning-Oriented)
- **Role:** Taking a beginner by the hand and delivering a reliable, predictable learning experience.
- **Tone:** Encouraging, step-by-step, directive.
- **Critical Rules:**
  - Every step must be reproducible and yield immediate, verifiable output.
  - Do NOT explain options, alternative configs, or deep theory.
  - Do NOT assume prior tooling knowledge (e.g., if a CLI tool is needed, show how to run it).
  - Minimum cognitive load: Provide a single golden path to a working "Hello World".

### Quadrant 2: How-To Guides (Problem-Oriented)
- **Role:** Assisting a practitioner in solving a specific real-world problem or use case.
- **Tone:** Direct, efficient, recipe-style.
- **Critical Rules:**
  - Assumes basic competence: The reader already knows what the system is and how to launch it.
  - Title must follow an action pattern: *"How to [perform action]..."* (e.g., *"How to configure Redis caching in production"*).
  - Focus strictly on the goal; omit tutorial hand-holding and deep philosophical background.

### Quadrant 3: Reference (Information-Oriented)
- **Role:** Providing an authoritative, austere, and complete description of the system's machinery.
- **Tone:** Neutral, precise, exhaustive.
- **Critical Rules:**
  - Structure follows the code architecture: modules, classes, API endpoints, configuration schemas, CLI flags.
  - Contains exact specifications: parameter names, types, default values, ranges, error codes, HTTP status responses.
  - Must remain strictly up to date with code contracts.

### Quadrant 4: Explanation (Understanding-Oriented)
- **Role:** Clarifying the architectural context, historical rationale, and design trade-offs of the system.
- **Tone:** Discursive, reflective, illuminating.
- **Critical Rules:**
  - Answers *why* things are designed the way they are.
  - Explores alternatives that were considered and rejected.
  - Does not contain step-by-step instructions or dry parameter lists.

---

## 2. Preventing Cross-Quadrant Contamination

| Anti-Pattern | Root Cause | Consequence | Remedy |
| :--- | :--- | :--- | :--- |
| **Tutorial with Theory Dumps** | Explaining architectural details inside a step-by-step guide. | Cognitive overload; learner fails to complete the tutorial. | Move theory to an **Explanation** document and link to it. |
| **How-To as Reference** | Listing every possible configuration flag in a practical recipe. | The recipe becomes bloated and impossible to scan. | Put flags in **Reference**; keep only relevant flags in the How-To. |
| **Reference with Tutorial Stories** | Adding conversational instructions in API parameter descriptions. | Developers seeking fast lookup are slowed down. | Keep reference strictly tabular/declarative; link to a How-To. |
| **Explanation with Code Instructions** | Mixing imperative setup commands into an architectural discussion. | Reader gets confused between understanding concepts and executing changes. | Extract commands into a How-To; leave explanation conceptual. |
