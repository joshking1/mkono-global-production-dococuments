import base64
from pathlib import Path
from PIL import Image

# Update this to the actual path of your image file
png_path = Path("image(1717).png")
svg_path = Path("MG_logo_exact.svg")

with Image.open(png_path) as img:
    width, height = img.size

png_base64 = base64.b64encode(png_path.read_bytes()).decode("ascii")

svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="{width}"
    height="{height}"
    viewBox="0 0 {width} {height}"
    preserveAspectRatio="xMidYMid meet">

    <image
        width="{width}"
        height="{height}"
        x="0"
        y="0"
        href="data:image/png;base64,{png_base64}"
        preserveAspectRatio="none"
    />

</svg>
'''

svg_path.write_text(svg_content, encoding="utf-8")
print(f"SVG created: {svg_path.resolve()}")