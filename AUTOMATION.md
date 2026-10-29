# AUTOMATION.md: dnevni posao (zakazani zadatak u Claude-u)

Ovo je uputstvo koje Claude prati pri svakom dnevnom pokretanju. Cilj: **2 nova reela dnevno**, zakazana u Buffer-u za **12:30 i 19:30** (Europe/Belgrade), bez ičijeg ručnog rada. Na kraju ide kratak izveštaj za Gajica.

Tajne (GH_TOKEN, BUFFER_TOKEN, SV_BASIC) stižu u promptu zakazanog zadatka. Nikada se ne upisuju u repo, u fajlove koji se commit-uju niti u izveštaj.

## 0. Priprema
```bash
umask 077; mkdir -p ~/.secrets
# GH_TOKEN, BUFFER_TOKEN, SV_BASIC postavi kao env iz prompta
AUTH="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)"
git -c http.extraHeader="$AUTH" clone -q https://github.com/Gajic97/supervision-reels.git ~/sr && cd ~/sr
git config user.name Gajic97; git config user.email freelancenemanjagajic@gmail.com
```
Pročitaj **BRAND.md** (obavezna pravila), **brag/SKILL.md** (kako se pravi video) i oba šablona u `templates/`. Gajicu se najviše dopao **reel-v2**, pa je on glavni uzor za stil, tempo i kvalitet.

GitHub API (releases i ostalo) je blokiran kroz proxy. Radi samo `git` preko HTTPS-a sa gornjim headerom.

## 1. Katalog
```bash
SV_BASE=https://super-vision.rs python3 scripts/fetch_products.py > /tmp/products.json \
 || SV_BASE=https://new.super-vision.rs SV_BASIC="$SV_BASIC" python3 scripts/fetch_products.py > /tmp/products.json
```
Novi sajt ide uživo 30.10.2026. Ako super-vision.rs vraća stari sajt (nema `/wp-json/wc/store`) ili je blokiran, koristi new.super-vision.rs. Linkovi u opisima uvek glase **super-vision.rs**.

## 2. Izbor 2 proizvoda
Uslovi (svi moraju biti ispunjeni):
- `in_stock` je true
- cena je javna (`price_html` ne sadrži „Ulogujte“)
- ima bar jednu sliku
- opis je duži od oko 600 znakova (dovoljno činjenica za video)
- nije u `data/posted.json` u poslednjih 30 dana

Prioritet kategorija:
1. Kompleti video nadzora i Kamere
2. Interfoni i Video interfoni
3. Alarm i Senzori
4. Rampe i motori za kapije
5. Kontrola pristupa
6. Ostalo (osim kablova, vijaka i sitnog pribora)

Raznovrsnost: dva reela istog dana nisu iz iste kategorije, a ne ponavlja se kategorija iz prethodna 2 dana ako postoji alternativa. Proizvodi namenjeni krajnjem kupcu (Wi-Fi kamere, kompleti, interfoni) imaju prednost nad profesionalnom opremom.

## 3. Pravljenje reela (brag)
Za svaki proizvod u `~/work/<slug>/`:
1. **Proveri stranicu uživo:** cena, „Na stanju“, sadržaj paketa, šta NIJE u paketu. Ako nešto ne može da se potvrdi, ne ide u video.
2. **Slike:** koristi samo prave slike sa sajta. Kod kompleta pronađi svaki deo kao zaseban proizvod (pretraga po šifri modela u /tmp/products.json) i uzmi njegovu sliku; ne seci delove iz slike kompleta.
3. **brag-plan.md:**
   - glavna ključna reč, onako kako je ljudi kucaju
   - hook
   - 5–6 scena po strukturi iz BRAND.md
   - spisak činjenica sa izvorom
4. **Kompozicija:** `index.html` sa `window.render(t)` i `window.ready`, 1080×1920, 21 s, rezovi na 3,5 / 8,5 / 13 / 15,5 / 18,5 s, kao u šablonima. Scene i tekst prilagodi proizvodu: hook mora biti specifičan za taj proizvod, a ne kopija prethodnog. Ključna reč se mora pojaviti na ekranu.
5. **Zvuk:** kopiraj `templates/reel-v2/sound.py` i pomeri tempiranje efekata (swish, shutter, impact) tako da prati ulaske elemenata u tvojoj kompoziciji. `OUT_WAV=music.wav python3 sound.py`. Bez tonskih blipova.
6. **Provera kadrova:** pre rendera pregledaj stillove svake scene i sredine prelaza (Playwright screenshot, pa Read), pa ispravi preklapanja, prelome i kontrast.
7. **Render:** `node scripts/render.js ~/work/<slug> ~/work/<slug>/music.wav ~/work/<slug>/reel.mp4 21 <poster_t>`. Za `poster_t` uzmi najjači smiren kadar, obično kraj hook-a (oko 2,9 s).
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
- date, product_id, product, category, keyword
- channels, scheduled, video, buffer_post_id

Uz to sačuvaj `templates/runs/<datum>-<slug>/` sa fajlovima brag-plan.md, index.html, sound.py i opisima. MP4 i frejmove ne čuvaj. Zatim commit i push na main.

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
