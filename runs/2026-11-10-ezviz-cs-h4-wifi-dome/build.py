"""Gradi 2 reela za 10.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py).
R['cam'] = EZVIZ CS-H4 (id 4878), f5 Za koga je, 12:30
R['dvr'] = HiLook DVR-108G-M1/T (id 2866), f2 Problem -> rešenje, 19:30
"""
import json, os, sys, shutil
GEN = os.path.expanduser('~/sr/templates/formati-demo/gen.py')
src = open(GEN, encoding='utf-8').read()
head, build = src.split('# ---------------------------------------------------------------- build')
g = {'__file__': GEN}
exec(head, g)
exec(build.split('for k, f in F.items():')[0], g)
hook, BASE, sfx_for, persona, CAMDOT = g['hook'], g['BASE'], g['sfx_for'], g['persona'], g['CAMDOT']

FONTS = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};src:url(assets/fonts/poppins-{s}-{w}-normal.woff2) format('woff2');unicode-range:{r}}}"
    for w in (400, 500, 600, 700, 800)
    for s, r in (('latin', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD,U+2713,U+2715'),
                 ('latin-ext', 'U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF')))
R = {}
CH = 'position:relative;left:auto;top:auto'
PRIMER = '<text x="%d" y="%d" font-family="Poppins" font-weight="500" font-size="24" fill="%s">Primer, ilustracija</text>'

# ============================================================ EZVIZ CS-H4 (f5, Za koga je)
SVG_A = ('<svg width="920" height="640" viewBox="0 0 920 640">'
  '<rect y="500" width="920" height="140" fill="#cfe6d8"/>'
  '<rect x="90" y="140" width="190" height="170" rx="8" fill="#fff" stroke="#123528" stroke-width="7"/><line x1="185" y1="140" x2="185" y2="310" stroke="#123528" stroke-width="5"/>'
  '<rect x="380" y="330" width="380" height="90" rx="34" fill="#439665"/><rect x="360" y="400" width="420" height="100" rx="30" fill="#2f7a50"/>'
  '<rect x="120" y="390" width="160" height="110" rx="10" fill="#123528"/><rect x="132" y="402" width="136" height="70" rx="4" fill="#6cc08f"/>'
  '<path id="aFov" d="M860 70 L985 960 L-31 -55 Z" fill="rgba(47,122,80,.28)" stroke="#2f7a50" stroke-width="3" stroke-dasharray="14 10" opacity="0"/>'
  '<g transform="translate(860 70)"><circle r="30" fill="#fff" stroke="#123528" stroke-width="7"/><circle r="11" fill="#123528"/></g>'
  '<text id="aDeg" x="560" y="250" font-family="Poppins" font-weight="800" font-size="110" fill="#123528">0°</text>'
  + PRIMER % (30, 625, '#5d6b64') + '</svg>')
PERSON = '<g id="%s"><circle cx="0" cy="-150" r="30" fill="#123528"/><rect x="-34" y="-115" width="68" height="110" rx="26" fill="#123528"/><rect x="-28" y="-14" width="22" height="90" rx="10" fill="#123528"/><rect x="6" y="-14" width="22" height="90" rx="10" fill="#123528"/></g>'
SVG_B = ('<svg width="920" height="640" viewBox="0 0 920 640">'
  '<rect y="500" width="920" height="140" fill="#cfe6d8"/>'
  '<rect x="60" y="110" width="440" height="390" fill="#fff" stroke="#123528" stroke-width="7"/><path d="M40 110 L520 110 L490 50 L70 50 Z" fill="#2f7a50"/>'
  '<rect x="110" y="190" width="150" height="310" fill="#cfe6d8" stroke="#123528" stroke-width="6"/><rect x="300" y="190" width="160" height="140" fill="#6cc08f"/>'
  + CAMDOT % (480, 140) +
  '<g id="bPw" transform="translate(-80 0)">' + PERSON % 'bP' + '<g id="bPb" opacity="0"><rect x="-60" y="-200" width="120" height="290" fill="none" stroke="#d64545" stroke-width="6"/><rect x="-60" y="-246" width="138" height="44" fill="#d64545"/><text x="-50" y="-213" font-family="Poppins" font-weight="800" font-size="28" fill="#fff">OSOBA</text></g></g>'
  '<g id="bCw" transform="translate(1000 0)"><g transform="translate(0 420)"><path d="M0 60 L18 18 Q28 0 55 0 L170 0 Q196 0 210 18 L240 60 L262 68 L262 112 L0 112 Z" fill="#123528"/><rect x="36" y="12" width="70" height="44" rx="7" fill="#6cc08f"/><rect x="120" y="12" width="76" height="44" rx="7" fill="#6cc08f"/><circle cx="62" cy="116" r="24" fill="#0b1a14"/><circle cx="206" cy="116" r="24" fill="#0b1a14"/></g>'
  '<g id="bCb" opacity="0"><rect x="-14" y="400" width="292" height="160" fill="none" stroke="#2f7a50" stroke-width="6"/><rect x="-14" y="354" width="152" height="44" fill="#2f7a50"/><text x="-4" y="387" font-family="Poppins" font-weight="800" font-size="28" fill="#fff">VOZILO</text></g></g>'
  + PRIMER % (30, 625, '#5d6b64') + '</svg>')
SVG_C = ('<svg width="920" height="640" viewBox="0 0 920 640">'
  '<rect y="520" width="920" height="120" fill="#cfe6d8"/>'
  '<rect x="120" y="150" width="520" height="370" fill="#fff" stroke="#123528" stroke-width="7"/><path d="M90 150 L670 150 L640 100 L120 100 Z" fill="#2f7a50"/>'
  '<rect x="300" y="260" width="140" height="260" rx="6" fill="#439665" stroke="#123528" stroke-width="6"/><circle cx="415" cy="395" r="9" fill="#fff"/>'
  + CAMDOT % (370, 180) +
  '<g id="cW" fill="none" stroke="#2f7a50" stroke-width="7" stroke-linecap="round"><path d="M410 205 q30 30 0 60"/><path d="M432 190 q48 45 0 90"/><path d="M454 175 q66 60 0 120"/></g>'
  + PERSON.replace('id="%s"', 'id="cP" transform="translate(560 445)"') +
  '<g id="cPh" transform="translate(770 300)"><rect x="-58" y="-110" width="116" height="220" rx="20" fill="#123528"/><rect x="-46" y="-90" width="92" height="160" rx="6" fill="#6cc08f"/><circle id="cMic" cx="0" cy="-10" r="22" fill="#fff"/><rect x="-8" y="-28" width="16" height="30" rx="8" fill="#123528"/></g>'
  + PRIMER % (30, 625, '#5d6b64') + '</svg>')

R['cam'] = dict(
  tag='WI-FI KAMERA 2K', hook=hook('Stan, radnja ili ulaz: jedna kamera.', (4, 5), 5), hsize=128, subtop=1080,
  sub='Wi-Fi kamera koja radi i unutra i napolju.', p=('Wi-Fi kamera', 'unutra i napolju'),
  inc='✓  Adapter za napajanje je u pakovanju', price='8.190', img='assets/cam.jpg',
  style='deep_house', key=9, seed=4878,
  scn=[['a', 0, 4.5], ['b', 4.5, 9], ['c', 9, 13], ['d', 13, 15.5]],
  slams=[0, 4.5, 9, 13, 15.5, 18.5],
  html=persona('a', '1 · DNEVNA SOBA', 'Cela soba <span class="green">iz jednog ugla</span>', 'Objektiv 2,8 mm hvata 106° horizontalno.', SVG_A)
     + persona('b', '2 · RADNJA', 'Osoba ili vozilo? <span class="green">Zna razliku.</span>', 'AI detekcija smanjuje lažne uzbune.', SVG_B)
     + persona('c', '3 · ISPOD STREHE', 'Javiš se <span class="green">sa telefona</span>', 'Mikrofon i zvučnik: razgovor kroz EZVIZ aplikaciju.', SVG_C)
     + f'''
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:104px">Ista kamera.</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:300px;font-size:104px">Za sva tri.</div>
    <div class="disc" id="d3" style="left:270px;top:450px;width:540px;height:540px"><img src="assets/cam.jpg" style="left:70px;top:90px;width:400px;height:340px"></div>
    <div class="abs" style="left:80px;top:1060px;width:920px;display:flex;gap:22px;justify-content:center">
      <div class="chip" id="d4" style="{CH}">2K</div><div class="chip" id="d5" style="{CH}">IP67</div><div class="chip" id="d6" style="{CH}">Noću do 30 m</div></div>
    <div class="abs note" id="d7" style="left:80px;top:1190px;width:920px;text-align:center">Nema bateriju: treba napajanje u blizini.</div>
  </div>''',
  js='''function per(p,t,a){pop($(p+'l'),t,a,{dx:-60,dy:0,s0:1});slam($(p+'t'),t,a+.3,{s0:1.3});pop($(p+'c'),t,a+.5,{dy:200,s0:.85,d:.5,ry0:20});pop($(p+'s'),t,a+1.5,{dy:24,s0:1});}
function renderF(t){
  if(t<4.6){per('a',t,0);const p=eoc(P(t,1.2,.6));$('aFov').setAttribute('opacity',String(p));
    $('aFov').setAttribute('transform',`rotate(${Math.sin(t*1.3)*5} 860 70)`);$('aDeg').textContent=count(t,1.3,1.1,106)+'°';}
  if(t>=4.4&&t<9.1){per('b',t,4.6);const s=eio(P(t,5.1,1.5));
    $('bCw').setAttribute('transform',`translate(${lerp(1000,600,eio(P(t,5.3,1.4)))} 0)`);
    $('bPw').setAttribute('transform',`translate(${lerp(-80,330,s)} 470)`);
    const q1=eob(P(t,6.7,.3)),q2=eob(P(t,7.2,.3));$('bPb').setAttribute('opacity',String(clamp(q1*2,0,1)));$('bCb').setAttribute('opacity',String(clamp(q2*2,0,1)));}
  if(t>=8.9&&t<13.1){per('c',t,9.1);[...$('cW').children].forEach((w,i)=>{const k=((t*1.4-i*.22)%1+1)%1;w.setAttribute('opacity',String(t>10?(1-k):0));});
    $('cMic').setAttribute('r',String(22+6*Math.abs(Math.sin(t*5))));}
  if(t>=12.9&&t<15.6){pop($('d1'),t,13.05,{dx:-90,dy:0,s0:1});slam($('d2'),t,13.3);
    const hp=P(t,13.1,.6),he=eob(hp);tf($('d3'),{y:lerp(300,0,he)+Math.sin(t*2)*10,s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-60,0,eoc(hp))});
    ['d4','d5','d6'].forEach((id,i)=>pop($(id),t,13.8+i*.25,{dy:40,s0:.7}));pop($('d7'),t,14.5,{dy:20,s0:1});}
}''',
  pops=[0, .5, 1.5, 4.6, 5.1, 6.1, 6.7, 7.2, 9.1, 9.6, 10.6, 13.05, 13.8, 14.05, 14.3, 14.5], impacts=[.3, 4.9, 9.4, 13.3])

# ============================================================ HiLook DVR-108G-M1/T (f2, Problem -> rešenje)
PORTS = ''.join(f'<g class="pt4"><rect x="{180+i*95}" y="330" width="70" height="56" rx="10" fill="#6cc08f"/><text x="{215+i*95}" y="370" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="30" fill="#123528">{i+1}</text></g>' for i in range(4))
SVG_DA = ('<svg class="abs" id="aSv" style="left:80px;top:470px" width="920" height="720" viewBox="0 0 920 720">'
  '<rect x="140" y="280" width="420" height="150" rx="22" fill="#e6eee9"/>' + PORTS +
  ''.join(f'<path d="M{215+i*95} 430 L{215+i*95} 520 L{110+i*150} 600" fill="none" stroke="#6cc08f" stroke-width="5"/>' for i in range(4)) +
  ''.join(CAMDOT % (110 + i * 150, 620) for i in range(4)) +
  '<g id="a5"><path d="M560 355 L700 355" fill="none" stroke="#ff7b7b" stroke-width="5" stroke-dasharray="14 12"/>'
  '<g transform="translate(760 355)"><circle r="34" fill="#fff" stroke="#d64545" stroke-width="8"/><circle r="12" fill="#123528"/></g>'
  '<text id="aQ" x="730" y="270" font-family="Poppins" font-weight="800" font-size="120" fill="#ff7b7b">?</text></g>'
  '<text x="180" y="250" font-family="Poppins" font-weight="700" font-size="34" fill="#c9dbd0">Snimač 4 kanala</text>'
  + PRIMER % (0, 712, '#9db5aa') + '</svg>')
TILES = ''.join(
  f'<div class="tile" id="t{i}" style="left:{80+(i%5)*188}px;top:{470+(i//5)*176}px;width:168px;height:156px;background:{"#fff" if i<8 else "#e6f2ea"};display:flex;flex-direction:column;align-items:center;justify-content:center;color:#123528">'
  f'<div style="font-size:54px;font-weight:800;line-height:1">{i+1 if i<8 else "IP"}</div><div style="font-size:22px;font-weight:600;color:#5d6b64;margin-top:6px">{"analogna" if i<8 else "mrežna"}</div></div>'
  for i in range(10))
PROTO = ['HDTVI', 'AHD', 'CVI', 'CVBS', 'IP']
FEAT = '<div class="card feat" id="%s" style="top:%dpx;height:250px"><div class="ic" style="width:180px;height:180px">%s</div><div class="st"><b>%s</b><span>%s</span></div></div>'
IC_ZIP = '<svg width="150" height="150" viewBox="-75 -75 150 150"><rect x="-50" y="-60" width="100" height="120" rx="12" fill="#123528"/><rect id="z1" x="-36" y="-44" width="72" height="18" rx="6" fill="#6cc08f"/><rect id="z2" x="-36" y="-14" width="72" height="18" rx="6" fill="#6cc08f"/><rect id="z3" x="-36" y="16" width="72" height="18" rx="6" fill="#6cc08f"/></svg>'
IC_TV = '<svg width="150" height="150" viewBox="-75 -75 150 150"><rect x="-62" y="-46" width="124" height="80" rx="10" fill="#123528"/><rect id="tvs" x="-52" y="-36" width="104" height="60" rx="4" fill="#6cc08f"/><rect x="-10" y="34" width="20" height="14" fill="#123528"/><rect x="-32" y="46" width="64" height="8" rx="4" fill="#123528"/></svg>'
IC_HDD = '<svg width="150" height="150" viewBox="-75 -75 150 150"><rect x="-48" y="-62" width="96" height="124" rx="12" fill="#123528"/><circle cx="0" cy="-8" r="34" fill="#6cc08f"/><circle cx="0" cy="-8" r="8" fill="#123528"/><line id="arm" x1="0" y1="-8" x2="24" y2="-30" stroke="#fff" stroke-width="6" stroke-linecap="round"/></svg>'

R['dvr'] = dict(
  tag='SNIMAČ ZA VIDEO NADZOR', hook=hook('Ako planiraš više kamera, uzmi više kanala.', (5, 6), 6), hsize=110, subtop=1140,
  sub='8 analognih i do 2 IP kamere na jednom snimaču.', p=('Snimač za', 'video nadzor'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='7.860', img='assets/dvr.jpg',
  style='synthwave', key=2, seed=2866,
  scn=[['a', 0, 4.5], ['b', 4.5, 9], ['c', 9, 12.5], ['d', 12.5, 15.5]],
  slams=[0, 4.5, 9, 12.5, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:90px">Snimač sa 4 kanala</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:100px">je pun.</div>
    ''' + SVG_DA + '''
    <div class="abs sub" id="a3" style="left:80px;top:1250px;width:920px">Peta kamera nema gde da se uključi.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">8 kanala</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">+ 2 IP kamere</div>
    ''' + TILES + '''
    <div class="abs h1" id="b3" style="left:80px;top:860px;font-size:220px;letter-spacing:-6px"><span id="b3n">0</span></div>
    <div class="abs h1 green" id="b4" style="left:380px;top:930px;font-size:60px;line-height:1.1">kanala<br>ukupno</div>
    <div class="abs sub" id="b5" style="left:80px;top:1210px;width:920px">Do 8 analognih i do 2 IP kamere.</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">Stare kamere?</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:104px">Rade i dalje.</div>
    <div class="tile" id="c3" style="left:230px;top:450px;width:620px;height:420px"><img src="assets/dvr.jpg" style="left:30px;top:20px;width:560px;height:380px"></div>
    <div class="abs" style="left:80px;top:930px;width:920px;display:flex;gap:18px;justify-content:center;flex-wrap:wrap">''' + ''.join(f'<div class="chip" id="cp{i}" style="position:relative">{p}</div>' for i, p in enumerate(PROTO)) + '''</div>
    <div class="abs sub" id="c4" style="left:80px;top:1130px;width:920px">Radi sa gotovo svakom analognom ili mrežnom kamerom.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:100px">Niska cena</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:100px">po kanalu.</div>
    ''' + FEAT % ('f1', 450, IC_ZIP, 'H.265 Pro+', 'kompresija snimaka') + FEAT % ('f2', 730, IC_TV, 'HDMI i VGA', 'slika na TV-u ili monitoru') + FEAT % ('f3', 1010, IC_HDD, '1 SATA disk', 'kapaciteta do 4 TB') + '''
  </div>''',
  js='''function renderF(t){
  if(t>=0&&t<4.6){$('dark').style.opacity=.55;pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.5);
    {const p=P(t,.2,.5);$('aSv').style.opacity=p;}
    [...document.querySelectorAll('.pt4')].forEach((g,i)=>{const q=P(t,.9+i*.3,.25);g.style.opacity=.25+.75*q;});
    {const q=eob(P(t,2.3,.35));$('a5').style.opacity=clamp(q*2,0,1);$('aQ').setAttribute('transform',`translate(0 ${Math.sin(t*4)*10})`);}
    pop($('a3'),t,2.8,{dy:24,s0:1});}
  if(t>=4.4&&t<9.1){pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,5.0);
    for(let i=0;i<10;i++)pop($('t'+i),t,5.4+i*.17,{dy:60,s0:.6,d:.3});
    $('b3n').textContent=t<5.5?0:Math.min(10,Math.floor((t-5.5)/.17)+1);pop($('b3'),t,5.3,{dy:40,s0:.8});pop($('b4'),t,5.6,{dx:60,dy:0,s0:1});pop($('b5'),t,7.4,{dy:24,s0:1});}
  if(t>=8.9&&t<12.6){pop($('c1'),t,9.05,{dx:-90,dy:0,s0:1});slam($('c2'),t,9.4);
    pop($('c3'),t,9.2,{dy:200,s0:.8,d:.5,ry0:30});if(t>9.7)$('c3').style.transform+=` translateY(${Math.sin(t*2)*8}px)`;
    for(let i=0;i<5;i++)pop($('cp'+i),t,10.0+i*.22,{dy:40,s0:.6});pop($('c4'),t,11.2,{dy:24,s0:1});}
  if(t>=12.4&&t<15.6){pop($('d1'),t,12.55,{dx:-90,dy:0,s0:1});slam($('d2'),t,12.8);
    ['f1','f2','f3'].forEach((id,i)=>pop($(id),t,13.1+i*.45,{dx:200,dy:0,s0:.95,d:.42,ry0:-35}));
    ['z1','z2','z3'].forEach((id,i)=>$(id).setAttribute('width',String(72*(.45+.55*Math.abs(Math.sin(t*2.4+i))))));
    $('tvs').setAttribute('fill',Math.floor(t*2)%2?'#6cc08f':'#439665');$('arm').setAttribute('transform',`rotate(${Math.sin(t*3)*25} 0 -8)`);}
}''',
  pops=[.05, .9, 1.2, 1.5, 1.8, 2.8, 4.6, 5.4, 5.6, 6.1, 6.6, 7.4, 9.05, 9.2, 10.0, 10.4, 10.9, 11.2, 12.55, 13.1, 13.55, 14.0], impacts=[.5, 2.3, 5.0, 9.4, 12.8])

IMGS = {'cam': {'cam.jpg': 'cam.jpg'}, 'dvr': {'dvr.jpg': 'dvr.jpg'}}
FD = os.path.expanduser('~/work/fonts/package/files')
for k in sys.argv[1:] or R:
    f = R[k]; out = os.path.expanduser(f'~/work/{k}')
    os.makedirs(os.path.join(out, 'assets', 'fonts'), exist_ok=True)
    for w in (400, 500, 600, 700, 800):
        for s in ('latin', 'latin-ext'):
            shutil.copy(f'{FD}/poppins-{s}-{w}-normal.woff2', os.path.join(out, 'assets', 'fonts'))
    shutil.copy(os.path.expanduser('~/sr/templates/reel-v4/assets/supervision-ikonica-512.png'), os.path.join(out, 'assets'))
    for dst, s in IMGS[k].items():
        shutil.copy(os.path.expanduser(f'~/work/img/{s}'), os.path.join(out, 'assets', dst))
    h = BASE.replace('<style>', '<style>' + FONTS, 1)
    for tok, val in [('%%TAG%%', f['tag']), ('%%HOOK%%', f['hook']), ('%%HSIZE%%', str(f['hsize'])), ('%%SUBTOP%%', str(f['subtop'])),
                     ('%%SUB%%', f['sub']), ('%%SCENES%%', f['html']), ('%%P1%%', f['p'][0]), ('%%P2%%', f['p'][1]),
                     ('%%INC%%', f['inc']), ('%%PRICE%%', f['price']),
                     ('%%SCN%%', json.dumps(f['scn'])), ('%%SLAMS%%', json.dumps(f['slams'])), ('%%JS%%', f['js'])]:
        h = h.replace(tok, val)
    h = h.replace('src="assets/kit.jpg" class="abs"', f'src="{f["img"]}" class="abs"')
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
    json.dump({'style': f['style'], 'key': f['key'], 'seed': f['seed']}, open(os.path.join(out, 'music.json'), 'w'))
print('ok')
