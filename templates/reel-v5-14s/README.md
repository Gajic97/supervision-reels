# reel-v5-14s — šablon reela od 14 s

Primer: EZVIZ CS-H4 Wi-Fi dome 2K (8.190 RSD, cena sa sajta 9.11.2026), format f2, hook „provokativno“.

## Pravila
- 14 s, 1080×1920, bez posebne uvodne scene: na 0. s proizvod u pokretu + hook
  (glavni red ≤5–6 reči, drugi red ulazi posle ~1 s).
- Nova scena na 2–3 s (bljesak + trzaj scale +6%), ≤3–5 reči po kadru.
- Raspored (`CUTS` u index.html):
  - 0–2,6 hook
  - 2,6–5,4 korist 1
  - 5,4–8,4 korist 2
  - 8,4–10,9 tri „pečata“ po ~0,8 s
  - 10,9–14 cena + super-vision.rs · 062/618-736
- Formati iz FORMATS.md ostaju kao ugao, sabijeni u ovaj raspored. Hikvision bez cene.
  Podaci samo sa stranice proizvoda.
- Hook: yes-pitanje i provokativni su najbolji, komanda retko.
- Opis za IG/TikTok završava kratkim pitanjem za komentare.

## Muzika i render
Muzika iz prave pesme (biblioteka `assets/music/<grupa>/`, grupa `b2b` za B2B/usluge, inače `chill`):

    MUSIC_FILE=assets/music/chill/x.mp3 DUR=14 SFX=sfx.json OUT_WAV=music.wav python3 sound.py
    node scripts/render.js <dir> music.wav reel.mp4 14 1.5

Bez `MUSIC_FILE` sound.py radi stari sintetički režim (isti izlaz kao reel-v4).

## Sredstva
- `assets/h4.png` — slika sa sajta, beli fon uklonjen (flood-fill prag 238).
- `fonts.css` + `fonts/` — Poppins 600/700/800 (latin + latin-ext) iz npm @fontsource/poppins@5.0.8.
