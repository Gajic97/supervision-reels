# reel-v5-14s (standard od 10.11.2026)

**Glavni primer (odobren 10.11.2026):** EZVIZ CS-HB90 (id 3101), hook „izjava/broj“ („2 objektiva. 1 kamera.“): oznake na objektivima u hook-u, pa **ilustrovana scena primene** (dvorište: kuća, kapija, auto, osoba; vidno polje kamere, praćenje osobe, uvećan prikaz kao u aplikaciji), pečati, cena.
Drugi primer (jednostavniji, proizvod na pozadini): `primer-h4/` (EZVIZ CS-H4, hook „provokativno“).
- `index.html`: kompozicija 1080×1920, 14 s, `window.render(t)` / `window.ready`
- `fonts.css` + `assets/poppins-*.woff2`: Poppins 600–800 (npm @fontsource/poppins@5.0.8)
- `assets/hb90.png`, `assets/h4.png`: slike sa sajta bez belog fona (flood-fill od ivica, prag 238)
- `sound.py`: isti kao reel-v4 + režim `MUSIC_FILE=... DUR=14` (prava pesma iz `assets/music/`, SFX preko, ~6 dB tiše); bez MUSIC_FILE radi kao stari (sintetički)
- `sfx.json`: efekti na rezovima 2,6 / 5,4 / 8,4 / 10,9 i na ceni

Probni render:
```bash
MUSIC_FILE=../../assets/music/chill/zephiramusic-chill-lofi-585360.mp3 DUR=14 SFX=sfx.json OUT_WAV=music.wav python3 sound.py
node ../../scripts/render.js . music.wav reel.mp4 14 13.3
```
Raspored scena i pravila: AUTOMATION.md korak 4–5, HOOKS.md, FORMATS.md.

Krajnja kartica (10,9–14 s, `#end`) je ujedno **naslovna slika na Instagram gridu** (Buffer `thumbnailOffset` 13300 ms); sadržaj u srednjih 3:4 (y 240–1680).

VAŽNO (12.11.): HB90 slika u primeru je isečena ručno i pregledana. U automatici se slike sa belim fonom NE seku, nego proizvod ide na belu zaobljenu karticu (AUTOMATION.md korak 4, „Slika proizvoda“).
