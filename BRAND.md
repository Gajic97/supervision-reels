# BRAND.md: pravila za SuperVision reelove (brag)

Ova pravila se dodaju uz brag (brag-slim) pri svakom pravljenju reela. Kad se nešto u njima razlikuje od podrazumevanih brag tonova, važe ova pravila.

## Format
- Vertikalno 1080×1920, 30 fps, trajanje 18–22 s.
- Muzika na 120 BPM; svaki rez i svaki ulazak elementa pada na beat.
- Važan sadržaj stoji između y 170 i y 1500. Sa strane mora biti bar oko 115 px razmaka od ivice (u reel-v3 ovo rešava scale 0.92 na scenama). Donji i desni deo kadra ostaju slobodni za UI TikTok-a i Instagrama.
- Trajanje je 23 s: 2 s tekstualnog hook-a (HOOKS.md), pa 21 s proizvoda.

## Ton
- Brz, čist i pregledan, sa puno animacija, ali ozbiljan.
- Bez straha, senzacionalizma i „lopovi dolaze“ priča.
- Jezik je srpski, latinica. Rečenice su kratke, obraćanje je na „ti“, bez generičkih marketinških fraza.

## Vizuelni identitet (novi sajt)
- Pozadina: tamnozelena #123528 i #1b4636, sa suptilnom mrežom.
- Akcenti: #2f7a50, #439665 i #6cc08f. Crvena #d64545 (na tamnoj pozadini #ff8a80) koristi se samo za uštedu.
- Font Poppins (800 za naslove, 500–700 za tekst).
- Logo u kraju: teal ikonica, belo „Super“ i zeleno „Vision“, ispod „SURVEILLANCE & NETWORKING“.
- Proizvodi stoje na belim zaobljenim karticama sa senkom i odsjajem.

## Slike proizvoda
- Za komplete se NE seku pojedinačni delovi iz zajedničke slike kompleta. Svaki deo (kamera, snimač, disk, napajanje…) se nalazi kao zaseban proizvod na sajtu i koristi se njegova prava slika (Store API, pretraga po šifri modela).
- Slika kompleta koristi se samo kad se komplet prikazuje kao celina.
- Ne koristi se slika koja prikazuje drugi kapacitet ili model (npr. disk 6 TB umesto 1 TB).
- Koriste se samo originalne fotografije sa sajta. Nema AI fotografija proizvoda.

## Činjenice
- Svaki podatak mora da postoji na stranici proizvoda istog dana: specifikacije, cena, dostupnost, sadržaj paketa.
- Cena se prikazuje samo ako je javna. Kod B2B proizvoda („Ulogujte se…“) nema cene.
- Ako nešto nije u paketu (npr. kabl), to se jasno navodi.
- Šeme i rasporedi se označavaju kao „Primer…“. Nema lažnog snimka kamere ni „REC“ oznake.
- Nema izmišljenih recenzija, „najprodavanije“ tvrdnji ni garancija bezbednosti.

## Struktura (polazni oblik, ne kalup)
1. Hook (2–3,5 s): najjači vizuelni trenutak proizvoda, uz kratku tvrdnju.
2. Šta dobijaš ili šta radi: kartice uleću po beatu.
3. 2–3 potvrđene specifikacije, sa brojačima.
4. Namena ili primer upotrebe.
5. Cena ili ušteda (ako je javna) i simuliran tap na „Dodaj u korpu“.
6. Kraj: logo, super-vision.rs, „Isporuka za 2 radna dana“.

## Zvuk
- Zvuk je uvek ugrađen u video. Renderuje se samo jedna verzija, sa muzikom i efektima.
- **Muzika je za svaki reel drugačija:** 5 stilova (deep_house, lofi_chill, synthwave, cinematic, minimal_tech), uz nasumični tonalitet. Isti stil se ne ponavlja u 2 uzastopna reela (Gajic, 29.10.2026).
- Moderna house ili elektronska podloga, topli akordi (npr. Am9, Fmaj7, Cmaj9, G6), sub bas sa sidechain-om.
- Zvučni efekti:
  - mehanički škljocaji i sub udari
  - whoosh-evi usklađeni sa prelazima
  - meki swish-evi na kartice
  - riser-i
  - realističan tap
  - reverb na sve
- **Zabranjeno:** 8-bit i Nintendo zvuk, tonski „blip“ i pluck efekti.
- Glasnoća -14 LUFS, vrh -1,5 dBTP.
- Polazna osnova je `templates/reel-v3/sound.py`.

## Opisi
- Za svaku mrežu poseban opis:
  - TikTok: kratko, 3–5 hashtagova
  - Instagram: detaljnije, „link u bio“ (link super-vision.rs je u biografiji profila supervisionsm)
  - LinkedIn: stručno, bez hashtag spama
- Bez emodžija.

## Ključne reči (pretraga na Instagramu i TikTok-u)
- Svaki reel ima jednu glavnu ključnu reč, onako kako je ljudi kucaju, npr. „video nadzor za kuću“, „komplet video nadzora“, „kamera za dvorište“ ili „video interfon“.
- Glavna ključna reč stoji u prvoj rečenici opisa, pre naziva modela. Primer: „Komplet video nadzora za kuću: 4 kamere HiLook…“.
- U tekstu na ekranu (hook ili naslov scene) glavna ključna reč se pojavljuje bar jednom, jer platforme čitaju i tekst iz videa.
- Dodaju se 1–2 sporedne fraze i lokacija: „Srbija“, a za lokalne usluge (ugradnja) „Sremska Mitrovica“.
- Hashtagovi: 3–5 komada, prvi je glavna ključna reč bez razmaka (npr. #videonadzor), uz brend proizvođača (#hilook, #hikvision) i #supervision.
- Šifra modela (npr. THC-B120-P) ide u opis, za ljude koji traže tačan model.
