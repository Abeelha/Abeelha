# scripts/gen_header.py  ->  assets/header.svg
import math, random, os
W, H, R = 1200, 220, 24
dx, dy = R * 1.5, R * math.sqrt(3)
random.seed(7)

def hexpts(cx, cy, r):
    return " ".join(f"{cx + r*math.cos(math.radians(60*i)):.1f},{cy + r*math.sin(math.radians(60*i)):.1f}" for i in range(6))

cells = []
col = 0; x = 0.0
while x < W + R:
    yoff = (dy / 2) if col % 2 else 0
    y = yoff
    while y < H + R:
        cells.append((x, y)); y += dy
    x += dx; col += 1

polys = []
for cx, cy in cells:
    delay = (cx / W) * 3.0 + random.uniform(0, 0.5)     # honey sweep left->right
    fill = "#ffb300" if random.random() < 0.45 else "#1f6b1f"
    polys.append(
        f'<polygon points="{hexpts(cx, cy, R-2)}" fill="{fill}" opacity="0.10">'
        f'<animate attributeName="opacity" values="0.10;0.80;0.10" dur="6s" '
        f'begin="{delay:.2f}s" repeatCount="indefinite"/></polygon>'
    )

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
       f'<rect width="{W}" height="{H}" fill="#050807"/>{"".join(polys)}</svg>')
os.makedirs("assets", exist_ok=True)
open("assets/header.svg", "w", encoding="utf-8").write(svg)
print("wrote assets/header.svg", len(svg), "bytes,", len(cells), "cells")
