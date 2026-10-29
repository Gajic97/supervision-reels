# HOOKS.md: tekstualni hook pre proizvoda (Hormozi pristup)

Svaki reel počinje **tekstualnim hook-om od 3 s** (scena `s0` u `templates/reel-v4`), pa tek onda ide proizvod. Hook ne pominje model. Obraća se kupcu i njegovom problemu, a proizvod u nastavku je odgovor.

## Kako se piše (Alex Hormozi, $100M Leads i Value Equation)
- **Jedna poruka, najviše 7–8 reči** u glavnom redu. Uz to idu kratka oznaka iznad (2–4 reči, „kome se obraćamo“) i jedna rečenica ispod, koja vodi u proizvod.
- Hook pogađa bar jednu polugu **Value Equation**:
  - **željeni ishod:** vidiš dvorište sa telefona, znaš ko je na vratima
  - **verovatnoća:** proverena marka, ceo komplet, ušteda u kompletu
  - **vreme:** isporuka za 2 radna dana, sve stiže odjednom
  - **trud:** bez kablova, bez kopanja, radi preko Wi-Fi-ja, isti kabl
- Reči koje su ključne reči ili korist bojimo zeleno (2–3 reči).
- Tipovi hook-a se **smenjuju**: isti tip se ne ponavlja dva reela zaredom (`hook_type` u posted.json).

## Tipovi i šabloni (srpski, za video nadzor)
| Tip | Šablon | Primer |
|---|---|---|
| **label** (prozivka publike) | „Vlasnici {kuće/lokala/placa}: …“ | „Vlasnici lokala: ovo je dovoljno za početak.“ |
| **yes-pitanje** | „Imaš {situacija}?“ | „Imaš plac ili vikendicu bez struje?“ |
| **ako–onda** | „Ako {situacija}, {rešenje}.“ | „Ako menjaš stari interfon, ne menjaš kabl.“ |
| **komanda** | „Pre nego što kupiš {kategorija}, pogledaj ovo.“ | „Pre nego što kupiš kameru, proveri ovo.“ |
| **izjava / broj** | „{broj} {stvar} za {cena/korist}.“ | „4 kamere i snimač za manje od 30.000.“ |
| **lista** | „3 stvari koje {kategorija} mora da ima.“ | „3 stvari koje dobra spoljna kamera mora da ima.“ |
| **mini-priča** | „Hteo je kameru, a nije imao struju.“ | (samo ako je istinito i opšte, bez izmišljenih ljudi i citata) |
| **provokativno (bez straha)** | „Najskuplja kamera je ona koju ne vidiš noću.“ | (oprezno, bez zastrašivanja) |

## Zabranjeno
- Strah, „lopovi“, „provalnici“, „spasite porodicu“, kao i garancije bezbednosti („nikad vas neće pokrasti“).
- Izmišljene brojke, recenzije, ljudi, „najprodavanije“, lažni rokovi i lažna hitnost („samo danas“).
- Ponude koje ne postoje na sajtu (besplatna montaža, popust, poklon).

## Prava „ponuda“ (samo ono što stvarno postoji na sajtu)
- **isporuka za 2 radna dana**, roba sa lagera
- **2 godine zakonske saobraznosti** i tehnička podrška telefonom (radnim danima 8–16)
- **„Uštedite u kompletu X RSD (Y%)“**, samo kod kompleta gde sajt to prikazuje
- **„Sve licence MUP-a“**, projektovanje i ugradnja iz jedne firme
- **besplatan savet ili ponuda** („Zatražite ponudu ili savet“)

Ako Gajic uvede pravu dodatnu ponudu (npr. popust na montažu uz komplet), ona se dodaje ovde i tek tada sme u video.
