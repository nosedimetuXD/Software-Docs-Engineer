# Docs-as-Code & Docs-as-Tests Implementation

The Docs-as-Code philosophy treats technical content as first-class software deliverables: authored in plain text, stored in version control, reviewed via Pull Requests, and verified through automated continuous integration (CI) pipelines.

---

## 1. Docs-as-Code Pipeline Architecture

```text
┌─────────────────┐       ┌────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Git Commit / PR │ ───►  │ Linter Checks  │ ───►  │  Docs-as-Tests  │ ───►  │ Static Portal   │
│ Markdown Source │       │ (Vale, md-lint)│       │ (Doc Detective) │       │ (SSG / CDN)     │
└─────────────────┘       └────────────────┘       └─────────────────┘       └─────────────────┘
```

### Components of the Toolchain:
1. **Markup Language:** CommonMark Markdown, MDX, or AsciiDoc.
2. **Structural Linter:** `markdownlint` to enforce consistent header depth, table formatting, and block syntax.
3. **Prose Linter:** `Vale` for style guide enforcement (spelling, tone of voice, forbidden words, inclusive terminology).
4. **Link Checker:** `lychee` or `markdown-link-check` to intercept broken internal and external URLs before deployment.
5. **Static Site Generators (SSG):** Docusaurus (React/MDX), Material for MkDocs (Python/Fast), Starlight (Astro), or Hugo.

---

## 2. Docs-as-Tests: Verifying Code Snippets

Documentation quickly becomes misleading when code examples break due to underlying API refactoring. Docs-as-Tests automates the verification of code blocks in markdown:

### Tools:
- **Doc Detective:** Executes end-to-end user tests directly from instructional steps in docs against real APIs or headless browsers.
- **markdown-code-runner / byexample:** Extracts code snippets (Python, TypeScript, Bash, etc.) from ` ``` ` blocks, executes them in an isolated test environment, and asserts that the actual stdout matches the output printed in the doc.

### Example in GitHub Actions

```yaml
name: Documentation CI

on:
  pull_request:
    paths:
      - 'docs/**'
      - '*.md'

jobs:
  validate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Markdownlint
        uses: DavidAnson/markdownlint-cli2-action@v16
        with:
          globs: 'docs/**/*.md'

      - name: Run Vale Prose Linter
        uses: errata-ai/vale-action@reviewdog
        with:
          files: 'docs'

      - name: Check Broken Links
        uses: lycheeverse/lychee-action@v1
        with:
          args: '--no-progress docs/**/*.md'

      - name: Run Docs-as-Tests Snippets
        run: |
          npx doc-detective run --input docs/
```
