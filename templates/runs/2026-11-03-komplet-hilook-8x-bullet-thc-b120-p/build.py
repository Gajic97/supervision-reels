"""Gradi 2 reela za 03.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
import json, os, sys, shutil
GEN = os.path.expanduser('~/sr/templates/formati-demo/gen.py')
src = open(GEN, encoding='utf-8').read()
head, build = src.split('# ---------------------------------------------------------------- build')
g = {'__file__': GEN}
exec(head, g)
exec(build.split('for k, f in F.items():')[0], g)
hook, BASE, sfx_for, numscene = g['hook'], g['BASE'], g['sfx_for'], g['numscene']

FONTS = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};src:url(assets/fonts/poppins-{s}-{w}-normal.woff2) format('woff2');unicode-range:{r}}}"
    for w in (400, 500, 600, 700, 800)
    for s, r in (('latin', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD,U+2713,U+2715'),
                 ('latin-ext', 'U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF')))

R = {}

# ============================================================ KOMPLET (f3, 3 stvari)
MINI = ''.join(f'<div class="tile" id="m{i}" style="left:{80 + (i % 4) * 240}px;top:{640 + (i // 4) * 240}px;width:200px;height:200px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:190px;height:190px"></div>' for i in range(8))
R['kit'] = dict(
  tag='PRE NEGO ŠTO KUPIŠ', hook=hook('Komplet video nadzora za 8 kamera: 3 stvari.', (0, 1, 2), 2), hsize=112, subtop=1150,
  sub='Odbrojavamo od 3 do 1.', p=('Komplet video', 'nadzora · 8 kamera'),
  inc='✓  Uštedite u kompletu 15.920 RSD (30%)', price='37.100', img='assets/kit.jpg',
  scn=[['a', 0, 4], ['b', 4, 8], ['c', 8, 12], ['d', 12, 15.5]],
  slams=[0, 4, 8, 12, 15.5, 18.5],
  html=numscene('a', 3, '8 kamera<br><span class="green" style="white-space:nowrap">THC-B120-P</span>', '2 MP, infracrveno do 20 m, kućište IP66.', MINI)
    + numscene('b', 2, 'Snimač sa <span class="green">8 kanala</span>', 'DVR-108G-M1/T, H.265 Pro+. Prima i do 2 IP kamere.',
      '<div class="tile" id="bm1" style="left:240px;top:620px;width:600px;height:560px"><img src="assets/dvr.jpg" style="left:30px;top:10px;width:540px;height:540px"></div><div class="chip" id="bm2" style="left:700px;top:580px;background:#2f7a50">8 CH</div>')
    + numscene('c', 1, 'Disk <span class="green">2 TB</span> već u kutiji', 'WD Purple. Snimač prima disk do 4 TB.',
      '<div class="tile" id="cm1" style="left:290px;top:640px;width:500px;height:500px"><img src="assets/hdd.webp" style="left:25px;top:25px;width:450px;height:450px"></div><div class="chip" id="cm2" style="left:660px;top:600px;background:#2f7a50">2 TB</div>')
    + '''
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:104px">Ovaj ima</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:300px;font-size:104px">sve tri.</div>
    <div class="tile" id="d3" style="left:80px;top:450px;width:440px;height:440px"><img src="assets/kit.jpg" style="left:10px;top:10px;width:420px;height:420px"></div>
    <div class="row" id="r1" style="top:960px"><span class="chk">✓</span>8 kamera 2 MP</div>
    <div class="row" id="r2" style="top:1060px"><span class="chk">✓</span>Snimač 8 kanala</div>
    <div class="row" id="r3" style="top:1160px"><span class="chk">✓</span>Disk 2 TB</div>
    <div class="abs" id="d4" style="left:560px;top:500px;width:440px;font-size:38px;font-weight:700;line-height:1.3">HiLook<br><span class="green">8× THC-B120-P</span><br>+ DVR-108G-M1/T<br><span style="font-size:30px;color:#c9dbd0;font-weight:500">uz napajanje 6 A i konektore</span></div>
  </div>''',
  js='''function numS(p,t,a){const n=$(p+'n');const q=P(t,a,.35);tf(n,{s:lerp(2.2,1,eoc(q)),o:clamp(q*3,0,1),r:lerp(-12,0,eoc(q))});n.style.textShadow=`0 0 ${40*(1-q)}px #6cc08f`;
  pop($(p+'t'),t,a+.35,{dx:90,dy:0,s0:1});pop($(p+'s'),t,a+1.6,{dy:24,s0:1});}
function renderF(t){
  if(t<4.1){numS('a',t,0);for(let i=0;i<8;i++){const el=$('m'+i);fly(el,t,.7+i*.12,{y0:-700,r0:(i%2?20:-20),d:.45});if(t>1.6+i*.12)el.style.transform+=` translateY(${Math.sin(t*2.4+i)*5}px)`;}}
  if(t>=3.9&&t<8.1){numS('b',t,4);fly($('bm1'),t,4.7,{x0:-700,y0:0,r0:-12,d:.55});if(t>5.3)$('bm1').style.transform+=` translateY(${Math.sin(t*2.2)*8}px)`;slam($('bm2'),t,5.3,{s0:2});$('bm2').style.transform+=` rotate(${Math.sin(t*3)*4}deg)`;}
  if(t>=7.9&&t<12.1){numS('c',t,8);fly($('cm1'),t,8.7,{y0:600,r0:15});if(t>9.3)$('cm1').style.transform+=` translateY(${Math.sin(t*2.2)*8}px)`;slam($('cm2'),t,9.3,{s0:2});$('cm2').style.transform+=` rotate(${Math.sin(t*3)*4}deg)`;}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});slam($('d2'),t,12.35);pop($('d3'),t,12.3,{dy:200,s0:.8,d:.5});if(t>12.9)$('d3').style.transform+=` translateY(${Math.sin(t*2)*7}px)`;pop($('d4'),t,12.6,{dx:80,dy:0,s0:1});
    ['r1','r2','r3'].forEach((id,i)=>{pop($(id),t,13+i*.45,{dx:-60,dy:0,s0:1});const c=$(id).firstElementChild;const q=eob(P(t,13.15+i*.45,.3));c.style.transform=`scale(${q})`;});}
}''',
  pops=[.35, .7, 1.1, 1.5, 4.35, 4.7, 8.35, 8.7, 12.05, 12.6, 13, 13.45, 13.9], impacts=[0, 4, 5.3, 8, 9.3, 12.35],
  extra=[('tap', 13.15, .4), ('tap', 13.6, .4), ('tap', 14.05, .4), ('confirm', 14.1, .2)])

# ============================================================ KAMERA (f8, Greška pre kupovine)
R['c8c'] = dict(
  tag='WI-FI KAMERA ZA DVORIŠTE', hook=hook('Pre nego što kupiš Wi-Fi kameru, proveri struju.', (4, 5, 7), 7), hsize=112, subtop=1150,
  sub='Wi-Fi ne znači bez kabla za struju.', p=('Wi-Fi kamera', 'za dvorište'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='10.530', img='assets/cam.jpg',
  scn=[['a', 0, 4], ['b', 4, 8], ['c', 8, 12], ['d', 12, 15.5]],
  slams=[0, 2.0, 4, 8, 12, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Greška:</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:92px">„Wi-Fi je bez struje.”</div>
    <div class="tile" id="aA" style="left:80px;top:500px;width:440px;height:440px"><img src="assets/cam.jpg" style="left:10px;top:10px;width:420px;height:420px"></div>
    <div class="abs" id="aB" style="left:580px;top:560px;width:420px;height:320px;border-radius:34px;background:rgba(255,255,255,.06);border:5px dashed #ff8a80;display:flex;flex-direction:column;align-items:center;justify-content:center">
      <svg width="200" height="120" viewBox="0 0 200 120"><rect x="10" y="20" width="160" height="80" rx="14" fill="none" stroke="#ff8a80" stroke-width="10"/><rect x="170" y="45" width="20" height="30" rx="4" fill="#ff8a80"/><rect id="batf" x="24" y="34" width="40" height="52" rx="6" fill="#ff8a80"/></svg>
      <div style="font-size:44px;font-weight:800;color:#ff8a80;margin-top:10px">baterija</div></div>
    <div class="abs" id="ax" style="left:740px;top:440px;width:110px;height:110px;border-radius:50%;background:#d64545;border:6px solid #fff;display:flex;align-items:center;justify-content:center;font-size:70px;font-weight:800">✕</div>
    <div class="abs sub" id="a3" style="left:80px;top:1010px;width:920px">EZVIZ C8C ne radi na bateriju.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">Treba joj</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">utičnica.</div>
    <svg class="abs" id="pw" style="left:80px;top:460px" width="920" height="260" viewBox="0 0 920 260">
      <g transform="translate(70 130)"><rect x="-60" y="-80" width="120" height="160" rx="24" fill="#fff"/><circle cx="-22" cy="-10" r="11" fill="#123528"/><circle cx="22" cy="-10" r="11" fill="#123528"/></g>
      <path id="cx" d="M140 130 C 340 20, 560 240, 790 130" fill="none" stroke="#6cc08f" stroke-width="14" stroke-linecap="round" stroke-dasharray="1000" stroke-dashoffset="1000"/>
      <circle id="cxd" r="14" fill="#fff"/>
      <g transform="translate(850 130)"><circle r="62" fill="#fff"/><circle r="30" fill="#123528"/><circle r="12" fill="#6cc08f"/></g>
    </svg>
    <div class="chip" id="c1x" style="left:80px;top:770px">DC 12 V / 1 A</div>
    <div class="chip" id="c2x" style="left:470px;top:770px">do 12 W</div>
    <div class="chip" id="c3x" style="left:80px;top:880px">Wi-Fi 2,4 GHz</div>
    <div class="chip" id="c4x" style="left:470px;top:880px">ili kabl RJ45</div>
    <div class="abs sub" id="b3" style="left:80px;top:1030px;width:920px">Predvidi utičnicu kod mesta montaže.</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="cc1" style="left:80px;top:190px;font-size:104px">Zauzvrat:</div>
    <div class="abs h1 green" id="cc2" style="left:80px;top:300px;font-size:92px">jedna umesto dve.</div>
    <svg class="abs" id="ring" style="left:190px;top:450px" width="700" height="700" viewBox="-350 -350 700 700">
      <defs><radialGradient id="cg" cx="0" cy="0" r="1"><stop offset="0" stop-color="#6cc08f" stop-opacity=".55"/><stop offset="1" stop-color="#6cc08f" stop-opacity="0"/></radialGradient></defs>
      <path id="cone" d="M0 0 L-150 -300 A335 335 0 0 1 150 -300 Z" fill="url(#cg)"/>
      <circle r="300" fill="none" stroke="rgba(108,192,143,.25)" stroke-width="6"/>
      <circle id="ringp" r="300" fill="none" stroke="#6cc08f" stroke-width="10" stroke-linecap="round" stroke-dasharray="1885" stroke-dashoffset="1885" transform="rotate(-90)"/>
      <circle id="rdot" r="20" fill="#fff"/>
    </svg>
    <div class="disc" id="cd" style="left:340px;top:600px;width:400px;height:400px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:360px;height:360px"></div>
    <div class="chip" id="cc3" style="left:80px;top:1190px">4K · 3840 × 2160</div>
    <div class="chip" id="cc4" style="left:560px;top:1190px">sama prati pokret</div>
    <div class="abs note" id="cc5" style="left:80px;top:1300px;width:920px">Objektiv se okreće daljinski. AI prepoznaje čoveka i vozilo.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Pre kupovine</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">proveri:</div>
    <div class="row" id="r1" style="top:500px"><span class="chk">1</span><span>Struja <span class="green">· DC 12 V / 1 A</span></span></div>
    <div class="row" id="r2" style="top:640px"><span class="chk">2</span><span>Mreža <span class="green">· Wi-Fi 2,4 GHz ili RJ45</span></span></div>
    <div class="row" id="r3" style="top:780px"><span class="chk">3</span><span>Noću <span class="green">· IR 30 m, belo svetlo 20 m</span></span></div>
    <div class="row" id="r4" style="top:920px"><span class="chk">4</span><span>Snimci <span class="green">· microSD do 512 GB</span></span></div>
    <div class="abs note" id="d3" style="left:80px;top:1090px;width:920px">Vrednosti za EZVIZ C8C, kućište IP65.</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.1){pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.4);
    fly($('aA'),t,.6,{x0:-600,y0:0,r0:-15});fly($('aB'),t,.9,{x0:600,y0:0,r0:15});
    if(t>1.6)$('aA').style.transform+=` translateY(${Math.sin(t*2.4)*8}px)`;
    $('batf').setAttribute('width',String(Math.max(4,40*(1-P(t,1.2,.8)))));
    const s=Math.sin(t*14)*6*(t>2.0&&t<2.6?1:0);$('aB').style.transform+=` translateX(${s}px)`;
    slam($('ax'),t,2.0,{s0:2.4});$('ax').style.transform+=` rotate(${Math.sin(t*5)*8}deg)`;pop($('a3'),t,2.6,{dy:24,s0:1});}
  if(t>=3.9&&t<8.1){pop($('b1'),t,4.1,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.4);pop($('pw'),t,4.5,{dy:40,s0:.9});
    const cp=eio(P(t,4.8,1.0));$('cx').style.strokeDashoffset=String(1000*(1-cp));const path=$('cx');const L=path.getTotalLength();const pt=path.getPointAtLength(L*cp);$('cxd').setAttribute('cx',pt.x);$('cxd').setAttribute('cy',pt.y);$('cxd').style.opacity=cp>0&&cp<1?1:0;
    ['c1x','c2x','c3x','c4x'].forEach((id,i)=>{pop($(id),t,5.4+i*.3,{dy:60,s0:.7});if(t>5.9+i*.3)$(id).style.transform+=` translateY(${Math.sin(t*3+i)*5}px)`;});
    pop($('b3'),t,6.8,{dy:24,s0:1});}
  if(t>=7.9&&t<12.1){pop($('cc1'),t,8.1,{dx:-90,dy:0,s0:1});slam($('cc2'),t,8.4);
    const rp=eio(P(t,8.6,.9));$('ringp').style.strokeDashoffset=String(1885*(1-rp));tf($('ring'),{s:lerp(.7,1,eoc(P(t,8.5,.5))),o:clamp((t-8.5)*3,0,1)});
    const ang=Math.sin((t-8.6)*1.3)*70;$('cone').setAttribute('transform',`rotate(${ang})`);const ra=(ang-90)*Math.PI/180;$('rdot').setAttribute('cx',String(300*Math.cos(ra)));$('rdot').setAttribute('cy',String(300*Math.sin(ra)));
    {const hp=P(t,8.6,.6),he=eob(hp);tf($('cd'),{s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-60,0,eoc(hp))+ang*.25,y:Math.sin(t*2)*6});}
    pop($('cc3'),t,9.7,{dy:40,s0:.8});pop($('cc4'),t,10.1,{dy:40,s0:.8});pop($('cc5'),t,10.6,{dy:20,s0:1});}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.25,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4'].forEach((id,i)=>{pop($(id),t,12.7+i*.5,{dx:-80,dy:0,s0:1});const c=$(id).firstElementChild;c.style.transform=`scale(${eob(P(t,12.85+i*.5,.3))})`;});pop($('d3'),t,14.8,{dy:20,s0:1});}
}''',
  pops=[.05, .6, .9, 2.6, 4.1, 4.5, 5.4, 5.7, 6.0, 6.3, 6.8, 8.1, 9.7, 10.1, 10.6, 12.05, 12.25, 12.7, 13.2, 13.7, 14.2], impacts=[.4, 2.0, 4.4, 8.4],
  extra=[('riser', 4.8, .1, 1.0), ('riser', 8.6, .1, .9)])

FD = os.path.expanduser('~/work/fonts/package/files')
for k in sys.argv[1:] or R:
    f = R[k]; out = os.path.expanduser(f'~/work/{k}')
    os.makedirs(os.path.join(out, 'assets', 'fonts'), exist_ok=True)
    for w in (400, 500, 600, 700, 800):
        for s in ('latin', 'latin-ext'):
            shutil.copy(f'{FD}/poppins-{s}-{w}-normal.woff2', os.path.join(out, 'assets', 'fonts'))
    shutil.copy(os.path.expanduser('~/sr/templates/reel-v4/assets/supervision-ikonica-512.png'), os.path.join(out, 'assets'))
    h = BASE.replace('<style>', '<style>' + FONTS, 1)
    for tok, val in [('%%TAG%%', f['tag']), ('%%HOOK%%', f['hook']), ('%%HSIZE%%', str(f['hsize'])), ('%%SUBTOP%%', str(f['subtop'])),
                     ('%%SUB%%', f['sub']), ('%%SCENES%%', f['html']), ('%%P1%%', f['p'][0]), ('%%P2%%', f['p'][1]),
                     ('%%INC%%', f['inc']), ('%%PRICE%%', f['price']),
                     ('%%SCN%%', json.dumps(f['scn'])), ('%%SLAMS%%', json.dumps(f['slams'])), ('%%JS%%', f['js'])]:
        h = h.replace(tok, val)
    h = h.replace('src="assets/kit.jpg"', f'src="{f["img"]}"')
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
print('ok')
