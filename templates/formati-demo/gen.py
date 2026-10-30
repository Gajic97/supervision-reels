"""Pravi 8 demo formata za komplet HiLook 4x turret THC-T120-P + DVR-104G-K1 (id 2939)."""
import json, os, shutil
D = os.path.dirname(os.path.abspath(__file__))
BASE = open(os.path.join(D, 'base.html'), encoding='utf-8').read()
IMG = {'kit.jpg': 'komplet-video-nadzora-hilook-4-turret-thc-t120-p-dvr-104g-k1.jpg', 'cam.jpg': '444.jpg', 'dvr.jpg': '10405.jpg',
       'hdd.webp': 'px-3861-1.webp', 'ipkit.jpg': 'komplet-video-nadzora-hilook-4-turret-ip-ipc-t220ha-luc-nvr-104h-d.jpg'}
LOGO = '/home/claude/repo/templates/reel-v4/assets/supervision-ikonica-512.png'

def hook(text, green=(), mark=None):
    out = []
    for i, w in enumerate(text.split()):
        cls = 'w green' if i in green else 'w'
        mk = '<i class="mark" id="mk"></i>' if i == mark else ''
        out.append(f'<span class="{cls}">{w}{mk}</span>')
    return ' '.join(out)

F = {}

# ---------------------------------------------------------------- 1 PRIKAZ PROIZVODA
F['f1'] = dict(name='Prikaz proizvoda', style='deep_house', key=2,
  tag='KOMPLET VIDEO NADZORA', hook=hook('4 kamere, snimač i disk. Jedna kutija.', (5, 6), 6), hsize=118, subtop=1180,
  sub='Bez naknadnog usklađivanja delova.', p=('Ceo plac', 'na oku'),
  scn=[['a', 0, 3.5], ['b', 3.5, 8.5], ['c', 8.5, 13], ['d', 13, 15.5]],
  slams=[0, .5, 3.5, 8.5, 13, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:120px;transform-origin:0 50%">KOMPLET</div>
    <div class="abs h1 green" id="a2" style="left:80px;top:315px;font-size:120px;transform-origin:0 50%">4 KAMERE</div>
    <svg class="abs" id="ring" style="left:140px;top:470px" width="800" height="800" viewBox="-400 -400 800 800">
      <circle r="330" fill="none" stroke="rgba(108,192,143,.25)" stroke-width="6"/>
      <circle id="ringp" r="330" fill="none" stroke="#6cc08f" stroke-width="10" stroke-linecap="round" stroke-dasharray="2073" stroke-dashoffset="2073" transform="rotate(-90)"/>
      <g id="dots"><circle cx="0" cy="-330" r="22" fill="#fff"/><circle cx="330" cy="0" r="22" fill="#fff"/><circle cx="0" cy="330" r="22" fill="#fff"/><circle cx="-330" cy="0" r="22" fill="#fff"/></g>
    </svg>
    <div class="disc" id="hero" style="left:250px;top:580px;width:580px;height:580px"><img src="assets/kit.jpg" style="left:40px;top:40px;width:500px;height:500px"></div>
    <div class="abs h1" id="a3" style="left:0;width:1080px;text-align:center;top:1330px;font-size:58px;letter-spacing:-1px"><span class="green">HiLook komplet</span> za kuću</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b0" style="left:80px;top:190px;font-size:110px">ŠTA DOBIJAŠ?</div>
    <div class="card feat" id="b1c" style="top:360px"><div class="ic"><img src="assets/dvr.jpg"></div><div class="st"><b>Usklađeno odmah</b><span>kamere i snimač iz jedne kutije</span></div></div>
    <div class="card feat" id="b2c" style="top:680px"><div class="ic"><svg width="170" height="170" viewBox="-85 -85 170 170"><rect x="-38" y="-70" width="76" height="140" rx="14" fill="#123528"/><rect x="-30" y="-56" width="60" height="100" rx="4" fill="#6cc08f"/><circle id="bdot" cx="0" cy="-6" r="10" fill="#fff"/></svg></div><div class="st"><b>Slika na telefonu</b><span>Hik-Connect aplikacija</span></div></div>
    <div class="card feat" id="b3c" style="top:1000px"><div class="ic"><svg width="170" height="170" viewBox="-85 -85 170 170"><rect x="-70" y="-50" width="140" height="90" rx="10" fill="#123528"/><rect id="bscr" x="-60" y="-40" width="120" height="70" rx="4" fill="#6cc08f"/><rect x="-12" y="40" width="24" height="16" fill="#123528"/><rect x="-36" y="54" width="72" height="8" rx="4" fill="#123528"/></svg></div><div class="st"><b>HDMI i VGA</b><span>slika na monitoru ili TV-u</span></div></div>
  </div>
  <div class="scene" id="c">
    <div class="abs tag" id="c0" style="left:80px;top:190px;font-size:38px;letter-spacing:3px">THC-T120-P + DVR-104G-K1</div>
    <div class="gauge" id="g1" style="left:80px;top:270px"><svg viewBox="-60 -60 120 120"><circle r="50" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="9"/><circle id="ga1" r="50" fill="none" stroke="#6cc08f" stroke-width="9" stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="314" transform="rotate(-90)"/></svg><div class="gv" id="gv1">2 MP</div><div class="gl">Slika</div><div class="gs">1920 × 1080</div></div>
    <div class="gauge" id="g2" style="left:555px;top:270px"><svg viewBox="-60 -60 120 120"><circle r="50" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="9"/><circle id="ga2" r="50" fill="none" stroke="#6cc08f" stroke-width="9" stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="314" transform="rotate(-90)"/></svg><div class="gv" id="gv2">0 m</div><div class="gl">Vidi i noću</div><div class="gs">infracrveno</div></div>
    <div class="gauge" id="g3" style="left:80px;top:730px"><svg viewBox="-60 -60 120 120"><circle r="50" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="9"/><circle id="ga3" r="50" fill="none" stroke="#6cc08f" stroke-width="9" stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="314" transform="rotate(-90)"/></svg><div class="gv" id="gv3">1 TB</div><div class="gl">Disk u kompletu</div><div class="gs">snimač prima do 4 TB</div></div>
    <div class="gauge" id="g4" style="left:555px;top:730px"><svg viewBox="-60 -60 120 120"><circle r="50" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="9"/><circle id="ga4" r="50" fill="none" stroke="#6cc08f" stroke-width="9" stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="314" transform="rotate(-90)"/></svg><div class="gv" id="gv4">0</div><div class="gl">Kanala</div><div class="gs">H.265 Pro+</div></div>
    <div class="abs note" id="c5" style="left:80px;top:1200px;width:920px;font-size:31px">Kućište IP66, radi od −40 do +60 °C.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Ulaz, prilaz</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">i dve strane</div>
    <svg class="abs" id="map" style="left:80px;top:450px" width="920" height="760" viewBox="0 0 920 760">
      <defs><radialGradient id="cg" cx="0" cy="0" r="1"><stop offset="0" stop-color="#6cc08f" stop-opacity=".65"/><stop offset="1" stop-color="#6cc08f" stop-opacity="0"/></radialGradient></defs>
      <rect x="20" y="20" width="880" height="720" rx="26" fill="rgba(255,255,255,.04)" stroke="#439665" stroke-width="5"/>
      <rect x="300" y="230" width="320" height="300" rx="12" fill="rgba(255,255,255,.12)" stroke="#c9dbd0" stroke-width="4"/><text x="460" y="390" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="40" fill="#fff">KUĆA</text>
      <rect x="420" y="530" width="80" height="210" fill="rgba(255,255,255,.07)"/><text x="460" y="700" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="26" fill="#c9dbd0">prilaz</text>
      <g class="cam" id="k1" transform="translate(460 530)"><path d="M0 0 L-170 210 L170 210 Z" fill="rgba(108,192,143,.30)"/><circle r="22" fill="#fff" stroke="#2f7a50" stroke-width="7"/></g>
      <g class="cam" id="k2" transform="translate(300 300)"><path d="M0 0 L-260 -180 L-260 180 Z" fill="rgba(108,192,143,.30)"/><circle r="22" fill="#fff" stroke="#2f7a50" stroke-width="7"/></g>
      <g class="cam" id="k3" transform="translate(620 300)"><path d="M0 0 L260 -180 L260 180 Z" fill="rgba(108,192,143,.30)"/><circle r="22" fill="#fff" stroke="#2f7a50" stroke-width="7"/></g>
      <g class="cam" id="k4" transform="translate(460 230)"><path d="M0 0 L-180 -190 L180 -190 Z" fill="rgba(108,192,143,.30)"/><circle r="22" fill="#fff" stroke="#2f7a50" stroke-width="7"/></g>
    </svg>
    <div class="abs note" id="d3" style="left:80px;top:1230px;width:920px">Primer rasporeda 4 kamere.</div>
  </div>''',
  js='''function renderF(t){
  if(t<3.6){slam($('a1'),t,0,{s0:1.6,d:.22});slam($('a2'),t,.5,{s0:1.6,d:.22});
    const hp=P(t,.15,.6),he=eob(hp);tf($('hero'),{y:lerp(380,0,he)+Math.sin(t*2.2)*12,s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-70,0,eoc(hp))+Math.sin(t*1.6)*8});
    const rp=eio(P(t,.6,1.6));$('ringp').style.strokeDashoffset=String(2073*(1-rp));$('ring').style.opacity=clamp((t-.5)*4,0,1);
    [...$('dots').children].forEach((c,i)=>{const p=eob(P(t,.8+i*.35,.3));c.setAttribute('r',String(22*p));});
    $('dots').setAttribute('transform',`rotate(${t*12})`);pop($('a3'),t,2.0,{dy:40,s0:.9,d:.35});}
  if(t>=3.4&&t<8.6){pop($('b0'),t,3.55,{dx:-90,dy:0,s0:1});
    ['b1c','b2c','b3c'].forEach((id,i)=>pop($(id),t,4+i,{dx:200,dy:0,s0:.95,d:.42,ry0:-35}));
    $('bdot').setAttribute('r',String(10+6*Math.abs(Math.sin(t*4))));$('bscr').setAttribute('fill',Math.floor(t*2)%2?'#6cc08f':'#439665');}
  if(t>=8.4&&t<13.1){pop($('c0'),t,8.55,{dx:-60,dy:0,s0:1});
    [[9,1],[9.7,.8],[10.4,.25],[11.1,1]].forEach(([a,f],i)=>{pop($('g'+(i+1)),t,a,{dy:80,s0:.8,d:.4});const p=gauge('ga'+(i+1),t,a+.15,f);
      if(i==1)$('gv2').textContent=Math.round(p*20)+' m';if(i==3)$('gv4').textContent=Math.round(p*4);});
    pop($('c5'),t,11.8,{dy:24,s0:1});}
  if(t>=12.9&&t<15.6){pop($('d1'),t,13.05,{dx:-90,dy:0,s0:1});pop($('d2'),t,13.25,{dx:-90,dy:0,s0:1});
    {const p=P(t,13.1,.4);$('map').style.opacity=p;}
    ['k1','k2','k3','k4'].forEach((id,i)=>{const p=eob(P(t,13.4+i*.3,.35));const g=$(id);g.style.opacity=clamp(p*2,0,1);g.querySelector('path').style.transform=`scale(${p})`;g.querySelector('path').style.transformOrigin='0 0';});
    pop($('d3'),t,14.6,{dy:20,s0:1});}
}''',
  pops=[3.55, 4, 5, 6, 8.55, 9, 9.7, 10.4, 11.1, 13.05, 13.4, 13.7, 14, 14.3], impacts=[0, 3.5, 13])

# ---------------------------------------------------------------- 2 PROBLEM -> RESENJE
NIGHT_YARD = '''<svg class="abs" id="%s" style="left:80px;top:420px" width="920" height="820" viewBox="0 0 920 820">
      <rect x="0" y="0" width="920" height="820" rx="30" fill="#07120d"/>
      <circle cx="760" cy="130" r="56" fill="#e9f3ec" opacity=".85"/><circle cx="782" cy="114" r="52" fill="#07120d"/>
      <path d="M120 520 L120 330 L300 210 L480 330 L480 520 Z" fill="#14261d" stroke="#28463a" stroke-width="5"/>
      <rect x="260" y="400" width="80" height="120" fill="#0b1a14" stroke="#28463a" stroke-width="4"/>
      <rect x="370" y="360" width="70" height="60" fill="#e8c46a" opacity=".55"/>
      <path d="M0 640 L920 640" stroke="#1e3a2d" stroke-width="6"/>
      <g stroke="#1e3a2d" stroke-width="10">%s</g>
      <circle cx="700" cy="560" r="80" fill="#10241a"/><rect x="690" y="560" width="20" height="90" fill="#10241a"/>
      %s
    </svg>'''
fence = ''.join(f'<line x1="{x}" y1="600" x2="{x}" y2="700"/>' for x in range(520, 920, 40))
F['f2'] = dict(name='Problem → rešenje', style='cinematic', key=5,
  tag='VLASNICI KUĆE', hook=hook('Pas je lajao celu noć. Na šta?', (5, 6), 6), hsize=128, subtop=1060,
  sub='Ujutru samo nagađaš.', p=('Više ne', 'nagađaš'),
  scn=[['a', 0, 4.5], ['b', 4.5, 9], ['c', 9, 12.5], ['d', 12.5, 15.5]],
  slams=[0, 4.5, 9, 12.5, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Bez kamere:</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:104px">samo nagađaš.</div>
    ''' + NIGHT_YARD % ('ya', fence, '<g id="qs" font-family="Poppins" font-weight="800" font-size="110" fill="#ff7b7b"><text id="q1" x="560" y="300">?</text><text id="q2" x="660" y="420">?</text><text id="q3" x="200" y="620">?</text></g>') + '''
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">Sa kamerom:</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">vidiš i noću.</div>
    ''' + NIGHT_YARD % ('yb', fence, '''<defs><radialGradient id="ir" cx="0" cy="0" r="1"><stop offset="0" stop-color="#cfe9da" stop-opacity=".55"/><stop offset="1" stop-color="#cfe9da" stop-opacity="0"/></radialGradient></defs>
      <path id="beam" d="M480 340 L920 560 L920 820 L560 820 Z" fill="url(#ir)" opacity="0"/>
      <g id="cat" transform="translate(1000 700)"><ellipse cx="0" cy="0" rx="62" ry="30" fill="#dfeee5"/><circle cx="58" cy="-26" r="24" fill="#dfeee5"/><path d="M44 -44 l6 -22 l12 18 z M66 -46 l10 -20 l8 22 z" fill="#dfeee5"/><path d="M-60 -6 q-40 -30 -30 -70" stroke="#dfeee5" stroke-width="10" fill="none" stroke-linecap="round"/><rect x="-46" y="20" width="12" height="34" rx="6" fill="#dfeee5"/><rect x="30" y="20" width="12" height="34" rx="6" fill="#dfeee5"/></g>
      <g transform="translate(480 340)"><circle r="26" fill="#fff" stroke="#2f7a50" stroke-width="8"/><circle id="led" r="9" fill="#6cc08f"/></g>''') + '''
    <div class="chip" id="b3" style="left:80px;top:1270px">IR do 20 m</div>
    <div class="abs h1" id="b4" style="left:420px;top:1272px;font-size:64px">Mačka. <span class="green">Opet.</span></div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">Premotaš</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:104px">na telefonu.</div>
    <div class="phone" id="ph" style="left:260px;top:440px"><div class="scr">
      <div class="abs" style="left:30px;top:50px;font-size:28px;font-weight:700;color:#c9dbd0">Dvorište · snimak</div>
      <svg class="abs" style="left:0;top:110px" width="532" height="400" viewBox="0 0 532 400"><rect width="532" height="400" fill="#1d2622"/><rect y="300" width="532" height="100" fill="#26322c"/><g id="pcat" fill="#e6eee9"><ellipse cx="0" cy="300" rx="44" ry="20"/><circle cx="40" cy="282" r="17"/></g><text x="20" y="380" font-family="Poppins" font-weight="700" font-size="30" fill="#fff" id="ts">02:14</text></svg>
      <div class="abs" style="left:30px;top:560px;width:472px;height:12px;border-radius:6px;background:#2c3a33"><div id="tl" style="height:12px;border-radius:6px;background:#6cc08f;width:20%"></div><div id="kn" class="abs" style="top:-12px;width:36px;height:36px;border-radius:50%;background:#fff"></div></div>
      <div class="abs" style="left:30px;top:620px;font-size:26px;color:#9db5aa">00:00</div><div class="abs" style="left:420px;top:620px;font-size:26px;color:#9db5aa">06:00</div>
    </div></div>
    <div class="abs note" id="c3" style="left:80px;top:1290px;width:920px">Hik-Connect aplikacija. Prikaz je ilustracija.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">4 kamere oko</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">cele kuće</div>
    <div class="tile" id="d3" style="left:180px;top:450px;width:720px;height:620px"><img src="assets/kit.jpg" style="left:60px;top:10px;width:600px;height:600px"></div>
    <div class="chip" id="d4" style="left:80px;top:1130px">2 MP</div>
    <div class="chip" id="d5" style="left:300px;top:1130px">Disk 1 TB</div>
    <div class="chip" id="d6" style="left:610px;top:1130px">IP66</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.6){$('dark').style.opacity=.8;pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.5);
    {const p=P(t,0,.6);$('ya').style.opacity=p;}
    ['q1','q2','q3'].forEach((id,i)=>{const p=eob(P(t,1+i*.6,.35));const el=$(id);el.style.opacity=clamp(p*2,0,1);el.style.transform=`translateY(${Math.sin(t*3+i)*8}px)`;});}
  if(t>=4.4&&t<9.1){$('dark').style.opacity=.6;pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,5.0);
    const on=P(t,5.4,.4);$('beam').style.opacity=on*(.85+.15*Math.sin(t*9));$('led').setAttribute('fill',on>0?'#d64545':'#6cc08f');
    const cx=lerp(1000,640,eio(P(t,5.9,1.8)));$('cat').setAttribute('transform',`translate(${cx} 700)`);
    pop($('b3'),t,6.2,{dy:30,s0:.9});pop($('b4'),t,7.6,{dx:60,dy:0,s0:1});}
  if(t>=8.9&&t<12.6){pop($('c1'),t,9.05,{dx:-90,dy:0,s0:1});pop($('c2'),t,9.25,{dx:-90,dy:0,s0:1});
    pop($('ph'),t,9.1,{dy:300,s0:.9,d:.5});
    const s=eio(P(t,9.8,1.8));const x=lerp(.2,.37,s);$('tl').style.width=(x*100)+'%';$('kn').style.left=(x*472-18)+'px';
    const mins=Math.round(lerp(72,134,s));$('ts').textContent=String(Math.floor(mins/60)).padStart(2,'0')+':'+String(mins%60).padStart(2,'0');
    $('pcat').setAttribute('transform',`translate(${lerp(-60,300,s)} 0)`);pop($('c3'),t,11,{dy:20,s0:1});}
  if(t>=12.4&&t<15.6){pop($('d1'),t,12.55,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.75,{dx:-90,dy:0,s0:1});
    pop($('d3'),t,12.7,{dy:200,s0:.8,d:.5,ry0:30});$('d3').style.transform+=` translateY(${Math.sin(t*2)*8}px)`;
    ['d4','d5','d6'].forEach((id,i)=>pop($(id),t,13.5+i*.3,{dy:40,s0:.7}));}
}''',
  pops=[.05, 1, 1.6, 2.2, 4.6, 6.2, 7.6, 9.05, 11, 12.55, 13.5, 13.8, 14.1], impacts=[.5, 5.0, 12.7], extra=[('riser', 5.4, .14, 1.0), ('confirm', 7.65, .2)])

# ---------------------------------------------------------------- 3 TRI STVARI
def numscene(sid, n, title, sub, media):
    return f'''
  <div class="scene" id="{sid}">
    <div class="big" id="{sid}n" style="left:60px;top:150px">{n}</div>
    <div class="abs h1" id="{sid}t" style="left:400px;top:250px;width:620px;font-size:76px;line-height:1.05">{title}</div>
    {media}
    <div class="abs sub" id="{sid}s" style="left:80px;top:1250px;width:920px">{sub}</div>
  </div>'''
F['f3'] = dict(name='3 stvari (odbrojavanje)', style='minimal_tech', key=9,
  tag='PRE NEGO ŠTO KUPIŠ', hook=hook('3 stvari koje komplet mora da ima.', (4,), 4), hsize=128, subtop=1190,
  sub='Gledaj do broja 1.', p=('Sve tri', 'u kutiji'),
  scn=[['a', 0, 4], ['b', 4, 8], ['c', 8, 12], ['d', 12, 15.5]],
  slams=[0, 4, 8, 12, 15.5, 18.5],
  html=numscene('a', 3, 'Kamere i snimač zajedno', 'Iz jedne kutije, bez naknadnog usklađivanja.',
      '<div class="tile" id="am1" style="left:110px;top:720px;width:400px;height:400px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:360px;height:360px"></div><div class="abs h1 green" id="aplus" style="left:510px;top:830px;width:60px;font-size:120px;text-align:center">+</div><div class="tile" id="am2" style="left:570px;top:720px;width:400px;height:400px"><img src="assets/dvr.jpg" style="left:20px;top:20px;width:360px;height:360px"></div>')
    + numscene('b', 2, 'Disk već u kompletu', 'Snimač prima disk do 4 TB, ako ti zatreba više.',
      '<div class="tile" id="bm1" style="left:290px;top:640px;width:500px;height:500px"><img src="assets/hdd.webp" style="left:25px;top:25px;width:450px;height:450px"></div><div class="chip" id="bm2" style="left:640px;top:600px;background:#2f7a50">1 TB</div>')
    + numscene('c', 1, 'Slika na telefonu', 'Hik-Connect aplikacija, preko mreže.',
      '''<div class="phone" id="cm1" style="left:330px;top:600px;width:420px;height:620px;border-radius:56px"><div class="scr"><div class="abs" style="left:24px;top:40px;width:174px;height:130px;border-radius:12px;background:#2c3a33" id="t1"></div><div class="abs" style="left:206px;top:40px;width:174px;height:130px;border-radius:12px;background:#2c3a33" id="t2"></div><div class="abs" style="left:24px;top:180px;width:174px;height:130px;border-radius:12px;background:#2c3a33" id="t3"></div><div class="abs" style="left:206px;top:180px;width:174px;height:130px;border-radius:12px;background:#2c3a33" id="t4"></div><div class="abs" style="left:24px;top:350px;font-size:30px;font-weight:700;color:#6cc08f">● UŽIVO</div><div class="abs" style="left:24px;top:400px;font-size:26px;color:#9db5aa">4 kamere</div></div></div>''')
    + '''
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:104px">Ovaj ima</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:300px;font-size:104px">sve tri.</div>
    <div class="tile" id="d3" style="left:80px;top:450px;width:440px;height:440px"><img src="assets/kit.jpg" style="left:10px;top:10px;width:420px;height:420px"></div>
    <div class="row" id="r1" style="top:960px"><span class="chk">✓</span>Kamere + snimač</div>
    <div class="row" id="r2" style="top:1060px"><span class="chk">✓</span>Disk 1 TB</div>
    <div class="row" id="r3" style="top:1160px"><span class="chk">✓</span>Slika na telefonu</div>
    <div class="abs" id="d4" style="left:560px;top:520px;width:440px;font-size:40px;font-weight:700;line-height:1.25">HiLook<br><span class="green">4× THC-T120-P</span><br>+ DVR-104G-K1</div>
  </div>''',
  js='''function numS(p,t,a){const n=$(p+'n');const q=P(t,a,.35);tf(n,{s:lerp(2.2,1,eoc(q)),o:clamp(q*3,0,1),r:lerp(-12,0,eoc(q))});n.style.textShadow=`0 0 ${40*(1-q)}px #6cc08f`;
  pop($(p+'t'),t,a+.35,{dx:90,dy:0,s0:1});pop($(p+'s'),t,a+1.6,{dy:24,s0:1});}
function renderF(t){
  if(t<4.1){numS('a',t,0);fly($('am1'),t,.8,{x0:-500,y0:0,r0:-20});fly($('am2'),t,1.0,{x0:500,y0:0,r0:20});slam($('aplus'),t,1.35);}
  if(t>=3.9&&t<8.1){numS('b',t,4);fly($('bm1'),t,4.7,{y0:600,r0:15});slam($('bm2'),t,5.3,{s0:2});}
  if(t>=7.9&&t<12.1){numS('c',t,8);pop($('cm1'),t,8.7,{dy:300,s0:.9,d:.5});
    ['t1','t2','t3','t4'].forEach((id,i)=>{const on=t>9.2+i*.25;$(id).style.background=on?['#3d5a4b','#4a6b58','#365246','#55776a'][i]:'#2c3a33';});}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});slam($('d2'),t,12.35);pop($('d3'),t,12.3,{dy:200,s0:.8,d:.5});pop($('d4'),t,12.6,{dx:80,dy:0,s0:1});
    ['r1','r2','r3'].forEach((id,i)=>{pop($(id),t,13+i*.45,{dx:-60,dy:0,s0:1});const c=$(id).firstElementChild;const q=eob(P(t,13.15+i*.45,.3));c.style.transform=`scale(${q})`;});}
}''',
  pops=[.35, .8, 1.0, 4.35, 4.7, 8.35, 8.7, 12.05, 12.6, 13, 13.45, 13.9], impacts=[0, 4, 8, 12.35], extra=[('tap', 13.15, .4), ('tap', 13.6, .4), ('tap', 14.05, .4), ('confirm', 14.1, .2)])

# ---------------------------------------------------------------- 4 A ILI B
F['f4'] = dict(name='Poređenje A ili B', style='synthwave', key=7,
  tag='ANALOGNI ILI IP?', hook=hook('Isti broj kamera. Drugačiji kabl.', (4,), 4), hsize=128, subtop=1180,
  sub='Koji bi ti uzeo?', p=('Komplet A', 'analogni'),
  scn=[['a', 0, 3.5], ['b', 3.5, 8], ['c', 8, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.0, 3.5, 8, 11.5, 13.2, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="tile" id="aA" style="left:60px;top:330px;width:460px;height:560px"><img src="assets/kit.jpg" style="left:10px;top:10px;width:440px;height:440px"><div class="abs" style="left:0;top:450px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">A · Analogni</div><div class="abs" style="left:0;top:500px;width:460px;text-align:center;font-size:26px;color:#5d6b64">Turbo HD</div></div>
    <div class="tile" id="aB" style="left:560px;top:330px;width:460px;height:560px"><img src="assets/ipkit.jpg" style="left:10px;top:10px;width:440px;height:440px"><div class="abs" style="left:0;top:450px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">B · IP</div><div class="abs" style="left:0;top:500px;width:460px;text-align:center;font-size:26px;color:#5d6b64">mrežni</div></div>
    <div class="abs" id="vs" style="left:420px;top:520px;width:240px;height:240px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:96px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.5)">VS</div>
    <div class="abs h1" id="a3" style="left:0;width:1080px;text-align:center;top:970px;font-size:64px">4 kamere · 2 MP · disk 1 TB</div>
    <div class="abs note" id="a4" style="left:0;width:1080px;text-align:center;top:1060px">HiLook, oba kompleta sa sajta</div>
  </div>
  %%ROWS%%''',
  js='''function rowS(p,t,a){pop($(p+'h'),t,a,{dx:-90,dy:0,s0:1});pop($(p+'A'),t,a+.4,{dx:-300,dy:0,s0:.95,ry0:-30});pop($(p+'B'),t,a+.9,{dx:300,dy:0,s0:.95,ry0:30});}
function renderF(t){
  if(t<3.6){fly($('aA'),t,.05,{x0:-700,y0:0,r0:-12});fly($('aB'),t,.35,{x0:700,y0:0,r0:12});const q=P(t,1.0,.3);tf($('vs'),{s:lerp(3,1,eoc(q))+.04*Math.sin(t*6),o:clamp(q*3,0,1),r:lerp(-90,0,eoc(q))});
    pop($('a3'),t,1.6,{dy:40,s0:.9});pop($('a4'),t,2.1,{dy:20,s0:1});}
  if(t>=3.4&&t<8.1){rowS('b',t,3.6);pop($('bA2'),t,5.5,{dy:30,s0:.9});pop($('bB2'),t,6.0,{dy:30,s0:.9});}
  if(t>=7.9&&t<11.6){rowS('c',t,8.1);pop($('cn'),t,9.8,{dy:30,s0:1});}
  if(t>=11.4&&t<15.6){rowS('d',t,11.6);
    const a=count(t,12.0,.9,30000),b=count(t,12.5,.9,43000);$('dAv').textContent=fmt(a);$('dBv').textContent=fmt(b);
    const q=P(t,13.2,.4);tf($('dq'),{s:lerp(1.5,1,eoc(q))+.03*Math.sin(t*5),o:clamp(q*3,0,1)});}
}''',
  pops=[.05, .35, 1.6, 3.6, 4.0, 4.5, 5.5, 6.0, 8.1, 8.5, 9.0, 9.8, 11.6, 12.0, 12.5], impacts=[1.0, 13.2])
def rowscene(sid, head, a_big, a_small, b_big, b_small, extra=''):
    box = 'position:absolute;top:470px;width:445px;height:620px;border-radius:34px;padding:40px 34px;display:flex;flex-direction:column;justify-content:center'
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs h1" id="{sid}h" style="left:80px;top:220px;font-size:110px">{head}</div>
    <div id="{sid}A" style="{box};left:80px;background:#fff;color:#123528"><div style="font-size:32px;font-weight:800;color:#2f7a50;letter-spacing:3px">A · ANALOGNI</div><div id="{sid}Av" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{a_big}</div><div id="{sid}A2" style="font-size:32px;color:#5d6b64;font-weight:500;margin-top:22px;line-height:1.3">{a_small}</div></div>
    <div id="{sid}B" style="{box};left:555px;background:rgba(255,255,255,.08);border:3px solid #6cc08f"><div style="font-size:32px;font-weight:800;color:#6cc08f;letter-spacing:3px">B · IP</div><div id="{sid}Bv" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{b_big}</div><div id="{sid}B2" style="font-size:32px;color:#c9dbd0;font-weight:500;margin-top:22px;line-height:1.3">{b_small}</div></div>
    {extra}
  </div>'''
F['f4']['html'] = F['f4']['html'].replace('%%ROWS%%',
    rowscene('b', 'Kabl', 'Koaksijalni', 'bez mrežne opreme', 'Mrežni', 'PoE svič: slika i struja kroz 1 kabl')
  + rowscene('c', 'Snimač', 'DVR 4 kanala', 'DVR-104G-K1, H.265 Pro+', 'NVR 4 kanala', 'kamere do 6 MP, rezerva za nadogradnju',
             '<div class="abs note" id="cn" style="left:80px;top:1150px;width:920px">Disk 1 TB je u oba kompleta.</div>')
  + rowscene('d', 'Cena', '30.000', 'RSD sa PDV-om', '43.000', 'RSD sa PDV-om',
             '<div class="abs h1" id="dq" style="left:0;width:1080px;text-align:center;top:1160px;font-size:76px">Napiši u komentar: <span class="green">A ili B?</span></div>'))

# ---------------------------------------------------------------- 5 ZA KOGA JE
def persona(sid, label, title, sub, svg):
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs tag" id="{sid}l" style="left:80px;top:200px;font-size:46px">{label}</div>
    <div class="abs h1" id="{sid}t" style="left:80px;top:270px;width:920px;font-size:96px">{title}</div>
    <div class="card" id="{sid}c" style="left:80px;top:520px;width:920px;height:640px;background:#e6f2ea">{svg}</div>
    <div class="abs sub" id="{sid}s" style="left:80px;top:1210px;width:920px">{sub}</div>
  </div>'''
CAMDOT = '<g transform="translate(%d %d)"><circle r="20" fill="#fff" stroke="#2f7a50" stroke-width="7"/><circle r="7" fill="#123528"/></g>'
F['f5'] = dict(name='Za koga je', style='lofi_chill', key=4,
  tag='JEDAN KOMPLET', hook=hook('Tri različita kupca. Isti komplet.', (3, 4), 4), hsize=128, subtop=1060,
  sub='Pronađi sebe.', p=('Isti komplet', 'za sve tri'),
  scn=[['a', 0, 4.5], ['b', 4.5, 9], ['c', 9, 13], ['d', 13, 15.5]],
  slams=[0, 4.5, 9, 13, 15.5, 18.5],
  html=persona('a', '1 · KUĆA', 'Ulaz, prilaz <span class="green">i dve strane</span>', 'Komplet je za kuću, dvorište ili garažu.',
      '<svg width="920" height="640" viewBox="0 0 920 640"><rect y="470" width="920" height="170" fill="#cfe6d8"/><path d="M250 470 L250 270 L460 130 L670 270 L670 470 Z" fill="#fff" stroke="#123528" stroke-width="8"/><rect x="420" y="360" width="80" height="110" fill="#2f7a50"/><rect x="300" y="300" width="80" height="70" fill="#6cc08f"/><rect x="540" y="300" width="80" height="70" fill="#6cc08f"/><g id="aC">' + ''.join(CAMDOT % xy for xy in [(250, 280), (670, 280), (460, 340), (460, 200)]) + '</g></svg>')
    + persona('b', '2 · VIKENDICA', 'Kiša, mraz, <span class="green">vrućina</span>', 'Kućište IP66, radi od −40 do +60 °C.',
      '<svg width="920" height="640" viewBox="0 0 920 640"><path d="M0 470 L200 220 L380 470 Z M300 470 L520 160 L760 470 Z" fill="#cfe6d8"/><rect y="470" width="920" height="170" fill="#b9dcc6"/><path d="M560 470 L560 360 L660 290 L760 360 L760 470 Z" fill="#fff" stroke="#123528" stroke-width="8"/><g id="snow" fill="#fff" stroke="#2f7a50" stroke-width="3">' + ''.join(f'<circle cx="{x}" cy="{y}" r="9"/>' for x, y in [(120, 80), (260, 140), (420, 60), (640, 110), (820, 70), (760, 190)]) + '</g>' + CAMDOT % (760, 370) + '<g id="therm" transform="translate(120 330)"><rect x="-22" y="-120" width="44" height="160" rx="22" fill="#fff" stroke="#123528" stroke-width="6"/><rect id="tm" x="-10" y="-60" width="20" height="90" rx="10" fill="#d64545"/><circle cy="40" r="30" fill="#d64545" stroke="#123528" stroke-width="6"/></g></svg>')
    + persona('c', '3 · MALA RADNJA', 'Slika odmah <span class="green">na monitoru</span>', 'HDMI i VGA izlaz istovremeno.',
      '<svg width="920" height="640" viewBox="0 0 920 640"><rect x="80" y="120" width="420" height="380" fill="#fff" stroke="#123528" stroke-width="8"/><path d="M60 120 L520 120 L490 60 L90 60 Z" fill="#2f7a50"/><rect x="130" y="200" width="150" height="300" fill="#cfe6d8" stroke="#123528" stroke-width="6"/><rect x="310" y="200" width="150" height="140" fill="#6cc08f"/>' + CAMDOT % (480, 150) + '<rect x="560" y="200" width="300" height="200" rx="12" fill="#123528"/><g id="mon"><rect x="575" y="215" width="132" height="82" fill="#3d5a4b"/><rect x="713" y="215" width="132" height="82" fill="#4a6b58"/><rect x="575" y="303" width="132" height="82" fill="#365246"/><rect x="713" y="303" width="132" height="82" fill="#55776a"/></g><rect x="690" y="400" width="40" height="40" fill="#123528"/><rect x="640" y="440" width="140" height="14" rx="7" fill="#123528"/></svg>')
    + '''
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:104px">Isti komplet.</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:300px;font-size:104px">Za sve tri.</div>
    <div class="disc" id="d3" style="left:250px;top:470px;width:580px;height:580px"><img src="assets/kit.jpg" style="left:40px;top:40px;width:500px;height:500px"></div>
    <div class="chip" id="d4" style="left:110px;top:1120px">Kuća</div><div class="chip" id="d5" style="left:370px;top:1120px">Vikendica</div><div class="chip" id="d6" style="left:720px;top:1120px">Radnja</div>
  </div>''',
  js='''function per(p,t,a){pop($(p+'l'),t,a,{dx:-60,dy:0,s0:1});slam($(p+'t'),t,a+.3,{s0:1.3});pop($(p+'c'),t,a+.5,{dy:200,s0:.85,d:.5,ry0:20});pop($(p+'s'),t,a+1.5,{dy:24,s0:1});}
function renderF(t){
  if(t<4.6){per('a',t,0);[...$('aC').children].forEach((g,i)=>{const q=eob(P(t,1.4+i*.35,.3));g.style.transform=`scale(${q})`;g.style.transformBox='fill-box';g.style.transformOrigin='center';});}
  if(t>=4.4&&t<9.1){per('b',t,4.6);[...$('snow').children].forEach((c,i)=>c.setAttribute('transform',`translate(0 ${((t*60+i*70)%300)})`));
    const k=.5+.5*Math.sin((t-5.5)*2.2);$('tm').setAttribute('y',String(-110+90*(1-k)));$('tm').setAttribute('height',String(30+90*k));}
  if(t>=8.9&&t<13.1){per('c',t,9.1);[...$('mon').children].forEach((r,i)=>r.style.opacity=t>10.4+i*.2?1:.15);}
  if(t>=12.9&&t<15.6){pop($('d1'),t,13.05,{dx:-90,dy:0,s0:1});slam($('d2'),t,13.3);
    const hp=P(t,13.1,.6),he=eob(hp);tf($('d3'),{y:lerp(300,0,he)+Math.sin(t*2)*10,s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-60,0,eoc(hp))});
    ['d4','d5','d6'].forEach((id,i)=>pop($(id),t,13.8+i*.25,{dy:40,s0:.7}));}
}''',
  pops=[0, .5, 1.4, 1.75, 2.1, 2.45, 4.6, 5.1, 9.1, 9.6, 10.4, 13.05, 13.8, 14.05, 14.3], impacts=[.3, 4.9, 9.4, 13.3])

# ---------------------------------------------------------------- 6 STA DOBIJES
F['f6'] = dict(name='Šta dobiješ u kompletu', style='deep_house', key=10,
  tag='KOMPLET HILOOK', hook=hook('Šta dobiješ za 30.000 dinara?', (3,), 3), hsize=136, subtop=1060,
  sub='Brojimo deo po deo.', p=('Sve ovo', 'u kompletu'),
  scn=[['a', 0, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.2, 1.9, 2.6, 3.3, 6.3, 9.3, 11.5, 13.6, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="al" style="left:80px;top:210px;width:660px;font-size:56px;height:200px"></div>
    <div class="abs" id="ac" style="left:780px;top:190px;width:220px;height:220px;border-radius:50%;background:#2f7a50;border:6px solid #6cc08f;display:flex;align-items:center;justify-content:center;font-size:110px;font-weight:800">0</div>
    <div class="tile" id="i1" style="left:80px;top:450px;width:210px;height:210px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i2" style="left:316px;top:450px;width:210px;height:210px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i3" style="left:552px;top:450px;width:210px;height:210px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i4" style="left:788px;top:450px;width:210px;height:210px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i5" style="left:80px;top:700px;width:540px;height:440px"><img src="assets/dvr.jpg" style="left:50px;top:0;width:440px;height:440px"></div>
    <div class="tile" id="i6" style="left:650px;top:700px;width:350px;height:440px"><img src="assets/hdd.webp" style="left:0;top:45px;width:350px;height:350px"></div>
    <div class="abs note" id="an" style="left:80px;top:1190px;width:920px">Prave slike delova sa sajta.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs note" id="d0" style="left:80px;top:220px;font-size:40px">Kupljeno pojedinačno</div>
    <div class="abs h1" id="d1" style="left:80px;top:280px;font-size:130px;color:#c9dbd0"><span id="d1v">0</span> RSD<div id="strike" class="abs" style="left:-10px;top:68px;height:14px;width:0;background:#ff7b7b;border-radius:7px"></div></div>
    <div class="abs note" id="d2" style="left:80px;top:520px;font-size:40px">U kompletu</div>
    <div class="abs h1 green" id="d3" style="left:80px;top:580px;font-size:170px">30.000 RSD</div>
    <div class="abs" id="d4" style="left:80px;top:860px;width:920px;height:260px;border-radius:34px;background:#fff;color:#123528;display:flex;flex-direction:column;justify-content:center;padding:0 50px"><div style="font-size:40px;font-weight:600;color:#5d6b64">Uštedite u kompletu</div><div style="font-size:96px;font-weight:800;color:#2f7a50;letter-spacing:-2px"><span id="d4v">0</span> RSD <span style="font-size:60px">(30%)</span></div></div>
  </div>''',
  js='''const LBL=[[1.2,'Kamera THC-T120-P'],[6.3,'Snimač DVR-104G-K1'],[9.3,'Hard disk 1 TB']];
function renderF(t){
  if(t<11.6){let l='';for(const [a,s] of LBL)if(t>=a-.1)l=s;$('al').innerHTML=l+(t>=1.1&&t<6.2?'<br><span class="green">2 MP, 2.8 mm</span>':t>=6.2&&t<9.2?'<br><span class="green">4 kanala, H.265 Pro+</span>':t>=9.2?'<br><span class="green">prima do 4 TB</span>':'');
    pop($('al'),t,[1.2,6.3,9.3].filter(a=>t>=a-.1).pop()||99,{dx:-60,dy:0,s0:1});
    const n=t<1.2?0:t<1.9?1:t<2.6?2:t<3.3?3:t<6.3?4:t<9.3?5:6;$('ac').textContent=n;
    {let pulse=0;for(const b of [1.2,1.9,2.6,3.3,6.3,9.3]){const d=t-b;if(d>=0&&d<.3)pulse=Math.max(pulse,(1-d/.3)*.25);}tf($('ac'),{s:(t<.8?eob(P(t,.3,.4)):1)+pulse,o:clamp((t-.3)*4,0,1)});}
    fly($('i1'),t,1.2,{y0:-700,r0:-30});fly($('i2'),t,1.9,{y0:-700,r0:25});fly($('i3'),t,2.6,{y0:-700,r0:-20});fly($('i4'),t,3.3,{y0:-700,r0:30});
    fly($('i5'),t,6.3,{x0:-900,y0:0,r0:-10,d:.6});fly($('i6'),t,9.3,{x0:900,y0:0,r0:15,d:.6});
    pop($('an'),t,4.2,{dy:20,s0:1});
    if(t>=11){const q=eio(P(t,11,.5));['i1','i2','i3','i4','i5','i6'].forEach(id=>{$(id).style.transform+=` scale(${1-q*.3})`;$(id).style.opacity=String(1-q);});}}
  if(t>=11.4&&t<15.6){pop($('d0'),t,11.6,{dx:-60,dy:0,s0:1});pop($('d1'),t,11.7,{dx:-60,dy:0,s0:1});$('d1v').textContent=fmt(count(t,11.8,1.0,42930));
    $('strike').style.width=(eio(P(t,13.0,.35))*680)+'px';
    pop($('d2'),t,13.4,{dx:-60,dy:0,s0:1});slam($('d3'),t,13.6,{s0:1.8,d:.3});
    pop($('d4'),t,14.2,{dy:80,s0:.85});$('d4v').textContent=fmt(count(t,14.3,.8,12930));}
}''',
  pops=[1.2, 1.9, 2.6, 3.3, 4.2, 6.3, 9.3, 11.6, 11.7, 13.4, 14.2], impacts=[1.2, 6.3, 9.3, 13.6], extra=[('swish', 13.0, .3), ('confirm', 15.0, .2)])

# ---------------------------------------------------------------- 7 POV TELEFON
TILES = [('Ulaz', '#3d5a4b'), ('Prilaz', '#4a6b58'), ('Dvorište', '#365246'), ('Garaža', '#55776a')]
tiles_html = ''.join(f'<div class="abs" id="pt{i}" style="left:{24 + (i % 2) * 254}px;top:{150 + (i // 2) * 250}px;width:236px;height:230px;border-radius:16px;background:{c};overflow:hidden"><div class="abs" style="left:14px;top:12px;font-size:24px;font-weight:700">{n}</div><div class="abs" style="left:14px;bottom:12px;font-size:20px;color:#6cc08f;font-weight:700">● UŽIVO</div></div>' for i, (n, c) in enumerate(TILES))
F['f7'] = dict(name='POV telefon', style='synthwave', key=0,
  tag='POV', hook=hook('Na poslu si. Dvorište ti je u džepu.', (6, 7), 7), hsize=128, subtop=1190,
  sub='4 kamere, jedna aplikacija.', p=('Dvorište', 'u džepu'),
  scn=[['a', 0, 9.5], ['c', 9.5, 12.5], ['d', 12.5, 15.5]],
  slams=[0, 5.6, 9.5, 12.5, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;width:920px;font-size:92px;height:200px"></div>
    <div class="phone" id="ph" style="left:260px;top:420px"><div class="scr">
      <div class="abs" style="left:24px;top:50px;font-size:30px;font-weight:800">Moja kuća</div><div class="abs" style="left:24px;top:92px;font-size:22px;color:#9db5aa">4 kamere</div>
      ''' + tiles_html + '''
      <div class="abs" id="full" style="left:0;top:0;width:532px;height:1032px;background:#1d2622;opacity:0">
        <svg width="532" height="1032" viewBox="0 0 532 1032"><rect y="640" width="532" height="392" fill="#26322c"/><path d="M200 1032 L240 640 L292 640 L332 1032 Z" fill="#33423b"/><g id="car"><rect x="-90" y="-50" width="180" height="90" rx="22" fill="#cfe6d8"/><rect x="-60" y="-90" width="120" height="50" rx="16" fill="#cfe6d8"/><circle cx="-55" cy="44" r="22" fill="#0a0f0d"/><circle cx="55" cy="44" r="22" fill="#0a0f0d"/></g></svg>
        <div class="abs" style="left:24px;top:50px;font-size:30px;font-weight:800">Prilaz</div><div class="abs" style="left:400px;top:52px;font-size:22px;color:#6cc08f;font-weight:700">● UŽIVO</div>
      </div>
    </div></div>
    <div class="abs" id="fg" style="width:110px;height:110px;border-radius:50%;background:rgba(255,255,255,.55);border:6px solid #fff;opacity:0"></div>
    <div class="abs note" id="a2" style="left:80px;top:1530px;width:920px;text-align:center">Prikaz je ilustracija.</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">I noću,</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:104px">do 20 m.</div>
    <div class="phone" id="ph2" style="left:260px;top:440px"><div class="scr" style="background:#1a1a1a">
      <svg width="532" height="1032" viewBox="0 0 532 1032"><defs><radialGradient id="nv" cx=".5" cy=".55" r=".7"><stop offset="0" stop-color="#9a9a9a"/><stop offset="1" stop-color="#202020"/></radialGradient></defs><rect width="532" height="1032" fill="url(#nv)"/><rect y="640" width="532" height="392" fill="#5a5a5a" opacity=".6"/><path d="M60 640 L60 420 L200 330 L340 420 L340 640 Z" fill="#3c3c3c"/><g id="ncat" fill="#e6e6e6"><ellipse cx="0" cy="700" rx="50" ry="24"/><circle cx="46" cy="680" r="20"/></g></svg>
      <div class="abs" style="left:24px;top:50px;font-size:30px;font-weight:800">Dvorište</div><div class="abs" style="left:330px;top:52px;font-size:22px;color:#fff;font-weight:700">IR · 02:14</div>
    </div></div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:104px">Iza toga:</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:300px;font-size:104px">ovaj komplet.</div>
    <div class="tile" id="d3" style="left:180px;top:450px;width:720px;height:620px"><img src="assets/kit.jpg" style="left:60px;top:10px;width:600px;height:600px"></div>
    <div class="abs sub" id="d4" style="left:80px;top:1120px;width:920px">4 kamere i snimač, aplikacija Hik-Connect.</div>
  </div>''',
  js='''function renderF(t){
  if(t<9.6){const txt=t<5.4?'4 kamere<br><span class="green">na jednom ekranu</span>':'Dodirneš.<br><span class="green">Uživo.</span>';if($('a1').innerHTML!==txt)$('a1').innerHTML=txt;
    pop($('a1'),t,t<5.4?.1:5.6,{dx:-80,dy:0,s0:1});
    const q=P(t,0,.6),e=eob(q);tf($('ph'),{y:lerp(900,0,e),r:lerp(10,0,eoc(q)),o:clamp(q*3,0,1),s:1+(t>5.6?.0:0)});
    [0,1,2,3].forEach(i=>{const p=eob(P(t,.9+i*.3,.35));$('pt'+i).style.transform=`scale(${p})`;$('pt'+i).style.opacity=clamp(p*2,0,1);});
    const fg=$('fg');const m=eio(P(t,4.4,.7));const fx=lerp(900,660,m),fy=lerp(1500,820,m);fg.style.left=(fx-55)+'px';fg.style.top=(fy-55)+'px';fg.style.opacity=String(clamp((t-4.4)*4,0,1)*(1-clamp((t-5.6)*4,0,1)));fg.style.transform=`scale(${t>=5.2&&t<5.4?.82:1})`;
    const op=P(t,5.4,.4);$('full').style.opacity=op>0?1:0;$('full').style.clipPath=`circle(${eio(op)*1200}px at 400px 270px)`;
    $('car').setAttribute('transform',`translate(266 ${lerp(560,900,eio(P(t,5.9,2.6)))}) scale(${lerp(.55,1.25,eio(P(t,5.9,2.6)))})`);
    pop($('a2'),t,2.5,{dy:20,s0:1});}
  if(t>=9.4&&t<12.6){$('dark').style.opacity=.5;pop($('c1'),t,9.55,{dx:-90,dy:0,s0:1});slam($('c2'),t,9.9);pop($('ph2'),t,9.6,{dy:250,s0:.9,d:.45});
    $('ncat').setAttribute('transform',`translate(${lerp(-60,420,eio(P(t,10.2,2.2)))} 0)`);}
  if(t>=12.4&&t<15.6){pop($('d1'),t,12.55,{dx:-90,dy:0,s0:1});slam($('d2'),t,12.85);pop($('d3'),t,12.7,{dy:200,s0:.8,d:.5,ry0:30});pop($('d4'),t,13.6,{dy:24,s0:1});}
}''',
  pops=[.1, .9, 1.2, 1.5, 1.8, 2.5, 4.4, 5.6, 9.55, 9.6, 12.55, 12.7, 13.6], impacts=[5.4, 9.9, 12.85], extra=[('tap', 5.25, .5)])

# ---------------------------------------------------------------- 8 NAJCESCA GRESKA
F['f8'] = dict(name='Greška pre kupovine', style='minimal_tech', key=3,
  tag='PRE KUPOVINE', hook=hook('Greška: kamere i snimač kupljeni odvojeno.', (5,), 5), hsize=118, subtop=1260,
  sub='Evo zašto se to ne isplati.', p=('Bez', 'greške'),
  scn=[['a', 0, 4.5], ['b', 4.5, 8.5], ['c', 8.5, 12], ['d', 12, 15.5]],
  slams=[0, 2.0, 4.5, 8.5, 9.7, 12, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Da li rade</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:104px">zajedno?</div>
    <div class="tile" id="aA" style="left:80px;top:520px;width:420px;height:420px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:380px;height:380px"></div>
    <div class="tile" id="aB" style="left:580px;top:520px;width:420px;height:420px"><img src="assets/dvr.jpg" style="left:20px;top:20px;width:380px;height:380px"></div>
    <div class="abs h1 red" id="aq" style="left:490px;top:640px;width:100px;text-align:center;font-size:150px">?</div>
    <div class="abs sub" id="a3" style="left:80px;top:1010px;width:920px">Kanali, kompresija, disk... sve proveravaš sam.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">I plaćaš</div>
    <div class="abs h1 red" id="b2" style="left:80px;top:300px;font-size:104px">više.</div>
    <div class="abs note" id="b3" style="left:80px;top:540px;font-size:40px">Isti delovi, kupljeni pojedinačno:</div>
    <div class="abs h1" id="b4" style="left:80px;top:610px;font-size:150px"><span id="b4v">0</span> RSD</div>
    <div class="abs" id="b5" style="left:80px;top:820px;width:920px;height:40px;border-radius:20px;background:rgba(255,255,255,.1);overflow:hidden"><div id="b5f" style="height:40px;width:0;background:linear-gradient(90deg,#d64545,#ff7b7b)"></div></div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">Rešenje:</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:104px">komplet.</div>
    <div class="tile" id="cA" style="left:80px;top:470px;width:420px;height:420px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:380px;height:380px"></div>
    <div class="tile" id="cB" style="left:580px;top:470px;width:420px;height:420px"><img src="assets/dvr.jpg" style="left:20px;top:20px;width:380px;height:380px"></div>
    <div class="abs" id="cok" style="left:440px;top:580px;width:200px;height:200px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:110px;font-weight:800">✓</div>
    <div class="abs" id="c3" style="left:80px;top:960px;width:920px;height:240px;border-radius:34px;background:#fff;color:#123528;display:flex;flex-direction:column;justify-content:center;padding:0 50px"><div style="font-size:40px;font-weight:600;color:#5d6b64">Usklađeno iz jedne kutije</div><div style="font-size:78px;font-weight:800;color:#2f7a50;letter-spacing:-2px">−12.930 RSD (30%)</div></div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Pre kupovine</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">proveri:</div>
    <div class="row" id="r1" style="top:500px"><span class="chk">1</span><span>Broj kanala snimača <span class="green">· 4</span></span></div>
    <div class="row" id="r2" style="top:640px"><span class="chk">2</span><span>Koliki disk prima <span class="green">· do 4 TB</span></span></div>
    <div class="row" id="r3" style="top:780px"><span class="chk">3</span><span>Vrsta kabla <span class="green">· koaksijalni</span></span></div>
    <div class="row" id="r4" style="top:920px"><span class="chk">4</span><span>Disk u kompletu <span class="green">· 1 TB</span></span></div>
    <div class="abs note" id="d3" style="left:80px;top:1090px;width:920px">Vrednosti za ovaj HiLook komplet.</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.6){pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.4);
    const s=Math.sin(t*14)*6*(t>2.0&&t<2.6?1:0);fly($('aA'),t,.6,{x0:-600,y0:0,r0:-15});fly($('aB'),t,.9,{x0:600,y0:0,r0:15});
    if(t>2.0){$('aA').style.transform+=` translateX(${s}px)`;$('aB').style.transform+=` translateX(${-s}px)`;}
    slam($('aq'),t,2.0,{s0:2.4});$('aq').style.transform+=` rotate(${Math.sin(t*5)*8}deg)`;pop($('a3'),t,2.8,{dy:24,s0:1});}
  if(t>=4.4&&t<8.6){pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.9);pop($('b3'),t,5.3,{dy:24,s0:1});pop($('b4'),t,5.5,{dx:-60,dy:0,s0:1});
    $('b4v').textContent=fmt(count(t,5.6,1.6,42930));$('b5f').style.width=(eoc(P(t,5.6,1.6))*100)+'%';}
  if(t>=8.4&&t<12.1){pop($('c1'),t,8.55,{dx:-90,dy:0,s0:1});slam($('c2'),t,8.85);
    const j=eio(P(t,9.2,.5));tf($('cA'),{x:lerp(-80,60,j),o:1});tf($('cB'),{x:lerp(80,-60,j),o:1});
    const q=P(t,9.7,.3);tf($('cok'),{s:lerp(2.5,1,eoc(q)),o:clamp(q*3,0,1)});pop($('c3'),t,10.3,{dy:80,s0:.85});}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.25,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4'].forEach((id,i)=>pop($(id),t,12.7+i*.5,{dx:-80,dy:0,s0:1}));pop($('d3'),t,14.8,{dy:20,s0:1});}
}''',
  pops=[.05, .6, .9, 2.8, 4.6, 5.3, 5.5, 8.55, 9.2, 10.3, 12.05, 12.25, 12.7, 13.2, 13.7, 14.2], impacts=[.4, 2.0, 4.9, 9.7], extra=[('confirm', 9.75, .22)])

# ---------------------------------------------------------------- build
def sfx_for(f):
    ev = []
    nw = f['hook'].count('class="w')
    for i in range(nw): ev.append({'type': 'thud', 't': 0.1 + i * 0.11, 'g': 0.35})
    ev.append({'type': 'swish', 't': 1.0, 'g': 0.2})
    ev.append({'type': 'riser', 't': 3.0, 'g': 0.12, 'len': 1.8})
    for _, a, _b in f['scn'] + [['sP', 15.5, 0], ['sO', 18.5, 0]]:
        ev.append({'type': 'whoosh', 't': 3 + a, 'g': 0.32})
    for a in f['pops']: ev.append({'type': 'swish', 't': 3 + a, 'g': 0.2})
    for a in f['impacts']: ev.append({'type': 'impact', 't': 3 + a, 'g': 0.55})
    for e in f.get('extra', []):
        d = {'type': e[0], 't': 3 + e[1], 'g': e[2]}
        if len(e) > 3: d['len'] = e[3]
        ev.append(d)
    ev += [{'type': 'swish', 't': 18.6, 'g': .2}, {'type': 'swish', 't': 19.5, 'g': .2}, {'type': 'tap', 't': 20.5, 'g': .55},
           {'type': 'confirm', 't': 20.62, 'g': .22}, {'type': 'revcym', 't': 21.5, 'g': .12}, {'type': 'impact_big', 't': 21.5, 'g': .6}]
    return ev

for k, f in F.items():
    out = os.path.join(D, k); os.makedirs(os.path.join(out, 'assets'), exist_ok=True)
    for a, src in IMG.items(): shutil.copy(os.path.join(D, 'img', src), os.path.join(out, 'assets', a))
    shutil.copy(LOGO, os.path.join(out, 'assets'))
    h = BASE
    for tok, val in [('%%TAG%%', f['tag']), ('%%HOOK%%', f['hook']), ('%%HSIZE%%', str(f['hsize'])), ('%%SUBTOP%%', str(f['subtop'])),
                     ('%%SUB%%', f['sub']), ('%%SCENES%%', f['html']), ('%%P1%%', f['p'][0]), ('%%P2%%', f['p'][1]),
                     ('%%INC%%', '✓  Uštedite u kompletu 12.930 RSD (30%)'), ('%%PRICE%%', '30.000'),
                     ('%%SCN%%', json.dumps(f['scn'])), ('%%SLAMS%%', json.dumps(f['slams'])), ('%%JS%%', f['js'])]:
        h = h.replace(tok, val)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
    json.dump({'name': f['name'], 'style': f['style'], 'key': f['key']}, open(os.path.join(out, 'meta.json'), 'w'), ensure_ascii=False)
print('ok', list(F))
