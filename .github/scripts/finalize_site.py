from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# --- Product data ---------------------------------------------------------
size_products = {
    'yuzu-lemon-mousse': ('£24', '£34', '£46', '£6.50'),
    'basque-original': ('£14', '£22', '£32', '£5'),
    'basque-cocoa': ('£15', '£24', '£34', '£5.50'),
    'basque-matcha': ('£15', '£24', '£34', '£5.50'),
    'basque-pistachio': ('£16', '£26', '£38', '£6'),
    'basque-matcha-yuzu': ('£16', '£26', '£38', '£6'),
    'jasmine-grape-matcha': ('£32', '£42', '£56', '£8'),
    'blueberry-cake': ('£30', '£40', '£52', '£7.50'),
    'matcha-yuzu-cheesecake': ('£28', '£38', '£48', '£7'),
    'mango-pomelo-coconut': ('£32', '£42', '£56', '£8'),
    'light-cheesecake': ('£18', '£26', '£36', '£5'),
    'strawberry-cream': ('£28', '£38', '£48', '£7'),
    'matcha-fig': ('£32', '£42', '£56', '£8'),
    'fig-cheesecake': ('£30', '£40', '£52', '£7.50'),
}

def update_product_line(line, p4, p6, p8, pslice):
    en = f"4″ {p4} · 6″ {p6} · 8″ {p8} · Slice {pslice}"
    zh = f"4寸 {p4} · 6寸 {p6} · 8寸 {p8} · 单片 {pslice}"
    repl = (
        f"priceEn:'{en}',priceZh:'{zh}',"
        f"sizePrices:{{'4':'{p4}','6':'{p6}','8':'{p8}',slice:'{pslice}'}}"
    )
    line = re.sub(
        r"priceEn:'[^']*',priceZh:'[^']*'(?:,sizePrices:\{[^}]*\})?",
        repl,
        line,
        count=1,
    )
    return line

lines = s.splitlines()
seen = set()
for i, line in enumerate(lines):
    for pid, prices in size_products.items():
        if line.startswith("{id:'" + pid + "'"):
            lines[i] = update_product_line(line, *prices)
            seen.add(pid)
            break

missing = set(size_products) - seen
if missing:
    raise RuntimeError(f'Missing size-priced products: {sorted(missing)}')

# Make the roll price explicit instead of a vague starting price.
for i, line in enumerate(lines):
    if line.startswith("{id:'coconut-angel-roll'"):
        line = re.sub(
            r"priceEn:'[^']*',priceZh:'[^']*'(?:,orderFormat:'[^']*')?",
            "priceEn:'Whole roll £18',priceZh:'整条 £18',orderFormat:'roll'",
            line,
            count=1,
        )
        lines[i] = line
        break
else:
    raise RuntimeError('Coconut Angel Roll product not found')

# Add the four-piece Chinese tasting box after the rice cake.
if "id:'chinese-tasting-box'" not in '\n'.join(lines):
    tasting = (
        "{id:'chinese-tasting-box',group:'chinese',en:'Chinese Pastry Tasting Box',zh:'中式糕点拼盘',"
        "descEn:'A four-piece tasting set with Peach Blossom Pastry, Osmanthus Cake, Mung Bean Cake and Steamed Rice Cake — one of each.',"
        "descZh:'四件中式糕点拼盘：桃花酥、桂花糕、绿豆糕和纯大米糕，每款各一件。',"
        "sellEn:'Four signatures, one box.',sellZh:'四款经典，一盒尝遍。',"
        "priceEn:'£12.80 per set',priceZh:'£12.80 / 套',orderFormat:'tasting',"
        "collage:['peach-blossom','osmanthus-cake','mung-bean-cake','rice-cake']},"
    )
    inserted = False
    for i, line in enumerate(lines):
        if line.startswith("{id:'rice-cake'"):
            lines.insert(i + 1, tasting)
            inserted = True
            break
    if not inserted:
        raise RuntimeError('Rice Cake insertion point not found')

s = '\n'.join(lines) + '\n'

# --- Visual polish --------------------------------------------------------
if '.product-collage{' not in s:
    css = (
        ".product-collage{display:grid!important;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:2px}"
        ".product-collage img{position:relative!important;z-index:1;width:100%!important;height:100%!important;min-width:0;min-height:0;object-fit:cover}"
        ".cake-size-btn{border-radius:999px;background:rgba(255,253,248,.45);padding:8px 5px}"
        ".cake-size-btn:focus-visible{outline:2px solid var(--gold);outline-offset:2px}"
        ".cake-price-value{font-size:30px}"
        "@media(max-width:520px){.cake-size-tabs{gap:5px}.cake-size-btn{padding:8px 3px;font-size:8px}.cake-price-display{margin-top:11px}.cake-price-value{font-size:28px}}"
    )
    s = s.replace('</style>', css + '\n</style>', 1)

# More accurate menu intro now that whole-cake prices are interactive.
old_intro = (
    'data-en="Open a collection to explore the current menu. Indicative prices are shown for each item; final pricing depends on size and customisation and is confirmed when you enquire." '
    'data-zh="点击 ＋ 展开每个系列。每款均标注参考价格；尺寸和定制会影响最终价格，以咨询确认为准。">'
    'Open a collection to explore the current menu. Indicative prices are shown for each item; final pricing depends on size and customisation and is confirmed when you enquire.'
)
new_intro = (
    'data-en="Open a collection to explore the current menu. Select a size on whole cakes to see its price; other items show their current set or portion price. Custom decoration is confirmed when you enquire." '
    'data-zh="点击 ＋ 展开每个系列。整蛋糕可点击尺寸查看对应价格；其他产品显示当前套装或单份价格。定制装饰以咨询确认为准。">'
    'Open a collection to explore the current menu. Select a size on whole cakes to see its price; other items show their current set or portion price. Custom decoration is confirmed when you enquire.'
)
if old_intro in s:
    s = s.replace(old_intro, new_intro, 1)

# --- Rendering ------------------------------------------------------------
img_func = "function imgTag(p,cls=''){const fallback=p.group==='festival'?'assets/campaigns/festival-mid-autumn.webp':'';return `<img loading=\"lazy\" class=\"${cls}\" src=\"${imagePath(p)}\" alt=\"${locale==='en'?p.en:p.zh}\"${fallback?` data-fallback=\"${fallback}\"`:''}>`}"
visual_func = "function productVisual(p,cls='product-photo'){if(!p.collage)return `<div class=\"${cls}\">${imgTag(p)}</div>`;return `<div class=\"${cls} product-collage\">${p.collage.map(id=>{const item=products.find(x=>x.id===id);return item?imgTag(item):''}).join('')}</div>`}"
if 'function productVisual(p' not in s:
    if img_func not in s:
        raise RuntimeError('imgTag function insertion point not found')
    s = s.replace(img_func, img_func + '\n' + visual_func, 1)

old_bind = "function bindCakePricing(root=document){root.querySelectorAll('.cake-size-btn').forEach(b=>{b.onclick=()=>{const box=b.closest('.cake-pricing');box.querySelectorAll('.cake-size-btn').forEach(x=>{const active=x===b;x.classList.toggle('active',active);x.setAttribute('aria-pressed',String(active))});box.dataset.selectedSize=b.dataset.size;box.querySelector('.cake-price-size').textContent=b.dataset.label;box.querySelector('.cake-price-value').textContent=b.dataset.price}})}"
new_bind = "function bindCakePricing(root=document){root.querySelectorAll('.cake-pricing').forEach(box=>{const sync=b=>{box.querySelectorAll('.cake-size-btn').forEach(x=>{const active=x===b;x.classList.toggle('active',active);x.setAttribute('aria-pressed',String(active))});box.dataset.selectedSize=b.dataset.size;box.querySelector('.cake-price-size').textContent=b.dataset.label;box.querySelector('.cake-price-value').textContent=b.dataset.price;const trigger=box.closest('.product-card,.seasonal-card')?.querySelector('.order-trigger');if(trigger){trigger.dataset.size=b.dataset.size;trigger.dataset.price=b.dataset.price}};box.querySelectorAll('.cake-size-btn').forEach(b=>b.onclick=()=>sync(b));const initial=box.querySelector('.cake-size-btn.active');if(initial)sync(initial)})}"
if old_bind not in s:
    raise RuntimeError('bindCakePricing function not found')
s = s.replace(old_bind, new_bind, 1)

old_card = "function productCard(p){return `<article class=\"product-card\"><div class=\"product-photo\">${imgTag(p)}</div><div class=\"product-copy\"><h4>${locale==='en'?p.en:p.zh}</h4><p>${locale==='en'?p.descEn:p.descZh}</p><p class=\"selling\">${locale==='en'?p.sellEn:p.sellZh}</p>${p.group==='cakes'?cakePricing(p):`<p class=\"price\">${locale==='en'?p.priceEn:p.priceZh}</p>`}<button class=\"enquire order-trigger\" data-product=\"${p.id}\">${locale==='en'?'Enquire ↗':'预约咨询 ↗'}</button></div></article>`}"
new_card = "function productCard(p){return `<article class=\"product-card\">${productVisual(p)}<div class=\"product-copy\"><h4>${locale==='en'?p.en:p.zh}</h4><p>${locale==='en'?p.descEn:p.descZh}</p><p class=\"selling\">${locale==='en'?p.sellEn:p.sellZh}</p>${p.sizePrices?cakePricing(p):`<p class=\"price\">${locale==='en'?p.priceEn:p.priceZh}</p>`}<button class=\"enquire order-trigger\" data-product=\"${p.id}\">${locale==='en'?'Enquire ↗':'预约咨询 ↗'}</button></div></article>`}"
if old_card not in s:
    raise RuntimeError('productCard function not found')
s = s.replace(old_card, new_card, 1)

old_seasonal = "function renderSeasonal(){const items=products.filter(p=>p.group==='seasonal');$('#seasonalCards').innerHTML=items.map(p=>`<article class=\"seasonal-card\"><div class=\"seasonal-product-photo\">${imgTag(p)}</div><div class=\"product-copy\"><h3>${locale==='en'?p.en:p.zh}</h3><p>${locale==='en'?p.descEn:p.descZh}</p><p class=\"selling\">${locale==='en'?p.sellEn:p.sellZh}</p><p class=\"price\">${locale==='en'?p.priceEn:p.priceZh}</p><button class=\"enquire order-trigger\" data-product=\"${p.id}\">${locale==='en'?'Enquire ↗':'预约咨询 ↗'}</button></div></article>`).join('');bindOrder();wireImages($('#seasonalCards'))}"
new_seasonal = "function renderSeasonal(){const items=products.filter(p=>p.group==='seasonal');const root=$('#seasonalCards');root.innerHTML=items.map(p=>`<article class=\"seasonal-card\">${productVisual(p,'seasonal-product-photo')}<div class=\"product-copy\"><h3>${locale==='en'?p.en:p.zh}</h3><p>${locale==='en'?p.descEn:p.descZh}</p><p class=\"selling\">${locale==='en'?p.sellEn:p.sellZh}</p>${p.sizePrices?cakePricing(p):`<p class=\"price\">${locale==='en'?p.priceEn:p.priceZh}</p>`}<button class=\"enquire order-trigger\" data-product=\"${p.id}\">${locale==='en'?'Enquire ↗':'预约咨询 ↗'}</button></div></article>`).join('');bindCakePricing(root);bindOrder();wireImages(root)}"
if old_seasonal not in s:
    raise RuntimeError('renderSeasonal function not found')
s = s.replace(old_seasonal, new_seasonal, 1)

# --- Order flow -----------------------------------------------------------
s = re.sub(r'<select id="size" required>.*?</select>', '<select id="size" required></select>', s, count=1)

old_populate = "function populateProducts(){const sel=$('#product');const current=sel.value;sel.innerHTML=`<option value=\"\">${locale==='en'?'Please select':'请选择'}</option>`+products.map(p=>`<option value=\"${p.id}\">${locale==='en'?p.en:p.zh} · ${locale==='en'?p.priceEn:p.priceZh}</option>`).join('');if([...sel.options].some(o=>o.value===current))sel.value=current}"
new_populate = "function productMenuPrice(p){return p.sizePrices?(locale==='en'?`6″ ${p.sizePrices['6']}`:`6寸 ${p.sizePrices['6']}`):(locale==='en'?p.priceEn:p.priceZh)}\nfunction populateProducts(){const sel=$('#product');const current=sel.value;sel.innerHTML=`<option value=\"\">${locale==='en'?'Please select':'请选择'}</option>`+products.map(p=>`<option value=\"${p.id}\">${locale==='en'?p.en:p.zh} · ${productMenuPrice(p)}</option>`).join('');if([...sel.options].some(o=>o.value===current))sel.value=current}\nfunction sizeOptionLabel(key){const en={single:'Single / portion',box:'Dessert box',tasting:'4-piece tasting box',roll:'Whole roll','4':'4-inch','6':'6-inch','8':'8-inch',slice:'Slice (1/8 of 8-inch cake)',other:'Other / discuss'};const zh={single:'单份',box:'甜品盒',tasting:'四件中式糕点拼盘',roll:'整条','4':'4寸','6':'6寸','8':'8寸',slice:'单片（8寸蛋糕的1/8）',other:'其他 / 沟通确认'};return (locale==='en'?en:zh)[key]||key}\nfunction setOrderSizeForProduct(p,preferred=''){const sel=$('#size');let keys;if(p?.sizePrices)keys=['4','6','8','slice','other'];else if(p?.orderFormat==='tasting')keys=['tasting','other'];else if(p?.orderFormat==='roll')keys=['roll','other'];else keys=['single','box','other'];sel.innerHTML=`<option value=\"\">${locale==='en'?'Please select':'请选择'}</option>`+keys.map(k=>`<option value=\"${k}\">${sizeOptionLabel(k)}</option>`).join('');const fallback=p?.sizePrices?'6':(p?.orderFormat||'');const chosen=keys.includes(preferred)?preferred:fallback;if(chosen)sel.value=chosen}\nfunction resolveOrderPrice(p,sizeKey){if(!p)return '';if(p.sizePrices&&p.sizePrices[sizeKey])return p.sizePrices[sizeKey];return locale==='en'?p.priceEn:p.priceZh}"
if old_populate not in s:
    raise RuntimeError('populateProducts function not found')
s = s.replace(old_populate, new_populate, 1)

old_bind_order = "function bindOrder(){$$('.order-trigger').forEach(b=>{if(b.dataset.bound)return;b.dataset.bound='1';b.onclick=()=>{populateProducts();if(b.dataset.product)$('#product').value=b.dataset.product;$('#orderForm').hidden=false;$('#result').hidden=true;modal.showModal()}})}"
new_bind_order = "function bindOrder(){$$('.order-trigger').forEach(b=>{if(b.dataset.bound)return;b.dataset.bound='1';b.onclick=()=>{populateProducts();if(b.dataset.product)$('#product').value=b.dataset.product;const p=products.find(x=>x.id===$('#product').value);setOrderSizeForProduct(p,b.dataset.size||p?.orderFormat||'');$('#orderForm').hidden=false;$('#result').hidden=true;modal.showModal()}})}"
if old_bind_order not in s:
    raise RuntimeError('bindOrder function not found')
s = s.replace(old_bind_order, new_bind_order, 1)

old_submit = "$('#close').onclick=()=>modal.close();$('#cancel').onclick=()=>modal.close();modal.onclick=e=>{if(e.target===modal)modal.close()};$('#orderForm').onsubmit=e=>{e.preventDefault();const p=products.find(x=>x.id===$('#product').value);const data={p:p?(locale==='en'?p.en:p.zh):'',size:$('#size').value,date:$('#date').value,name:$('#name').value,contact:$('#contact').value,notes:$('#notes').value,price:p?(locale==='en'?p.priceEn:p.priceZh):''};$('#summary').textContent=locale==='en'?`PhDessert Order Enquiry\\nDessert: ${data.p}\\nListed price: ${data.price}\\nFormat / size: ${data.size}\\nCollection date: ${data.date}\\nName: ${data.name}\\nContact: ${data.contact}\\nNotes: ${data.notes||'—'}`:`PhDessert 预约咨询\\n甜品：${data.p}\\n参考价格：${data.price}\\n规格 / 尺寸：${data.size}\\n取货日期：${data.date}\\n姓名：${data.name}\\n联系方式：${data.contact}\\n备注：${data.notes||'—'}`;"
new_submit = "$('#close').onclick=()=>modal.close();$('#cancel').onclick=()=>modal.close();modal.onclick=e=>{if(e.target===modal)modal.close()};$('#product').onchange=()=>{const p=products.find(x=>x.id===$('#product').value);setOrderSizeForProduct(p,p?.sizePrices?'6':p?.orderFormat||'')};$('#orderForm').onsubmit=e=>{e.preventDefault();const p=products.find(x=>x.id===$('#product').value);const sizeKey=$('#size').value;const data={p:p?(locale==='en'?p.en:p.zh):'',size:sizeOptionLabel(sizeKey),date:$('#date').value,name:$('#name').value,contact:$('#contact').value,notes:$('#notes').value,price:resolveOrderPrice(p,sizeKey)};$('#summary').textContent=locale==='en'?`PhDessert Order Enquiry\\nDessert: ${data.p}\\nPrice: ${data.price}\\nFormat / size: ${data.size}\\nCollection date: ${data.date}\\nName: ${data.name}\\nContact: ${data.contact}\\nNotes: ${data.notes||'—'}`:`PhDessert 预约咨询\\n甜品：${data.p}\\n价格：${data.price}\\n规格 / 尺寸：${data.size}\\n取货日期：${data.date}\\n姓名：${data.name}\\n联系方式：${data.contact}\\n备注：${data.notes||'—'}`;"
if old_submit not in s:
    raise RuntimeError('Order submit block not found')
s = s.replace(old_submit, new_submit, 1)

old_locale = "renderMenu();renderSeasonal();renderFestival();populateProducts();bindContact()}"
new_locale = "renderMenu();renderSeasonal();renderFestival();const currentProduct=products.find(x=>x.id===$('#product').value);const currentSize=$('#size').value;populateProducts();setOrderSizeForProduct(currentProduct,currentSize);bindContact()}"
if old_locale not in s:
    raise RuntimeError('applyLocale tail not found')
s = s.replace(old_locale, new_locale, 1)

if 'From £' in s or '£ 起' in s:
    raise RuntimeError('A vague starting price remains after finalization')

p.write_text(s, encoding='utf-8')
