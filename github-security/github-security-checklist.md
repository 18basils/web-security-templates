# 🛡️ GitHub Repository Security Checklist & Hardening Guide

A complete, production-tested checklist for securing GitHub repositories when moving from **Private to Public**, setting up **CI/CD**, or enabling **Automated Vulnerability Scanning**.

---

## 📋 Pre-Flight Audit (Before Making a Repository Public)

1. **Scan Git Tree for Secrets & Credentials**:
   * Search commit history for API keys, private certificates, tokens, and passwords:
     ```bash
     git log -p | grep -E "(AIzaSy|sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{20,}|password|secret_key)"
     ```
   * Ensure local configuration files containing user-specific data (e.g. `config.json`, `.env`, `*.keystore`) are listed in `.gitignore`.
2. **Verify Commit Email Privacy**:
   * Go to **GitHub Settings > Emails** and check **"Keep my email addresses private"** and **"Block command line pushes that expose my email"**.
   * Use your privacy email: `<username>@users.noreply.github.com`.
3. **Verify License & Intellectual Property**:
   * Ensure a clear `LICENSE.md` is present (e.g. Proprietary / All Rights Reserved, MIT, Apache 2.0).

---

## 🔒 Automated GitHub Security Suite (Free on Public Repos)

### 1. Secret Scanning & Push Protection
GitHub automatically blocks accidental pushes containing API keys, OAuth tokens, and secrets.
* **Enable via Web**: `Settings > Code security and analysis > Secret scanning > Enable` and enable `Push protection`.
* **Enable via GitHub CLI**:
  ```bash
  gh api -X PUT /repos/:owner/:repo/secret-scanning/push-protection
  ```

### 2. Private Vulnerability Reporting
Allows security researchers to report vulnerabilities privately without public exploit disclosure.
* **Enable via Web**: `Settings > Code security and analysis > Private vulnerability reporting > Enable`.
* **Enable via GitHub CLI**:
  ```bash
  gh api -X PUT /repos/:owner/:repo/private-vulnerability-reporting -f enabled=true
  ```

### 3. Dependabot Alerts & Version Updates
* **Step 1**: Enable vulnerability alerts:
  ```bash
  gh api -X PUT /repos/:owner/:repo/vulnerability-alerts
  gh api -X PUT /repos/:owner/:repo/automated-security-fixes
  ```
* **Step 2**: Deploy `.github/dependabot.yml` (see `github-security/dependabot.template.yml`).
* **⚠️ CRITICAL GOTCHA - Missing Labels Trap**:
  If your `dependabot.yml` defines custom labels (e.g., `dependencies`, `python`, `github-actions`, `android`), **you MUST create those labels in GitHub first**! If they do not exist, Dependabot will fail to label PRs and automatically close them.
  ```bash
  gh label create dependencies --description "Updates dependencies" --color "0366D6"
  gh label create python --description "Python packages" --color "3572A5"
  gh label create github-actions --description "GitHub Actions workflows" --color "2088FF"
  gh label create android --description "Android & Gradle" --color "3DDC84"
  ```

---

## 🔬 CodeQL Code Scanning & Static Analysis (SAST)

### ⚠️ The Monorepo & Multi-Language Trap
* **The Problem**: GitHub CodeQL Default Setup assumes compiled languages (Java/Kotlin, Swift, C/C++, Go) have their build files (`build.gradle`, `.xcodeproj`, `Makefile`) located at the **repository root**.
* If compiled code lives in a subfolder (e.g., `/phone-companion` or `/apple-companion`), default autobuild fails with:
  `ERROR: CodeQL detected code written in Java/Kotlin but could not automatically build any of it.`
* **Solution A (Recommended for Monorepos)**: Restrict CodeQL Default Setup to interpreted/script languages (`python`, `actions`, `javascript`) which require zero build steps:
  ```bash
  python -c "
  import json, subprocess
  payload = json.dumps({'state': 'configured', 'languages': ['actions', 'python'], 'query_suite': 'default'})
  subprocess.run(['gh', 'api', '-X', 'PATCH', '/repos/:owner/:repo/code-scanning/default-setup', '--input', '-'], input=payload, text=True)
  "
  ```
* **Solution B (Advanced Setup)**: Use a dedicated workflow file (`.github/workflows/codeql.yml`) with manual build commands specifying the directory (`cd phone-companion && ./gradlew assembleDebug`).

### ⚠️ CWE-275 Least-Privilege Actions Permissions Alert
CodeQL flags workflows lacking explicit permissions with:
`actions/missing-workflow-permissions: Workflow does not limit the permissions of the GITHUB_TOKEN.`
* **Fix**: Always add an explicit least-privilege `permissions` block to every workflow:
  ```yaml
  permissions:
    contents: read
  ```

---

## 🛡️ Repository Protection Settings

1. **Branch Protection (`Settings > Branches`)**:
   * Branch pattern: `main`
   * Check **"Require a pull request before merging"** (optional for single maintainer).
   * Check **"Do not allow force pushes"** (`git push --force` blocked).
   * Check **"Do not allow deletions"**.
2. **Restrict GitHub Actions for Forks (`Settings > Actions > General`)**:
   * Set **"Fork pull request workflows"** to **"Require approval for all outside collaborators"**.
   * Prevents malicious PRs from secretly executing crypto-miners on your free runner minutes.
3. **Bandwidth Shielding (GitHub Releases vs Free Hosting)**:
   * **Rule**: Never serve files > 10 MB (installers, `.zip`, `.exe`, `.apk`, `.dmg`) from free hosting providers (Firebase Spark, Vercel, Netlify).
   * **Action**: Host all heavy binaries on **GitHub Releases CDN** (free, unlimited bandwidth, up to 2 GB per file).
   * Update download buttons on your website to point to `https://github.com/:owner/:repo/releases/download/vX.Y.Z/...`.

---

## 🏷️ Official Status Badges

Add these to your `README.md` header:

```markdown
<!-- GitHub Releases Badge -->
[![Release](https://img.shields.io/badge/release-v2.0.0-blue?logo=github)](https://github.com/:owner/:repo/releases/latest)

<!-- Native CodeQL Live Badge (Never Stale) -->
[![CodeQL](https://github.com/:owner/:repo/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/:owner/:repo/actions/workflows/github-code-scanning/codeql)

<!-- Security Policy Badge -->
[![Security Policy](https://img.shields.io/badge/security-SECURITY.md-blue)](SECURITY.md)
```
