# FORMATS.md: formati reelova (Gajicova odluka, 30.10.2026)

Svi demo snimci su na https://gajic97.github.io/supervision-reels/demo/formati/. Kod je u `templates/formati-demo/`: `base.html` je zajednička osnova (stil, cena, outro, prelazi), a `gen.py` sadrži scene svakog formata.

Stil se ne menja: boje, Poppins, logo, margine 92%, hook od 3 s, scena sa cenom i dugmetom „Dodaj u korpu“, outro i 24 s trajanja. Menja se **scenario**.

## Koji formati se koriste

| # | Format | Status | Za šta |
|---|---|---|---|
| 1 | Prikaz proizvoda (hook → specifikacije → cena) | **IZBAČEN**, ne koristi se | — |
| 2 | Problem → rešenje | **koristi** | sve kategorije |
| 3 | 3 stvari (odbrojavanje 3, 2, 1) | **koristi, samo kompleti** | kompleti |
| 4 | Poređenje A ili B | **koristi, jedan od najboljih** | kamere, snimači, kompleti |
| 5 | Za koga je (3 kupca) | **koristi** | sve kategorije |
| 6 | Šta dobiješ u kompletu | **koristi** | samo kompleti |
| 7 | POV telefon | **retko**, samo kad nema bolje ideje (najviše 1 nedeljno) | proizvodi sa aplikacijom |
| 8 | Greška pre kupovine | **koristi** | sve kategorije |

## Rotacija
- Jutarnji i večernji reel istog dana moraju biti **različitog formata**.
- Format se ne ponavlja ako je korišćen u **poslednja 2 reela** (`format` u posted.json).
- Format 4 ima malu prednost: kad postoje 2 dobra proizvoda za poređenje, izaberi ga bar svaki drugi dan.
- Ako format ne odgovara proizvodu (npr. 3 ili 6 za kameru), izaberi drugi.

## Pravila po formatu

**2. Problem → rešenje.** Svakodnevni problem kupca, pa proizvod kao rešenje. Problem mora biti **neutralan, bez straha**: bez lopova, provala i „zaštitite porodicu“. Malo humora je dobrodošlo („Mačka. Opet.“). Rešenje mora biti osobina sa stranice proizvoda. Banka problema:
- Pas laje noću, a ne znaš na šta. → kamera sa IR / noćnim snimanjem
- Kurir kaže da je zvonio, a ti nisi čuo. → interfon / video interfon, kamera na ulazu
- Vikendica je daleko, a hoćeš da vidiš da je sve u redu posle nevremena. → kamera sa aplikacijom, 4G ili solarna
- Plac ili vikendica bez struje. → baterijska ili solarna kamera
- Stari snimač je pun i snimci traju samo par dana. → veći disk ili H.265+ kompresija
- Noću je slika mutna ili crno-bela, a treba ti boja. → ColorVu / dual light kamera (samo ako sajt to navodi)
- Odsjaj noću na staklenoj kupoli kamere. → turret kamera bez staklene kupole (samo ako sajt to navodi)
- U radnji ne vidiš ulaz i kasu u isto vreme. → više kamera i snimač sa više kanala
- Ne znaš ko je parkirao ispred kapije. → kamera sa dobrim uglom ili objektivom
- Kapiju po kiši otvaraš ručno. → motor za kapiju (kad kategorija uđe u fazu)
- Ne čuješ zvono iz dvorišta. → interfon (kad kategorija uđe u fazu)

**3. 3 stvari (samo kompleti).** Tri stvari su **fizički delovi kompleta**, ne funkcije aplikacije: kamere, snimač, hard disk, napajanje, PoE svič i slično. Uzmi samo delove koji su **navedeni na stranici kompleta** (sadržaj paketa, specifikacije). Za svaki deo pokaži pravu sliku tog dela sa sajta. Kraj: „Ovaj ima sve tri.“

**4. Poređenje A ili B.** Dva prava proizvoda sa sajta, **oba na stanju**, iz iste kategorije i sličnog nivoa. Na primer: analogni ili IP komplet, 2 MP ili 4 MP kamera, 4 ili 8 kanala, bullet ili turret. Tri reda poređenja (npr. kabl, snimač, cena) i poziv na komentar „Napiši u komentar: A ili B?“. Sve vrednosti moraju biti sa stranica oba proizvoda. Scena sa cenom na kraju je za proizvod A. U posted.json upiši oba product_id-ja (`product_id` za A, `product_id_b` za B).

**5. Za koga je.** Tri tipa kupca (kuća, vikendica, radnja, plac, garaža, kancelarija), svaki sa jednom pravom osobinom proizvoda. Upotrebu za sve tipove kupaca mora da navodi stranica proizvoda („Za šta je idealan“).

**6. Šta dobiješ (samo kompleti).** Delovi uleću jedan po jedan, uz brojač i prave slike pojedinačnih delova sa sajta. Na kraju ide „Kupljeno pojedinačno X“ precrtano, pa cena kompleta i „Uštedite Y (Z%)“, i to **samo ako sajt prikazuje uštedu**.

**7. POV telefon (retko).** Ekran aplikacije je ilustracija i to mora pisati na ekranu („Prikaz je ilustracija.“). Ime aplikacije samo ako ga navodi stranica proizvoda.

**8. Greška pre kupovine.** Greška koju je lako napraviti, na primer kamere i snimač kupljeni odvojeno, premali disk ili pogrešan tip kabla. Ne tvrdi „najčešća greška“, jer to nije provereno. Kraj je lista „Pre kupovine proveri:“ sa vrednostima tog proizvoda.

## Evidencija
U `data/posted.json` svaki reel dobija polje `format` (`f2`–`f8`). Nedeljni zaključak poredi formate (pregledi, prosečno vreme gledanja, interakcije), a ocena formata se daje tek posle bar 3 reela tog formata.
