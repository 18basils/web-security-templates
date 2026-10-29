# 🛡️ Web Security, Bot Defense & Automation Blueprint Suite

[![GitHub Template](https://img.shields.io/badge/template-modular%20recipes-blue?logo=github)](AGENT_RECIPES.md)
[![CodeQL](https://github.com/18basils/web-security-templates/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/18basils/web-security-templates/actions/workflows/github-code-scanning/codeql)
[![Security Grade](https://img.shields.io/badge/security%20headers-A%2B%20Target-brightgreen)](https://securityheaders.com)
[![CSP Evaluator](https://img.shields.io/badge/CSP-Google%20Evaluator%20Clean-cyan)](https://csp-evaluator.withgoogle.com)
[![PageSpeed](https://img.shields.io/badge/PageSpeed-95--100%20Target-orange)](https://pagespeed.web.dev/)
[![Propose an Idea](https://img.shields.io/badge/ideas-propose%20a%20recipe-blueviolet)](https://github.com/18basils/web-security-templates/issues/new/choose)
[![Security Policy](https://img.shields.io/badge/security-SECURITY.md-blue)](SECURITY.md)
[![License](https://img.shields.io/badge/license-terms-lightgrey)](LICENSE.md)

A modular, production-grade security, optimization, and automation blueprint repository. Designed as an **Agent Execution Playbook** so developers and AI coding agents can parse conditional "Switch Cases" to patch security headers, bot defense policies, repository security, PageSpeed optimizations, Open Graph cards, and live `.md` / GitHub `About` metadata synchronization into any project in one command—**without ever overriding or breaking the target product's intended purpose**.

---

## 🤖 The AI Agent Playbook (`AGENT_RECIPES.md`)

When working with an AI coding assistant, simply tell the agent:
> *"Read `AGENT_RECIPES.md` from `18basils/web-security-templates` and parse & patch my project in one go."*

The agent will follow **[`AGENT_RECIPES.md`](AGENT_RECIPES.md)** to:
1. **Preserve Product Intent (Golden Rule 0)**: Inspect your app's features, APIs, and branding first so security headers and CSP rules adapt to your product without breaking anything.
2. **Apply Conditional Switch-Cases (CASES 1–10)**: Configure only the hosting headers, crawler defenses, GitHub security settings, PageSpeed optimizations, and UI components your project actually needs.
3. **Auto-Sync `.md` Files & GitHub `About`/Topics (CASE 11)**: Automatically detect changes from your latest commits and live website to update `README.md`, `CHANGELOG.md`, and your GitHub repository's `About` description, live URL, and topic tags without manual intervention.

---

## 📁 Repository Directory Structure

```
web-security-templates/
├── AGENT_RECIPES.md                   # 🤖 Master conditional switch-case playbook for AI agents
├── README.md                          # 📖 Main documentation & usage guide
├── CONTRIBUTING.md                    # 💡 Idea-only contribution guide & credit system
├── SECURITY.md                        # 🔒 Vulnerability disclosure policy
├── LICENSE.md                         # ⚖️ Copyright & license terms
│
├── hosting/                           # 🌐 Hosting provider security headers & caching
│   ├── firebase.template.json         # Firebase Hosting (headers array, HSTS, CSP, SPA rewrites, cache)
│   ├── vercel.template.json           # Vercel (vercel.json headers, cleanUrls & cache controls)
│   ├── render.template.yaml           # Render static site blueprint (render.yaml)
│   ├── _headers.template              # Universal _headers for Cloudflare Pages & Netlify
│   ├── security-headers.nginx.conf    # Nginx drop-in server block include (inheritance-safe)
│   ├── .htaccess.template             # Apache 2.4+ HTTP Server drop-in configuration
│   └── security.template.txt          # RFC 9116 /.well-known/security.txt vulnerability contact
│
├── github-security/                   # 🔒 GitHub repository hardening & CI/CD
│   ├── github-security-checklist.md   # Step-by-step checklist (CWE-275, CWE-338 randomness, rulesets)
│   ├── dependabot.template.yml        # Universal Dependabot configuration (npm, pip, gradle, actions)
│   ├── codeql-advanced.template.yml   # Custom SHA-pinned CodeQL workflow for monorepos & compiled languages
│   └── SECURITY.template.md           # Responsible vulnerability disclosure policy template
│
├── github-boilerplate/                # 📑 Complete Markdown & issue boilerplate
│   ├── README.template.md             # Modern high-converting README with badge row & tabs
│   ├── CONTRIBUTING.template.md       # Code of conduct, coding standards, and PR process
│   ├── PULL_REQUEST_TEMPLATE.template.md # Structured PR checklist (quality & security)
│   ├── CHANGELOG.template.md          # Keep a Changelog format (Semantic Versioning 2.0.0)
│   ├── LICENSE-PROPRIETARY.template.md # All-rights-reserved terms of use for commercial/proprietary products
│   ├── markdown-tab-cheatsheet.md     # Native Markdown collapsible tab/accordion cheatsheet
│   └── issue-templates/               # GitHub YAML issue forms (Bug report, Feature, Config)
│
├── pagespeed-and-performance/         # ⚡ 100/100 Core Web Vitals & CSP Evaluator
│   ├── pagespeed-checklist.md         # Preconnects, CLS=0, critical CSS, WebP & caching
│   ├── vite.config.template.js        # High-performance Vite bundler with multi-chunk vendor splitting
│   └── csp-evaluator-guide.md         # Passing Google CSP Evaluator with zero high-severity warnings
│
├── client-features/                   # 💻 Modular client-side scripts & manifests
│   ├── device-detection.template.js   # Zero-dependency OS detector (Windows, Android, macOS, iOS, Linux)
│   ├── tab-view.template.html         # Accessible WAI-ARIA dark glassmorphic web tab component
│   ├── manifest.template.json         # Universal Progressive Web App (PWA) manifest
│   └── sw.template.js                 # Same-origin PWA Service Worker (Stale-While-Revalidate + Cache Bypass)
│
└── social-and-crawlers/               # 🕷️ Crawler defense & social sharing
    ├── robots.template.txt            # Hardened robots.txt (allows search bots & OG, blocks AI scrapers)
    ├── html-head-meta.template.html   # SEO, OpenGraph, Twitter Cards, PWA head tags & Schema.org JSON-LD
    ├── opengraph-banner-requirements.template.md # 1200x630, <300 KB WhatsApp rule & safe zones
    └── generate_og_banner.template.py # 1-click Python PIL script to generate dark-gradient banners
```

---

## 🔀 Decision Matrix Overview

| Project Requirement | Condition | Template / Action to Apply |
| :--- | :--- | :--- |
| **Product Intent Protection** | **Always (Golden Rule 0)** | **Never override or break product features/purpose**; adapt CSP & headers to the app |
| **Hosting: Firebase** | Target deploys to Firebase | Copy or merge `hosting/firebase.template.json` (includes SPA rewrites & cache headers) |
| **Hosting: Vercel** | Target deploys to Vercel | Copy or merge `hosting/vercel.template.json` |
| **Hosting: Render** | Target deploys to Render | Use `hosting/render.template.yaml` |
| **Hosting: Cloudflare / Netlify** | Target uses static edge pages | Copy `hosting/_headers.template` to publish root as `_headers` |
| **Hosting: Nginx / Apache** | Traditional web server | Include `hosting/security-headers.nginx.conf` or `hosting/.htaccess.template` |
| **RFC 9116 Security Contact** | Any public web application | Copy `hosting/security.template.txt` to `/.well-known/security.txt` |
| **Custom Paid Domain** | Bought apex/subdomain | Enable `includeSubDomains; preload` in HSTS, canonical link, domain restrictions in GA4 |
| **Google Analytics (GA4)** | Analytics enabled | Whitelist GTM in CSP (`script-src`, `connect-src`), add DNS prefetch & preconnect |
| **Google Fonts** | External web fonts | Whitelist in CSP (`style-src`, `font-src`), add preconnect to Google Fonts |
| **Heavy Binaries (> 10 MB)** | Distributing software | **Never host on free hosting storage**; route to GitHub Releases CDN + `X-Robots-Tag: noindex` |
| **OS / Device Detection** | Multiplatform app downloads | Drop in `client-features/device-detection.template.js` |
| **PWA Web App** | Installable mobile/desktop web app | Drop in `client-features/manifest.template.json` + `client-features/sw.template.js` |
| **GitHub: Public Repo** | Releasing code publicly | Enable Secret Scanning, Push Protection, Private Vulnerability Reporting, Fork Actions guard |
| **Dependabot Updates** | Automated dependency bumps | Deploy `github-security/dependabot.template.yml` + **create labels first** (`gh label create ...`) |
| **CodeQL Code Scanning** | Monorepo / Multi-language | Restrict Default Setup to interpreted languages (`actions`, `python`, `javascript`), fix CWE-275 & CWE-338 |
| **PageSpeed 100/100** | Core Web Vitals optimization | Apply `pagespeed-and-performance/pagespeed-checklist.md` + `vite.config.template.js` (manual chunks) |
| **Open Graph Banners** | Social media link previews | Follow `< 300 KB` rule (WhatsApp) or run `social-and-crawlers/generate_og_banner.template.py` |
| **Proprietary Commercial License** | Closed-source / proprietary product | Deploy `github-boilerplate/LICENSE-PROPRIETARY.template.md` as `LICENSE.md` |
| **Repo Documentation** | Setting up clean docs | Deploy `github-boilerplate/` (`README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, Issue templates) |
| **Tab Views (Markdown)** | Multi-platform README docs | Use `<details><summary>` accordion tabs from `github-boilerplate/markdown-tab-cheatsheet.md` |
| **Tab Views (Web UI)** | Interactive web platform/code tabs | Use accessible WAI-ARIA component from `client-features/tab-view.template.html` |
| **Auto-Sync `.md` & GitHub `About`** | **Always (CASE 11)** | Detect drift from commits/live site and auto-update `*.md`, GitHub `About` description, URL, and `topics` |

---

## 🔍 Testing & Verification Tools

Once deployed, verify your configurations with these free industry audit tools:

1. **Security Headers Grade (Target: A+)**: [https://securityheaders.com](https://securityheaders.com)
2. **Google CSP Evaluator (Target: Clean)**: [https://csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com)
3. **Google PageSpeed Insights (Target: 95–100)**: [https://pagespeed.web.dev/](https://pagespeed.web.dev/)
4. **Social Sharing Debugger**: [https://www.opengraph.xyz](https://www.opengraph.xyz)
5. **HSTS Preload Verification**: [https://hstspreload.org](https://hstspreload.org)

---

## 💡 Have a New Idea? (Propose a Recipe & Get Credited!)

To maintain strict security auditing across all blueprints, this repository uses an **Idea-Only Contribution Model** (we do not accept external Pull Requests directly).

* **Suggest an Idea**: Open a **[💡 Propose a New Template / Security Recipe](https://github.com/18basils/web-security-templates/issues/new?template=recipe_proposal.yml)** issue describing a new hosting config, CSP rule, crawler policy, or optimization.
* **Report a Bug**: Open a **[🐛 Report a Template Bug / Header Issue](https://github.com/18basils/web-security-templates/issues/new?template=template_bug.yml)** if you spot a false positive or syntax issue.
* **Maintainer Implementation & Credits**: If your proposal is approved, **`@18basils`** will build, test, and integrate it into the suite and credit you in the **Community Idea Contributors** Hall of Fame below! See **[`CONTRIBUTING.md`](CONTRIBUTING.md)** for full details.

### 🏆 Community Idea Contributors

| Contributor | Credited Recipe / Improvement | Issue |
| :--- | :--- | :--- |
| **[@18basils](https://github.com/18basils)** | Creator & Maintainer of the Web Security Blueprint Suite | — |
| *Your name here!* | *[Submit a Recipe Proposal](https://github.com/18basils/web-security-templates/issues/new?template=recipe_proposal.yml) to get featured!* | — |
