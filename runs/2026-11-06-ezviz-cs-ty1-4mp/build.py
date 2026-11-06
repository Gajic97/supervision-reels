"""Gradi 2 reela za 06.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
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

# ============================================================ EZVIZ CS-TY1 4MP (f2, problem -> rešenje)
ROOM = '''<svg class="abs" id="%s" style="left:80px;top:470px" width="920" height="720" viewBox="0 0 920 720">
      <defs><radialGradient id="%sg" cx="0" cy="0" r="1"><stop offset="0" stop-color="#6cc08f" stop-opacity=".55"/><stop offset="1" stop-color="#6cc08f" stop-opacity=".08"/></radialGradient></defs>
      <rect x="20" y="20" width="880" height="680" rx="26" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.55)" stroke-width="8"/>
      <rect x="60" y="70" width="300" height="130" rx="22" fill="rgba(255,255,255,.12)"/><text x="210" y="148" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="28" fill="#c9dbd0">kauč</text>
      <rect x="600" y="80" width="250" height="170" rx="18" fill="rgba(255,255,255,.12)"/><text x="725" y="175" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="28" fill="#c9dbd0">sto</text>
      <rect x="70" y="470" width="170" height="190" rx="18" fill="rgba(255,255,255,.12)"/><text x="155" y="575" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="28" fill="#c9dbd0">orman</text>
      <path d="M700 700 A120 120 0 0 1 820 580" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="5" stroke-dasharray="10 10"/><text x="790" y="660" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="28" fill="#c9dbd0">vrata</text>
      <clipPath id="%sk"><rect x="24" y="24" width="872" height="672" rx="24"/></clipPath><path id="%sc" fill="url(#%sg)" clip-path="url(#%sk)"/>
      %s
    </svg>'''

R['ty1'] = dict(
  style='lofi_chill', key=8, seed=5401,
  tag='WIFI KAMERA ZA STAN', hook=hook('Kamera ti vidi samo jedan ugao sobe?', (3, 4, 5), 5), hsize=118, subtop=1050,
  sub='Ova se okreće u pun krug.', p=('Wi-Fi kamera', 'za stan'),
  inc='Samo za unutra · napajanje micro USB 5 V', price='5.260', img='assets/cam.png',
  scn=[['a', 0, 4], ['b', 4, 8.5], ['c', 8.5, 12.5], ['d', 12.5, 15.5]],
  slams=[0, 4, 8.5, 12.5, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Fiksna kamera:</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:96px">jedan ugao.</div>
    ''' + ROOM % ('ra', 'ra', 'ra', 'ra', 'ra', 'ra', '''<g transform="translate(460 690)"><circle r="26" fill="#fff" stroke="#2f7a50" stroke-width="8"/><circle r="9" fill="#2f7a50"/></g>
      <g font-family="Poppins" font-weight="800" font-size="104" fill="#ff7b7b"><text id="q1" x="120" y="400">?</text><text id="q2" x="780" y="420">?</text><text id="q3" x="430" y="140">?</text></g>''') + '''
    <div class="abs note" id="a3" style="left:80px;top:1230px;width:920px">Primer, ilustracija: ostatak sobe ostaje van kadra.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">CS-TY1 se okreće:</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">pun krug.</div>
    <svg class="abs" id="ring" style="left:190px;top:450px" width="700" height="700" viewBox="-350 -350 700 700">
      <circle r="300" fill="none" stroke="rgba(108,192,143,.25)" stroke-width="6"/>
      <circle id="ringp" r="300" fill="none" stroke="#6cc08f" stroke-width="10" stroke-linecap="round" stroke-dasharray="1885" stroke-dashoffset="1885" transform="rotate(-90)"/>
      <circle id="rdot" r="20" fill="#fff"/>
    </svg>
    <div class="disc" id="bd" style="left:340px;top:600px;width:400px;height:400px"><img src="assets/cam.png" style="left:25px;top:25px;width:350px;height:350px"></div>
    <div class="abs h1" id="deg" style="left:80px;top:1190px;font-size:96px;width:400px">0°</div>
    <div class="chip" id="b3" style="left:470px;top:1200px">pan i tilt, motorni</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">Sama prati</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:104px">pokret.</div>
    ''' + ROOM % ('rc', 'rc', 'rc', 'rc', 'rc', 'rc', '''<g id="man"><circle r="30" fill="#ffffff"/><circle r="52" fill="none" stroke="#fff" stroke-width="5" opacity=".5"/></g>
      <g transform="translate(460 380)"><circle r="30" fill="#fff" stroke="#2f7a50" stroke-width="8"/><circle r="10" fill="#2f7a50"/></g>''') + '''
    <div class="chip" id="c3" style="left:80px;top:1230px">noću IR do 10 m</div>
    <div class="abs note" id="c4" style="left:500px;top:1240px;width:500px">Primer, ilustracija.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">I još, uz</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">jednu kameru:</div>
    <div class="row" id="r1" style="top:500px"><span class="chk">✓</span><span>2K+ <span class="green">· 2560 × 1440</span></span></div>
    <div class="row" id="r2" style="top:640px"><span class="chk">✓</span><span>Ugao <span class="green">· 124° dijagonalno</span></span></div>
    <div class="row" id="r3" style="top:780px"><span class="chk">✓</span><span>microSD <span class="green">· do 256 GB</span></span></div>
    <div class="row" id="r4" style="top:920px"><span class="chk">✓</span><span>Dvosmerni razgovor</span></div>
    <div class="row" id="r5" style="top:1060px"><span class="chk">✓</span><span>Režim spavanja <span class="green">· privatnost</span></span></div>
  </div>''',
  js='''function wedge(cx,cy,r,a,h){const A=(a-h)*Math.PI/180,B=(a+h)*Math.PI/180;return `M${cx} ${cy} L${cx+r*Math.cos(A)} ${cy+r*Math.sin(A)} A${r} ${r} 0 0 1 ${cx+r*Math.cos(B)} ${cy+r*Math.sin(B)} Z`;}
function renderF(t){
  if(t<4.1){pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.45);pop($('ra'),t,.3,{dy:60,s0:.92});
    const sw=Math.sin(t*1.6)*3;$('rac').setAttribute('d',wedge(460,690,520,-90+sw,24));
    ['q1','q2','q3'].forEach((id,i)=>{const p=eob(P(t,1.1+i*.45,.35));const el=$(id);el.style.opacity=clamp(p*2,0,1);el.style.transform=`translateY(${Math.sin(t*3+i)*8}px)`;});
    pop($('a3'),t,2.6,{dy:24,s0:1});}
  if(t>=3.9&&t<8.6){pop($('b1'),t,4.1,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.45);
    tf($('ring'),{s:lerp(.7,1,eoc(P(t,4.3,.5))),o:clamp((t-4.3)*3,0,1)});
    const rp=eio(P(t,4.8,2.6));$('ringp').style.strokeDashoffset=String(1885*(1-rp));
    const ra=(rp*360-90)*Math.PI/180;$('rdot').setAttribute('cx',String(300*Math.cos(ra)));$('rdot').setAttribute('cy',String(300*Math.sin(ra)));
    {const hp=P(t,4.4,.6),he=eob(hp);tf($('bd'),{s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-70,0,eoc(hp))+Math.sin(t*2.2)*14,y:Math.sin(t*2)*6});}
    pop($('deg'),t,4.8,{dy:30,s0:.9});$('deg').textContent=Math.round(rp*360)+'°';
    if(rp>=1){const d=t-7.4;if(d>=0&&d<.3)$('deg').style.transform+=` scale(${1+.15*(1-d/.3)})`;}
    pop($('b3'),t,5.6,{dy:40,s0:.8});}
  if(t>=8.3&&t<12.6){pop($('c1'),t,8.55,{dx:-90,dy:0,s0:1});slam($('c2'),t,8.9);pop($('rc'),t,8.7,{dy:60,s0:.92});
    const s=eio(P(t,9.3,2.6));const mx=lerp(640,190,s),my=lerp(560,330,s)+Math.sin(s*Math.PI)*-120;
    $('man').setAttribute('transform',`translate(${mx} ${my})`);
    const ang=Math.atan2(my-380,mx-460)*180/Math.PI;$('rcc').setAttribute('d',wedge(460,380,560,ang,42));
    pop($('c3'),t,10.0,{dy:40,s0:.8});pop($('c4'),t,10.5,{dy:20,s0:1});}
  if(t>=12.3&&t<15.6){pop($('d1'),t,12.55,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.75,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4','r5'].forEach((id,i)=>{pop($(id),t,13.0+i*.35,{dx:-80,dy:0,s0:1});const c=$(id).firstElementChild;c.style.transform=`scale(${eob(P(t,13.15+i*.35,.3))})`;});}
}''',
  pops=[.05, .3, 1.1, 1.55, 2.0, 2.6, 4.1, 4.8, 5.6, 8.55, 8.7, 10.0, 10.5, 12.55, 12.75, 13.0, 13.35, 13.7, 14.05, 14.4],
  impacts=[.45, 4.45, 8.9], extra=[('riser', 4.8, .1, 2.4), ('confirm', 7.4, .2), ('swish', 9.3, .15)])

# ============================================================ KOMPLET HiLook 8x turret (f6, šta dobiješ)
CAMS = ''.join(f'<div class="tile" id="i{i}" style="left:{80 + (i % 4) * 240}px;top:{450 + (i // 4) * 235}px;width:200px;height:200px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:190px;height:190px"></div>' for i in range(8))
R['kit'] = dict(
  style='deep_house', key=1, seed=2937,
  tag='KOMPLET VIDEO NADZORA', hook=hook('Vlasnici veće kuće: 8 kamera iz jedne kutije.', (3, 4), 4), hsize=112, subtop=1150,
  sub='Brojimo šta je unutra, deo po deo.', p=('Komplet video', 'nadzora · 8 kamera'),
  inc='Kabl za kamere nije u kompletu', price='39.200', img='assets/kit.jpg',
  scn=[['a', 0, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 6.3, 8.8, 11.5, 13.6, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="al" style="left:80px;top:200px;width:660px;font-size:54px;height:200px;line-height:1.25"></div>
    <div class="abs" id="ac" style="left:780px;top:180px;width:220px;height:220px;border-radius:50%;background:#2f7a50;border:6px solid #6cc08f;display:flex;align-items:center;justify-content:center;font-size:110px;font-weight:800">0</div>
    ''' + CAMS + '''
    <div class="tile" id="i8" style="left:80px;top:940px;width:540px;height:340px"><img src="assets/dvr.jpg" style="left:100px;top:0;width:340px;height:340px"></div>
    <div class="tile" id="i9" style="left:660px;top:940px;width:340px;height:340px"><img src="assets/hdd.png" style="left:20px;top:20px;width:300px;height:300px"></div>
    <div class="chip" id="an" style="left:80px;top:1320px">+ napajanje 6 A i konektori</div>
  </div>
  <div class="scene" id="d">
    <div class="abs note" id="d0" style="left:80px;top:220px;font-size:40px">Kupljeno pojedinačno</div>
    <div class="abs h1" id="d1" style="left:80px;top:280px;font-size:124px;color:#c9dbd0;white-space:nowrap"><span id="d1v">0</span> RSD<div id="strike" class="abs" style="left:-10px;top:66px;height:14px;width:0;background:#ff7b7b;border-radius:7px"></div></div>
    <div class="abs note" id="d2" style="left:80px;top:520px;font-size:40px">U kompletu</div>
    <div class="abs h1 green" id="d3" style="left:80px;top:580px;font-size:150px;white-space:nowrap">39.200 RSD</div>
    <div class="abs" id="d4" style="left:80px;top:860px;width:920px;height:260px;border-radius:34px;background:#fff;color:#123528;display:flex;flex-direction:column;justify-content:center;padding:0 50px"><div style="font-size:40px;font-weight:600;color:#5d6b64">Uštedite u kompletu</div><div style="font-size:88px;font-weight:800;color:#2f7a50;letter-spacing:-2px;white-space:nowrap"><span id="d4v">0</span> RSD <span style="font-size:56px">(28%)</span></div></div>
    <div class="abs note" id="d5" style="left:80px;top:1170px;width:920px">Cene sa stranice kompleta, sa PDV-om.</div>
  </div>''',
  js='''const CT=[1.2,1.55,1.9,2.25,2.6,2.95,3.3,3.65,6.3,8.8];
function renderF(t){
  if(t<11.6){const l=t<1.1?'':t<6.2?'Kamera THC-T120-P<br><span class="green">8 komada · 2 MP, 2.8 mm</span>':t<8.7?'Snimač DVR-108G-M1/T<br><span class="green">8 kanala · H.265 Pro+</span>':'Hard disk WD Purple<br><span class="green">2 TB, već u kompletu</span>';
    $('al').innerHTML=l;pop($('al'),t,[1.2,6.3,8.8].filter(a=>t>=a-.1).pop()||99,{dx:-60,dy:0,s0:1});
    const n=CT.filter(a=>t>=a).length;$('ac').textContent=n;
    {let pulse=0;for(const b of CT){const d=t-b;if(d>=0&&d<.3)pulse=Math.max(pulse,(1-d/.3)*.25);}tf($('ac'),{s:(t<.8?eob(P(t,.3,.4)):1)+pulse,o:clamp((t-.3)*4,0,1)});}
    for(let i=0;i<8;i++){fly($('i'+i),t,CT[i],{y0:-700,r0:(i%2?25:-25),d:.42});if(t>CT[i]+.5)$('i'+i).style.transform+=` translateY(${Math.sin(t*2.4+i)*5}px)`;}
    fly($('i8'),t,6.3,{x0:-900,y0:0,r0:-10,d:.6});if(t>7)$('i8').style.transform+=` translateY(${Math.sin(t*2.1)*6}px)`;
    fly($('i9'),t,8.8,{x0:900,y0:0,r0:15,d:.6});if(t>9.5)$('i9').style.transform+=` translateY(${Math.sin(t*2.3)*6}px)`;
    pop($('an'),t,10.0,{dy:40,s0:.8});
    if(t>=11){const q=eio(P(t,11,.5));['i0','i1','i2','i3','i4','i5','i6','i7','i8','i9','an'].forEach(id=>{$(id).style.transform+=` scale(${1-q*.3})`;$(id).style.opacity=String(1-q);});}}
  if(t>=11.4&&t<15.6){pop($('d0'),t,11.6,{dx:-60,dy:0,s0:1});pop($('d1'),t,11.7,{dx:-60,dy:0,s0:1});$('d1v').textContent=fmt(count(t,11.8,1.0,54780));
    $('strike').style.width=(eio(P(t,13.0,.35))*700)+'px';
    pop($('d2'),t,13.4,{dx:-60,dy:0,s0:1});slam($('d3'),t,13.6,{s0:1.8,d:.3});
    pop($('d4'),t,14.2,{dy:80,s0:.85});$('d4v').textContent=fmt(count(t,14.3,.8,15580));pop($('d5'),t,14.6,{dy:20,s0:1});}
}''',
  pops=[1.2, 1.55, 1.9, 2.25, 2.6, 2.95, 3.3, 3.65, 6.3, 8.8, 10.0, 11.6, 11.7, 13.4, 14.2, 14.6], impacts=[1.2, 6.3, 8.8, 13.6],
  extra=[('swish', 13.0, .3), ('confirm', 15.0, .2)])

IMGS = {'ty1': {'cam.png': 'cs-ty1-4mp-ezviz-unutrasnja-wi-fi-kamera-2k-koja-se-okrece.png'},
        'kit': {'kit.jpg': 'komplet-video-nadzora-hilook-8-turret-thc-t120-p-dvr-108g-m1-t.jpg', 'cam.jpg': '444.jpg',
                'dvr.jpg': '10405-1.jpg', 'hdd.png': 'hdd.png'}}
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
