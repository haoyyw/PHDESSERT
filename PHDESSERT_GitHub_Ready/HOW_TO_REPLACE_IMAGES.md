# How to replace PhDessert images on GitHub

The website is designed so photographs can be replaced without editing `index.html`.

## Core rule

Replace the existing image at the same path and keep the **exact same filename**.

## Product photograph example

To replace the photo for Matcha Fig Cake / 抹茶无花果蛋糕:

1. Open this repository on GitHub.
2. Open `assets` → `products`.
3. Open `matcha-fig.webp`.
4. Use the file menu to delete the old file, or navigate back to `assets/products` and use **Add file → Upload files**.
5. Upload your new high-resolution image named exactly `matcha-fig.webp`.
6. Commit the change directly to `main`.
7. Wait for GitHub Pages to redeploy, then refresh the website.

## Campaign photograph example

The three desktop hero images are:

- `assets/campaigns/hero-main.webp`
- `assets/campaigns/hero-chinese.webp`
- `assets/campaigns/hero-seasonal.webp`

Festival and closing artwork:

- `assets/campaigns/festival-mid-autumn.webp`
- `assets/campaigns/closing-waistband.webp`
- `assets/campaigns/brand-logo.webp`

## Recommended export settings

### Product cards
- WebP
- sRGB
- 1:1 square
- ideally 1400×1400 px or larger
- quality around 90–94

### Hero campaigns
- WebP
- sRGB
- 16:9 landscape
- ideally 2400×1350 px or larger
- no embedded words on the three hero backgrounds

### Closing waist banner
- around 2400×750–900 px
- embedded PhDessert branding and text are suitable here

See `IMAGE_REPLACEMENT_GUIDE.md` for the complete product-to-filename map.
