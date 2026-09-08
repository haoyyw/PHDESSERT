# PhDessert Website Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the PhDessert GitHub Pages site as a bilingual, long-form boutique dessert website with category accordions, 27 product entries, three hero campaigns, seasonal content, high-resolution product photography, concise sourcing copy, and customer-facing order enquiry flow.

**Architecture:** Keep the site static and dependency-light. Use `index.html` for document structure, `styles.css` and `menu.css` for responsive presentation, `app.js` for language switching, accordions, hero rotation and product rendering, `i18n.js` for bilingual copy, and `order.js` for enquiry validation/summary. Product images live under `phdessert/assets/products/` and campaign images under `phdessert/assets/campaigns/`.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript ES modules, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-07-phdessert-menu-redesign.md`

## Global Constraints

- Public URL remains `https://haoyyw.github.io/phdessert/` after merge.
- English mode shows English-only product names and descriptions.
- Chinese mode shows Chinese-only product names and descriptions.
- No `All` menu filter.
- Menu is a long page with anchored category sections and `＋` accordion controls.
- Seasonal Edit remains separate from the permanent menu.
- Use the user-provided logo and original campaign artwork unchanged as the first hero slide.
- Chinese pastry is presented as a distinctive collection without repeated positioning copy.
- Mention Costco UK sourcing once, concisely, in the ingredients/about area.
- Remove internal notes, design explanations, and author-facing meta-copy from the customer site.
- Rename `抹茶格莱斯无花果蛋糕` to `抹茶无花果蛋糕` / `Matcha Fig Cake`.
- Include `无花果芝士蛋糕` / `Fig Cheesecake` and `蓝莓蛋糕` / `Blueberry Cake`.

---

### Task 1: Product catalogue and bilingual copy

**Files:**
- Modify: `phdessert/src/app.js`
- Modify: `phdessert/src/i18n.js`

**Interfaces:**
- Produces: `PRODUCTS`, `MENU_SECTIONS`, language-aware `productName()`, `productDescription()`, `productSellingPoint()`.

- [ ] Define all 27 products with stable IDs, category IDs, English and Chinese names, descriptions, selling points and image paths.
- [ ] Define menu sections in customer-facing order: Chinese Handcrafted, Pâtisserie, Basque Collection, Cakes, Small Desserts.
- [ ] Remove `all` filtering and bilingual mixed product labels.
- [ ] Verify by running a Node smoke script that asserts 27 unique IDs, non-empty copy in both languages and valid section membership.

### Task 2: Long-page accordion menu and navigation

**Files:**
- Modify: `phdessert/index.html`
- Modify: `phdessert/src/app.js`
- Modify: `phdessert/src/menu.css`
- Modify: `phdessert/src/styles.css`

**Interfaces:**
- Produces: anchor IDs `chinese`, `patisserie`, `basque`, `cakes`, `small-desserts`, `seasonal`, `about`, `order`.

- [ ] Replace filter-bar menu with long-page category accordions.
- [ ] Preserve top navigation as anchor links.
- [ ] Make each category header keyboard-accessible and toggle with `＋` / `−`.
- [ ] Product cards render image, name, flavour description, selling point and Enquire button.
- [ ] Verify accordion state, keyboard focus and responsive layout in Chromium.

### Task 3: Three-slide hero and campaigns

**Files:**
- Modify: `phdessert/index.html`
- Modify: `phdessert/src/app.js`
- Modify: `phdessert/src/styles.css`
- Create/use: `phdessert/assets/campaigns/brand-original.*`
- Create/use: `phdessert/assets/campaigns/chinese-handcrafted.*`
- Create/use: `phdessert/assets/campaigns/seasonal-edit.*`

- [ ] Slide 1 uses the user-provided campaign artwork unchanged.
- [ ] Slide 2 uses the generated Chinese pastry campaign.
- [ ] Slide 3 uses the seasonal campaign.
- [ ] Add accessible previous/next controls and slide indicators; no aggressive autoplay.
- [ ] Verify images stay sharp at desktop and mobile breakpoints.

### Task 4: Product imagery

**Files:**
- Create: `phdessert/assets/products/*.webp`

- [ ] Select one strongest generated photograph for each of the 27 products.
- [ ] Resize/crop consistently for web display, retain high visual quality, convert to WebP.
- [ ] Use ASCII filenames mapped in `PRODUCTS`.
- [ ] Verify every product path resolves and no generated placeholder/SVG remains.

### Task 5: Customer-facing copy audit and sourcing

**Files:**
- Modify: `phdessert/index.html`
- Modify: `phdessert/src/i18n.js`

- [ ] Remove copy such as `Chinese classics at the centre...`, `Product names stay bilingual by design`, and all internal design rationale.
- [ ] Replace sourcing copy with concise freshness/quality language mentioning Costco UK once.
- [ ] Keep Chinese origin present in the brand story without repetitive emphasis.
- [ ] Review all visible copy from a customer's perspective in both languages.

### Task 6: Order flow and final verification

**Files:**
- Modify: `phdessert/src/app.js`
- Modify: `phdessert/src/order.js` only if required by catalogue changes.

- [ ] Product selector follows current locale and includes all 27 products.
- [ ] Enquire buttons preselect the correct product.
- [ ] Run JS syntax/import smoke tests.
- [ ] Render desktop and mobile screenshots in Chromium.
- [ ] Test EN ↔ 中文, accordion open/close, hero controls, FAQ, order form validation and copy-summary flow.
- [ ] Confirm no broken image requests and no customer-visible internal notes.
