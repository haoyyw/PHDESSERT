# PhDessert

Official static website for **PhDessert · 匠心手作 · HANDCRAFTED**.

## Structure

- `index.html` — complete website, including layout, bilingual content and interactions.
- `assets/campaigns/` — hero, festival, logo and closing waist-banner artwork.
- `assets/products/` — one image per menu item.
- `IMAGE_REPLACEMENT_GUIDE.md` — exact image-to-product mapping and recommended dimensions.

## Menu architecture

The long-form homepage is organised into Chinese Handcrafted, Pâtisserie, Basque Collection, Cakes, Rolls, Small Desserts, Seasonal Edit and Festival Editions. English mode displays English menu names; Chinese mode displays Chinese menu names.

## Image replacement

To change photography without touching the website code, replace the relevant file in `assets/products/` or `assets/campaigns/` and keep the **same filename**.

Recommended source files:

- Product images: WebP, sRGB, 1:1, ideally 1400×1400 px or larger.
- Hero images: WebP, sRGB, 16:9, ideally 2400×1350 px or larger.
- Closing waist banner: roughly 2400×750–900 px; embedded branding/text is acceptable here.
- Main hero images should not contain embedded text because website typography is layered separately.

See `IMAGE_REPLACEMENT_GUIDE.md` for the full file map.

## GitHub Pages

This repository is intended to be published directly from the repository root using GitHub Pages. No build command, database or server-side runtime is required.
