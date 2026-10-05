# The `llms.txt` Standard: Documentation for Autonomous Agents and AI

As autonomous coding agents (like Gemini, Claude, Cursor, and Copilot Workspace) increasingly navigate software repositories, technical documentation must serve two audiences simultaneously: human engineers and language models.

The `llms.txt` file (standardized at [llmstxt.org](https://llmstxt.org/)) serves as an AI-oriented index of project documentation, stripping away heavy frontend HTML, CSS, JavaScript, and navigation sidebars in favor of lean, semantic markdown.

---

## 1. Specification of `llms.txt`

Place an `llms.txt` file at the root of your project or documentation portal (`/llms.txt`):

```markdown
# Project Name

> High-level summary of the software system (1-2 sentences).

## Documentation

- [Getting Started](https://example.com/docs/quickstart.md): Tutorial for new developers.
- [Architecture Overview](https://example.com/docs/architecture.md): arc42 summary and C4 container topology.
- [API Reference](https://example.com/docs/api.md): Endpoints, payloads, and error codes.
- [Configuration Reference](https://example.com/docs/config.md): Environment variables and CLI flags.

## Optional Reference Links

- [Changelog](https://example.com/CHANGELOG.md): Historical versions and breaking changes.
- [Architecture Decision Records](https://example.com/docs/adr/): Log of accepted ADRs.
```

---

## 2. Best Practices for Agent-Friendly Documentation

1. **Clear Header Hierarchies:** Always use monotonic heading levels (`#` -> `##` -> `###`). Avoid skipping levels (e.g., `#` followed immediately by `####`).
2. **Explicit Language Blocks:** Always specify the syntax identifier on triple-backtick blocks (e.g., ```` ```typescript ````, ```` ```yaml ````, ```` ```bash ````). Never leave code fences untyped.
3. **Structured Tables for Discrete Data:** Use markdown tables for matrices of parameters, error codes, and configuration options.
4. **Self-Contained File Paths:** When referencing files, use unambiguous paths from the repository root (e.g., `src/services/auth.ts` instead of `auth.ts`).
5. **Zero Ambiguity in Commands:** Do not embed interactive CLI placeholders without clear notation (use `<placeholder>` or uppercase `VARIABLE` consistently).
