# 💡 Contributing Ideas & Security Recipes

Thank you for your interest in improving **`web-security-templates`**!

To keep all security configurations, CSP rules, and AI Agent Playbook switch-cases strictly audited, cohesive, and free of regressions, **this repository uses an Idea-Only Contribution Model**.

---

## 🚫 Why No External Pull Requests?

Security headers, crawler policies, and CI/CD templates require uniform structure and strict verification against our AI Agent Playbook (`AGENT_RECIPES.md`). Therefore, **we do not accept external Pull Requests directly**.

Instead, **you share the idea, and the maintainer (`@18basils`) builds, verifies, and integrates it**—while giving you full credit!

---

## 🛠️ How to Propose a New Idea or Report an Issue

### 1. 💡 Propose a New Template or Security Recipe
Have a great idea for a new hosting provider config, a third-party CSP recipe, a new AI crawler rule, a PageSpeed optimization, or a client feature?

1. Go to **[Issues > New Issue](https://github.com/18basils/web-security-templates/issues/new/choose)**.
2. Select **"💡 Propose a New Template / Security Recipe"**.
3. Fill out:
   * **Category** (Hosting Headers, CSP Matrix, Bot/AI Crawler Defense, GitHub CI/CD, PageSpeed, Client Feature, etc.)
   * **Problem / Use Case** (Why is this needed?)
   * **Draft Idea or Reference** (Optional snippet, link, or specification)
   * **Credit Handle** (How you'd like to be credited in `README.md` once implemented)

### 2. 🐛 Report a Bug or False Positive
Found a header syntax issue, a CSP directive blocking a legitimate service, or an outdated specification?

1. Go to **[Issues > New Issue](https://github.com/18basils/web-security-templates/issues/new/choose)**.
2. Select **"🐛 Report a Template Bug / Header Issue"**.
3. Share the affected file path and scanner/browser output.

### 3. 🔒 Report a Security Vulnerability
If you discover a security vulnerability in any template or script in this repository, **do not open a public issue**. Please report it privately via **[GitHub Private Vulnerability Reporting](https://github.com/18basils/web-security-templates/security/advisories/new)** (see [`SECURITY.md`](SECURITY.md)).

---

## 🏆 Contributor Recognition & Credits

When your proposed idea or bug report is approved and implemented by `@18basils`:

1. **README Hall of Fame**: Your name / GitHub handle (`@username`) and a link to the recipe you inspired will be added to the **🏆 Community Idea Contributors** section in [`README.md`](README.md).
2. **Commit & Release Attribution**: The implementation commit and release notes will explicitly reference your proposal issue (`Suggested by @username in #issue`).
