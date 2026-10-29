# supervision-reels

Automatizacija kratkih video objava (Reels/TikTok/LinkedIn) za SuperVision d.o.o. (super-vision.rs).

## Kako radi
1. `scripts/fetch_products.py` preuzima katalog sa sajta (WooCommerce Store API).
2. Claude (zakazani zadatak) bira 2 proizvoda dnevno, koji su na stanju i nisu skoro objavljeni (`data/posted.json`).
3. Za svaki proizvod Claude pravi reel po skill-u **brag** (`brag/SKILL.md`, MIT, github.com/latent-spaces/brag) i pravilima iz `BRAND.md`:
   - HTML kompozicija sa funkcijom `window.render(t)`
   - zvuk u Pythonu
   - `scripts/render.js` za MP4
4. `scripts/publish_release.py` postavlja MP4 kao GitHub Release asset, pa dobijamo javni link.
5. Buffer zakazuje objavu u 11:30 i 19:30, sa posebnim opisom za svaku mrežu.
6. Dnevni izveštaj sadrži:
   - šta je objavljeno
   - predloge odgovora na komentare
   - 5 naloga za ručno praćenje

## Šablon
`templates/reel-v1/` sadrži prvi odobreni reel (komplet HiLook 4x THC-B120-P): kompoziciju, zvuk, plan i opise.

## Bezbednost
U repou nema šifri ni tokena. Oni se prosleđuju samo kroz promenljive okruženja (`GH_TOKEN`, `BUFFER_TOKEN`, `SV_BASIC`).
