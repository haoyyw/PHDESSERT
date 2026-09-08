# PhDessert Menu and Brand Website Redesign

## Goal

Refine the existing PhDessert GitHub Pages site into a customer-facing bilingual boutique dessert website with a long-form editorial layout, category accordions, a three-slide hero, 27 products, stronger product photography, and a cleaner brand voice.

## Non-negotiable brand constraints

- Keep the public URL unchanged: `https://haoyyw.github.io/phdessert/`.
- Keep the supplied PhDessert logo artwork unchanged. The logo wording is `匠心手作 · HANDCRAFTED` and `PÂTISSERIE ARTISANALE` must not return.
- Keep the supplied original PhDessert campaign artwork unchanged as the first hero slide.
- Preserve the dark forest green, ivory, restrained gold, high-end serif, boutique pâtisserie / perfume / hotel visual language.
- Preserve the hidden PhD reference and very small graduation-cap motif.
- English mode shows English product names and English descriptions only.
- Chinese mode shows Chinese product names and Chinese descriptions only.
- No explanatory internal design notes may appear to customers.
- Chinese desserts should read as a distinctive strength of the British offering, without repeatedly foregrounding ethnicity or using copy such as `Chinese classics at the centre...`.

## Customer-facing page architecture

The site remains one continuous long page rather than separate menu pages.

### Sticky top navigation

Use compact anchor links that scroll to sections:

`Home · Chinese · Pâtisserie · Basque · Cakes · Small Desserts · Seasonal · About · Order`

The existing `EN / 中文` switch stays visible.

### Hero carousel

Three editorial slides:

1. **Brand Campaign**: use the supplied original PhDessert campaign image exactly as provided.
2. **Chinese Handcrafted Campaign**: new campaign image featuring selected Chinese pastries such as peach blossom pastry, osmanthus cake, mung bean cake and taro pastry. The visual style should remain PhDessert, not a generic Chinese restaurant aesthetic.
3. **Seasonal Edit**: a rotating seasonal campaign driven by the current seasonal selection. Initially it may use the late-summer fig direction, but the content must be easy to replace without redesigning the page.

Carousel controls should be discreet and accessible. It should also work as swipeable content on mobile.

## Menu interaction

There is no `All` section.

The main menu is divided into category blocks in the long page. Each category appears as an elegant horizontal accordion header with a short customer-facing descriptor and a `+` control. Opening the category reveals all products in that category. Closing it returns the page to a compact editorial state.

A category can also be opened directly from the sticky navigation.

Each product card contains:

- one dedicated product photograph;
- product name in the active language only;
- one short flavour description;
- one short differentiating selling point;
- `Enquire` / `预约` action.

No price is added until the owner supplies final pricing.

## Product taxonomy and order

### 01 Chinese Handcrafted / 中式手作

1. 桃花酥 / Peach Blossom Pastry
2. 桂花糕 / Osmanthus Cake
3. 台式芋头酥 / Taiwanese Taro Pastry
4. 肉松小贝 / Pork Floss Mini Cake
5. 绿豆糕 / Mung Bean Cake
6. 纯大米糕 / Steamed Rice Cake
7. 蜂蜜蛋糕 / Honey Cake
8. 双皮奶 / Double-Skin Milk Pudding

This collection should be presented as a distinctive handcrafted selection in the UK. Avoid repetitive identity commentary elsewhere on the site.

### 02 Pâtisserie / 法式灵感

9. 蝴蝶酥 / Palmier
10. 柠檬巴巴露亚 / Lemon Bavarois
11. 提拉米苏 / Tiramisu
12. 柚子柠檬乳酪慕斯蛋糕 / Yuzu Lemon Cheesecake Mousse

### 03 Basque Collection / 巴斯克系列

13. 原味巴斯克 / Original Basque Cheesecake
14. 可可巴斯克 / Cocoa Basque Cheesecake
15. 抹茶巴斯克 / Matcha Basque Cheesecake
16. 开心果巴斯克 / Pistachio Basque Cheesecake
17. 抹茶柚子巴斯克 / Matcha Yuzu Basque Cheesecake

### 04 Cakes / 蛋糕系列

18. 茉莉青提抹茶奶油蛋糕 / Jasmine Grape Matcha Cream Cake
19. 椰子天使卷 / Coconut Angel Roll
20. 抹茶无花果蛋糕 / Matcha Fig Cake
21. 无花果芝士蛋糕 / Fig Cheesecake
22. 抹茶柚子芝士蛋糕 / Matcha Yuzu Cheesecake
23. 椰奶冻冻杨枝甘露蛋糕 / Coconut Mango Pomelo Cake
24. 轻乳酪蛋糕 / Japanese-Style Light Cheesecake
25. 草莓鲜奶蛋糕 / Strawberry Fresh Cream Cake
26. 蓝莓蛋糕 / Blueberry Cake

### 05 Small Desserts / 小甜品

27. 酸奶碗 / Yoghurt Bowl

A future Biscuits category may be added once there are actual biscuit products. Do not show an empty category now.

### 06 Seasonal Edit / 时令限定

Seasonal remains structurally separate from the permanent 27-item menu. Seasonal products must be data-driven so they can rotate without changing page structure. The third hero slide links here.

## Product naming and copy rules

### English mode

- English only.
- Use idiomatic British menu English rather than literal translations.
- Descriptions should be concise, sensory and commercially useful.
- Avoid generic luxury filler such as `crafted with passion`, `premium experience`, or internal explanations of the concept.

Example:

**Matcha Fig Cake**  
Matcha sponge, fresh fig and light cream.  
`Earthy tea depth, ripe fruit and restrained sweetness.`

### Chinese mode

- Chinese only.
- Names and descriptions should read naturally to Chinese customers.
- Avoid showing the English name beneath every Chinese product.

Example:

**抹茶无花果蛋糕**  
抹茶蛋糕、鲜无花果和轻盈奶油。  
`茶香清苦，果香柔和，甜度克制。`

## Photography system

Generate one dedicated image for every permanent product, plus the Chinese campaign and seasonal campaign.

The images should draw from contemporary high-quality East Asian social-food photography, including the strongest visual conventions commonly seen on Xiaohongshu, while remaining original rather than copying a specific photograph.

Unified visual direction:

- editorial food photography;
- natural side light;
- tactile cream, pastry and crumb texture;
- ivory, stone, muted green and warm neutral backgrounds;
- restrained props;
- premium café / boutique pâtisserie styling;
- consistent crop system, preferably 4:5 for product cards;
- no visible text, watermarks, fake logos or hands unless materially useful;
- food must remain recognisable as the named product.

The supplied logo and original campaign image are not regenerated.

## Ingredients and sourcing copy

Mention Costco UK once in a restrained About / Ingredients block.

English:

`Thoughtfully sourced. We select our dairy, fruit and baking ingredients from Costco UK for freshness, consistency and quality.`

Chinese:

`认真选材。乳制品、水果和烘焙原料主要采购自 Costco UK，重视新鲜度、稳定性和品质。`

Do not imply that every single ingredient is necessarily sourced from Costco if that is not operationally guaranteed.

## About section

Retain the PhDessert research / PhD origin quietly. Keep it human and customer-facing. Remove self-referential design commentary such as explanations that the PhD element is `hidden in the details` if it reads like an internal branding note.

The brand story should communicate:

- handcrafted small-batch production;
- careful ingredient selection;
- a broad dessert repertoire spanning Chinese handmade pastries, French-inspired desserts, cheesecakes and celebration cakes;
- Sheffield pickup and advance ordering.

## Order flow

Retain the existing enquiry modal and bilingual behaviour.

The product selector must contain all 27 permanent products plus active seasonal products. Product names displayed in the selector follow the current language.

Retain:

- product selection;
- size selection;
- collection date;
- customer name;
- contact / WeChat;
- notes;
- allergy note;
- copyable enquiry summary.

## Customer-perspective editorial audit

Before release, review the full site from the perspective of a new customer and remove:

- internal project notes;
- explanations of why a design choice was made;
- redundant identity language;
- repeated sourcing claims;
- empty categories;
- untranslated strings;
- awkward literal English translations;
- duplicate product definitions;
- placeholder imagery;
- broken image paths;
- old `PÂTISSERIE ARTISANALE` references;
- old `All` filtering controls.

## Responsive behaviour

Desktop should feel editorial and spacious. Mobile should preserve hierarchy without forcing all 27 products onto the screen at once. Accordions, hero swipe, enquiry modal and language switching must remain fully usable on iPhone-size screens.

## Acceptance criteria

The redesign is accepted when:

1. The URL remains unchanged and loads successfully on GitHub Pages.
2. The supplied original logo and first campaign artwork are used unchanged.
3. `PÂTISSERIE ARTISANALE` is absent from customer-facing copy.
4. The hero contains three working slides.
5. There is no `All` product section.
6. The permanent menu contains exactly 27 products in the taxonomy above.
7. `抹茶格莱斯无花果蛋糕` has been renamed `抹茶无花果蛋糕`.
8. `无花果芝士蛋糕` and `蓝莓蛋糕` are present.
9. English mode is entirely English for menu content and Chinese mode entirely Chinese.
10. Category accordions open and close correctly from both the page and top anchors.
11. Every permanent product has a dedicated image and concise flavour / selling-point copy.
12. Seasonal content is separate from the permanent menu.
13. Costco UK appears once in restrained sourcing copy.
14. Order selection covers the complete menu.
15. Desktop and mobile rendering pass visual review with no broken assets.
16. A final customer-perspective audit finds no internal-note-style copy or obsolete branding.
