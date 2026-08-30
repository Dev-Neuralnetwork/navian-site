# Navian Digital — website

Static site. No build step, no dependencies. Every file here is served as-is.

```
index.html      home — hero, feature blocks, game grid, studio, contact
press.html      press kit for The Offering
privacy.html    privacy policy
css/style.css   all styles
js/main.js      sticky header, mobile menu, parallax, scroll reveals
assets/img/     key art, screenshots, favicon
assets/video/   looping background clips
assets/brand/   logo system + email signature (see its own README)
tools/          build_brand_png.py — regenerates the brand PNGs
CNAME           custom domain for GitHub Pages
```

The logo is the wordmark, set in HTML — there is no logo image on the page. The
N-in-a-square is only for square contexts (favicon, avatars, email). Rules are in
[assets/brand/README.md](assets/brand/README.md).

## Local preview

```powershell
npx serve .
```

Or open `index.html` directly — the only thing that needs a server is nothing, so
a file:// open works too.

## Deploying to GitHub Pages

1. Create a repo (e.g. `navian-site`) and push this folder to `main`.
2. Repo → Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Put your domain in `CNAME` (one line, no protocol, no trailing slash).
4. At your DNS host add:

   | Type  | Name | Value |
   |-------|------|-------|
   | A     | @    | `185.199.108.153` |
   | A     | @    | `185.199.109.153` |
   | A     | @    | `185.199.110.153` |
   | A     | @    | `185.199.111.153` |
   | CNAME | www  | `<username>.github.io.` |

5. Back in Settings → Pages, tick **Enforce HTTPS** once the certificate is issued
   (can take up to an hour).

`.nojekyll` is present so GitHub Pages serves files starting with `_` and skips
the Jekyll build.

## Editing content

Games are plain `<article class="card">` blocks in `index.html` — copy one to add
a game. `card--tba` is the dimmed placeholder variant.

Colours and type live in the `:root` block at the top of `css/style.css`.
