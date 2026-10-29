# 🛡️ Web Security, Bot Defense & Automation Blueprint Suite

[![GitHub Private/Template](https://img.shields.io/badge/template-modular%20recipes-blue?logo=github)](https://github.com/18basils/web-security-templates)
[![Security Grade](https://img.shields.io/badge/security%20headers-A%2B%20Target-brightgreen)](https://securityheaders.com)
[![CSP Evaluator](https://img.shields.io/badge/CSP-Google%20Evaluator%20Clean-cyan)](https://csp-evaluator.withgoogle.com)
[![PageSpeed](https://img.shields.io/badge/PageSpeed-95--100%20Target-orange)](https://pagespeed.web.dev/)

A modular, production-grade security, optimization, and automation blueprint repository. Designed as an **Agent Execution Playbook** so developers and AI coding agents can parse conditional "Switch Cases" to patch security headers, bot defense policies, repository security, PageSpeed optimizations, and Open Graph cards into any project in seconds.

---

## 🤖 The AI Agent Playbook (`AGENT_RECIPES.md`)

When working with an AI coding assistant, simply tell the agent:
> *"Read `AGENT_RECIPES.md` from `web-security-templates` and patch my website for [Hosting: Firebase/Vercel/Render, Analytics: Enabled, OS Detection: Yes, Repo: Public/Private]."*

The agent will follow the step-by-step conditional logic in **[`AGENT_RECIPES.md`](AGENT_RECIPES.md)** to configure only what is required without introducing unnecessary overhead.

---

## 📁 Repository Directory Structure

```
web-security-templates/
├── AGENT_RECIPES.md                   # 🤖 Master conditional switch-case playbook for AI agents
├── README.md                          # 📖 Main documentation & usage guide
│
├── hosting/                           # 🌐 Hosting provider security headers
│   ├── firebase.template.json         # Firebase Hosting (headers array, HSTS, CSP, cache)
│   ├── vercel.template.json           # Vercel (vercel.json headers & cleanUrls)
│   ├── render.template.yaml           # Render static site blueprint (render.yaml)
│   ├── _headers.template              # Universal _headers for Cloudflare Pages & Netlify
│   ├── security-headers.nginx.conf    # Nginx drop-in server block include
│   └── .htaccess.template             # Apache HTTP Server drop-in configuration
│
├── github-security/                   # 🔒 GitHub repository hardening & CI/CD
│   ├── github-security-checklist.md   # Step-by-step checklist (Public vs. Private repos)
│   ├── dependabot.template.yml        # Universal Dependabot configuration (pip, npm, gradle, actions)
│   ├── codeql-advanced.template.yml   # Custom CodeQL workflow for monorepos & compiled languages
│   └── SECURITY.template.md           # Responsible vulnerability disclosure policy
│
├── github-boilerplate/                # 📑 Complete Markdown & issue boilerplate
│   ├── README.template.md             # Modern high-converting README with badge row & tabs
│   ├── CONTRIBUTING.template.md       # Code of conduct, coding standards, and PR process
│   ├── PULL_REQUEST_TEMPLATE.template.md # Structured PR checklist (quality & security)
│   ├── CHANGELOG.template.md          # Keep a Changelog format (Semantic Versioning 2.0.0)
│   ├── markdown-tab-cheatsheet.md     # Native Markdown collapsible tab/accordion cheatsheet
│   └── issue-templates/               # GitHub YAML issue forms (Bug report, Feature, Config)
│
├── pagespeed-and-performance/         # ⚡ 100/100 Core Web Vitals & CSP Evaluator
│   ├── pagespeed-checklist.md         # Preconnects, CLS=0, critical CSS, WebP & caching
│   └── csp-evaluator-guide.md         # Passing Google CSP Evaluator with zero high-severity warnings
│
├── client-features/                   # 💻 Modular client-side scripts & manifests
│   ├── device-detection.template.js   # Zero-dependency OS detector (Windows, Android, macOS, iOS, Linux)
│   ├── tab-view.template.html         # Accessible WAI-ARIA dark glassmorphic web tab component
│   └── manifest.template.json         # Universal Progressive Web App (PWA) manifest
│
└── social-and-crawlers/               # 🕷️ Crawler defense & social sharing
    ├── robots.template.txt            # Hardened robots.txt (allows search bots, blocks AI scrapers)
    ├── html-head-meta.template.html   # SEO, OpenGraph, Twitter Cards & PWA head tags
    ├── opengraph-banner-requirements.template.md # 1200x630, <300 KB WhatsApp rule & safe zones
    └── generate_og_banner.template.py # 1-click Python PIL script to generate dark-gradient banners
```

---

## 🔀 Decision Matrix Overview

| Project Requirement | Condition | Template / Action to Apply |
| :--- | :--- | :--- |
| **Hosting: Firebase** | Target deploys to Firebase | Copy or merge `hosting/firebase.template.json` |
| **Hosting: Vercel** | Target deploys to Vercel | Copy or merge `hosting/vercel.template.json` |
| **Hosting: Render** | Target deploys to Render | Use `hosting/render.template.yaml` |
| **Hosting: Cloudflare / Netlify** | Target uses static edge pages | Copy `hosting/_headers.template` to publish root as `_headers` |
| **Hosting: Nginx / Apache** | Traditional web server | Include `hosting/security-headers.nginx.conf` or `hosting/.htaccess.template` |
| **Custom Paid Domain** | Bought apex/subdomain | Enable `includeSubDomains; preload` in HSTS, canonical link, domain restrictions in GA4 |
| **Google Analytics (GA4)** | Analytics enabled | Whitelist GTM in CSP (`script-src`, `connect-src`), add DNS prefetch & preconnect |
| **Google Fonts** | External web fonts | Whitelist in CSP (`style-src`, `font-src`), add preconnect to Google Fonts |
| **Heavy Binaries (> 10 MB)** | Distributing software | **Never host on free hosting storage**; route to GitHub Releases CDN + `X-Robots-Tag: noindex` |
| **OS / Device Detection** | Multiplatform app downloads | Drop in `client-features/device-detection.template.js` |
| **PWA Web App** | Installable mobile/desktop web app | Drop in `client-features/manifest.template.json` |
| **GitHub: Public Repo** | Releasing code publicly | Enable Secret Scanning, Push Protection, Private Vulnerability Reporting, Fork Actions guard |
| **Dependabot Updates** | Automated dependency bumps | Deploy `github-security/dependabot.template.yml` + **create labels first** (`gh label create ...`) |
| **CodeQL Code Scanning** | Monorepo / Multi-language | Restrict Default Setup to interpreted languages (`actions`, `python`), add `permissions: contents: read` |
| **PageSpeed 100/100** | Core Web Vitals optimization | Apply `pagespeed-and-performance/pagespeed-checklist.md` (CLS=0, preconnect, defer JS) |
| **Open Graph Banners** | Social media link previews | Follow `< 300 KB` rule (WhatsApp) or run `social-and-crawlers/generate_og_banner.template.py` |
| **Repo Documentation** | Setting up clean docs | Deploy `github-boilerplate/` (`README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, Issue templates) |
| **Tab Views (Markdown)** | Multi-platform README docs | Use `<details><summary>` accordion tabs from `github-boilerplate/markdown-tab-cheatsheet.md` |
| **Tab Views (Web UI)** | Interactive web platform/code tabs | Use accessible WAI-ARIA component from `client-features/tab-view.template.html` |

---

## 🔍 Testing & Verification Tools

Once deployed, verify your configurations with these free industry audit tools:

1. **Security Headers Grade (Target: A+)**: [https://securityheaders.com](https://securityheaders.com)
2. **Google CSP Evaluator (Target: Clean)**: [https://csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com)
3. **Google PageSpeed Insights (Target: 95–100)**: [https://pagespeed.web.dev/](https://pagespeed.web.dev/)
4. **Social Sharing Debugger**: [https://www.opengraph.xyz](https://www.opengraph.xyz)
5. **HSTS Preload Verification**: [https://hstspreload.org](https://hstspreload.org)
