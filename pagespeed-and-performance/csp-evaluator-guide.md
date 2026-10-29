# 🛡️ Google CSP Evaluator & Strict Content Security Policy Guide

How to design and verify your Content Security Policy to achieve a **100% green checkmark** on [Google CSP Evaluator](https://csp-evaluator.withgoogle.com) and an **A+ rating** on [SecurityHeaders.com](https://securityheaders.com).

---

## 🚫 The 4 Critical Traps Flagged by Google CSP Evaluator

| Evaluator Warning | Vulnerability Risk | Required Fix |
| :--- | :--- | :--- |
| **Missing `object-src`** | High: Allows malicious Flash/Java applets or plugin execution. | Add **`object-src 'none';`** |
| **Missing `base-uri`** | High: Attackers can inject a `<base href="https://evil.com">` tag to redirect all relative scripts and form actions to their server. | Add **`base-uri 'self';`** |
| **Missing `frame-ancestors`** | Medium/High: Allows other websites to embed your page in a transparent `<iframe>` (Clickjacking). | Add **`frame-ancestors 'none';`** |
| **`script-src 'unsafe-inline'`** | High: Allows Cross-Site Scripting (XSS) if user input is reflected into HTML. | Omit `'unsafe-inline'` from `script-src`; use external scripts, **Hashes**, or **Nonces**. |

---

## 🛡️ Clean Baseline CSP (Zero High-Severity Warnings)

All 6 hosting templates in `hosting/` ship with this strict, zero-warning baseline out of the box:

```text
default-src 'self';
script-src 'self';
style-src 'self' 'unsafe-inline';
img-src 'self' data: blob:;
font-src 'self';
connect-src 'self';
frame-ancestors 'none';
base-uri 'self';
form-action 'self';
object-src 'none';
upgrade-insecure-requests;
```

---

## 🔒 Allowing Necessary Inline Scripts Safely (Without `'unsafe-inline'`)

If your page requires small inline scripts (such as a theme bootstrap or Google Analytics initialization):

### Method 1: Inline Script Hashes (Best for Static Sites)
1. Compute the SHA-256 hash of your exact script contents:
   ```bash
   echo -n "console.log('hello');" | openssl dgst -sha256 -binary | openssl base64
   ```
2. Add the hash directly into `script-src`:
   ```text
   script-src 'self' 'sha256-abc123xyz...' https://www.googletagmanager.com;
   ```
3. The browser will execute *only* the exact script matching that hash, completely neutralizing arbitrary XSS injection!

### Method 2: Nonce-Based CSP (Best for SSR / Next.js / Server Backends)
1. Generate a cryptographically random nonce per request on your server: `crypto.randomBytes(16).toString('base64')`.
2. Send header: `script-src 'nonce-{RANDOM}' 'strict-dynamic';`.
3. In HTML: `<script nonce="{RANDOM}">...</script>`.

---

## 🧩 Opt-In Third-Party CSP Whitelist Recipes

Only append the origins your project actually uses (see `AGENT_RECIPES.md` CASE 3):

* **Google Analytics 4 & Google Tag Manager**:
  * `script-src`: `https://www.googletagmanager.com`
  * `img-src`: `https://www.google-analytics.com https://*.google-analytics.com https://*.googletagmanager.com`
  * `connect-src`: `https://www.google-analytics.com https://analytics.google.com https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com`
* **Google Fonts**:
  * `style-src`: `https://fonts.googleapis.com`
  * `font-src`: `https://fonts.gstatic.com`
* **External QR Code API (`qrserver`)**:
  * `img-src`: `https://api.qrserver.com`
* **Stripe Payments**:
  * `script-src`: `https://js.stripe.com`
  * `frame-src`: `https://js.stripe.com`
* **YouTube Embeds**:
  * `frame-src`: `https://www.youtube.com https://www.youtube-nocookie.com`
