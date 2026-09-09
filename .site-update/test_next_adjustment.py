from pathlib import Path
import re

s = Path('index.html').read_text(encoding='utf-8')
failures = []

img = Path('assets/products/chinese-tasting-box.webp')
if not img.exists():
    failures.append('tasting-box image file missing')
else:
    data = img.read_bytes()
    if len(data) < 25000 or data[:4] != b'RIFF' or data[8:12] != b'WEBP':
        failures.append('tasting-box image is not a valid staged WebP')

line = next((x for x in s.splitlines() if x.startswith("{id:'chinese-tasting-box'")), '')
if "image:'assets/products/chinese-tasting-box.webp'" not in line:
    failures.append('tasting-box product does not use approved single image')
if 'collage:' in line:
    failures.append('old tasting-box collage remains')

roll = next((x for x in s.splitlines() if x.startswith("{id:'coconut-angel-roll'")), '')
for needle, label in [
    ("priceEn:'Whole roll £18 · Slice £5'", 'roll English price text'),
    ("priceZh:'整条 £18 · 小片 £5'", 'roll Chinese price text'),
    ("rollPrices:{whole:'£18',slice:'£5'}", 'roll price data'),
]:
    if needle not in roll:
        failures.append(label)

required = {
    'roll selector renderer': 'function rollPricing(p)',
    'roll selector in product card': 'p.rollPrices?rollPricing(p)',
    'roll menu price': "p.rollPrices?(locale==='en'?`Whole ${p.rollPrices.whole}`",
    'roll slice label': "rollslice:'Slice'",
    'Chinese roll slice label': "rollslice:'小片'",
    'roll order choices': "else if(p?.rollPrices)keys=['roll','rollslice','other']",
    'roll whole price resolver': "if(sizeKey==='roll')return p.rollPrices.whole",
    'roll slice price resolver': "if(sizeKey==='rollslice')return p.rollPrices.slice",
    'roll default selection': "p?.rollPrices?'roll'",
    'whole-value note': "Whole rolls offer better value.",
}
for label, needle in required.items():
    if needle not in s:
        failures.append(label)

if failures:
    print('NEXT-ADJUSTMENT TEST FAIL')
    for f in failures:
        print('-', f)
    raise SystemExit(1)

print('NEXT-ADJUSTMENT TEST PASS')
