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

# ============================================================ KOMPLET HiLook 4x bullet IP (f6, šta dobiješ)
CAMS = ''.join(f'<div class="tile" id="i{i}" style="left:{80 + i * 240}px;top:450px;width:200px;height:200px"><img src="assets/cam.jpg" style="left:5px;top:5px;width:190px;height:190px"></div>' for i in range(4))
R['kit'] = dict(
  style='deep_house', key=6, seed=2897,
  tag='KOMPLET VIDEO NADZORA', hook=hook('Vlasnici kuće: slika i struja kroz jedan kabl.', (6, 7), 7), hsize=104, subtop=1150,
  sub='Otvaramo IP komplet, deo po deo.', p=('Komplet video', 'nadzora · 4 IP kamere'),
  inc='Mrežni kabl nije u kompletu', price='38.100', img='assets/kit.jpg',
  scn=[['a', 0, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 4.6, 6.6, 8.6, 11.5, 13.6, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="al" style="left:80px;top:200px;width:680px;font-size:48px;height:200px;line-height:1.25"></div>
    <div class="abs" id="ac" style="left:780px;top:180px;width:220px;height:220px;border-radius:50%;background:#2f7a50;border:6px solid #6cc08f;display:flex;align-items:center;justify-content:center;font-size:110px;font-weight:800">0</div>
    ''' + CAMS + '''
    <div class="tile" id="i4" style="left:80px;top:700px;width:440px;height:330px"><img src="assets/nvr.jpg" style="left:55px;top:0;width:330px;height:330px"></div>
    <div class="tile" id="i5" style="left:560px;top:700px;width:440px;height:330px"><img src="assets/hdd.webp" style="left:65px;top:15px;width:310px;height:300px"></div>
    <div class="abs" id="i6" style="left:80px;top:1070px;width:920px;height:190px;border-radius:28px;background:#fff;color:#123528;box-shadow:0 20px 50px rgba(0,0,0,.35);display:flex;align-items:center;gap:34px;padding:0 44px">
      <svg width="150" height="110" viewBox="0 0 150 110"><rect x="4" y="20" width="142" height="70" rx="12" fill="#e8efe9" stroke="#2f7a50" stroke-width="5"/>
        <g fill="#2f7a50"><rect x="18" y="42" width="20" height="18" rx="3"/><rect x="46" y="42" width="20" height="18" rx="3"/><rect x="74" y="42" width="20" height="18" rx="3"/><rect x="102" y="42" width="20" height="18" rx="3"/></g>
        <circle id="led" cx="132" cy="34" r="5" fill="#6cc08f"/></svg>
      <div><div style="font-size:46px;font-weight:800;letter-spacing:-1px">PoE svič WK-PS206(V2)</div><div style="font-size:34px;font-weight:600;color:#2f7a50">4 porta · napaja kamere</div></div>
    </div>
    <div class="abs note" id="an" style="left:80px;top:1300px;width:920px">Do 100 m mrežnog kabla od sviča do kamere.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs note" id="d0" style="left:80px;top:220px;font-size:40px">Kupljeno pojedinačno</div>
    <div class="abs h1" id="d1" style="left:80px;top:280px;font-size:124px;color:#c9dbd0;white-space:nowrap"><span id="d1v">0</span> RSD<div id="strike" class="abs" style="left:-10px;top:66px;height:14px;width:0;background:#ff7b7b;border-radius:7px"></div></div>
    <div class="abs note" id="d2" style="left:80px;top:520px;font-size:40px">U kompletu</div>
    <div class="abs h1 green" id="d3" style="left:80px;top:580px;font-size:150px;white-space:nowrap">38.100 RSD</div>
    <div class="abs" id="d4" style="left:80px;top:860px;width:920px;height:260px;border-radius:34px;background:#fff;color:#123528;display:flex;flex-direction:column;justify-content:center;padding:0 50px"><div style="font-size:40px;font-weight:600;color:#5d6b64">Uštedite u kompletu</div><div style="font-size:88px;font-weight:800;color:#2f7a50;letter-spacing:-2px;white-space:nowrap"><span id="d4v">0</span> RSD <span style="font-size:56px">(22%)</span></div></div>
    <div class="abs note" id="d5" style="left:80px;top:1170px;width:920px">Cene sa stranice kompleta, sa PDV-om.</div>
  </div>''',
  js='''const CT=[1.2,1.6,2.0,2.4,4.6,6.6,8.6];
function renderF(t){
  if(t<11.6){const l=t<1.1?'':t<4.5?'Kamera IPC-B120HA-LUC<br><span class="green">4 komada · 2 MP, IP67</span>':t<6.5?'Snimač NVR-104H-D<br><span class="green">4 kanala · do 6 MP</span>':t<8.5?'Hard disk WD Purple<br><span class="green">1 TB, već u kompletu</span>':'Slika i napajanje<br><span class="green">kroz isti mrežni kabl</span>';
    $('al').innerHTML=l;pop($('al'),t,[1.2,4.6,6.6,8.6].filter(a=>t>=a-.1).pop()||99,{dx:-60,dy:0,s0:1});
    const n=CT.filter(a=>t>=a).length;$('ac').textContent=n;
    {let pulse=0;for(const b of CT){const d=t-b;if(d>=0&&d<.3)pulse=Math.max(pulse,(1-d/.3)*.25);}tf($('ac'),{s:(t<.8?eob(P(t,.3,.4)):1)+pulse,o:clamp((t-.3)*4,0,1)});}
    for(let i=0;i<4;i++){fly($('i'+i),t,CT[i],{y0:-700,r0:(i%2?25:-25),d:.42});if(t>CT[i]+.5)$('i'+i).style.transform+=` translateY(${Math.sin(t*2.4+i)*5}px)`;}
    fly($('i4'),t,4.6,{x0:-900,y0:0,r0:-10,d:.6});if(t>5.3)$('i4').style.transform+=` translateY(${Math.sin(t*2.1)*6}px)`;
    fly($('i5'),t,6.6,{x0:900,y0:0,r0:15,d:.6});if(t>7.3)$('i5').style.transform+=` translateY(${Math.sin(t*2.3)*6}px)`;
    fly($('i6'),t,8.6,{x0:-1000,y0:0,r0:-6,d:.6});if(t>9.3)$('i6').style.transform+=` translateY(${Math.sin(t*2.0)*5}px)`;
    $('led').setAttribute('opacity',String(.35+.65*Math.abs(Math.sin(t*4))));
    pop($('an'),t,9.6,{dy:30,s0:1});
    if(t>=11){const q=eio(P(t,11,.5));['i0','i1','i2','i3','i4','i5','i6','an'].forEach(id=>{$(id).style.transform+=` scale(${1-q*.3})`;$(id).style.opacity=String(1-q);});}}
  if(t>=11.4&&t<15.6){pop($('d0'),t,11.6,{dx:-60,dy:0,s0:1});pop($('d1'),t,11.7,{dx:-60,dy:0,s0:1});$('d1v').textContent=fmt(count(t,11.8,1.0,48710));
    $('strike').style.width=(eio(P(t,13.0,.35))*700)+'px';
    pop($('d2'),t,13.4,{dx:-60,dy:0,s0:1});slam($('d3'),t,13.6,{s0:1.8,d:.3});
    pop($('d4'),t,14.2,{dy:80,s0:.85});$('d4v').textContent=fmt(count(t,14.3,.8,10610));pop($('d5'),t,14.6,{dy:20,s0:1});}
}''',
  pops=[1.2, 1.6, 2.0, 2.4, 4.6, 6.6, 8.6, 9.6, 11.6, 11.7, 13.4, 14.2, 14.6], impacts=[1.2, 4.6, 6.6, 8.6, 13.6],
  extra=[('swish', 13.0, .3), ('confirm', 15.0, .2)])

# ============================================================ EZVIZ CS-H3c 2K+ Color (f2, problem -> rešenje)
YARD = '''<svg class="abs" id="%s" style="left:80px;top:470px" width="920" height="700" viewBox="0 0 920 700">
      <defs><clipPath id="%sk"><rect x="0" y="0" width="920" height="700" rx="30"/></clipPath>
        <radialGradient id="%sl" cx="0.5" cy="0" r="1"><stop offset="0" stop-color="#fffbe8" stop-opacity=".75"/><stop offset="1" stop-color="#fffbe8" stop-opacity="0"/></radialGradient></defs>
      <g clip-path="url(#%sk)">
        <rect width="920" height="700" fill="%s"/>
        <rect y="470" width="920" height="230" fill="%s"/>
        <rect x="60" y="150" width="20" height="330" fill="%s"/><rect x="840" y="150" width="20" height="330" fill="%s"/>
        <g fill="%s"><rect x="80" y="300" width="760" height="12"/><rect x="80" y="400" width="760" height="12"/></g>
        <g id="%scar" transform="translate(470 470)">
          <path d="M-250 0 L-250 -70 Q-240 -100 -190 -110 L-120 -170 Q-100 -185 -60 -185 L90 -185 Q130 -185 150 -165 L210 -110 Q250 -100 255 -70 L255 0 Z" fill="%s"/>
          <path d="M-105 -115 L-55 -160 L20 -160 L20 -115 Z M40 -115 L40 -160 L95 -160 Q120 -160 135 -145 L165 -115 Z" fill="%s"/>
          <circle cx="-150" r="48" fill="#222"/><circle cx="150" r="48" fill="#222"/><circle cx="-150" r="20" fill="#888"/><circle cx="150" r="20" fill="#888"/></g>
        <g id="%sman" transform="translate(800 470)"><circle cy="-235" r="34" fill="%s"/><path d="M-50 -195 Q0 -210 50 -195 L60 -80 L-60 -80 Z" fill="%s"/><rect x="-45" y="-82" width="38" height="82" fill="%s"/><rect x="7" y="-82" width="38" height="82" fill="%s"/></g>
        %s
      </g>
      <rect x="4" y="4" width="912" height="692" rx="28" fill="none" stroke="rgba(255,255,255,.5)" stroke-width="8"/>
    </svg>'''
def yard(i, color, extra=''):
    if color:  # u boji, osvetljeno belim svetlom
        c = ('#2b3b46', '#4a5a3a', '#7a6a55', '#7a6a55', '#8a7a62', '#c0392b', '#9fc6dd', '#e0b48c', '#2f6db5', '#2b3550', '#2b3550')
    else:      # IR: sivo
        c = ('#1a1d1c', '#3a3d3c', '#5a5d5c', '#5a5d5c', '#555857', '#6e7170', '#a3a6a5', '#8a8d8c', '#777a79', '#5f6261', '#5f6261')
    return YARD % (i, i, i, i, c[0], c[1], c[2], c[3], c[4], i, c[5], c[6], i, c[7], c[8], c[9], c[10], extra)

R['h3c'] = dict(
  style='cinematic', key=9, seed=5396,
  tag='WI-FI KAMERA ZA DVORIŠTE', hook=hook('Ako noću vidiš samo sivo, uključi boju.', (5, 6), 6), hsize=116, subtop=1100,
  sub='Ova kamera i noću snima u boji.', p=('Wi-Fi kamera', 'za dvorište'),
  inc='Napajanje 12 V iz utičnice, nema bateriju', price='7.020', img='assets/cam.png',
  scn=[['a', 0, 4], ['b', 4, 8.5], ['c', 8.5, 12.5], ['d', 12.5, 15.5]],
  slams=[0, 4, 8.5, 12.5, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Noću, sa IR:</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:104px">sve je sivo.</div>
    ''' + yard('ya', False, '<text id="qq" x="460" y="140" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="64" fill="#ffffff">Koje je boje auto?</text>') + '''
    <div class="abs note" id="a3" style="left:80px;top:1210px;width:920px">Primer, ilustracija.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">CS-H3c pali</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">belo svetlo.</div>
    <svg class="abs" id="beam" style="left:80px;top:440px" width="920" height="560" viewBox="0 0 920 560">
      <defs><linearGradient id="bg1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fffbe8" stop-opacity=".85"/><stop offset="1" stop-color="#fffbe8" stop-opacity="0"/></linearGradient></defs>
      <path id="beamp" d="M330 270 L920 20 L920 520 Z" fill="url(#bg1)"/>
    </svg>
    <div class="disc" id="bd" style="left:80px;top:480px;width:460px;height:460px"><img src="assets/cam.png" style="left:30px;top:30px;width:400px;height:400px"></div>
    <div class="abs h1" id="bm" style="left:80px;top:1010px;font-size:150px;white-space:nowrap"><span id="bmv">0</span> m</div>
    <div class="abs note" id="bn" style="left:84px;top:1170px;font-size:44px;font-weight:700;color:#fff">domet belog svetla</div>
    <div class="chip" id="b3" style="left:80px;top:1250px">umesto infracrvenog</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:104px">Noću u boji:</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:96px">odeća i vozilo.</div>
    ''' + yard('yc', True) + '''
    <div class="chip" id="c3" style="left:80px;top:1210px">ulaz u dvorište, ispred radnje</div>
    <div class="abs note" id="c4" style="left:80px;top:1320px;width:920px">Primer, ilustracija.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">I još, uz</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">jednu kameru:</div>
    <div class="row" id="r1" style="top:500px"><span class="chk">✓</span><span>2K+ <span class="green">· 2560 × 1440</span></span></div>
    <div class="row" id="r2" style="top:640px"><span class="chk">✓</span><span>Kadar <span class="green">· 98° dijagonalno</span></span></div>
    <div class="row" id="r3" style="top:780px"><span class="chk">✓</span><span>IP67 <span class="green">· od -30 do 50 °C</span></span></div>
    <div class="row" id="r4" style="top:920px"><span class="chk">✓</span><span>microSD <span class="green">· do 512 GB</span></span></div>
    <div class="row" id="r5" style="top:1060px"><span class="chk">✓</span><span>Wi-Fi 2,4 GHz <span class="green">· i RJ45 port</span></span></div>
  </div>''',
  js='''function renderF(t){
  if(t>=0&&t<4.1){$('dark').style.opacity=.75;pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.45);pop($('ya'),t,.3,{dy:60,s0:.92});
    $('yacar').setAttribute('transform',`translate(${470+Math.sin(t*1.3)*6} 470)`);
    {const p=eob(P(t,1.3,.4));const q=$('qq');q.setAttribute('opacity',String(clamp(p*2,0,1)));q.setAttribute('transform',`translate(0 ${Math.sin(t*3)*6})`);}
    pop($('a3'),t,2.4,{dy:24,s0:1});}
  if(t>=3.9&&t<8.6){$('dark').style.opacity=.55;pop($('b1'),t,4.1,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.45);
    {const hp=P(t,4.3,.6),he=eob(hp);tf($('bd'),{s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-70,0,eoc(hp))+Math.sin(t*2.2)*12,y:Math.sin(t*2)*6});}
    {const bp=eoc(P(t,5.0,.5));$('beam').style.opacity=String(bp*(.8+.2*Math.sin(t*6)));$('beam').style.transform=`scaleX(${lerp(.3,1,bp)})`;$('beam').style.transformOrigin='330px 270px';}
    pop($('bm'),t,5.3,{dy:30,s0:.9});$('bmv').textContent=count(t,5.3,1.2,30);
    {const d=t-6.5;if(d>=0&&d<.3)$('bm').style.transform+=` scale(${1+.15*(1-d/.3)})`;}
    pop($('bn'),t,5.6,{dy:20,s0:1});pop($('b3'),t,6.6,{dy:40,s0:.8});}
  if(t>=8.3&&t<12.6){$('dark').style.opacity=.35;pop($('c1'),t,8.55,{dx:-90,dy:0,s0:1});slam($('c2'),t,8.9);pop($('yc'),t,8.7,{dy:60,s0:.92});
    $('yccar').setAttribute('transform',`translate(${470+Math.sin(t*1.3)*6} 470)`);
    $('ycman').setAttribute('transform',`translate(${800+Math.sin(t*2)*8} ${470-Math.abs(Math.sin(t*3))*6})`);
    pop($('c3'),t,10.0,{dy:40,s0:.8});pop($('c4'),t,10.5,{dy:20,s0:1});}
  if(t>=12.3&&t<15.6){pop($('d1'),t,12.55,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.75,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4','r5'].forEach((id,i)=>{pop($(id),t,13.0+i*.35,{dx:-80,dy:0,s0:1});const c=$(id).firstElementChild;c.style.transform=`scale(${eob(P(t,13.15+i*.35,.3))})`;});}
}''',
  pops=[.05, .3, 1.3, 2.4, 4.1, 5.3, 5.6, 6.6, 8.55, 8.7, 10.0, 10.5, 12.55, 12.75, 13.0, 13.35, 13.7, 14.05, 14.4],
  impacts=[.45, 4.45, 8.9], extra=[('riser', 4.6, .1, 1.6), ('confirm', 6.5, .2), ('swish', 9.2, .15)])

IMGS = {'kit': {'kit.jpg': 'komplet-video-nadzora-hilook-4-bullet-ip-ipc-b120ha-luc-nvr-104h-d.jpg', 'cam.jpg': '777.jpg',
                'nvr.jpg': '555.jpg', 'hdd.webp': 'px-3861-1.webp'},
        'h3c': {'cam.png': 'cs-h3c-2k-ezviz-wi-fi-kamera-4mp-2-8mm-color.png'}}
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
