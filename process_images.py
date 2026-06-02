"""
Stage 1 image processing for Blitz Cut n Core website.
Crops overlays from job photos and generates the OG share card.
Run with: c:\dphplumbing\.venv\Scripts\python.exe process_images.py
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

MEDIA = r'c:\blitzcutncore\assets\media'

def save(img, name, quality=88):
    path = os.path.join(MEDIA, name)
    img.save(path, 'JPEG', quality=quality, optimize=True)
    print(f"  saved {name}  {img.size[0]}x{img.size[1]}")
    return path

def crop_pct(img, top_pct=0, bottom_pct=0, left_pct=0, right_pct=0):
    w, h = img.size
    x0 = int(w * left_pct)
    y0 = int(h * top_pct)
    x1 = w - int(w * right_pct)
    y1 = h - int(h * bottom_pct)
    return img.crop((x0, y0, x1, y1))

print("=== Blitz Cut n Core — image processing ===")
print()

# ── IMG_0613 → hero background + wall-sawing card
# Portrait Instagram story.  Top: "Wall Cutting" title + "CORK, IRELAND" sticker.
# Bottom: Blitz badge BR + @WEKAringsaw / #WEKAprecutsaw BL.
# Keep middle band: worker on ladder in structural opening.
print("1. Hero (IMG_0613 — wall cutting Cork action shot)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0613.jpg'))
print(f"   original: {src.size}")
cropped = crop_pct(src, top_pct=0.17, bottom_pct=0.30)
save(cropped, 'blitz-hero.jpg', quality=90)
save(cropped, 'blitz-wall-sawing-card.jpg')

# ── IMG_0614 → core drilling / stitch coring card
# Top: "Stitchcoring" title + #hashtags left + Doneraile sticker.
# Bottom: Blitz badge BR.  Middle: stunning serrated cored-wall opening.
print("\n2. Core drilling card (IMG_0614 — stitch coring Doneraile)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0614.jpg'))
print(f"   original: {src.size}")
cropped = crop_pct(src, top_pct=0.13, bottom_pct=0.26, right_pct=0.04)
save(cropped, 'blitz-coring-card.jpg')

# ── IMG_0612 → wall-chasing card
# "Wall Cutting" text is centred vertically — take the TOP slice above it
# (wall saw bolted to smooth concrete wall — very clean industrial detail shot).
print("\n3. Wall chasing card (IMG_0612 — wall saw on concrete wall, top slice)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0612.jpg'))
print(f"   original: {src.size}")
# Text lands ~43-55% down; take top 40%, skip tiny IG header at very top
cropped = crop_pct(src, top_pct=0.05, bottom_pct=0.60)
save(cropped, 'blitz-wall-chasing-card.jpg')

# ── IMG_0616 → structural openings card
# Top: "2 x skylight opes 1.4m x 1.4m" text.  BR: Blitz badge.
# Keep: dramatic square opening from above.
print("\n4. Structural openings card (IMG_0616 — skylight from above)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0616.jpg'))
print(f"   original: {src.size}")
cropped = crop_pct(src, top_pct=0.19, bottom_pct=0.05, right_pct=0.05)
save(cropped, 'blitz-structural-card.jpg')

# ── IMG_0618 → floor sawing card
# 4-panel collage.  Extract top-right panel (clean trench/cut, no logo).
print("\n5. Floor sawing card (IMG_0618 — top-right panel, clean trench)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0618.jpg'))
w, h = src.size
print(f"   original: {w}x{h}")
# Top-right panel: x 50-100%, y 0-50%
panel = src.crop((w // 2, 0, w, h // 2))
# That panel has no logo; trim a small border strip just in case
panel = crop_pct(panel, top_pct=0.04, bottom_pct=0.04)
save(panel, 'blitz-floor-sawing-card.jpg')

# ── IMG_0617 → project showcase / gallery (lighter crop, keep Blitz badge is fine in gallery)
print("\n6. Skylight alt (IMG_0617 — second angle, gallery / showcase)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0617.jpg'))
print(f"   original: {src.size}")
cropped = crop_pct(src, top_pct=0.07, bottom_pct=0.05)
save(cropped, 'blitz-skylight-gallery.jpg')

# ── OG share card — 1200 x 630
print("\n7. OG / OpenGraph share card (1200x630)")
OG_W, OG_H = 1200, 630
bg_dark   = (13, 18, 30)     # near-black charcoal
blue_elec = (26, 140, 255)   # electric blue
gold      = (245, 166, 35)   # amber/gold

card = Image.new('RGB', (OG_W, OG_H), bg_dark)
draw = ImageDraw.Draw(card)

# Subtle blue accent bar at bottom
draw.rectangle([(0, OG_H - 7), (OG_W, OG_H)], fill=blue_elec)

# Faint diagonal stripe texture (brand feel)
for x in range(-OG_H, OG_W, 60):
    draw.line([(x, OG_H), (x + OG_H, 0)], fill=(255, 255, 255), width=1)

# Re-draw background over the stripes on the logo zone so it stays clean
logo_zone_top = 95
logo_zone_bot = 345
logo_pad = 60
draw.rectangle([(OG_W // 2 - 130, logo_zone_top - 10),
                (OG_W // 2 + 130, logo_zone_bot + 10)], fill=bg_dark)

# Load and paste logo
logo_src = os.path.join(MEDIA, 'blitzlogo.jpg')
logo = Image.open(logo_src).convert('RGB')
logo_size = 240
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
lx = (OG_W - logo_size) // 2
ly = logo_zone_top
card.paste(logo, (lx, ly))

# Fonts — try system bold, fall back to default
def load_font(size, bold=False):
    candidates = [
        r'C:\Windows\Fonts\arialbd.ttf' if bold else r'C:\Windows\Fonts\arial.ttf',
        r'C:\Windows\Fonts\Arial Bold.ttf',
        r'C:\Windows\Fonts\calibrib.ttf' if bold else r'C:\Windows\Fonts\calibri.ttf',
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

font_title = load_font(52, bold=True)
font_sub   = load_font(32)
font_small = load_font(24)

cx = OG_W // 2

draw.text((cx, 375), "Precision Concrete Cutting & Coring",
          fill=(255, 255, 255), font=font_title, anchor="mm")
draw.text((cx, 438), "PROFESSIONAL  ·  CLEAN  ·  ON TIME",
          fill=gold, font=font_sub, anchor="mm")
draw.text((cx, 490), "Munster  |  blitzcutncore.com  |  083 303 7476",
          fill=(150, 175, 210), font=font_small, anchor="mm")

save(card, 'blitz-og.jpg', quality=95)

print("\n=== All done. ===")
