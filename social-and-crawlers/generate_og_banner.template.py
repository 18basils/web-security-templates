#!/usr/bin/env python3
"""
================================================================================
OPEN GRAPH 1200x630 BANNER GENERATOR TEMPLATE
================================================================================
Generates a high-contrast, modern Open Graph banner (1200 x 630 px) with safe-zone
padding, customizable branding, gradient backgrounds, and optimized file size (<300 KB)
compatible with WhatsApp, Twitter/X, Facebook, LinkedIn, Slack, and Discord.

Requirements:
    pip install pillow

Usage:
    python generate_og_banner.template.py
================================================================================
"""

import os
from PIL import Image, ImageDraw, ImageFont

def generate_og_banner(
    output_path="og-image.png",
    title="Your Product Title",
    subtitle="Your catchphrase or primary value proposition goes here",
    tagline="Key feature 1 • Key feature 2 • Key feature 3",
    pill_text="v1.0 UNIVERSAL",
    primary_color=(56, 189, 248),    # Neon Cyan (#38bdf8)
    accent_color=(2, 132, 199),     # Deep Sky Blue (#0284c7)
    bg_color_top=(15, 23, 42),       # Dark Slate Navy (#0f172a)
    bg_color_bottom=(8, 12, 21),     # Cosmic Black (#080c15)
):
    width = 1200
    height = 630

    # 1. Create base RGB image and draw smooth vertical dark gradient
    img = Image.new("RGBA", (width, height), bg_color_top)
    draw_base = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / float(height)
        r = int(bg_color_top[0] * (1 - ratio) + bg_color_bottom[0] * ratio)
        g = int(bg_color_top[1] * (1 - ratio) + bg_color_bottom[1] * ratio)
        b = int(bg_color_top[2] * (1 - ratio) + bg_color_bottom[2] * ratio)
        draw_base.line([(0, y), (width, y)], fill=(r, g, b, 255))

    # 2. Transparent overlay layer for all semi-transparent geometric elements
    # (prevents alpha-channel flattening bugs on final RGB conversion)
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # 3. Ambient glow ellipse in center
    for radius in range(360, 0, -20):
        alpha = int((1 - (radius / 360.0)) * 38)
        odraw.ellipse(
            [(width // 2 - radius, height // 2 - radius - 20),
             (width // 2 + radius, height // 2 + radius - 20)],
            fill=(accent_color[0], accent_color[1], accent_color[2], alpha)
        )

    # 4. Subtle Outer Border (Safe frame: 16px inset, 80 alpha)
    odraw.rounded_rectangle(
        [(16, 16), (width - 16, height - 16)],
        radius=20,
        outline=(primary_color[0], primary_color[1], primary_color[2], 80),
        width=2
    )

    # 5. Font loader with cross-platform OS font filenames
    def get_font(size, bold=False):
        font_candidates = (
            [
                "segoeuib.ttf",
                "arialbd.ttf",
                "calibrib.ttf",
                "DejaVuSans-Bold.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                "Segoe UI Bold.ttf",
                "Arial Bold.ttf"
            ]
            if bold else
            [
                "segoeui.ttf",
                "arial.ttf",
                "calibri.ttf",
                "DejaVuSans.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/System/Library/Fonts/Supplemental/Arial.ttf",
                "Segoe UI.ttf",
                "Arial.ttf"
            ]
        )
        for name in font_candidates:
            try:
                return ImageFont.truetype(name, size)
            except (IOError, OSError):
                continue
        try:
            return ImageFont.load_default(size=size)
        except TypeError:
            return ImageFont.load_default()

    font_title = get_font(52, bold=True)
    font_pill = get_font(14, bold=True)
    font_subtitle = get_font(22, bold=False)
    font_tagline = get_font(16, bold=False)

    # 6. Dynamic Pill Badge (Auto-sizes width to fit text with 48px padding)
    bbox = odraw.textbbox((0, 0), pill_text, font=font_pill)
    text_w = bbox[2] - bbox[0]
    pill_w = max(160, text_w + 48)
    pill_h = 36
    pill_x = (width - pill_w) // 2
    pill_y = 115

    odraw.rounded_rectangle(
        [(pill_x, pill_y), (pill_x + pill_w, pill_y + pill_h)],
        radius=18,
        fill=(primary_color[0], primary_color[1], primary_color[2], 35),
        outline=(primary_color[0], primary_color[1], primary_color[2], 180),
        width=2
    )

    # 7. Merge translucent overlay with base image
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # 8. Render Typography with full opacity (Crisp text & perfect contrast)
    # Centered pill badge text
    draw.text((width // 2, pill_y + pill_h // 2), pill_text, fill=primary_color, font=font_pill, anchor="mm")

    # Main Title (Bold, Center)
    title_y = 235
    draw.text((width // 2, title_y), title, fill=(248, 250, 252), font=font_title, anchor="mm")

    # Subtitle / Value Proposition (Center)
    sub_y = 315
    draw.text((width // 2, sub_y), subtitle, fill=(203, 213, 225), font=font_subtitle, anchor="mm")

    # Tagline / Key Features (Center)
    tag_y = 375
    draw.text((width // 2, tag_y), tagline, fill=(148, 163, 184), font=font_tagline, anchor="mm")

    # Accent Line Underneath
    line_w = 320
    line_x = (width - line_w) // 2
    line_y = 435
    draw.line([(line_x, line_y), (line_x + line_w, line_y)], fill=(primary_color[0], primary_color[1], primary_color[2], 180), width=2)

    # 9. Convert to RGB and Save with Optimization (<300 KB for WhatsApp preview)
    final_img = img.convert("RGB")
    final_img.save(output_path, "PNG", optimize=True)
    file_size_kb = os.path.getsize(output_path) / 1024.0

    print(f"[OK] Open Graph Banner generated: {output_path}")
    print(f"     Resolution: {width} x {height} px")
    print(f"     File Size:  {file_size_kb:.1f} KB (Target < 300 KB: {'PASS' if file_size_kb < 300 else 'WARN'})")

if __name__ == "__main__":
    generate_og_banner(output_path="og-image-sample.png")
