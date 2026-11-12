#!/usr/bin/env python3
"""Priprema slike proizvoda za reel (Gajic 12.11.2026: proizvodi ne smeju biti iscepani ni mutni).

Upotreba: python3 scripts/product_tile.py <url-ili-fajl-slike> <izlaz.png> [--tile]
- uzima sliku u punoj veličini (za super-vision.rs URL proba i original bez -300x300 sufiksa),
- NE seče belu pozadinu: iseče samo prazne bele ivice oko proizvoda (bbox) + 8 % margine,
- --tile: proizvod na beloj zaobljenoj kartici (kvadrat, providni uglovi) — podrazumevano za
  slike sa belim fonom i za tamne proizvode (DVR/NVR/crne kamere) na tamnoj pozadini,
- ispisuje MAX_PX = najveća širina (px) u kojoj sme da se prikaže bez uvećanja preko 1,1×.
  U kompoziciji element sa ovom slikom NE SME biti širi od MAX_PX (uračunaj i scale()).
"""
import sys, io, re, urllib.request
from PIL import Image, ImageDraw, ImageChops

src, out = sys.argv[1], sys.argv[2]
tile = '--tile' in sys.argv
def load(u):
    if re.match(r'https?://', u):
        cands = [re.sub(r'-\d+x\d+(\.\w+)$', r'\1', u), u]
        for c in cands:
            try:
                req = urllib.request.Request(c, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130'})
                return Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=30).read()))
            except Exception:
                continue
        raise SystemExit('slika nije preuzeta: ' + u)
    return Image.open(u)
im = load(src)
has_alpha = im.mode in ('RGBA', 'LA') and im.getchannel('A').getextrema()[0] < 250
rgba = im.convert('RGBA')
if has_alpha:
    bbox = rgba.getchannel('A').point(lambda a: 255 if a > 10 else 0).getbbox()
else:
    rgb = rgba.convert('RGB')
    diff = ImageChops.difference(rgb, Image.new('RGB', rgb.size, (255, 255, 255))).convert('L')
    bbox = diff.point(lambda v: 255 if v > 12 else 0).getbbox()
bbox = bbox or (0, 0, *rgba.size)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
m = int(max(w, h) * 0.08)
crop = rgba.crop((max(0, bbox[0] - m), max(0, bbox[1] - m), min(rgba.width, bbox[2] + m), min(rgba.height, bbox[3] + m)))
if tile:
    s = max(crop.size); pad = int(s * 0.06); S = s + 2 * pad
    canvas = Image.new('RGBA', (S, S), (255, 255, 255, 255))
    canvas.alpha_composite(crop if has_alpha else crop.convert('RGBA'), ((S - crop.width) // 2, (S - crop.height) // 2))
    mask = Image.new('L', (S, S), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.09), fill=255)
    canvas.putalpha(mask); crop = canvas
crop.save(out)
print(f'{out}: {crop.width}x{crop.height}  MAX_PX={int(crop.width * 1.1)}  izvorni_proizvod={w}x{h}  alfa={has_alpha}')
if crop.width < 450:
    print('UPOZORENJE: slika je mala; prikaži proizvod manjim (npr. kartica do MAX_PX) i ne uvećavaj je.')
