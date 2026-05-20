# scripts/gen_band.py  ->  assets/hive-band.png
# Horizontal hive divider: rotate the vertical pillar art 90deg, tile across, thin band.
from PIL import Image

SRC = "assets/hive-sides.png"
H, TARGET_W = 150, 1600

src = Image.open(SRC).convert("RGB").rotate(90, expand=True)   # vertical -> horizontal
w = max(1, int(src.width * H / src.height))
tile = src.resize((w, H))
band = Image.new("RGB", (TARGET_W, H))
x = 0
while x < TARGET_W:
    band.paste(tile, (x, 0))
    x += w
band.crop((0, 0, TARGET_W, H)).save("assets/hive-band.png")
print("wrote assets/hive-band.png", TARGET_W, "x", H, "(at 100% width ~= 95px tall)")
