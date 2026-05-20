# scripts/gen_band.py  ->  assets/hive-band.png
# Thin horizontal hive divider: EXACTLY 3 clean repeats (no chopped tile at the
# right edge), vertically cropped so it renders short, not fat.
from PIL import Image

SRC = "assets/hive-sides.png"
REPEATS = 3
CROP_FRAC = 0.42                       # vertical slice of the rotated art -> thinner band

src = Image.open(SRC).convert("RGB").rotate(90, expand=True)   # vertical pillar -> horizontal
rw, rh = src.size
ch = int(rh * CROP_FRAC)
top = (rh - ch) // 2
tile = src.crop((0, top, rw, top + ch))                       # one clean repeat (rw x ch)
band = Image.new("RGB", (rw * REPEATS, ch))
for i in range(REPEATS):
    band.paste(tile, (i * rw, 0))
band.save("assets/hive-band.png")
print("band", band.size, "| at ~1012 width renders ~", round(1012 * ch / (rw * REPEATS)), "px tall,", REPEATS, "exact repeats")
