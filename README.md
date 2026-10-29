# supervision-reels

Automatizacija kratkih video objava (Reels/TikTok/LinkedIn) za SuperVision d.o.o. (super-vision.rs).

## Kako radi
1. `scripts/fetch_products.py` preuzima katalog sa sajta (WooCommerce Store API).
2. Claude (zakazani zadatak) bira 2 proizvoda dnevno, koji su na stanju i nisu skoro objavljeni (`data/posted.json`).
3. Za svaki proizvod Claude pravi reel po skill-u **brag** (`brag/SKILL.md`, MIT, github.com/latent-spaces/brag) i pravilima iz `BRAND.md`:
   - HTML kompozicija sa funkcijom `window.render(t)`
   - zvuk u Pythonu
   - `scripts/render.js` za MP4
4. MP4 ide na granu `media`, koja se servira preko GitHub Pages (javni link gajic97.github.io/supervision-reels/v/...).
5. `scripts/schedule_buffer.py` zakazuje objavu preko Buffer API-ja u 12:30 i 19:30, sa posebnim opisom za svaku mrežu.

Detaljno dnevno uputstvo je u `AUTOMATION.md`.
6. Dnevni izveštaj sadrži:
   - šta je objavljeno
   - predloge odgovora na komentare
   - 5 naloga za ručno praćenje

## Šablon
`templates/reel-v1/` sadrži prvi odobreni reel (komplet HiLook 4x THC-B120-P): kompoziciju, zvuk, plan i opise.

## Bezbednost
U repou nema šifri ni tokena. Oni se prosleđuju samo kroz promenljive okruženja (`GH_TOKEN`, `BUFFER_TOKEN`, `SV_BASIC`).
