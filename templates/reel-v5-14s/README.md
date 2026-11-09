# reel-v5-14s (standard od 10.11.2026)

Primer: EZVIZ CS-H4 Wi-Fi dome 2K (id 4878), format f2, hook „provokativno“.
- `index.html`: kompozicija 1080×1920, 14 s, `window.render(t)` / `window.ready`
- `fonts.css` + `assets/poppins-*.woff2`: Poppins 600–800 (npm @fontsource/poppins@5.0.8)
- `assets/h4.png`: slika sa sajta bez belog fona (flood-fill od ivica, prag 238)
- `sound.py`: isti kao reel-v4 + režim `MUSIC_FILE=... DUR=14` (prava pesma iz `assets/music/`, SFX preko, ~6 dB tiše); bez MUSIC_FILE radi kao stari (sintetički)
- `sfx.json`: efekti na rezovima 2,6 / 5,4 / 8,4 / 10,9 i na ceni

Probni render:
```bash
MUSIC_FILE=../../assets/music/chill/zephiramusic-chill-lofi-585360.mp3 DUR=14 SFX=sfx.json OUT_WAV=music.wav python3 sound.py
node ../../scripts/render.js . music.wav reel.mp4 14 1.5
```
Raspored scena i pravila: AUTOMATION.md korak 4–5, HOOKS.md, FORMATS.md.
