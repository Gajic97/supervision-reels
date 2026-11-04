# FOLLOW.md: nalozi za praćenje (poseban zakazani zadatak)

Ovaj posao je **odvojen od pravljenja reelova** (Gajic, 4.11.2026): reelovi se prave i zakazuju u jutarnjem zadatku po AUTOMATION.md, a ovaj zadatak samo dopunjava listu naloga. Ako ovde nešto ne uspe, to ne utiče na objave.

Repo: klon kao u AUTOMATION.md (korak 0). Nikad ne pratiš naloge i ne šalješ poruke, samo praviš listu. Praćenje radi Gajic, ili Claude preko Gajicovog Chrome-a kad Gajic to zatraži u razgovoru.

Web pretragom nađi do **10 Instagram, 10 TikTok i 10 LinkedIn** naloga. Samo ljudi i firme koji se **bave video nadzorom i sigurnosnom opremom**:
- instalateri i serviseri video nadzora, alarma i interfona **isključivo iz Srbije** (prednost Srem, Novi Sad, Beograd)
- firme za tehničku zaštitu, električari koji ugrađuju kamere
- kreatori sadržaja o video nadzoru i pametnoj kući iz Srbije

**Samo Srbija:** lokacija mora biti potvrđena (bio, adresa, broj +381, grad u Srbiji). Nikako Banja Luka, Republika Srpska, BiH, Hrvatska, Crna Gora, Severna Makedonija ni druge zemlje. Ako lokacija nije sigurna, preskoči.

**Zabranjeno:** agencije za nekretnine, opšti izvođači bez veze sa nadzorom, oglasi i članci, prodavnice-konkurenti. Nikad ne izmišljaj URL: ako direktan link profila nisi video, stavi `"url": null` i upiši ime (Gajic traži po imenu). Ne ponavljaj naloge koji već postoje u `data/follow.json` (ista mreža i isto ime ili handle). Ako nema dovoljno sigurnih, daj manje.

Upiši ih alatom Write u `/tmp/novi_nalozi.json` (lista `{"date","network":"instagram|tiktok|linkedin","name","handle","url","city","reason"}`) i pokreni `python3 scripts/add_follow.py /tmp/novi_nalozi.json`. Zatim objavi stranicu: `cd ~/sr && GH_TOKEN="$GH_TOKEN" bash scripts/publish_media.sh` (bez videa, samo osvežava stranice), pa commit i push `data/follow.json` na main (pre push-a `git pull --rebase`).
Stranica: **https://gajic97.github.io/supervision-reels/nalozi/**. Folder `nalozi/` se nikad ne briše. U izveštaju daj link stranice i broj novih naloga po mreži.

Ne prati ih sam.

Izveštaj: broj novih naloga po mreži i link stranice.
