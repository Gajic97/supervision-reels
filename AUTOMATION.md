# AUTOMATION.md: dnevni posao (zakazani zadatak u Claude-u)

> **Zaštita od dupliranja:** pre svega proveri `data/posted.json`. Ako za današnji datum (Europe/Belgrade) već postoje 2 unosa, ne pravi i ne zakazuj ništa, samo pošalji izveštaj. Ako postoji 1 unos, napravi samo onaj termin koji fali.

Ovo je uputstvo koje Claude prati pri svakom dnevnom pokretanju. Cilj: **2 nova reela dnevno**, zakazana u Buffer-u za **12:30 i 19:30** (Europe/Belgrade), bez ičijeg ručnog rada. Na kraju ide kratak izveštaj za Gajica.

> **NOVO od 10.11.2026 (Gajic): reel traje 14 s, struktura `templates/reel-v5-14s`, prava muzika iz `assets/music/` (samo grupe `chill` i `b2b`).** Gde se pravila ispod razlikuju (24 s, hook od 3 s, sintetička muzika, reel-v4), važi ovo novo. Razlog: ljudi odlaze u prve 2–3 s (prosečno gledanje 2–7 s), a sintetička muzika „zvuči katastrofa“.
>
> **Formati (Gajic, 30.10.2026):** od 31.10. svaki reel je jedan od formata iz **FORMATS.md** (2, 3, 4, 5, 6, 8; 7 retko; 1 nikad). Nivo animacije ostaje kao u reel-v4.
>
> **Odobreni uzor (Gajic, 29.10.2026):** demo `templates/reel-v4` (EZVIZ CS-TY1) je tačno ono što Gajic želi: tekstualni hook od 3 s, šire margine, animacije u svakom trenutku, prelazi koji se smenjuju, odometar cene i drugačija muzika. Svaki novi reel mora biti bar ovog nivoa animacije i kvaliteta, uz scene prilagođene proizvodu (ne kopija istih scena). Sam demo se ne objavljuje.

> **Važi ovaj fajl:** termini su 12:30 i 19:30 (Gajicova odluka 29.10.2026). Ako prompt zakazanog zadatka navodi 11:30, to je staro vreme i treba ga zanemariti.

Tajne (GH_TOKEN, BUFFER_TOKEN, SV_BASIC) su u promenljivim okruženja (Environment variables) zakazanog zadatka. Nikada se ne upisuju u repo, u fajlove koji se commit-uju niti u izveštaj.

## 0. Priprema
```bash
umask 077; mkdir -p ~/.secrets
# GH_TOKEN, BUFFER_TOKEN, SV_BASIC postavi kao env iz prompta
AUTH="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)"
git -c http.extraHeader="$AUTH" clone -q https://github.com/Gajic97/supervision-reels.git ~/sr && cd ~/sr
git config user.name Gajic97; git config user.email freelancenemanjagajic@gmail.com
GH_TOKEN="$GH_TOKEN" bash scripts/state_pull.sh
```
**Evidencija (od 6.11.2026) živi na grani `media`, u folderu `state/`** (posted.json, follow.json, postponed.json, weekly/). `state_pull.sh` je kopira u `~/sr/data/`, a `publish_media.sh` je vraća na granu media. Na **main se ne push-uje ništa** iz ovog zadatka (main je samo za pravila i kod koje menja Gajic sa Claude-om); push na main iz zakazanog zadatka nije prolazio.
Pročitaj **BRAND.md** (obavezna pravila), **FORMATS.md** (koji format reela danas, obavezno), **HOOKS.md** (tekstualni hook), **brag/SKILL.md** (kako se pravi video) i šablone u `templates/`. Standard je **reel-v5-14s** (od 10.11.2026): 14 s, hook i proizvod u pokretu od prvog kadra, nova scena na 2–3 s, prava muzika. reel-v4 ostaje kao uzor za nivo animacije.

GitHub API (releases i ostalo) je blokiran kroz proxy. Radi samo `git` preko HTTPS-a sa gornjim headerom.

## 1. Katalog
```bash
SV_BASE=https://super-vision.rs python3 scripts/fetch_products.py > /tmp/products.json
```
Novi sajt je javno pušten 30.10.2026 na super-vision.rs (staging new.super-vision.rs više ne radi). ID-jevi i cene su isti kao na stagingu.
Linkovi u opisima uvek glase **super-vision.rs**. Od 1.11.2026. pre izbora proveri da cena u /tmp/products.json odgovara javnoj stranici proizvoda na super-vision.rs. Ako se razlikuje, za taj proizvod ne prikazuj cenu i to napiši u izveštaju.

## 2. Izbor 2 proizvoda
```bash
python3 scripts/pick_candidates.py /tmp/products.json > /tmp/candidates.json
```
**Pre izbora proizvoda proveri FORMATS.md → „Usluge i B2B portal“:** neki dani umesto jednog proizvoda imaju reel o usluzi ili B2B portalu.

Biraj **isključivo** iz `/tmp/candidates.json`. Skripta već primenjuje Gajicovo pravilo: samo ozbiljna oprema, nikada kablovi, konektori, nosači, napajanja, moduli ni sitan pribor. Ručno ne dodaješ ništa van te liste.

**Trenutno važi FAZA 1:** samo jeftinije **kamere** (3.000–15.000 RSD), **snimači** (5.000–20.000) i **kompleti video nadzora** (10.000–50.000), od jeftinijih ka skupljim. Lista je sortirana po prioritetu i ceni.

Pravila izbora:
- uzmi prva 2 odgovarajuća proizvoda sa liste, ali ne 2 ista tipa istog dana (npr. kamera i snimač, ili kamera i komplet)
- ne biraj dva skoro ista modela zaredom (npr. ista kamera sa objektivom 2.8 i 4 mm)
- proizvodi namenjeni krajnjem kupcu (Wi-Fi kamere, kompleti) imaju prednost kad su cene slične

Odloženi proizvodi su u `data/postponed.json`. Oni ponovo mogu da se biraju, ali se za njih pravi **novi** reel po FORMATS.md (stari video je u starom formatu). Kad se objavi, ukloni ga iz postponed.json.

Ako je na listi manje od 2 proizvoda (svi su objavljeni u poslednjih 30 dana), u `scripts/pick_candidates.py` privremeno povećaj gornje granice cena u PHASE1 za 50% i to napiši u izveštaju. Ne izlazi van ove tri kategorije bez Gajicove odluke.

## 3. Pravljenje reela (brag)
Za svaki proizvod u `~/work/<slug>/`:
0. **Hikvision = bez cene** (BRAND.md → „Hikvision: bez cene“). Važi za video i sve opise.
1. **Proveri stranicu uživo:** cena, „Na stanju“, sadržaj paketa, šta NIJE u paketu. Ako nešto ne može da se potvrdi, ne ide u video.
2. **Slike:** koristi samo prave slike sa sajta. Kod kompleta pronađi svaki deo kao zaseban proizvod (pretraga po šifri modela u /tmp/products.json) i uzmi njegovu sliku; ne seci delove iz slike kompleta.
3. **brag-plan.md:**
   - glavna ključna reč, onako kako je ljudi kucaju
   - hook
   - 5–6 scena po strukturi iz BRAND.md
   - spisak činjenica sa izvorom
4. **Format i kompozicija (od 10.11.2026):** izaberi **format po FORMATS.md** (jutro i veče različiti, ne ponavljaj format iz poslednja 2 reela, format 1 se ne koristi) kao **ugao priče**, pa ga složi u strukturu od **14 s**. Polazi od `templates/reel-v5-14s/index.html` (**EZVIZ CS-HB90, stil koji je Gajic odobrio 10.11.**: u scenama koristi **SVG ilustraciju primene** prilagođenu proizvodu (dvorište, ulaz, stan, lokal, plac, vozilo…) i pokaži šta kamera radi u njoj: vidno polje, praćenje, noćni snop, uvećan prikaz kao u aplikaciji; nikad samo proizvod koji lebdi na pozadini kroz ceo reel. Jednostavniji primer je `primer-h4/`; `window.render(t)`, `window.ready`, 1080×1920, `fonts.css` sa Poppins woff2 u `assets/`). Scene, tekstovi i grafika se prilagođavaju proizvodu; ne kopiraj iste scene.
   - **0–2,6 s: hook + proizvod u pokretu od 0. kadra.** Nema posebne uvodne scene ni fade-a iz crnog. Glavni red **najviše 5–6 reči** (ključne reči `<em>`), drugi kraći red ulazi posle ~1 s. Tip hook-a po HOOKS.md, drugačiji od prethodnog reela.
   - **2,6–5,4 s i 5,4–8,4 s: dve koristi**, svaka sa svojom pozadinom/ilustracijom i „čipom“ sa činjenicom (najviše 3–5 reči po kadru).
   - **8,4–10,9 s: tri brze „pečat“ poruke** (~0,8 s svaka, krupno).
   - **10,9–14 s: krajnja kartica = naslovna slika na Instagram gridu** (Gajic, 11.11.2026; uzor u `templates/reel-v5-14s/index.html`, `#end`): svetla pozadina, velika slika proizvoda, iznad kategorija (npr. „WI-FI KAMERA · 2 OBJEKTIVA“), ispod model (npr. „EZVIZ CS-HB90“), jedna korist, cena u tamnom „čipu“ i `super-vision.rs · 062/618-736`. **Sav sadržaj u srednjih 3:4 kadra (y 240–1680)**, jer grid seče gore i dole. Model mora stati u **jedan red** (`white-space:nowrap`, font 80 px; ako je duži, smanji font dok ne stane u 1000 px). Kartica mora biti potpuno postavljena do 13,0 s. **Hikvision bez cene:** u čipu „Cena na upit“, a ispod „Zatraži ponudu · 062/618-736“. B2B reel: umesto proizvoda prikaz portala (telefon/laptop sa ponudom) i natpis „B2B portal“, čip „b2b.super-vision.rs“.
   - Na svakom rezu (2,6 / 5,4 / 8,4 / 10,9) kratak bljesak i „trzaj“ proizvoda (scale +6% pa nazad).
   - Format kao ugao: f2 problem → hook-problem pa 2 rešenja; f4 poređenje → koristi = A pa B; f5 za koga → 2 tipa kupca; f8 greška → hook-greška pa 2 scene ispravke; f3/f6 (samo kompleti) → delovi kompleta u pečatima.
   - Bočne margine: tekst ne bliže od 70 px ivici; ključna reč se mora pojaviti na ekranu.
   - **Slika proizvoda (Gajic 12.11.2026, posle obrisanog reela sa „iscepanim“ kamerama):**
     - Uzmi **originalnu sliku u punoj veličini** sa sajta (najveća iz `srcset`, obično 500–800 px), nikad umanjenu/thumbnail verziju.
     - **Ne seci beli fon** (flood-fill/prag) kod slika sa belom pozadinom: beli delovi proizvoda (kućište, nosač, nožice panela) nestaju i ivice izgledaju iscepano. Proizvod ide **na belu zaobljenu karticu** (`background:#fff; border-radius:48px; padding ~30 px; blaga senka`), slika `object-fit:contain` unutar nje. Seći se sme samo ako slika na sajtu već ima pravu providnost (PNG sa alfa kanalom).
     - **Ne uvećavaj** sliku više od ~1,1× njene prave širine (500 px slika → najviše ~550 px na ekranu); ako treba veće, uvećaj karticu, ne sliku.
     - U proveri kadrova (korak 6) obavezno pogledaj **uvećan isečak proizvoda u punoj rezoluciji** (hook i krajnja kartica): bez rupa, bez belih „otisaka“ oko ivica, bez mutnoće. Ako ne valja, ispravi pre rendera.
5. **Muzika (od 10.11.2026: prava pesma, ne sintetička):** kopiraj `templates/reel-v5-14s/sound.py` i napravi `sfx.json` u apsolutnom vremenu (primer u istom folderu; efekti na rezovima, tap/confirm na ceni).
   - **Grupa:** `b2b` ako je reel o B2B portalu ili usluzi, inače `chill`. Druge grupe se ne koriste (Gajic, 9.11.).
   - **Pesma:** iz `assets/music/<grupa>/` uzmi onu koja **nije korišćena u poslednjih 7 dana** (`music_track` u posted.json); ako su sve korišćene, onu najdavnije korišćenu.
   - Pokreni: `MUSIC_FILE=~/sr/assets/music/<grupa>/<pesma>.mp3 DUR=14 SFX=sfx.json OUT_WAV=music.wav python3 sound.py`
   - Licence su u `assets/music/LICENSES.md`; nove pesme dodaje samo Gajic (ručno sa Pixabay-a), obrada: `python3 scripts/prep_music.py <folder>`.
   - **Font:** koristi `fonts.css` i woff2 iz `templates/reel-v5-14s/assets/` (Poppins 600–800, latin + latin-ext).
6. **Provera kadrova:** pre rendera pregledaj stillove svake scene, hook-a i sredine prelaza (Playwright screenshot, pa Read), pa ispravi preklapanja, prelome, kontrast i tekst preblizu ivice.
7. **Render:** `node scripts/render.js ~/work/<slug> ~/work/<slug>/music.wav ~/work/<slug>/reel.mp4 14 13.3`. Naslovna slika je krajnja kartica: Buffer je uzima iz videa na 13,3 s (`schedule_buffer.py` po defaultu šalje `thumbnailOffset` 13300 ms). Ne ubacuj poster kao prvi kadar.
8. **Opisi** (BRAND.md): Instagram, TikTok i LinkedIn. Instagram tekst ide u `ig.txt`. Na kraj IG i TikTok opisa dodaj **kratko pitanje** za komentare (npr. „Kuća ili firma? Napiši u komentar.“), bez obećanja i nagrada.

Ako bilo koji korak ne uspe za neki proizvod, preskoči ga i uzmi sledeći sa liste. Nikad se ne objavljuje video sa neproverenim podacima.

## 4. Hosting videa (grana `media`, GitHub Pages)
Preimenuj render u konačno ime (`~/work/<slug>/<GGGG-MM-DD>-<slug>.mp4`, isto i .jpg), pa jednom pokreni:
```bash
cd ~/sr && GH_TOKEN="$GH_TOKEN" BUFFER_TOKEN="$BUFFER_TOKEN" bash scripts/publish_media.sh ~/work/<slug1>/<ime1>.mp4 ~/work/<slug2>/<ime2>.mp4
```
Skripta kopira videe, uklanja one starije od 14 dana, pravi stranice `nalozi/` i `izvestaj/` i radi običan `git push` (grana media se više ne prepisuje force push-om).

Napomena za pisanje komandi: podatke kao što su JSON liste (novi nalozi, unos za posted.json) upiši alatom **Write** u fajl, pa ih obradi skriptom (npr. `python3 scripts/add_follow.py /tmp/novi_nalozi.json`), umesto da ih ubacuješ u dugačku inline komandu.
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
- date, product_id, product, category, keyword, **format** (f2–f8), hook_type, hook_text, music_style (= grupa `chill`/`b2b`), **music_track** (npr. `chill/zephiramusic-chill-lofi-585360.mp3`), (kod formata 4 i product_id_b)
- `buffer_posts`: {"instagram": id, "tiktok": id, "linkedin": id}, gde je id iz izlaza schedule_buffer.py
- channels, scheduled, video, buffer_post_id

Uz to sačuvaj `templates/runs/<datum>-<slug>/` sa fajlovima brag-plan.md, index.html, sound.py i opisima. MP4 i frejmove ne čuvaj. Unose napiši alatom Write u `/tmp/posted_unosi.json` (lista), pa:
```bash
cd ~/sr && python3 scripts/add_posted.py /tmp/posted_unosi.json
GH_TOKEN="$GH_TOKEN" BUFFER_TOKEN="$BUFFER_TOKEN" bash scripts/publish_media.sh
```
Drugi poziv `publish_media.sh` (bez videa) šalje evidenciju i planove (`runs/`) na granu media i osvežava izveštaj. Ne radi commit ni push na main.

## 6b. Stranica sa rezultatima (svaki dan) i nedeljni zaključak (ponedeljkom)
Pre push-a grane `media` (korak 4), osveži stranicu sa rezultatima:
```bash
cd ~/sr && BUFFER_TOKEN="$BUFFER_TOKEN" python3 scripts/report.py ~/media/izvestaj --days 60
```
Javni link: **https://gajic97.github.io/supervision-reels/izvestaj/**. Folderi `izvestaj/` i `nalozi/` se nikad ne brišu pri čišćenju starih videa.

**Ponedeljkom** napiši i nedeljni zaključak, `data/weekly/<GGGG>-W<nedelja>.md` (grana main, pre generisanja stranice). Kratko, na srpskom:
- top 3 i najslabija 3 reela prošle nedelje (pregledi i interakcije po mreži)
- koji tip hook-a, koji muzički stil i koja kategorija najbolje prolaze (samo ako ima bar 3 reela po grupi, inače napiši da je uzorak mali)
- 1–3 konkretna predloga za sledeću nedelju (npr. češće neki tip hook-a, proširenje FAZE 1)

Predloge za promenu pravila (faze, kategorije, cene) samo predlaži; ne menjaj ih sam bez Gajicove odluke. Zaključak kopiraj i u dnevni izveštaj tog dana.

## 7. Izveštaj za Gajica (poslednja poruka zakazanog zadatka)
Kratko, na srpskom:
1. **Zakazano danas:** proizvod, vreme, kanal, link videa i ključna reč.
2. **Komentari:** Buffer API (29.10.2026) nema čitanje komentara. Napiši podsetnik da se novi komentari pogledaju u Buffer Community. Ako Gajic u promptu nalepi komentare, daj predloge odgovora na osnovu podataka sa sajta.
3. **Nalozi za praćenje:** u ovom zadatku se **ne traže** (od 4.11.2026 to radi poseban zakazani zadatak po `FOLLOW.md`, da pravljenje reelova ne zavisi od toga). Samo dodaj link stranice https://gajic97.github.io/supervision-reels/nalozi/ u izveštaj.
4. **Problemi:** šta nije uspelo i šta Gajic treba da uradi, ako išta.
