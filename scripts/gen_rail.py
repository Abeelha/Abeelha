# scripts/gen_rail.py  ->  assets/hive-pillar.png
# Tall vertical hive rail: tile hive-sides.png down to a long strip so it can
# frame the full-height README body when placed in side table cells.
from PIL import Image

SRC = r"C:\Users\Abeelha\Downloads\hive-sides.png"
W, TARGET_H = 200, 5300          # display at width=120 -> ~3180px tall, +3 tiles, reaches page bottom

src = Image.open(SRC).convert("RGBA")
h = max(1, int(src.height * W / src.width))
tile = src.resize((W, h))
rail = Image.new("RGBA", (W, TARGET_H))
y = 0
while y < TARGET_H:
    rail.paste(tile, (0, y))
    y += h
rail.convert("RGB").save("assets/hive-pillar.png")
print("wrote assets/hive-pillar.png", W, "x", TARGET_H, "(tile", W, "x", h, ")")
