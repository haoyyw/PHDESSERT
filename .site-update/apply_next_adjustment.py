from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# 1) Replace the temporary 2x2 collage with the approved single product photo.
old_tasting = "{id:'chinese-tasting-box',group:'chinese',en:'Chinese Pastry Tasting Box',zh:'中式糕点拼盘',descEn:'A four-piece tasting set with Peach Blossom Pastry, Osmanthus Cake, Mung Bean Cake and Steamed Rice Cake — one of each.',descZh:'四件中式糕点拼盘：桃花酥、桂花糕、绿豆糕和纯大米糕，每款各一件。',sellEn:'Four signatures, one box.',sellZh:'四款经典，一盒尝遍。',priceEn:'£12.80 per set',priceZh:'£12.80 / 套',orderFormat:'tasting',collage:['peach-blossom','osmanthus-cake','mung-bean-cake','rice-cake']},"
new_tasting = "{id:'chinese-tasting-box',group:'chinese',en:'Chinese Pastry Tasting Box',zh:'中式糕点拼盘',descEn:'A four-piece tasting set with Peach Blossom Pastry, Osmanthus Cake, Mung Bean Cake and Steamed Rice Cake — one of each.',descZh:'四件中式糕点拼盘：桃花酥、桂花糕、绿豆糕和纯大米糕，每款各一件。',sellEn:'Four signatures, one box.',sellZh:'四款经典，一盒尝遍。',image:'assets/products/chinese-tasting-box.webp',priceEn:'£12.80 per set',priceZh:'£12.80 / 套',orderFormat:'tasting'},"
if old_tasting not in s:
    raise RuntimeError('Chinese tasting box record not found in expected form')
s = s.replace(old_tasting, new_tasting, 1)

# 2) Give the roll a clear whole/slice choice with a retail premium on the slice.
old_roll = "{id:'coconut-angel-roll',group:'rolls',en:'Coconut Angel Roll',zh:'椰子天使卷',descEn:'A soft Swiss-style roll with airy cream and coconut fragrance.',descZh:'瑞士卷式松软蛋糕体搭配轻盈奶油和椰香。',sellEn:'Light sponge, soft cream, clean coconut finish.',sellZh:'蛋糕轻软，奶油细腻，椰香干净。',priceEn:'Whole roll £18',priceZh:'整条 £18',orderFormat:'roll'},"
new_roll = "{id:'coconut-angel-roll',group:'rolls',en:'Coconut Angel Roll',zh:'椰子天使卷',descEn:'A soft Swiss-style roll with airy cream and coconut fragrance.',descZh:'瑞士卷式松软蛋糕体搭配轻盈奶油和椰香。',sellEn:'Light sponge, soft cream, clean coconut finish.',sellZh:'蛋糕轻软，奶油细腻，椰香干净。',priceEn:'Whole roll £18 · Slice £5',priceZh:'整条 £18 · 小片 £5',rollPrices:{whole:'£18',slice:'£5'},orderFormat:'roll'},"
if old_roll not in s:
    raise RuntimeError('Coconut Angel Roll record not found in expected form')
s = s.replace(old_roll, new_roll, 1)

# 3) Add a boutique two-option price selector for rolls, reusing the same visual language as cake size selectors.
needle = "function cakePricing(p){const sizes=[['4','4″'],['6','6″'],['8','8″'],['slice',locale==='en'?'Slice':'单片']];return `<div class=\"cake-pricing\" data-product=\"${p.id}\" data-selected-size=\"6\"><div class=\"cake-size-tabs\" role=\"group\" aria-label=\"${locale==='en'?'Choose cake size':'选择蛋糕尺寸'}\">${sizes.map(([key,label])=>`<button type=\"button\" class=\"cake-size-btn${key==='6'?' active':''}\" data-size=\"${key}\" data-label=\"${label}\" data-price=\"${p.sizePrices[key]}\" aria-pressed=\"${key==='6'}\">${label}</button>`).join('')}</div><div class=\"cake-price-display\"><span class=\"cake-price-size\">6″</span><strong class=\"cake-price-value\">${p.sizePrices['6']}</strong></div><p class=\"cake-price-note\">${locale==='en'?'Slice = 1/8 of an 8″ cake · whole cakes offer better value.':'单片为8寸蛋糕的1/8 · 整蛋糕购买更优惠。'}</p></div>`}"
roll_func = "function rollPricing(p){const options=[['roll',locale==='en'?'Whole':'整条',p.rollPrices.whole],['rollslice',locale==='en'?'Slice':'小片',p.rollPrices.slice]];return `<div class=\"cake-pricing roll-pricing\" data-product=\"${p.id}\" data-selected-size=\"roll\"><div class=\"cake-size-tabs roll-price-tabs\" role=\"group\" aria-label=\"${locale==='en'?'Choose roll format':'选择卷类规格'}\">${options.map(([key,label,price],i)=>`<button type=\"button\" class=\"cake-size-btn${i===0?' active':''}\" data-size=\"${key}\" data-label=\"${label}\" data-price=\"${price}\" aria-pressed=\"${i===0}\">${label}</button>`).join('')}</div><div class=\"cake-price-display\"><span class=\"cake-price-size\">${locale==='en'?'Whole':'整条'}</span><strong class=\"cake-price-value\">${p.rollPrices.whole}</strong></div><p class=\"cake-price-note\">${locale==='en'?'Whole rolls offer better value.':'整条购买更优惠。'}</p></div>`}"
if needle not in s:
    raise RuntimeError('cakePricing insertion point not found')
s = s.replace(needle, needle + '\n' + roll_func, 1)

old_card = "function productCard(p){return `<article class=\"product-card\">${productVisual(p)}<div class=\"product-copy\"><h4>${locale==='en'?p.en:p.zh}</h4><p>${locale==='en'?p.descEn:p.descZh}</p><p class=\"selling\">${locale==='en'?p.sellEn:p.sellZh}</p>${p.sizePrices?cakePricing(p):`<p class=\"price\">${locale==='en'?p.priceEn:p.priceZh}</p>`}<button class=\"enquire order-trigger\" data-product=\"${p.id}\">${locale==='en'?'Enquire ↗':'预约咨询 ↗'}</button></div></article>`}"
new_card = "function productCard(p){return `<article class=\"product-card\">${productVisual(p)}<div class=\"product-copy\"><h4>${locale==='en'?p.en:p.zh}</h4><p>${locale==='en'?p.descEn:p.descZh}</p><p class=\"selling\">${locale==='en'?p.sellEn:p.sellZh}</p>${p.sizePrices?cakePricing(p):p.rollPrices?rollPricing(p):`<p class=\"price\">${locale==='en'?p.priceEn:p.priceZh}</p>`}<button class=\"enquire order-trigger\" data-product=\"${p.id}\">${locale==='en'?'Enquire ↗':'预约咨询 ↗'}</button></div></article>`}"
if old_card not in s:
    raise RuntimeError('productCard renderer not found')
s = s.replace(old_card, new_card, 1)

# 4) Keep product-menu and order form in sync with the selected roll format.
old_menu_price = "function productMenuPrice(p){return p.sizePrices?(locale==='en'?`6″ ${p.sizePrices['6']}`:`6寸 ${p.sizePrices['6']}`):(locale==='en'?p.priceEn:p.priceZh)}"
new_menu_price = "function productMenuPrice(p){return p.sizePrices?(locale==='en'?`6″ ${p.sizePrices['6']}`:`6寸 ${p.sizePrices['6']}`):p.rollPrices?(locale==='en'?`Whole ${p.rollPrices.whole}`:`整条 ${p.rollPrices.whole}`):(locale==='en'?p.priceEn:p.priceZh)}"
if old_menu_price not in s:
    raise RuntimeError('productMenuPrice function not found')
s = s.replace(old_menu_price, new_menu_price, 1)

old_labels = "function sizeOptionLabel(key){const en={single:'Single / portion',box:'Dessert box',tasting:'4-piece tasting box',roll:'Whole roll','4':'4-inch','6':'6-inch','8':'8-inch',slice:'Slice (1/8 of 8-inch cake)',other:'Other / discuss'};const zh={single:'单份',box:'甜品盒',tasting:'四件中式糕点拼盘',roll:'整条','4':'4寸','6':'6寸','8':'8寸',slice:'单片（8寸蛋糕的1/8）',other:'其他 / 沟通确认'};return (locale==='en'?en:zh)[key]||key}"
new_labels = "function sizeOptionLabel(key){const en={single:'Single / portion',box:'Dessert box',tasting:'4-piece tasting box',roll:'Whole roll',rollslice:'Slice','4':'4-inch','6':'6-inch','8':'8-inch',slice:'Slice (1/8 of 8-inch cake)',other:'Other / discuss'};const zh={single:'单份',box:'甜品盒',tasting:'四件中式糕点拼盘',roll:'整条',rollslice:'小片','4':'4寸','6':'6寸','8':'8寸',slice:'单片（8寸蛋糕的1/8）',other:'其他 / 沟通确认'};return (locale==='en'?en:zh)[key]||key}"
if old_labels not in s:
    raise RuntimeError('sizeOptionLabel function not found')
s = s.replace(old_labels, new_labels, 1)

old_sizes = "function setOrderSizeForProduct(p,preferred=''){const sel=$('#size');let keys;if(p?.sizePrices)keys=['4','6','8','slice','other'];else if(p?.orderFormat==='tasting')keys=['tasting','other'];else if(p?.orderFormat==='roll')keys=['roll','other'];else keys=['single','box','other'];sel.innerHTML=`<option value=\"\">${locale==='en'?'Please select':'请选择'}</option>`+keys.map(k=>`<option value=\"${k}\">${sizeOptionLabel(k)}</option>`).join('');const fallback=p?.sizePrices?'6':(p?.orderFormat||'');const chosen=keys.includes(preferred)?preferred:fallback;if(chosen)sel.value=chosen}"
new_sizes = "function setOrderSizeForProduct(p,preferred=''){const sel=$('#size');let keys;if(p?.sizePrices)keys=['4','6','8','slice','other'];else if(p?.rollPrices)keys=['roll','rollslice','other'];else if(p?.orderFormat==='tasting')keys=['tasting','other'];else keys=['single','box','other'];sel.innerHTML=`<option value=\"\">${locale==='en'?'Please select':'请选择'}</option>`+keys.map(k=>`<option value=\"${k}\">${sizeOptionLabel(k)}</option>`).join('');const fallback=p?.sizePrices?'6':p?.rollPrices?'roll':(p?.orderFormat||'');const chosen=keys.includes(preferred)?preferred:fallback;if(chosen)sel.value=chosen}"
if old_sizes not in s:
    raise RuntimeError('setOrderSizeForProduct function not found')
s = s.replace(old_sizes, new_sizes, 1)

old_resolve = "function resolveOrderPrice(p,sizeKey){if(!p)return '';if(p.sizePrices&&p.sizePrices[sizeKey])return p.sizePrices[sizeKey];return locale==='en'?p.priceEn:p.priceZh}"
new_resolve = "function resolveOrderPrice(p,sizeKey){if(!p)return '';if(p.sizePrices&&p.sizePrices[sizeKey])return p.sizePrices[sizeKey];if(p.rollPrices){if(sizeKey==='roll')return p.rollPrices.whole;if(sizeKey==='rollslice')return p.rollPrices.slice}return locale==='en'?p.priceEn:p.priceZh}"
if old_resolve not in s:
    raise RuntimeError('resolveOrderPrice function not found')
s = s.replace(old_resolve, new_resolve, 1)

old_change = "$('#close').onclick=()=>modal.close();$('#cancel').onclick=()=>modal.close();modal.onclick=e=>{if(e.target===modal)modal.close()};$('#product').onchange=()=>{const p=products.find(x=>x.id===$('#product').value);setOrderSizeForProduct(p,p?.sizePrices?'6':p?.orderFormat||'')};"
new_change = "$('#close').onclick=()=>modal.close();$('#cancel').onclick=()=>modal.close();modal.onclick=e=>{if(e.target===modal)modal.close()};$('#product').onchange=()=>{const p=products.find(x=>x.id===$('#product').value);setOrderSizeForProduct(p,p?.sizePrices?'6':p?.rollPrices?'roll':p?.orderFormat||'')};"
if old_change not in s:
    raise RuntimeError('product onchange handler not found')
s = s.replace(old_change, new_change, 1)

p.write_text(s, encoding='utf-8')
