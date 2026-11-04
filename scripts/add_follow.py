#!/usr/bin/env python3
"""Dodaje nove naloge za praćenje u data/follow.json bez duplikata.
Upotreba: python3 scripts/add_follow.py /tmp/novi_nalozi.json
Ulazni fajl je JSON lista: [{"date","network","name","handle","url","city","reason"}, ...]"""
import json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(root, 'data', 'follow.json')
data = json.load(open(path, encoding='utf-8'))
new = json.load(open(sys.argv[1], encoding='utf-8'))
def key(x): return (x.get('network'), (x.get('handle') or x.get('url') or x.get('name') or '').lower().strip('@/'))
seen = {key(x) for x in data} | {(x.get('network'), (x.get('name') or '').lower()) for x in data}
added = 0
for x in new:
    if key(x) in seen or (x.get('network'), (x.get('name') or '').lower()) in seen: continue
    data.append(x); seen.add(key(x)); added += 1
json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'dodato {added}, preskočeno {len(new) - added}')
