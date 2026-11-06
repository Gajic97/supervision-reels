#!/usr/bin/env python3
"""Dodaje unose u data/posted.json iz JSON fajla (lista unosa), bez duplikata (isti date + scheduled + product).
Upotreba: python3 scripts/add_posted.py /tmp/posted_unosi.json"""
import json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(root, 'data', 'posted.json')
data = json.load(open(path, encoding='utf-8'))
new = json.load(open(sys.argv[1], encoding='utf-8'))
if isinstance(new, dict): new = [new]
seen = {(x.get('date'), x.get('scheduled'), x.get('product')) for x in data}
n = 0
for x in new:
    k = (x.get('date'), x.get('scheduled'), x.get('product'))
    if k in seen: continue
    data.append(x); seen.add(k); n += 1
json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'dodato {n} u posted.json (ukupno {len(data)})')
