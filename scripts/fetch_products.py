#!/usr/bin/env python3
"""Preuzima katalog sa SuperVision prodavnice (WooCommerce Store API, javan, bez ključa).

Upotreba:
  python3 scripts/fetch_products.py > data/products.json
Okruženje:
  SV_BASE   osnovni URL sajta (podrazumevano https://super-vision.rs)
  SV_BASIC  "korisnik:šifra" samo za staging pod Basic Auth (ne čuva se u repou)
"""
import base64, html, json, os, re, sys, urllib.request

BASE = os.environ.get("SV_BASE", "https://super-vision.rs").rstrip("/")
AUTH = os.environ.get("SV_BASIC")

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "supervision-reels/1.0"})
    if AUTH:
        req.add_header("Authorization", "Basic " + base64.b64encode(AUTH.encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r), r.headers

def text(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(h or ""))).strip()

def main():
    out, page = [], 1
    while True:
        items, headers = get(f"{BASE}/wp-json/wc/store/v1/products?per_page=100&page={page}")
        for p in items:
            price = p.get("prices", {})
            out.append({
                "id": p["id"],
                "name": p["name"],
                "url": p["permalink"],
                "sku": p.get("sku"),
                "in_stock": p.get("is_in_stock"),
                "price": price.get("price"),
                "currency": price.get("currency_code"),
                "price_html": text(p.get("price_html")),
                "categories": [c["name"] for c in p.get("categories", [])],
                "images": [i["src"] for i in p.get("images", [])],
                "short": text(p.get("short_description")),
                "description": text(p.get("description")),
                "attributes": {a["name"]: [t["name"] for t in a.get("terms", [])] for a in p.get("attributes", [])},
            })
        total_pages = int(headers.get("X-WP-TotalPages", "1"))
        if page >= total_pages:
            break
        page += 1
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print(f"{len(out)} proizvoda", file=sys.stderr)

if __name__ == "__main__":
    main()
