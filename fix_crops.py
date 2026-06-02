"""Fix crops for hero, coring card, and structural card."""
from PIL import Image
import os

MEDIA = r'c:\blitzcutncore\assets\media'

def save(img, name, quality=88):
    path = os.path.join(MEDIA, name)
    img.save(path, 'JPEG', quality=quality, optimize=True)
    w, h = img.size
    print(f"  {name}  {w}x{h}")

def crop_pct(img, top=0, bottom=0, left=0, right=0):
    w, h = img.size
    return img.crop((int(w*left), int(h*top), w - int(w*right), h - int(h*bottom)))

# ── HERO (IMG_0613): "Wall Cutting" title bottom edge is ~33% down original
# Go to 33% top crop; bottom badge/hashtags gone by 68% so keep to ~67%.
print("1. Hero re-crop (IMG_0613)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0613.jpg'))
print(f"   original: {src.size}")
fixed = crop_pct(src, top=0.33, bottom=0.30)
save(fixed, 'blitz-hero.jpg', quality=90)
save(fixed, 'blitz-wall-sawing-card.jpg')

# ── CORING CARD (IMG_0614): hashtags on left side (~left 28%), title at top,
# Doneraile sticker top-right.  The stunning serrated opening is centre-right.
print("\n2. Coring card re-crop (IMG_0614)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0614.jpg'))
print(f"   original: {src.size}")
fixed = crop_pct(src, top=0.14, bottom=0.22, left=0.30)
save(fixed, 'blitz-coring-card.jpg')

# ── STRUCTURAL CARD (IMG_0616): text banner at top (~26%), Blitz badge BR.
# Square opening is dead centre.  Crop heavily top + bottom-right corner.
print("\n3. Structural card re-crop (IMG_0616)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0616.jpg'))
print(f"   original: {src.size}")
fixed = crop_pct(src, top=0.27, bottom=0.20, right=0.18)
save(fixed, 'blitz-structural-card.jpg')

print("\nDone.")
