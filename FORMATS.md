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

## Usluge i B2B portal (Gajic, 30.10.2026)
Ne moraju svi reelovi biti proizvodi. **Povremeno**, umesto jednog proizvoda tog dana, ide reel o **B2B portalu** ili o **uslugama**:
- najviše **2 takva reela nedeljno** (najviše 1 dnevno; drugi reel tog dana je proizvod)
- smenjuju se: B2B portal, ugradnja video nadzora, akt o proceni rizika, projektovanje, kalkulator ugradnje
- isti tip ne ide dve nedelje zaredom ako ima drugih
- **31.10.2026: jutarnji reel (12:30) je B2B portal.** Večernji je proizvod.

Pravila su ista kao za proizvode: hook po HOOKS.md, formati 2, 4, 5 i 8 (3 i 6 samo za komplete, pa ovde ne idu), samo činjenice sa stranice, bez straha i bez izmišljenih ponuda. Umesto scene sa cenom (`sP`) ide **CTA kartica** sa istom animacijom (kartica, sjaj, dodir prsta), sa tekstom poziva (npr. „Zatražite ponudu“ ili „b2b.super-vision.rs“) i telefonom 062/618-736. Slike su samo sa sajta (fotografije sa stranica usluga, licence MUP-a, slike proizvoda). U posted.json: `product_id: null`, `category: "B2B"` ili `"Usluge"`, `product`: naziv usluge, `url`: stranica.

### Činjenice koje smeju (izvor: super-vision.rs, 30.10.2026; pre upotrebe proveri da i dalje stoje na stranici)
**B2B portal** (b2b.super-vision.rs; tekst sa naslovne super-vision.rs, sekcija „Za koga radimo → Instalateri“):
- za instalatere i firme; veleprodajne cene; roba sa lagera; slanje u roku od 2 radna dana
- „Pomažemo oko izbora opreme i sastavljamo spisak po objektu, da na terenu ne fali ni jedan konektor.“
- 2.000+ artikala na lageru, „poručeno danas, poslato sutra“; Hikvision ovlašćeni partner i tehnička podrška; radimo od 2011.
- na glavnom sajtu kod dela opreme piše „Ulogujte se na nalog da vidite cenu“ (cene za firme su na portalu)
- Ideje: f2 „Na terenu fali jedan konektor i ceo dan staje.“ → spisak po objektu; f5 instalater / firma / servis; f8 „Greška: nabavka sa pet strana“ (samo ako je izvedeno iz činjenica iznad)

**Ugradnja video nadzora** (/ugradnja-video-nadzora/): u celoj Srbiji; licence MUP-a; izlazak na objekat i izrada ponude se ne naplaćuju; provera slike danju i noću na licu mesta; u cenu radova ulaze montaža, kablovi, konektori i sitan materijal, konfiguracija, daljinski pristup i obuka; oprema se obračunava posebno; kalkulator ugradnje za grubu procenu. Slika: `wp-content/uploads/2026/10/bermix-studio-bAGo7O4prtY-unsplash-800x500-1.jpg`.

**Akt o proceni rizika** (/akt-o-proceni-rizika/): cena od 140.000 din + PDV; sme da ga izradi samo lice sa licencom MUP-a; nije isto što i BZR procena; ne mora svaka firma da ga ima (izuzeci po čl. 20 st. 6 Zakona o privatnom obezbeđenju, npr. mikro pravna lica i preduzetnici); na stranici je provera „za 30 sekundi“ da li firma mora da ima akt. Slike: licence MUP-a (`licenca-mup-*.png`).

**Projektovanje** (/projektovanje-sistema-tehnicke-zastite/): redosled procena → plan → projekat → izvođenje → nadzor → održavanje; kategorije II i III traže projekat izvedenog objekta, IV i V grafički prikaz; provera da li se obaveza odnosi na objekat se ne naplaćuje.

**Usluge uopšte** (/usluge-tehnicke-zastite/): sve licence MUP-a, sve kroz jednu firmu bez podizvođača; 5 usluga: akt o proceni rizika, plan i projekat, ugradnja, stručni nadzor, održavanje i servis. Slika salona: `usluge-tehnicke-zastite-supervision.jpg`.

Za zakonske teme (akt, projektovanje) ton je informativan: „proverite da li se odnosi na vas“, nikad zastrašivanje kaznama ili inspekcijom.
