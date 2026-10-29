# ⚡ PageSpeed Insights & Core Web Vitals Optimization Guide

Target: **95–100 / 100 on Mobile and Desktop** on Google PageSpeed Insights & Lighthouse.

---

## 🎯 1. Resource Hints (`preconnect` & `dns-prefetch`)

Save 100–300 ms on DNS lookups and TLS handshakes by preconnecting to critical external domains in `<head>`:

```html
<!-- Google Analytics / Tag Manager -->
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<link rel="dns-prefetch" href="https://www.googletagmanager.com">

<!-- Google Fonts (if used) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- External API / QR Code Origin (if used) -->
<link rel="preconnect" href="https://api.qrserver.com">
```

---

## 🚫 2. Eliminate Render-Blocking Resources

1. **Scripts**:
   * NEVER place unadorned `<script src="...">` in `<head>`.
   * Always use `defer` for scripts that interact with the DOM:
     ```html
     <script src="/js/app.js" defer></script>
     ```
   * Use `async` for non-dependent analytics or tracking:
     ```html
     <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXX"></script>
     ```
2. **Critical CSS**:
   * Inline above-the-fold styling directly inside `<style>` in `<head>` (e.g. navigation, hero section, background colors).
   * Defer non-critical stylesheets:
     ```html
     <link rel="preload" href="/css/extended.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
     <noscript><link rel="stylesheet" href="/css/extended.css"></noscript>
     ```

---

## 📐 3. Eliminate Cumulative Layout Shift (CLS = 0)

Layout shift destroys user experience and heavily penalizes your Core Web Vitals score.

1. **Always specify explicit `width` and `height` (or CSS `aspect-ratio`)**:
   ```html
   <!-- DO THIS -->
   <img src="/assets/hero.webp" width="600" height="400" alt="Hero illustration" style="aspect-ratio: 3/2; max-width: 100%; height: auto;">
   ```
2. **Reserve container space for dynamic elements**:
   If an element is populated via JavaScript (like QR codes, dynamic charts, or user avatars), give the parent container an explicit minimum height (`min-height: 200px;`) so the page doesn't jump when the asset loads.

---

## 🖼️ 4. Modern Image Formats & Vector SVGs

1. **Use Vector SVGs for UI Icons & Logos**:
   * SVGs have zero pixelation, scale cleanly on Retina displays, and are typically 1–4 KB.
2. **Convert Photos & Raster Art to WebP / AVIF**:
   * Compress with 80–85% quality. WebP produces 30–50% smaller files than PNG/JPEG without visible degradation.
   * Use responsive `<picture>` tags with fallbacks:
     ```html
     <picture>
       <source srcset="/assets/hero.avif" type="image/avif">
       <source srcset="/assets/hero.webp" type="image/webp">
       <img src="/assets/hero.png" width="800" height="500" alt="Preview" loading="lazy">
     </picture>
     ```
3. **Lazy Load Below-the-Fold Images**:
   ```html
   <img src="..." loading="lazy" decoding="async">
   ```

---

## 📦 5. Cache-Control Header Strategy

Configure caching headers in your hosting configuration (`firebase.json`, `vercel.json`, `_headers`):

| Asset Type | Cache-Control Header | Reason |
| :--- | :--- | :--- |
| **HTML (`/index.html`)** | `no-cache, no-store, must-revalidate` | Ensures users immediately receive new releases without manual browser refreshes. |
| **Service Worker (`/sw.js`)** | `no-cache, no-store, must-revalidate` | Prevents clients from getting trapped on outdated PWA service workers. |
| **Hashed Static Assets (`*.js`, `*.css`, `*.woff2`)** | `public, max-age=31536000, immutable` | Cached for 1 full year; instantaneous subsequent page loads. |
| **Images & SVGs** | `public, max-age=604800, stale-while-revalidate=86400` | Balances freshness with high cache hit rates. |
| **Download Binaries (`/downloads/*`)** | `public, max-age=86400, attachment` | Relieves server load and triggers direct browser download manager. |

---

## 🔤 6. Web Font Optimization

* Add `font-display: swap;` in `@font-face` rules to prevent the Flash of Invisible Text (FOIT).
* Preload the primary font file:
  ```html
  <link rel="preload" href="/fonts/inter-bold.woff2" as="font" type="font/woff2" crossorigin>
  ```

---

## ⚡ 7. Parallel Vendor Code Splitting & Bundler Optimization

Monolithic JavaScript bundles trigger high **Total Blocking Time (TBT)** during V8 parse & compilation:

1. **Split Heavy Vendor Packages**:
   Configure your bundler (Vite, Rollup, Webpack) to separate framework runtime, icons, and utilities into dedicated chunks:
   ```javascript
   // vite.config.js
   build: {
     target: 'es2022',
     rollupOptions: {
       output: {
         manualChunks(id) {
           if (id.includes('node_modules')) {
             if (id.includes('react')) return 'vendor-react';
             if (id.includes('icons') || id.includes('lucide')) return 'vendor-icons';
             return 'vendor-libs';
           }
         }
       }
     }
   }
   ```
   *(See `pagespeed-and-performance/vite.config.template.js` for the complete reference implementation).*
2. **Benefits**:
   * Takes full advantage of HTTP/2 parallel multiplexing.
   * Subsequent deployments only invalidate modified chunks instead of the entire app bundle.
   * Keeps the main thread responsive, ensuring zero Total Blocking Time on mobile devices.
