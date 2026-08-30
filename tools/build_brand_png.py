"""Rasterise the Navian box mark to PNG.

The N is drawn from the same outline polygon as assets/brand/navian-n.svg, so the
SVG and the PNGs can never drift. Everything is drawn at 16x and downsampled with
LANCZOS, which is what keeps the diagonal clean at 16px.

    py tools/build_brand_png.py
"""

from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent / "assets" / "brand"

NAVY = (2, 11, 24, 255)
WHITE = (255, 255, 255, 255)

SS = 16  # supersample factor

# Letterform outline on a 100x100 artboard — identical to navian-n.svg.
N_OUTLINE = [
    (22, 24.3), (39.5, 24.3), (65.2, 61.7), (65.2, 24.3),
    (78, 24.3), (78, 75.7), (59.3, 75.7), (34.8, 40.7),
    (34.8, 75.7), (22, 75.7),
]

CORNER_RADIUS = 18  # on the 100 artboard


def _scaled(points, size):
    k = size / 100.0
    return [(x * k, y * k) for x, y in points]


def box(size, fg=WHITE, bg=NAVY, radius=CORNER_RADIUS):
    """The N in a rounded square."""
    big = size * SS
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, big - 1, big - 1], radius=radius / 100.0 * big, fill=bg)
    d.polygon(_scaled(N_OUTLINE, big), fill=fg)
    return img.resize((size, size), Image.LANCZOS)


def glyph(size, fg=WHITE):
    """The N alone, transparent background — for email signatures."""
    big = size * SS
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    ImageDraw.Draw(img).polygon(_scaled(N_OUTLINE, big), fill=fg)
    return img.resize((size, size), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    written = []

    for size in (16, 32, 48, 180, 512):
        p = OUT / f"navian-box-{size}.png"
        box(size).save(p)
        written.append(p)

    # Email signatures need a raster: Outlook will not render SVG.
    # 2x of a 40px display size, both on navy and transparent-on-white.
    for size in (80, 160):
        p = OUT / f"navian-box-mail-{size}.png"
        box(size).save(p)
        written.append(p)

    p = OUT / "navian-n-dark-160.png"
    glyph(160, fg=NAVY).save(p)
    written.append(p)

    for p in written:
        print(f"{p.name:28} {p.stat().st_size:>7} B")


if __name__ == "__main__":
    main()
