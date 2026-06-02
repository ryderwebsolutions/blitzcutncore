"""Generate blitz-favicon.png from blitzlogo.jpg."""
from PIL import Image
import os

src  = r'c:\blitzcutncore\assets\media\blitzlogo.jpg'
dst  = r'c:\blitzcutncore\assets\media\blitz-favicon.png'
logo = Image.open(src).convert('RGBA')
logo = logo.resize((64, 64), Image.LANCZOS)
logo.save(dst, 'PNG')
print(f"Favicon saved: {dst}  {logo.size}")
