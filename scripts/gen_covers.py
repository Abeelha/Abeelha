# scripts/gen_covers.py  ->  assets/covers/*.png
from PIL import Image, ImageDraw, ImageFont
import os, math

COVERS = [
    ("01-odinochestvo",  "одиночество",        "russian · solitude",   (58,10,10),  (193,18,31)),
    ("02-macroblank",    "MacroBlank",          "phonk · vaporwave",    (42,10,58),  (255,0,170)),
    ("03-coding",        "coding music",        "focus · terminal",     (3,26,3),    (57,255,20)),
    ("04-exphiphop",     "experimental hiphop", "leftfield · abstract", (58,36,0),   (255,179,0)),
    ("05-electro",       "electro",             "gaming · drive",       (0,26,42),   (0,229,255)),
    ("06-random",        "Random",              "grab-bag",             (20,20,20),  (255,179,0)),
]
S = 500
def font(sz):
    for p in ("C:/Windows/Fonts/consolab.ttf", "C:/Windows/Fonts/consola.ttf"):
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

def hexpts(cx, cy, r):
    return [(cx + r*math.cos(math.radians(60*i+30)), cy + r*math.sin(math.radians(60*i+30))) for i in range(6)]

os.makedirs("assets/covers", exist_ok=True)
for fn, name, vibe, c0, c1 in COVERS:
    im = Image.new("RGB", (S, S), c0); d = ImageDraw.Draw(im)
    for y in range(S):                                   # vertical gradient c0 -> c1
        t = y / S
        d.line([(0, y), (S, y)], fill=tuple(int(c0[i]+(c1[i]-c0[i])*t) for i in range(3)))
    for gx in range(0, S+80, 80):                        # faint hex lattice
        for j, gy in enumerate(range(0, S+80, 70)):
            ox = 40 if j % 2 else 0
            d.line(hexpts(gx+ox, gy, 26) + [hexpts(gx+ox, gy, 26)[0]], fill=(255,255,255), width=1)
    ov = Image.new("RGBA", (S, S), (0,0,0,0)); od = ImageDraw.Draw(ov)
    od.polygon(hexpts(S//2, S//2-20, 120), outline=(255,255,255,200), width=4)
    od.text((S//2, S//2-20), "▶", font=font(64), fill=(255,255,255,230), anchor="mm")
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB"); d = ImageDraw.Draw(im)
    d.text((30, S-110), name, font=font(40), fill=(255,255,255))
    d.text((30, S-58),  vibe, font=font(22), fill=(220,220,220))
    im.save(f"assets/covers/{fn}.png")
    print("wrote", fn)
