# scripts/gen_rail.py  ->  assets/hive-rail.png
# Tall vertical hive rail: tile hive-sides.png down to a long strip so it can
# frame the full-height README body when placed in side table cells.
from PIL import Image

SRC = r"C:\Users\Abeelha\Downloads\hive-sides.png"
W, TARGET_H = 200, 4100          # display at width=90 -> ~1845px tall, thicker rails, full body

src = Image.open(SRC).convert("RGBA")
h = max(1, int(src.height * W / src.width))
tile = src.resize((W, h))
rail = Image.new("RGBA", (W, TARGET_H))
y = 0
while y < TARGET_H:
    rail.paste(tile, (0, y))
    y += h
rail.convert("RGB").save("assets/hive-rail.png")
print("wrote assets/hive-rail.png", W, "x", TARGET_H, "(tile", W, "x", h, ")")
