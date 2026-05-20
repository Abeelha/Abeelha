# scripts/gen_sections.py  ->  assets/sec/0X.svg
# Big honey section titles (SVG text renders bigger + on-palette, unlike <sub><code>).
import os

SECS = [
    ("01", "IDENTITY"),
    ("02", "MANIFESTO · the invisible walls"),
    ("03", "ARSENAL"),
    ("04", "SIGNALS"),
    ("05", "FREQUENCIES · what's in my ears"),
    ("06", "TRANSMISSIONS"),
]
os.makedirs("assets/sec", exist_ok=True)
for num, name in SECS:
    label = f"§ {num} · {name}"          # § NUM · NAME
    w = int(len(label) * 13 + 40)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="44" viewBox="0 0 {w} 44" '
        f'font-family="\'JetBrains Mono\',Consolas,ui-monospace,monospace">'
        f'<text x="{w//2}" y="29" text-anchor="middle" font-size="22" font-weight="700" '
        f'letter-spacing="1.5" fill="#ffb300">{label}</text></svg>'
    )
    open(f"assets/sec/{num}.svg", "w", encoding="utf-8").write(svg)
    print("wrote assets/sec/" + num + ".svg", "w=", w)
