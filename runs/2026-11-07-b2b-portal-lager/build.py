"""Gradi 2 reela za 07.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
import json, os, sys, shutil
GEN = os.path.expanduser('~/sr/templates/formati-demo/gen.py')
src = open(GEN, encoding='utf-8').read()
head, build = src.split('# ---------------------------------------------------------------- build')
g = {'__file__': GEN}
exec(head, g)
exec(build.split('for k, f in F.items():')[0], g)
hook, BASE, sfx_for = g['hook'], g['BASE'], g['sfx_for']

FONTS = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};src:url(assets/fonts/poppins-{s}-{w}-normal.woff2) format('woff2');unicode-range:{r}}}"
    for w in (400, 500, 600, 700, 800)
    for s, r in (('latin', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD,U+2713,U+2715'),
                 ('latin-ext', 'U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF')))

R = {}

# ============================================================ B2B PORTAL (f8, greška pre nabavke)
LROW = lambda i, img, name, top: f'''<div class="abs" id="l{i}" style="left:40px;top:{top}px;width:840px;height:150px;border-radius:24px;background:#f1f7f3;display:flex;align-items:center;gap:26px;padding:0 26px">
        <div style="width:110px;height:110px;border-radius:18px;background:#fff;position:relative;overflow:hidden;flex:none"><img src="assets/{img}" style="position:absolute;left:5px;top:5px;width:100px;height:100px;object-fit:contain"></div>
        <div style="flex:1;font-size:32px;font-weight:700;color:#123528;line-height:1.2">{name}</div>
        <div id="lb{i}" style="flex:none;background:#2f7a50;color:#fff;font-size:26px;font-weight:700;border-radius:999px;padding:10px 22px">Na stanju</div></div>'''

R['b2b'] = dict(
  style='minimal_tech', key=6, seed=3111,
  tag='VELEPRODAJA VIDEO NADZORA', hook=hook('Pre nego što obećaš rok, proveri lager.', (3, 4, 6), 6), hsize=112, subtop=1180,
  sub='Greška koju je lako napraviti u nabavci.', p=('Veleprodaja', 'video nadzora'),
  inc='✓  Nalog otvaramo firmama i instalaterima', price='2.000+', img='assets/supervision-ikonica-512.png',
  scn=[['a', 0, 4.5], ['b', 4.5, 8.5], ['c', 8.5, 12], ['d', 12, 15.5]],
  slams=[0, 2.2, 4.5, 8.5, 12, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Obećaš rok,</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:96px">pa zoveš lager.</div>
    <svg class="abs" id="acal" style="left:80px;top:500px" width="420" height="440" viewBox="0 0 420 440">
      <rect x="10" y="40" width="400" height="390" rx="34" fill="#fff"/><rect x="10" y="40" width="400" height="110" rx="34" fill="#2f7a50"/><rect x="10" y="110" width="400" height="40" fill="#2f7a50"/>
      <rect x="100" y="10" width="26" height="70" rx="13" fill="#123528"/><rect x="294" y="10" width="26" height="70" rx="13" fill="#123528"/>
      <text x="210" y="122" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="46" fill="#fff">ROK</text>
      <text x="210" y="330" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="150" fill="#123528">?</text>
    </svg>
    <svg class="abs" id="aph" style="left:580px;top:500px" width="420" height="440" viewBox="0 0 420 440">
      <rect x="110" y="10" width="200" height="400" rx="36" fill="#0a0f0d" stroke="#22302a" stroke-width="10"/><rect x="128" y="50" width="164" height="300" rx="10" fill="#1b4636"/>
      <g id="ring1" fill="none" stroke="#6cc08f" stroke-width="8" stroke-linecap="round"><path d="M70 150 A120 120 0 0 0 70 290"/><path d="M350 150 A120 120 0 0 1 350 290"/></g>
      <g id="ring2" fill="none" stroke="#6cc08f" stroke-width="8" stroke-linecap="round" opacity=".6"><path d="M30 120 A170 170 0 0 0 30 320"/><path d="M390 120 A170 170 0 0 1 390 320"/></g>
      <g font-family="Poppins" font-weight="800" font-size="70" fill="#fff"><text id="dt1" x="150" y="225">.</text><text id="dt2" x="195" y="225">.</text><text id="dt3" x="240" y="225">.</text></g>
    </svg>
    <div class="abs sub" id="a3" style="left:80px;top:1010px;width:920px">Klijent čeka, a ti čekaš potvrdu da je roba na stanju.</div>
    <div class="abs note" id="a4" style="left:80px;top:1150px;width:920px">Primer, ilustracija.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">Na B2B portalu:</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">lager uživo.</div>
    <div class="card" id="bcard" style="left:80px;top:470px;width:920px;height:720px">
      <div class="abs" style="left:40px;top:34px;font-size:30px;font-weight:700;color:#5d6b64;letter-spacing:2px">STANJE LAGERA</div>
      ''' + LROW(1, 'cam1.jpg', 'Turret kamera 5 MP', 100) + LROW(2, 'cam2.jpg', 'Bullet kamera 5 MP', 270) + LROW(3, 'dvr.jpg', 'DVR snimač 8 kanala', 440) + '''
      <div class="abs" style="left:40px;top:620px;font-size:28px;color:#5d6b64;font-weight:500">Vidiš šta je na stanju pre nego što obećaš rok.</div>
      <div class="shine" id="bshine"></div>
    </div>
    <div class="abs note" id="b3" style="left:80px;top:1230px;width:920px">Prikaz je ilustracija. Slike proizvoda sa sajta.</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">Tvoje cene</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:96px">čim se prijaviš.</div>
    <div class="card" id="ccard" style="left:80px;top:470px;width:920px;height:560px">
      <div class="abs" style="left:50px;top:44px;font-size:30px;font-weight:600;color:#5d6b64">PIB ili email</div>
      <div class="abs" style="left:50px;top:94px;width:820px;height:110px;border:3px solid #c9dbd0;border-radius:20px;background:#f1f7f3;display:flex;align-items:center;padding:0 30px;font-size:44px;font-weight:700;color:#123528"><span id="ctyp"></span><span id="ccur" style="display:inline-block;width:4px;height:52px;background:#2f7a50;margin-left:4px"></span></div>
      <div class="abs" id="cbtn" style="left:50px;top:240px;width:820px;height:120px;background:#2f7a50;border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:700;color:#fff">Prijavite se</div>
      <div class="abs" id="cprice" style="left:50px;top:400px;width:820px;height:120px;border-radius:20px;background:#e6f2ea;display:flex;align-items:center;justify-content:center;gap:20px;font-size:40px;font-weight:800;color:#2f7a50"><span class="chk" style="width:56px;height:56px;font-size:34px">✓</span>Veleprodajne cene</div>
    </div>
    <div class="chip" id="c3" style="left:80px;top:1080px">poručuješ bez poziva, u svako doba</div>
    <div class="abs note" id="c4" style="left:80px;top:1190px;width:920px">Prikaz je ilustracija prijave na b2b.super-vision.rs.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Pre nabavke</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">proveri:</div>
    <div class="row" id="r1" style="top:500px"><span class="chk">1</span><span>Lager <span class="green">· uživo na portalu</span></span></div>
    <div class="row" id="r2" style="top:640px"><span class="chk">2</span><span>Cena <span class="green">· veleprodajna, odmah</span></span></div>
    <div class="row" id="r3" style="top:780px"><span class="chk">3</span><span>Spisak <span class="green">· po objektu, mi ga sastavimo</span></span></div>
    <div class="row" id="r4" style="top:920px"><span class="chk">4</span><span>Slanje <span class="green">· u roku od 2 radna dana</span></span></div>
    <div class="abs note" id="d3" style="left:80px;top:1080px;width:920px">Da na terenu ne fali ni jedan konektor.</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.6){pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.4);
    fly($('acal'),t,.7,{x0:-600,y0:0,r0:-15});fly($('aph'),t,1.0,{x0:600,y0:0,r0:15});
    if(t>1.5){$('acal').style.transform+=` translateY(${Math.sin(t*2.2)*7}px)`;const sh=t>2.2&&t<2.8?Math.sin(t*40)*8:0;$('aph').style.transform+=` translateX(${sh}px) rotate(${Math.sin(t*9)*2}deg)`;}
    ['dt1','dt2','dt3'].forEach((id,i)=>{$(id).style.opacity=((Math.floor(t*3)%4)>i)?1:.15;});
    $('ring1').style.opacity=.4+.6*Math.abs(Math.sin(t*4));$('ring2').style.opacity=.2+.5*Math.abs(Math.sin(t*4+1));
    pop($('a3'),t,2.6,{dy:24,s0:1});pop($('a4'),t,3.1,{dy:20,s0:1});}
  if(t>=4.4&&t<8.6){pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.9);pop($('bcard'),t,5.0,{dy:120,s0:.88,ry0:20});
    [1,2,3].forEach(i=>{pop($('l'+i),t,5.4+i*.4,{dx:-80,dy:0,s0:1});const q=P(t,5.75+i*.4,.3);$('lb'+i).style.transform=`scale(${lerp(.3,1,eob(q))})`;$('lb'+i).style.opacity=clamp(q*3,0,1);});
    shine($('bshine'),t,7.3);pop($('b3'),t,7.4,{dy:20,s0:1});}
  if(t>=8.3&&t<12.1){pop($('c1'),t,8.55,{dx:-90,dy:0,s0:1});slam($('c2'),t,8.85);pop($('ccard'),t,8.9,{dy:120,s0:.88,ry0:-20});
    const s='Vaša firma';const n=Math.floor(clamp((t-9.3)/.8,0,1)*s.length);$('ctyp').textContent=s.slice(0,n);$('ccur').style.opacity=(Math.floor(t*4)%2)?1:0;
    const pr=t>=10.2&&t<10.36;$('cbtn').style.transform=`scale(${pr?.96:1})`;$('cbtn').style.background=t>=10.3?'#123528':'#2f7a50';
    const q=P(t,10.4,.4);tf($('cprice'),{s:lerp(.6,1,eob(q)),o:clamp(q*3,0,1)});
    pop($('c3'),t,10.9,{dy:40,s0:.8});pop($('c4'),t,11.2,{dy:20,s0:1});}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.25,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4'].forEach((id,i)=>{pop($(id),t,12.6+i*.45,{dx:-80,dy:0,s0:1});const c=$(id).firstElementChild;c.style.transform=`scale(${eob(P(t,12.75+i*.45,.3))})`;});
    pop($('d3'),t,14.5,{dy:20,s0:1});}
}''',
  pops=[.05, .7, 1.0, 2.6, 3.1, 4.6, 5.0, 5.8, 6.2, 6.6, 7.4, 8.55, 8.9, 10.9, 11.2, 12.05, 12.25, 12.6, 13.05, 13.5, 13.95, 14.5],
  impacts=[.4, 4.9, 8.85], extra=[('riser', 4.9, .1, 2.0), ('confirm', 10.3, .22), ('tap', 10.2, .4), ('swish', 7.3, .2)])

# ============================================================ HiLook 5 MP: turret za unutra vs bullet za napolje (f4)
def rowscene(sid, head, a_big, a_small, b_big, b_small, extra=''):
    box = 'position:absolute;top:470px;width:445px;height:620px;border-radius:34px;padding:40px 34px;display:flex;flex-direction:column;justify-content:center'
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs h1" id="{sid}h" style="left:80px;top:220px;font-size:110px">{head}</div>
    <div id="{sid}A" style="{box};left:80px;background:#fff;color:#123528"><div style="font-size:32px;font-weight:800;color:#2f7a50;letter-spacing:3px">A · TURRET</div><div id="{sid}Av" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{a_big}</div><div id="{sid}A2" style="font-size:32px;color:#5d6b64;font-weight:500;margin-top:22px;line-height:1.3">{a_small}</div></div>
    <div id="{sid}B" style="{box};left:555px;background:rgba(255,255,255,.08);border:3px solid #6cc08f"><div style="font-size:32px;font-weight:800;color:#6cc08f;letter-spacing:3px">B · BULLET</div><div id="{sid}Bv" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{b_big}</div><div id="{sid}B2" style="font-size:32px;color:#c9dbd0;font-weight:500;margin-top:22px;line-height:1.3">{b_small}</div></div>
    {extra}
  </div>'''

TILE = lambda tid, left, img, lab, sub: f'<div class="tile" id="{tid}" style="left:{left}px;top:330px;width:460px;height:560px"><img src="assets/{img}" style="left:30px;top:20px;width:400px;height:400px"><div class="abs" style="left:0;top:445px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">{lab}</div><div class="abs" style="left:0;top:500px;width:460px;text-align:center;font-size:26px;color:#5d6b64">{sub}</div></div>'

R['cam'] = dict(
  style='synthwave', key=3, seed=4231,
  tag='KAMERA ZA VIDEO NADZOR', hook=hook('Biraš kameru za unutra ili za napolje?', (3, 6), 6), hsize=118, subtop=1180,
  sub='Ista slika od 5 MP, drugo kućište.', p=('Kamera za unutra', '5 MP · HiLook'),
  inc='Samo za unutra · ide na DVR ili XVR snimač', price='3.590', img='assets/cam1.jpg',
  scn=[['a', 0, 3.5], ['b', 3.5, 8], ['c', 8, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.0, 3.5, 8, 11.5, 13.2, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    ''' + TILE('aA', 60, 'cam1.jpg', 'A · THC-T150-P', 'turret, za unutra') + TILE('aB', 560, 'cam2.jpg', 'B · THC-B150-M', 'bullet, za napolje') + '''
    <div class="abs" id="vs" style="left:420px;top:520px;width:240px;height:240px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:96px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.5)">VS</div>
    <div class="abs h1" id="a3" style="left:0;width:1080px;text-align:center;top:970px;font-size:64px">HiLook · 5 MP · 2.8 mm</div>
    <div class="abs note" id="a4" style="left:0;width:1080px;text-align:center;top:1060px">Obe kamere sa sajta, obe na stanju</div>
  </div>
  ''' + rowscene('b', 'Gde ide', 'Unutra', 'kancelarija, prodavnica, hodnik', 'Napolje', 'dvorište, prilaz, manji objekti')
      + rowscene('c', 'Kućište', 'Plastika', 'bez deklarisane IP zaštite', 'Metal', 'IP66: prašina i voda',
                 '<div class="abs note" id="cn" style="left:80px;top:1150px;width:920px">Obe: IR do 20 m, idu na DVR ili XVR, ne na NVR.</div>')
      + rowscene('d', 'Cena', '3.590', 'RSD sa PDV-om', '4.150', 'RSD sa PDV-om',
                 '<div class="abs h1" id="dq" style="left:0;width:1080px;text-align:center;top:1160px;font-size:76px">Napiši u komentar: <span class="green">A ili B?</span></div>'),
  js='''function rowS(p,t,a){pop($(p+'h'),t,a,{dx:-90,dy:0,s0:1});pop($(p+'A'),t,a+.4,{dx:-300,dy:0,s0:.95,ry0:-30});pop($(p+'B'),t,a+.9,{dx:300,dy:0,s0:.95,ry0:30});}
function renderF(t){
  if(t<3.6){fly($('aA'),t,.05,{x0:-700,y0:0,r0:-12});fly($('aB'),t,.35,{x0:700,y0:0,r0:12});
    if(t>.6){$('aA').style.transform+=` translateY(${Math.sin(t*2.3)*7}px)`;$('aB').style.transform+=` translateY(${Math.sin(t*2.3+1.5)*7}px)`;}
    const q=P(t,1.0,.3);tf($('vs'),{s:lerp(3,1,eoc(q))+.04*Math.sin(t*6),o:clamp(q*3,0,1),r:lerp(-90,0,eoc(q))});
    pop($('a3'),t,1.6,{dy:40,s0:.9});pop($('a4'),t,2.1,{dy:20,s0:1});}
  if(t>=3.4&&t<8.1){rowS('b',t,3.6);pop($('bA2'),t,5.5,{dy:30,s0:.9});pop($('bB2'),t,6.0,{dy:30,s0:.9});}
  if(t>=7.9&&t<11.6){rowS('c',t,8.1);pop($('cn'),t,9.8,{dy:30,s0:1});}
  if(t>=11.4&&t<15.6){rowS('d',t,11.6);
    const a=count(t,12.0,.9,3590),b=count(t,12.5,.9,4150);$('dAv').textContent=fmt(a);$('dBv').textContent=fmt(b);
    const q=P(t,13.2,.4);tf($('dq'),{s:lerp(1.5,1,eoc(q))+.03*Math.sin(t*5),o:clamp(q*3,0,1)});}
}''',
  pops=[.05, .35, 1.6, 2.1, 3.6, 4.0, 4.5, 5.5, 6.0, 8.1, 8.5, 9.0, 9.8, 11.6, 12.0, 12.5], impacts=[1.0, 13.2])

IMGS = {'b2b': {'cam1.jpg': 'thc-t150-p-hilook-turbo-hd-turret-kamera-5mp-unutrasnja.jpg',
                'cam2.jpg': 'thc-b150-m-hilook-turbo-hd-bullet-kamera-5mp-2-8mm.jpg', 'dvr.jpg': '10405-1.jpg'},
        'cam': {'cam1.jpg': 'thc-t150-p-hilook-turbo-hd-turret-kamera-5mp-unutrasnja.jpg',
                'cam2.jpg': 'thc-b150-m-hilook-turbo-hd-bullet-kamera-5mp-2-8mm.jpg'}}
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
    if k == 'b2b':  # CTA kartica umesto cene
        rep = [
          ('style="left:255px;top:6px;width:410px;height:360px;object-fit:contain"', 'style="left:330px;top:40px;width:260px;height:260px;object-fit:contain"'),
          ('padding:8px 28px">Na stanju</div>', 'padding:8px 28px">B2B portal · firme i instalateri</div>'),
          ('<span>RSD</span><span style="font-size:34px;color:#5d6b64;font-weight:500;letter-spacing:0">sa PDV-om</span>',
           '<span style="font-size:40px;color:#123528;font-weight:700;letter-spacing:0">artikala na lageru</span>'),
          ('>Dodaj u korpu</div>', '>Registruj firmu</div>'),
          ("$('sPbt').textContent=done?'✓  Dodato u korpu':'Dodaj u korpu'", "$('sPbt').textContent=done?'✓  b2b.super-vision.rs':'Registruj firmu'"),
          ('<div class="abs" id="sPfinger"', '<div class="abs note" id="sPtel" style="left:80px;top:1410px;width:920px;font-size:38px;font-weight:600;color:#fff">Pitanja: <span class="green">062/618-736</span></div>\n    <div class="abs" id="sPfinger"'),
          ("pop($('sPinc'),t,16.5,{dy:30,s0:.9});", "pop($('sPinc'),t,16.5,{dy:30,s0:.9});pop($('sPtel'),t,16.8,{dy:30,s0:1});"),
        ]
        for a, b in rep:
            assert a in h, a
            h = h.replace(a, b)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
    json.dump({'style': f['style'], 'key': f['key'], 'seed': f['seed']}, open(os.path.join(out, 'music.json'), 'w'))
print('ok')
