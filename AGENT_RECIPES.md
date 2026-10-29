# 🤖 AI Agent Execution Playbook: Conditional Web & Repo Patching

This document is the **Master Decision Matrix** for AI coding agents. When instructed to audit, secure, or patch a web project, evaluate the target project against the following conditional cases ("Switch Cases") and apply the corresponding templates and configurations.

---

## 🔀 Decision Matrix Index

* [CASE 1: Hosting Platform Configuration](#case-1-hosting-platform-configuration)
* [CASE 2: Domain Type (Custom Domain vs. Free Subdomain)](#case-2-domain-type-custom-domain-vs-free-subdomain)
* [CASE 3: Third-Party Integrations & CSP Matrix](#case-3-third-party-integrations--csp-matrix)
* [CASE 4: Heavy Binary Downloads & Bandwidth Shielding](#case-4-heavy-binary-downloads--bandwidth-shielding)
* [CASE 5: Smart Client-Side Features (OS Detection & PWA)](#case-5-smart-client-side-features-os-detection--pwa)
* [CASE 6: GitHub Repository Security (Public vs. Private)](#case-6-github-repository-security-public-vs-private)
* [CASE 7: PageSpeed & 100/100 Core Web Vitals](#case-7-pagespeed--100100-core-web-vitals)
* [CASE 8: Open Graph (OG) & Social Sharing](#case-8-open-graph-og--social-sharing)
* [CASE 9: GitHub Repository Documentation & Boilerplate](#case-9-github-repository-documentation--boilerplate)
* [CASE 10: Tab Views & Multi-Platform Switchers](#case-10-tab-views--multi-platform-switchers)

---

## CASE 1: Hosting Platform Configuration

Examine the hosting platform used by the target project:

```text
SWITCH (target.hostingPlatform):
```

### 1.1 IF `hostingPlatform == "firebase"`:
1. Copy `hosting/firebase.template.json` to the project root as `firebase.json` (or merge the `"headers"` array into the existing `firebase.json`).
2. Ensure public folder matches target (`"public": "public"` or `"public": "dist"`).
3. Test locally with `firebase emulators:start --only hosting`.
4. Deploy with `firebase deploy --only hosting`.

### 1.2 IF `hostingPlatform == "vercel"`:
1. Copy `hosting/vercel.template.json` to the project root as `vercel.json` (or merge the `"headers"` array).
2. Deploy via `vercel --prod` or GitHub Git integration.

### 1.3 IF `hostingPlatform == "render"`:
1. Copy `hosting/render.template.yaml` to project root as `render.yaml`.
2. Ensure `staticPublishPath` points to your build directory (e.g. `./public` or `./dist`).

### 1.4 IF `hostingPlatform in ["cloudflare-pages", "netlify"]`:
1. Copy `hosting/_headers.template` into the publish root directory as `_headers`.
2. Verify that `_headers` is copied into the final build artifact (e.g. `/public/_headers` or `/dist/_headers`).

### 1.5 IF `hostingPlatform == "nginx"`:
1. Place `hosting/security-headers.nginx.conf` in `/etc/nginx/conf.d/security-headers.conf`.
2. Inside your `server { ... }` block, add:
   ```nginx
   include /etc/nginx/conf.d/security-headers.conf;
   ```
3. Test and reload: `sudo nginx -t && sudo nginx -s reload`.

### 1.6 IF `hostingPlatform == "apache"`:
1. Copy `hosting/.htaccess.template` into your document root as `.htaccess`.
2. Ensure `mod_headers`, `mod_rewrite`, and `mod_mime` are enabled in Apache.

---

## CASE 2: Domain Type (Custom Domain vs. Free Subdomain)

```text
IF target.hasCustomPaidDomain (e.g. example.com):
```
1. **HSTS Preload**: Set `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`. (Submit domain to [https://hstspreload.org](https://hstspreload.org)).
2. **Canonical URL**: Add in `<head>`: `<link rel="canonical" href="https://example.com/">`.
3. **Google Analytics Restriction**: In Google Analytics Admin > Data Streams > Configure tag settings, restrict allowed measurement origins to ONLY `example.com` to prevent spam bots from polluting metrics.

```text
ELSE IF target.usesFreeSubdomain (e.g. *.web.app, *.vercel.app, *.onrender.com):
```
1. **HSTS**: Use `Strict-Transport-Security: max-age=31536000; includeSubDomains` (omit `preload` because public suffix subdomains cannot be preloaded globally).
2. **Canonical URL**: Set `<link rel="canonical" href="https://your-subdomain.web.app/">`.

---

## CASE 3: Third-Party Integrations & CSP Matrix

Evaluate required third-party services and patch the `Content-Security-Policy` header:

### 3.1 Base Strict CSP (Always Include):
```text
default-src 'self';
frame-ancestors 'none';
base-uri 'self';
form-action 'self';
object-src 'none';
```

### 3.2 IF `features.googleAnalytics == true`:
* **HTML `<head>`**:
  ```html
  <link rel="preconnect" href="https://www.googletagmanager.com">
  <link rel="dns-prefetch" href="https://www.google-analytics.com">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  ```
* **CSP Header Additions**:
  * `script-src`: add `https://www.googletagmanager.com`
  * `img-src`: add `https://*.google-analytics.com https://*.googletagmanager.com`
  * `connect-src`: add `https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com`

### 3.3 IF `features.googleFonts == true`:
* **HTML `<head>`**:
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  ```
* **CSP Header Additions**:
  * `style-src`: add `https://fonts.googleapis.com`
  * `font-src`: add `https://fonts.gstatic.com`

### 3.4 IF `features.qrCodeGenerator == true` (e.g. qrserver):
* **CSP Header Additions**:
  * `img-src`: add `https://api.qrserver.com`

### 3.5 IF `features.stripePayments == true`:
* **CSP Header Additions**:
  * `script-src`: add `https://js.stripe.com`
  * `frame-src`: add `https://js.stripe.com`

### 3.6 IF `features.strictCSPWithoutInline == true`:
* Replace `'unsafe-inline'` in `script-src` with exact SHA-256 script hashes (`'sha256-...'`) or request nonces (`'nonce-...'`).

---

## CASE 4: Heavy Binary Downloads & Bandwidth Shielding

```text
IF target.hasHeavyBinaries (> 10 MB, e.g. .zip, .exe, .apk, .dmg, .ipa):
```

1. **⚠️ NEVER host binaries directly on free hosting storage**:
   * 10 downloads of a 70 MB file burns 700 MB. Free Firebase Spark tier has a 360 MB/day limit (HTTP 503 Over Quota!).
2. **Deploy to GitHub Releases CDN**:
   * Upload all binaries as release assets via GitHub Releases.
   * Point all website download buttons to `https://github.com/:owner/:repo/releases/download/vX.Y.Z/FileName.zip`.
   * Benefits: Free, unlimited, global high-speed CDN.
3. **Shield Local Download Routes**:
   * If any `/downloads/**` files exist locally, apply:
     * `X-Robots-Tag: noindex, nofollow, noarchive, nosnippet`
     * `Content-Disposition: attachment`
     * `Cache-Control: public, max-age=86400`
   * Add `Disallow: /downloads/` in `robots.txt`.

---

## CASE 5: Smart Client-Side Features (OS Detection & PWA)

### 5.1 IF `features.deviceAutoDetection == true`:
1. Copy `client-features/device-detection.template.js` into project `js/` folder.
2. Ensure download cards in HTML carry IDs: `card-windows`, `card-android`, `card-macos`, `card-ios`.
3. Ensure primary CTA button carries ID `primaryDownloadBtn` and badge carries `deviceBadge`.

### 5.2 IF `features.progressiveWebApp == true`:
1. Copy `client-features/manifest.template.json` to web root as `manifest.json`.
2. Add in HTML `<head>`:
   ```html
   <link rel="manifest" href="/manifest.json">
   <meta name="theme-color" content="#080c15">
   <link rel="apple-touch-icon" href="/assets/icon-180.png">
   ```

---

## CASE 6: GitHub Repository Security (Public vs. Private)

### 6.1 IF `repo.visibility == "public"`:
1. **Secret Scanning & Push Protection**:
   ```bash
   gh api -X PUT /repos/:owner/:repo/secret-scanning/push-protection
   ```
2. **Private Vulnerability Reporting**:
   ```bash
   gh api -X PUT /repos/:owner/:repo/private-vulnerability-reporting -f enabled=true
   ```
3. **Fork Workflow Protection**: In `Settings > Actions > General`, set fork pull requests to "Require approval for all outside collaborators".
4. **Branch Protection**: Protect `main` branch against force-pushes (`git push --force`) and deletions.
5. **Dependabot Configuration**:
   * Deploy `github-security/dependabot.template.yml` as `.github/dependabot.yml`.
   * **MANDATORY STEP**: Create repository labels first to prevent Dependabot PR failures:
     ```bash
     gh label create dependencies --description "Updates dependencies" --color "0366D6"
     gh label create python --description "Python dependencies" --color "3572A5"
     gh label create github-actions --description "GitHub Actions workflows" --color "2088FF"
     ```
6. **CodeQL SAST Scanning**:
   * **Monorepo check**: If compiled code (Android/Xcode/Java/Swift) lives in subdirectories, DO NOT run Default Setup on compiled languages at the root! Restrict Default Setup to interpreted languages (`python`, `actions`, `javascript`):
     ```bash
     python -c "
     import json, subprocess
     payload = json.dumps({'state': 'configured', 'languages': ['actions', 'python'], 'query_suite': 'default'})
     subprocess.run(['gh', 'api', '-X', 'PATCH', '/repos/:owner/:repo/code-scanning/default-setup', '--input', '-'], input=payload, text=True)
     "
     ```
   * **CWE-275 least-privilege fix**: Ensure all `.github/workflows/*.yml` contain `permissions: contents: read`.
7. **Add Status Badges**: Add live badges to `README.md` header:
   ```markdown
   [![Release](https://img.shields.io/badge/release-v2.0.0-blue?logo=github)](https://github.com/:owner/:repo/releases/latest)
   [![CodeQL](https://github.com/:owner/:repo/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/:owner/:repo/actions/workflows/github-code-scanning/codeql)
   [![Security Policy](https://img.shields.io/badge/security-SECURITY.md-blue)](SECURITY.md)
   ```

---

## CASE 7: PageSpeed & 100/100 Core Web Vitals

1. **Preconnect Critical Domains**: Add `<link rel="preconnect">` for analytics, CDNs, and font providers in `<head>`.
2. **Cumulative Layout Shift (CLS = 0)**: Add explicit `width` and `height` attributes (or CSS `aspect-ratio`) on ALL `<img>`, `<svg>`, and video containers.
3. **Critical CSS**: Inline above-the-fold layout CSS in `<head>`.
4. **Deferred JS**: Use `defer` or `async` on all scripts.
5. **Modern Vector & WebP Assets**: Convert raster assets to WebP; use SVGs for UI icons.

---

## CASE 8: Open Graph (OG) & Social Sharing

1. **Banner Requirements**:
   * Exactly **`1200 x 630` px** (1.91:1 ratio).
   * **File size under 300 KB** (WhatsApp preview requirement).
   * Safe zone: 80 px left/right, 60 px top/bottom.
2. **Instant Banner Creation**: Run `python social-and-crawlers/generate_og_banner.template.py`.
3. **HTML Meta Tags**: Copy `social-and-crawlers/html-head-meta.template.html` into target `<head>`.
4. **Crawler Policy**: Copy `social-and-crawlers/robots.template.txt` to web root as `robots.txt`.

---

## CASE 9: GitHub Repository Documentation & Boilerplate

```text
IF target.needsDocumentationBoilerplate == true:
```

1. **Deploy Repository Boilerplate**:
   * Copy `github-boilerplate/README.template.md` to project root as `README.md`.
   * Copy `github-boilerplate/CONTRIBUTING.template.md` to project root as `CONTRIBUTING.md`.
   * Copy `github-boilerplate/PULL_REQUEST_TEMPLATE.template.md` to `.github/PULL_REQUEST_TEMPLATE.md`.
   * Copy `github-boilerplate/CHANGELOG.template.md` to project root as `CHANGELOG.md`.
2. **Deploy Issue Forms**:
   * Copy `github-boilerplate/issue-templates/*.template.yml` into `.github/ISSUE_TEMPLATE/` (rename removing `.template`).
   * This provides structured forms for Bug Reports, Feature Requests, and redirects security bugs to private advisories.

---

## CASE 10: Tab Views & Multi-Platform Switchers

```text
SWITCH (target.tabContext):
```

### 10.1 IF `tabContext == "markdown_readme"`:
* Follow `github-boilerplate/markdown-tab-cheatsheet.md`.
* Use native `<details><summary>` blocks with `<details open>` for the primary target (e.g. Windows) and collapsed `<details>` for other platforms (macOS, Linux, Mobile).
* Use horizontal Markdown anchor pill tables `| [Windows](#windows) | [macOS](#macos) |` for quick navigation.

### 10.2 IF `tabContext == "web_html"`:
* Copy the CSS and JS tab logic from `client-features/tab-view.template.html`.
* Follow the accessible WAI-ARIA pattern:
  * Container: `[data-tab-group="group-name"]`
  * Buttons: `role="tab"`, `aria-selected="true|false"`, `aria-controls="panel-id"`
  * Content: `role="tabpanel"`, `aria-labelledby="tab-id"`, `.tab-panel.active`
  * Provides seamless keyboard navigation (`ArrowLeft`, `ArrowRight`, `Home`, `End`) and dark glassmorphic styling.

