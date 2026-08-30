# Navian Digital — brand assets

**The logo is the wordmark.** `NAVIAN` over `DIGITAL`, set in Rubik. The
N-in-a-square is not a logo — it is the compact mark, and it appears only where
the container is square and too small for words: favicon, app icon, social
avatar, Steam partner avatar, email signature. It never sits on the page beside
the wordmark.

## Files

| File | Use |
|------|-----|
| `navian-n.svg` | The N alone, `currentColor`. For stamping onto an existing surface. |
| `navian-box.svg` | White N on navy. The compact mark. |
| `navian-box-inverse.svg` | Navy N on white. For light backgrounds and print. |
| `navian-box-{16,32,48}.png` | Favicon sizes. |
| `navian-box-180.png` | `apple-touch-icon`. |
| `navian-box-512.png` | PWA icon, social avatar, store listings. |
| `navian-box-mail-{80,160}.png` | Email signature, 2× of 40px / 80px display. |
| `navian-n-dark-160.png` | Navy N, transparent background. |
| `email-signature.html` | Copy-paste signature. Outlook-safe table markup. |

Regenerate every PNG from the SVG outline with:

```
py tools/build_brand_png.py
```

The script draws from the same polygon as `navian-n.svg`, so the vector and the
rasters cannot drift apart. Do not edit the PNGs by hand.

## The wordmark

```
NAVIAN    Rubik 900,  letter-spacing 0.15em
DIGITAL   Rubik 300,  letter-spacing 0.40em,  62% opacity
```

`DIGITAL` sits 6px under `NAVIAN` at a 20px cap. Both lines are optically
centred by pulling back the trailing letter-space with a negative right margin —
tracked type is always off-centre without it.

**Clear space** is the cap height of `NAVIAN` on all four sides.

**Never**: stretch it, re-set it in another face, add a tagline inside the
lockup, apply a gradient, or set `DIGITAL` at full opacity.

## Colour

There isn't one. White on `#020b18`, or `#020b18` on white — nothing else. A
studio mark that carries a colour competes with the art of every game it stamps,
so the games own the palette and the brand stays neutral.

## The letterform

The N is an outlined polygon, not a stroked polyline. A stroked N grows miter
spikes at the two sharp corners that lengthen unpredictably with weight; the
outline cuts the diagonal flat at cap line and baseline the way a drawn N is,
so it rasterises identically at 16px and 512px.

Stem width is 12.8 units against a 51.4 cap height (0.25), which matches Rubik
900 closely enough that the mark and the wordmark read as one family.
