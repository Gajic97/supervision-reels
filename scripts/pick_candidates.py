#!/usr/bin/env python3
"""Filtrira katalog na ozbiljnu sigurnosnu opremu koja sme u reel.

Upotreba: python3 scripts/pick_candidates.py /tmp/products.json > /tmp/candidates.json
Pravilo (Gajic, 29.10.2026): samo kamere, kompleti, snimači, hard diskovi, alarmi,
interfoni, rampe/motori za kapije i kontrola pristupa. NIKADA kablovi, konektori,
nosači, napajanja, moduli, rezervni delovi i sitan pribor.
"""
import json, re, sys
from datetime import date, timedelta

# kategorija -> minimalna cena u RSD
ALLOWED = {
    "Kamere": 3000,
    "Kompleti video nadzora": 10000,
    "Snimači": 5000,
    "Hard diskovi": 5000,
    "Centrale": 8000,          # alarmne centrale
    "Senzori": 9000,           # samo ozbiljniji alarmni senzori
    "Sirene": 5000,
    "Interfonski kompleti": 10000,
    "Audio video interfoni": 10000,
    "Rampe": 30000,
    "Motori za klizne kapije": 30000,
    "Motori za krilne kapije": 30000,
    "Terminali": 10000,        # kontrola pristupa
    "Pametna kuća": 5000,
}
BLOCK_WORDS = re.compile(
    r"kabl|konektor|nosa[cč]|adapter|napajanj|trafo|modul|slu[sš]alic|taster|privez|"
    r"vijak|vijc|rezervn|dodatn|regulator|kutij|dozn|baterij|akumulator|kartic|tag\b|"
    r"punja[cč]|antena|alat|kanalic|bu[zž]ir|pribor|zamensk|filter|"
    r"daljinsk|daljinac|prijemnik|fotoćelij|fotocelij|lampa|sijalic|magnetni kontakt|poplav", re.I)

# prioritet za izbor (manji broj = češće u reelovima)
PRIORITY = {"Kompleti video nadzora": 1, "Kamere": 1, "Snimači": 2, "Audio video interfoni": 1,
            "Interfonski kompleti": 1, "Centrale": 2, "Hard diskovi": 3, "Rampe": 2,
            "Motori za klizne kapije": 2, "Motori za krilne kapije": 2, "Terminali": 3,
            "Pametna kuća": 3, "Senzori": 3, "Sirene": 4}

# FAZA 1 (Gajic, 29.10.2026): prvo samo jeftinije kamere, snimači i kompleti, da vidimo kako ide.
# kategorija -> (min, max) cena u RSD. Za kasnije faze isprazni PHASE1 ili ga proširi.
PHASE1 = {
    "Kamere": (3000, 15000),
    "Snimači": (5000, 20000),
    "Kompleti video nadzora": (10000, 50000),
}

def main():
    products = json.load(open(sys.argv[1]))
    try:
        posted = json.load(open("data/posted.json"))
    except FileNotFoundError:
        posted = []
    cutoff = (date.today() - timedelta(days=30)).isoformat()
    recent = {p["product_id"] for p in posted if p.get("date", "") >= cutoff}
    out = []
    for p in products:
        try:
            price = int(p.get("price") or 0)
        except ValueError:
            continue
        cats = [c for c in p.get("categories", []) if c in ALLOWED and (not PHASE1 or c in PHASE1)]
        if not cats or not p.get("in_stock") or not p.get("images"):
            continue
        if "Ulogujte" in (p.get("price_html") or "") or price <= 0:
            continue
        if price < max(ALLOWED[c] for c in cats):
            continue
        if PHASE1 and not any(PHASE1[c][0] <= price <= PHASE1[c][1] for c in cats):
            continue
        if BLOCK_WORDS.search(p["name"]):
            continue
        if len(p.get("description") or "") < 600 or p["id"] in recent:
            continue
        cat = min(cats, key=lambda c: PRIORITY[c])
        out.append({**p, "reel_category": cat, "priority": PRIORITY[cat]})
    out.sort(key=lambda p: (p["priority"], int(p["price"])))  # jeftinije prvo
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    by = {}
    for p in out: by[p["reel_category"]] = by.get(p["reel_category"], 0) + 1
    print(f"{len(out)} kandidata: {by}", file=sys.stderr)

if __name__ == "__main__":
    main()
