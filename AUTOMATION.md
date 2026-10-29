# AUTOMATION.md: dnevni posao (zakazani zadatak u Claude-u)

Ovo je uputstvo koje Claude prati pri svakom dnevnom pokretanju. Cilj: **2 nova reela dnevno**, zakazana u Buffer-u za **12:30 i 19:30** (Europe/Belgrade), bez ičijeg ručnog rada. Na kraju ide kratak izveštaj za Gajica.

> **Važi ovaj fajl:** termini su 12:30 i 19:30 (Gajicova odluka 29.10.2026). Ako prompt zakazanog zadatka navodi 11:30, to je staro vreme i treba ga zanemariti.

Tajne (GH_TOKEN, BUFFER_TOKEN, SV_BASIC) su u promenljivim okruženja (Environment variables) zakazanog zadatka. Nikada se ne upisuju u repo, u fajlove koji se commit-uju niti u izveštaj.

## 0. Priprema
```bash
umask 077; mkdir -p ~/.secrets
# GH_TOKEN, BUFFER_TOKEN, SV_BASIC postavi kao env iz prompta
AUTH="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)"
git -c http.extraHeader="$AUTH" clone -q https://github.com/Gajic97/supervision-reels.git ~/sr && cd ~/sr
git config user.name Gajic97; git config user.email freelancenemanjagajic@gmail.com
```
Pročitaj **BRAND.md** (obavezna pravila), **HOOKS.md** (tekstualni hook), **brag/SKILL.md** (kako se pravi video) i šablone u `templates/`. Standard je **reel-v3**: reel-v2 stil, plus hook od 3 s, šire bočne margine i muzika koja se menja.

GitHub API (releases i ostalo) je blokiran kroz proxy. Radi samo `git` preko HTTPS-a sa gornjim headerom.

## 1. Katalog
```bash
if [ "$(date +%F)" \< "2026-11-01" ]; then
  # Prelaz: novi sajt još nije javno pušten, a stari sajt ima DRUGAČIJE cene i ID-jeve. Do 31.10. uvek novi sajt.
  SV_BASE=https://new.super-vision.rs SV_BASIC="$SV_BASIC" python3 scripts/fetch_products.py > /tmp/products.json
else
  SV_BASE=https://super-vision.rs python3 scripts/fetch_products.py > /tmp/products.json \
   || SV_BASE=https://new.super-vision.rs SV_BASIC="$SV_BASIC" python3 scripts/fetch_products.py > /tmp/products.json
fi
```
Linkovi u opisima uvek glase **super-vision.rs**. Od 1.11.2026. pre izbora proveri da cena u /tmp/products.json odgovara javnoj stranici proizvoda na super-vision.rs. Ako se razlikuje, za taj proizvod ne prikazuj cenu i to napiši u izveštaju.

## 2. Izbor 2 proizvoda
```bash
python3 scripts/pick_candidates.py /tmp/products.json > /tmp/candidates.json
```
Biraj **isključivo** iz `/tmp/candidates.json`. Skripta već primenjuje Gajicovo pravilo: samo ozbiljna oprema, nikada kablovi, konektori, nosači, napajanja, moduli ni sitan pribor. Ručno ne dodaješ ništa van te liste.

**Trenutno važi FAZA 1:** samo jeftinije **kamere** (3.000–15.000 RSD), **snimači** (5.000–20.000) i **kompleti video nadzora** (10.000–50.000), od jeftinijih ka skupljim. Lista je sortirana po prioritetu i ceni.

Pravila izbora:
- uzmi prva 2 odgovarajuća proizvoda sa liste, ali ne 2 ista tipa istog dana (npr. kamera i snimač, ili kamera i komplet)
- ne biraj dva skoro ista modela zaredom (npr. ista kamera sa objektivom 2.8 i 4 mm)
- proizvodi namenjeni krajnjem kupcu (Wi-Fi kamere, kompleti) imaju prednost kad su cene slične

Ako je na listi manje od 2 proizvoda (svi su objavljeni u poslednjih 30 dana), u `scripts/pick_candidates.py` privremeno povećaj gornje granice cena u PHASE1 za 50% i to napiši u izveštaju. Ne izlazi van ove tri kategorije bez Gajicove odluke.

## 3. Pravljenje reela (brag)
Za svaki proizvod u `~/work/<slug>/`:
1. **Proveri stranicu uživo:** cena, „Na stanju“, sadržaj paketa, šta NIJE u paketu. Ako nešto ne može da se potvrdi, ne ide u video.
2. **Slike:** koristi samo prave slike sa sajta. Kod kompleta pronađi svaki deo kao zaseban proizvod (pretraga po šifri modela u /tmp/products.json) i uzmi njegovu sliku; ne seci delove iz slike kompleta.
3. **brag-plan.md:**
   - glavna ključna reč, onako kako je ljudi kucaju
   - hook
   - 5–6 scena po strukturi iz BRAND.md
   - spisak činjenica sa izvorom
4. **Kompozicija:** polazi od `templates/reel-v3/index.html`, koji je trenutni standard. Ima `window.render(t)` i `window.ready`, format 1080×1920 i **24 s**:
   - **0–3 s: tekstualni hook (scena s0)** po `HOOKS.md`: oznaka iznad, glavni red od najviše 8 reči (svaka reč je `<span class="w">`, a ključne su `class="w green"`) i jedna rečenica ispod. Tip hook-a mora biti drugačiji od prethodnog reela u posted.json.
   - **3–24 s: glavni deo** (funkcija `renderMain`, vreme ide od 0), sa rezovima na 3,5 / 8,5 / 13 / 15,5 / 18,5 s glavnog dela.
   - **Bočne margine:** sav sadržaj scena je skaliran na 92%, tako da je razmak od ivice oko 117 px. Ne vraćaj `.scene` scale, ne stavljaj tekst bliže od x=80 unutar scene i ne pravi elemente šire od 920 px.
   - Scene i tekst prilagodi proizvodu: hook mora biti specifičan za taj proizvod, a ne kopija prethodnog. Ključna reč se mora pojaviti na ekranu.
5. **Muzika (svaki reel drugačija):** kopiraj `templates/reel-v3/sound.py`.
   - Izaberi `STYLE` iz skupa deep_house, lofi_chill, synthwave, cinematic, minimal_tech, tako da se **ne ponavlja nijedan od poslednja 2 reela** (`music_style` u posted.json).
   - `KEY` uzmi nasumično 0–11, a `SEED` = product_id.
   - Napravi `sfx.json` sa efektima u **apsolutnom vremenu**, usklađenim sa tvojim ulascima elemenata. Format je `[{"type":"shutter","t":2.0,"g":0.9}, ...]`, a tipovi su opisani na vrhu sound.py. Bez `SFX` se koristi raspored reel-v3.
   - Pokreni: `STYLE=.. KEY=.. SEED=.. INTRO=3.0 SFX=sfx.json OUT_WAV=music.wav python3 sound.py`
   - Bez tonskih blip i pluck zvukova.
6. **Provera kadrova:** pre rendera pregledaj stillove svake scene, hook-a i sredine prelaza (Playwright screenshot, pa Read), pa ispravi preklapanja, prelome, kontrast i tekst preblizu ivice.
7. **Render:** `node scripts/render.js ~/work/<slug> ~/work/<slug>/music.wav ~/work/<slug>/reel.mp4 24 2.6`. Poster (thumbnail) je tekstualni hook na 2,6 s.
8. **Opisi** (BRAND.md): Instagram, TikTok i LinkedIn. Instagram tekst ide u `ig.txt`.

Ako bilo koji korak ne uspe za neki proizvod, preskoči ga i uzmi sledeći sa liste. Nikad se ne objavljuje video sa neproverenim podacima.

## 4. Hosting videa (grana `media`, GitHub Pages)
```bash
git -c http.extraHeader="$AUTH" clone -q --branch media https://github.com/Gajic97/supervision-reels.git ~/media
cp ~/work/<slug>/reel.mp4 ~/media/v/$(date +%F)-<slug>.mp4
# obriši videe starije od 14 dana iz ~/media/v
cd ~/media && git checkout --orphan tmp && git add -A && git commit -qm "media $(date +%F)" \
 && git branch -D media && git branch -m media && git -c http.extraHeader="$AUTH" push -qf origin media
```
Javni link: `https://gajic97.github.io/supervision-reels/v/<fajl>.mp4`. Pre zakazivanja sačekaj da link vrati `200` i `content-type: video/mp4` (Pages se objavljuje 1–3 min; proveravaj na 20 s, najviše 10 min).

## 5. Zakazivanje (Buffer API)
```bash
BUFFER_TOKEN=... python3 scripts/schedule_buffer.py --service instagram --video <link> --text-file ig.txt --at "YYYY-MM-DD 12:30"
```
- Prvi reel ide u 12:30, drugi u 19:30, istog dana. Ako je termin prošao ili je bliže od 15 minuta, pomeri ga na isti termin sledećeg dana.
- Isto ponovi za `tiktok` i `linkedin` (sa njihovim opisima) samo ako je kanal povezan. Skripta javlja „Kanal nije povezan“, što nije greška: tada samo preskoči.
- Nikada ne briši niti menjaj postojeće objave u Buffer-u.

## 6. Evidencija
U `data/posted.json` (grana main) dodaj unos za svaki zakazani reel:
- date, product_id, product, category, keyword, hook_type, hook_text, music_style
- `buffer_posts`: {"instagram": id, "tiktok": id, "linkedin": id}, gde je id iz izlaza schedule_buffer.py
- channels, scheduled, video, buffer_post_id

Uz to sačuvaj `templates/runs/<datum>-<slug>/` sa fajlovima brag-plan.md, index.html, sound.py i opisima. MP4 i frejmove ne čuvaj. Zatim commit i push na main.

## 6b. Stranica sa rezultatima (svaki dan) i nedeljni zaključak (ponedeljkom)
Pre push-a grane `media` (korak 4), osveži stranicu sa rezultatima:
```bash
cd ~/sr && BUFFER_TOKEN="$BUFFER_TOKEN" python3 scripts/report.py ~/media/izvestaj --days 60
```
Javni link: **https://gajic97.github.io/supervision-reels/izvestaj/**. Folder `izvestaj/` se nikad ne briše pri čišćenju starih videa.

**Ponedeljkom** napiši i nedeljni zaključak, `data/weekly/<GGGG>-W<nedelja>.md` (grana main, pre generisanja stranice). Kratko, na srpskom:
- top 3 i najslabija 3 reela prošle nedelje (pregledi i interakcije po mreži)
- koji tip hook-a, koji muzički stil i koja kategorija najbolje prolaze (samo ako ima bar 3 reela po grupi, inače napiši da je uzorak mali)
- 1–3 konkretna predloga za sledeću nedelju (npr. češće neki tip hook-a, proširenje FAZE 1)

Predloge za promenu pravila (faze, kategorije, cene) samo predlaži; ne menjaj ih sam bez Gajicove odluke. Zaključak kopiraj i u dnevni izveštaj tog dana.

## 7. Izveštaj za Gajica (poslednja poruka zakazanog zadatka)
Kratko, na srpskom:
1. **Zakazano danas:** proizvod, vreme, kanal, link videa i ključna reč.
2. **Komentari:** Buffer API (29.10.2026) nema čitanje komentara. Napiši podsetnik da se novi komentari pogledaju u Buffer Community. Ako Gajic u promptu nalepi komentare, daj predloge odgovora na osnovu podataka sa sajta.
3. **5 naloga za praćenje:** pronađi ih web pretragom, pa za svaki daj link i jednu rečenicu zašto. Fokus:
   - lokalni majstori i partneri u Sremu i Srbiji (električari, izvođači, agencije za nekretnine)
   - ljudi koji traže video nadzor
   - lokalne firme

   Ne prati ih sam.
4. **Problemi:** šta nije uspelo i šta Gajic treba da uradi, ako išta.
