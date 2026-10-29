# 🛡️ Google CSP Evaluator & Strict Content Security Policy Guide

How to design and verify your Content Security Policy to achieve an **A+ rating** on [Google CSP Evaluator](https://csp-evaluator.withgoogle.com) and [SecurityHeaders.com](https://securityheaders.com).

---

## 🚫 The 4 Critical Traps Flagged by Google CSP Evaluator

| Evaluator Warning | Vulnerability Risk | Required Fix |
| :--- | :--- | :--- |
| **Missing `object-src`** | High: Allows malicious Flash/Java applets or plugin execution. | Add **`object-src 'none';`** |
| **Missing `base-uri`** | High: Attackers can inject a `<base href="https://evil.com">` tag to redirect all relative scripts and form actions to their server. | Add **`base-uri 'self';`** |
| **Missing `frame-ancestors`** | Medium/High: Allows other websites to embed your page in a transparent `<iframe>` (Clickjacking). | Add **`frame-ancestors 'none';`** |
| **`script-src 'unsafe-inline'`** | High: Allows Cross-Site Scripting (XSS) if user input is reflected into HTML. | Use **Hashes**, **Nonces**, or strict external source whitelisting. |

---

## 🛡️ Production-Grade Baseline CSP

Drop this into your hosting header configuration as your starting point:

```text
default-src 'self';
script-src 'self' 'unsafe-inline' https://www.googletagmanager.com;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
img-src 'self' data: https://api.qrserver.com https://*.google-analytics.com https://*.googletagmanager.com;
font-src 'self' https://fonts.gstatic.com;
connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com;
frame-ancestors 'none';
base-uri 'self';
form-action 'self';
object-src 'none';
```

---

## 🔒 Upgrading to Strict CSP (Eliminating `'unsafe-inline'`)

If you want a **flawless 100% green checkmark** on Google CSP Evaluator without `'unsafe-inline'`:

### Method 1: Inline Script Hashes (Best for Static Sites)
When you have small inline scripts (e.g. device detection or Google Analytics bootstrap):
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

## 🧩 Third-Party CSP Whitelist Recipes

* **Google Analytics 4 & Google Tag Manager**:
  * `script-src`: `https://www.googletagmanager.com`
  * `img-src`: `https://*.google-analytics.com https://*.googletagmanager.com`
  * `connect-src`: `https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com`
* **Google Fonts**:
  * `style-src`: `https://fonts.googleapis.com`
  * `font-src`: `https://fonts.gstatic.com`
* **Stripe Payments**:
  * `script-src`: `https://js.stripe.com`
  * `frame-src`: `https://js.stripe.com`
* **YouTube Embeds**:
  * `frame-src`: `https://www.youtube.com https://www.youtube-nocookie.com`
