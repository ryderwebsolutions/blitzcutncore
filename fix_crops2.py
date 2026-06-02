"""Final aggressive crops for coring + structural cards."""
from PIL import Image
import os

MEDIA = r'c:\blitzcutncore\assets\media'

def save(img, name, q=88):
    p = os.path.join(MEDIA, name)
    img.save(p, 'JPEG', quality=q, optimize=True)
    print(f"  {name}  {img.size[0]}x{img.size[1]}")

def crop_px(img, top=0, bottom=0, left=0, right=0):
    w, h = img.size
    return img.crop((int(w*left), int(h*top), w-int(w*right), h-int(h*bottom)))

# ── IMG_0614 coring card
# Hashtags extend ~42% from left. Doneraile sticker top-right ~18% from right.
# "Stitchcoring" title top ~14%. Blitz badge bottom-right ~20% bottom, 18% right.
# The serrated stitch-cored edge is the dead centre of the image — crop from all sides.
print("1. Coring card final (IMG_0614)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0614.jpg'))
print(f"   original: {src.size}")
fixed = crop_px(src, top=0.15, bottom=0.23, left=0.44, right=0.20)
save(fixed, 'blitz-coring-card.jpg')

# ── IMG_0616 structural card
# Text banner across top ~35%. Blitz badge bottom-right ~22% bottom, 26% right.
# Square opening is centred lower — worth the aggressive crop.
print("\n2. Structural card final (IMG_0616)")
src = Image.open(os.path.join(MEDIA, 'blitz-job-0616.jpg'))
print(f"   original: {src.size}")
fixed = crop_px(src, top=0.36, bottom=0.23, right=0.27)
save(fixed, 'blitz-structural-card.jpg')

print("\nDone.")
