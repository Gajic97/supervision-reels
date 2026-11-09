#!/usr/bin/env python3
"""Jednokratno spajanje: data/follow_sync.json (ručno praćenje kroz Chrome 8. i 9.11.2026) -> data/follow.json.
Prenosi polja followed/followed_as za iste naloge i dodaje naloge koji fale. Posle uspeha briše follow_sync.json
iz radne kopije (na main ostaje dok ga Gajic ne obriše; ponovno pokretanje ništa ne kvari).
Upotreba: python3 scripts/merge_follow_sync.py"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, 'data', 'follow_sync.json'); dst = os.path.join(root, 'data', 'follow.json')
if not os.path.exists(src): print('nema follow_sync.json'); raise SystemExit(0)
cur = json.load(open(dst, encoding='utf-8')); syn = json.load(open(src, encoding='utf-8'))
def k(x): return (x.get('network'), (x.get('handle') or x.get('url') or x.get('name') or '').lower().strip('@/'))
idx = {k(x): x for x in cur}; upd = add = 0
for x in syn:
    y = idx.get(k(x))
    if y is None:
        cur.append(x); idx[k(x)] = x; add += 1; continue
    if x.get('followed') and not y.get('followed'): y['followed'] = x['followed']; upd += 1
    if x.get('followed_as') and not y.get('followed_as'): y['followed_as'] = x['followed_as']
json.dump(cur, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'follow_sync: ažurirano {upd}, dodato {add}, ukupno {len(cur)}')
