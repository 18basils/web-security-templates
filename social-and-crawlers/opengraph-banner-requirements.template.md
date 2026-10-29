# 🎨 Open Graph (OG) Banner Requirements & Specification Template

This template defines the exact industry-standard requirements, safe zone dimensions, live release verification checks, platform behaviors, and meta tag configurations for creating and maintaining social share banners (`og:image`) that render with 100% fidelity across **WhatsApp, Twitter / X, Facebook, LinkedIn, Slack, Discord, Telegram, and iMessage**.

---

## 1. Technical Image Specifications

| Specification | Standard Requirement | Recommended Production Target |
| :--- | :--- | :--- |
| **Dimensions** | `1200 x 630` pixels | **`1200 x 630` px** (Exact 1.91:1 aspect ratio) |
| **Minimum Dimensions** | `600 x 315` pixels | Never go below `1200 x 630` for high-DPI / Retina screens |
| **Maximum File Size** | Under 8 MB (FB limit) / 5 MB (X limit) | **Under 300 KB** (Critical for WhatsApp auto-unfurl) |
| **File Format** | `PNG` or `JPEG` / `WebP` | **PNG-24** (graphics, logos, UI) or **JPEG 85%** (photo-heavy) |
| **Color Profile** | sRGB | **sRGB IEC61966-2.1** (prevents washed-out colors on mobile) |
| **Aspect Ratio** | 1.91 : 1 | Universal standard for rich cards across all platforms |

> [!IMPORTANT]
> **The 300 KB WhatsApp Rule**: WhatsApp will **refuse to display** an image preview automatically if the file size exceeds **300 KB**. Always compress your 1200x630 banner to stay between **100 KB and 280 KB**.

---

## 2. Existing OG Banner Audit & Live Release Sync (Anti-Stale Preview Rule)

Whenever auditing or patching a project where an Open Graph banner (`og-image.png`, `og-banner.jpg`, etc.) and `<meta property="og:...">` tags **already exist**, the AI agent **MUST NOT blindly skip them**. Instead, perform this mandatory 4-point verification against the **latest production / live release**:

1. **Inspect the Existing Banner Image Visually**:
   - View the existing `og:image` file (`public/assets/og-image.png`, `public/og-banner.jpg`, or the live `og:image` URL) and compare it against the current live application UI, version number, and feature set.
   - Check if the image displays an outdated version badge (e.g., `v1.0` when the project is now on `v2.0`), old product name, deprecated tagline, or an obsolete UI screenshot/theme.
2. **Verify Meta Tag Title & Description Parity (`<head>`)**:
   - Compare `<meta property="og:title">`, `<meta property="og:description">`, `<meta name="twitter:title">`, `<meta name="twitter:description">`, and Schema.org JSON-LD against the latest live website features and `README.md`.
   - If new platforms, capabilities, or branding changes were shipped in recent commits/releases, update the Open Graph and Twitter meta descriptions immediately.
3. **Verify Technical Compliance of the Existing Image**:
   - Confirm exact dimensions (`1200 x 630` px), file size (`< 300 KB`), and that `og:image` points to the live production absolute `https://` URL (never `localhost` or a staging domain).
4. **Regenerate & Cache-Bust When Outdated**:
   - If the existing OG banner image or its text/preview is behind the latest production release, regenerate the banner (via `generate_og_banner.template.py` or the project's custom banner generator) so its title, subtitle, feature tagline, and version pill reflect the **current live release**.
   - Append or bump a version query parameter on the image URL in `<head>` (e.g., `https://example.com/assets/og-image.png?v=2.0.0`) so WhatsApp, Telegram, Discord, Twitter/X, and LinkedIn immediately fetch the updated banner instead of serving a cached older preview.

---

## 3. Safe Zone & Visual Composition

Different platforms display cards in different ways: mobile chat bubbles crop edges, Twitter adds rounded corners, and Facebook overlays play buttons on videos.

```
+-------------------------------------------------------------------------+
|                                1200 px                                  |
|  +-------------------------------------------------------------------+  |
|  |                    TOP MARGIN SAFE ZONE (60 px)                   |  |
|  |  +-------------------------------------------------------------+  |  |
|  |  |                                                             |  |  |
|  |  |                      CORE CONTENT AREA                      |  |  |
|  |  |                                                             |  |  |
|  |  |  - Big Bold Title (Font size 48-56px, bold, high contrast)  |  |  | 630 px
|  |  |  - Brand Logo / Icon (Centered or top-left)                 |  |  |
|  |  |  - Subtitle / Value Proposition (Font size 20-24px)         |  |  |
|  |  |  - Feature Badges or Visual Preview                         |  |  |
|  |  |                                                             |  |  |
|  |  +-------------------------------------------------------------+  |  |
|  |                  BOTTOM MARGIN SAFE ZONE (60 px)                  |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
       <-- 80 px Left -->                       <-- 80 px Right -->
```

### Composition Guidelines:
1. **Centered Safe Zone (`1040 x 510` px)**:
   - Keep all critical typography, logos, and badges at least **80 px away from the left/right edges** and **60 px away from the top/bottom edges**.
2. **Text Hierarchy**:
   - **Primary Title**: 48px – 56px bold (Max 6 to 8 words).
   - **Subtitle / Value Proposition**: 20px – 24px regular (Max 12 to 15 words).
   - Avoid small body paragraphs — social cards are viewed at small sizes on phone screens.
3. **Contrast Ratio**:
   - Ensure a minimum contrast ratio of **4.5:1** between text and background. Dark themes (`#080c15` or `#0f172a`) with bright white/cyan typography render with highest impact.
4. **No UI Controls**:
   - Never draw fake "Play" or "Click Here" buttons on static images (violates Facebook & Google advertising policies).

---

## 4. Platform-by-Platform Card Behaviors

| Platform | Card Type | Behavior & Gotchas |
| :--- | :--- | :--- |
| **Twitter / X** | `summary_large_image` | Uses full-width 1200x630 banner. Requires `twitter:card` meta tag. |
| **Facebook & Meta** | Standard Share Card | Renders full 1200x630 banner above title/description. |
| **LinkedIn** | Rich Link Post | Renders full 1200x630 banner above snippet. |
| **WhatsApp** | Chat Bubble Preview | Shows a thumbnail or banner. **Requires image size < 300 KB**. |
| **Telegram** | Instant View / Card | Renders high-quality preview if `og:image` is accessible without login. |
| **Slack & Discord** | Message Attachment | Slack unfurls `og:image` automatically; Discord generates rich embeds. |
| **iMessage (Apple)** | Rich Link Balloon | Extracts `og:image` and rounds the four corners automatically. |

---

## 5. Complete HTML `<head>` Meta Tags Template

Place this block inside your `<head>` tag (see `social-and-crawlers/html-head-meta.template.html` for the full version):

```html
<!-- Open Graph / Facebook / LinkedIn / WhatsApp / Slack -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://example.com/">
<meta property="og:site_name" content="Your Brand">
<meta property="og:title" content="Your Website Title - Catchy Slogan">
<meta property="og:description" content="A clear, concise description of your service for social link cards.">
<meta property="og:image" content="https://example.com/assets/og-image.png">
<meta property="og:image:secure_url" content="https://example.com/assets/og-image.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Your Brand Website Preview Card">
<meta property="og:locale" content="en_US">

<!-- Twitter / X Cards -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="https://example.com/">
<meta name="twitter:site" content="@your_brand_handle">
<meta name="twitter:creator" content="@your_creator_handle">
<meta name="twitter:title" content="Your Website Title - Catchy Slogan">
<meta name="twitter:description" content="A clear, concise description of your service for social link cards.">
<meta name="twitter:image" content="https://example.com/assets/og-image.png">
<meta name="twitter:image:alt" content="Your Brand Website Preview Card">
```

> [!TIP]
> **Always Use Absolute URLs**: Platforms **cannot** resolve relative paths like `src="/assets/og-image.png"`. The URL MUST start with `https://`.

---

## 6. Free Testing & Validation Tools

Test your live URL or preview card before publishing:

1. **OpenGraph.xyz (Multi-Platform Live Preview)**:
   - [https://www.opengraph.xyz](https://www.opengraph.xyz)
2. **Facebook Sharing Debugger (Clears Facebook Cache)**:
   - [https://developers.facebook.com/tools/debug/](https://developers.facebook.com/tools/debug/)
3. **LinkedIn Post Inspector (Clears LinkedIn Cache)**:
   - [https://www.linkedin.com/post-inspector/](https://www.linkedin.com/post-inspector/)
4. **Twitter / X Card Validator**:
   - Test by composing a post or DM on [https://x.com](https://x.com).
