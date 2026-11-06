"""Gradi 2 reela za 02.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
import json, os, sys, shutil
GEN = os.path.expanduser('~/sr/templates/formati-demo/gen.py')
src = open(GEN, encoding='utf-8').read()
head, build = src.split('# ---------------------------------------------------------------- build')
g = {'__file__': GEN}
exec(head, g)
exec(build.split('for k, f in F.items():')[0], g)
hook, BASE, sfx_for, NIGHT = g['hook'], g['BASE'], g['sfx_for'], g['NIGHT_YARD']

FONTS = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};src:url(assets/fonts/poppins-{s}-{w}-normal.woff2) format('woff2');unicode-range:{r}}}"
    for w in (400, 500, 600, 700, 800)
    for s, r in (('latin', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD,U+2713,U+2715'),
                 ('latin-ext', 'U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF')))

GA = '''<div class="gauge" id="g%d" style="left:%dpx;top:%dpx"><svg viewBox="-60 -60 120 120"><circle r="50" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="9"/><circle id="ga%d" r="50" fill="none" stroke="#6cc08f" stroke-width="9" stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="314" transform="rotate(-90)"/></svg><div class="gv" id="gv%d">%s</div><div class="gl">%s</div><div class="gs">%s</div></div>'''
R = {}

# ============================================================ SNIMAČ (f4, A ili B)
def rowscene(sid, head, a_big, a_small, b_big, b_small, extra=''):
    box = 'position:absolute;top:470px;width:445px;height:620px;border-radius:34px;padding:40px 34px;display:flex;flex-direction:column;justify-content:center'
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs h1" id="{sid}h" style="left:80px;top:220px;font-size:110px">{head}</div>
    <div id="{sid}A" style="{box};left:80px;background:#fff;color:#123528"><div style="font-size:30px;font-weight:800;color:#2f7a50;letter-spacing:3px">A · DVR-104G-K1</div><div id="{sid}Av" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{a_big}</div><div id="{sid}A2" style="font-size:32px;color:#5d6b64;font-weight:500;margin-top:22px;line-height:1.3">{a_small}</div></div>
    <div id="{sid}B" style="{box};left:555px;background:rgba(255,255,255,.08);border:3px solid #6cc08f"><div style="font-size:30px;font-weight:800;color:#6cc08f;letter-spacing:2px">B · iDS-7104HQHI</div><div id="{sid}Bv" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{b_big}</div><div id="{sid}B2" style="font-size:32px;color:#c9dbd0;font-weight:500;margin-top:22px;line-height:1.3">{b_small}</div></div>
    {extra}
  </div>'''

R['dvr'] = dict(
  tag='SNIMAČ ZA VIDEO NADZOR', hook=hook('Biraš snimač za 4 kamere?', (1, 3, 4), 1), hsize=128, subtop=1060,
  sub='Dva snimača, ista 4 kanala. Koji je tvoj?', p=('Snimač A', 'DVR-104G-K1'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='5.620', img='assets/a.jpg',
  scn=[['a', 0, 3.5], ['b', 3.5, 8], ['c', 8, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.0, 3.5, 8, 11.5, 13.2, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="tile" id="aA" style="left:60px;top:330px;width:460px;height:560px"><img src="assets/a.jpg" style="left:20px;top:10px;width:420px;height:420px"><div class="abs" style="left:0;top:445px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">A · HiLook</div><div class="abs" style="left:0;top:498px;width:460px;text-align:center;font-size:26px;color:#5d6b64">DVR-104G-K1</div></div>
    <div class="tile" id="aB" style="left:560px;top:330px;width:460px;height:560px"><div class="abs" style="left:0;top:0;width:460px;height:440px;overflow:hidden"><img src="assets/b.jpg" style="left:-110px;top:-110px;width:680px;height:680px"></div><div class="abs" style="left:0;top:445px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">B · Hikvision</div><div class="abs" style="left:0;top:498px;width:460px;text-align:center;font-size:26px;color:#5d6b64">iDS-7104HQHI-M1/S</div></div>
    <div class="abs" id="vs" style="left:420px;top:520px;width:240px;height:240px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:96px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.5)">VS</div>
    <div class="abs h1" id="a3" style="left:0;width:1080px;text-align:center;top:970px;font-size:64px">Snimač za video nadzor</div>
    <div class="abs note" id="a4" style="left:0;width:1080px;text-align:center;top:1060px">4 kanala · Turbo HD · oba na stanju</div>
  </div>
  ''' + rowscene('b', 'Rezolucija', '2 MP Lite', '4 analogne + 1 IP kamera', 'do 6 MP', 'snimci 5 MP i 6 MP')
      + rowscene('c', 'Za šta je', 'Početni', 'kuća, stan ili manja radnja', 'AcuSense', 'prepoznaje ljude i vozila',
                 '<div class="abs note" id="cn" style="left:80px;top:1150px;width:920px">Oba: 1 ležište za disk, HDMI i VGA, H.265 Pro+.</div>')
      + rowscene('d', 'Cena', '5.620', 'RSD sa PDV-om', '9.660', 'RSD sa PDV-om',
                 '<div class="abs h1" id="dq" style="left:0;width:1080px;text-align:center;top:1160px;font-size:76px">Napiši u komentar: <span class="green">A ili B?</span></div>'),
  js='''function rowS(p,t,a){pop($(p+'h'),t,a,{dx:-90,dy:0,s0:1});pop($(p+'A'),t,a+.4,{dx:-300,dy:0,s0:.95,ry0:-30});pop($(p+'B'),t,a+.9,{dx:300,dy:0,s0:.95,ry0:30});}
function renderF(t){
  if(t<3.6){fly($('aA'),t,.05,{x0:-700,y0:0,r0:-12});fly($('aB'),t,.35,{x0:700,y0:0,r0:12});const q=P(t,1.0,.3);tf($('vs'),{s:lerp(3,1,eoc(q))+.04*Math.sin(t*6),o:clamp(q*3,0,1),r:lerp(-90,0,eoc(q))});
    if(t>1)['aA','aB'].forEach((id,i)=>$(id).style.transform+=` translateY(${Math.sin(t*2.2+i*2)*7}px)`);
    pop($('a3'),t,1.6,{dy:40,s0:.9});pop($('a4'),t,2.1,{dy:20,s0:1});}
  if(t>=3.4&&t<8.1){rowS('b',t,3.6);pop($('bA2'),t,5.5,{dy:30,s0:.9});pop($('bB2'),t,6.0,{dy:30,s0:.9});}
  if(t>=7.9&&t<11.6){rowS('c',t,8.1);pop($('cn'),t,9.8,{dy:30,s0:1});}
  if(t>=11.4&&t<15.6){rowS('d',t,11.6);
    const a=count(t,12.0,.9,5620),b=count(t,12.5,.9,9660);$('dAv').textContent=fmt(a);$('dBv').textContent=fmt(b);
    const q=P(t,13.2,.4);tf($('dq'),{s:lerp(1.5,1,eoc(q))+.03*Math.sin(t*5),o:clamp(q*3,0,1)});}
}''',
  pops=[.05, .35, 1.6, 3.6, 4.0, 4.5, 5.5, 6.0, 8.1, 8.5, 9.0, 9.8, 11.6, 12.0, 12.5], impacts=[1.0, 13.2])

# ============================================================ KAMERA ColorVu (f2, Problem -> rešenje)
fence = ''.join(f'<line x1="{x}" y1="600" x2="{x}" y2="700"/>' for x in range(520, 920, 40))
CAR = '''<g id="%s" transform="translate(560 560)"><path d="M0 70 L20 20 Q30 0 60 0 L190 0 Q220 0 235 20 L270 70 L300 80 L300 130 L0 130 Z" fill="%s"/><rect x="40" y="12" width="80" height="50" rx="8" fill="#0b1a14" opacity=".7"/><rect x="135" y="12" width="85" height="50" rx="8" fill="#0b1a14" opacity=".7"/><circle cx="70" cy="135" r="28" fill="#0b1a14"/><circle cx="235" cy="135" r="28" fill="#0b1a14"/></g>'''
R['cam'] = dict(
  tag='KAMERA U BOJI NOĆU', hook=hook('Noću je svaki auto siv.', (0, 4), 4), hsize=132, subtop=1060,
  sub='Osim kad kamera ima belo svetlo.', p=('Kamera u boji', 'i noću'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='6.620', img='assets/cam.jpg',
  scn=[['a', 0, 4.5], ['b', 4.5, 9], ['c', 9, 12.5], ['d', 12.5, 15.5]],
  slams=[0, 4.5, 9, 12.5, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:96px">Obična IC kamera:</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:96px">noću crno-belo.</div>
    ''' + NIGHT % ('ya', fence, CAR % ('carA', '#8a8f8c') + '<text x="30" y="795" font-family="Poppins" font-weight="500" font-size="26" fill="#9db5aa">Primer, ilustracija</text>' + '<g id="qs" font-family="Poppins" font-weight="800" font-size="110" fill="#ff7b7b"><text id="q1" x="600" y="300">?</text><text id="q2" x="760" y="430">?</text></g>') + '''
    <div class="abs sub" id="a3" style="left:80px;top:1270px;width:920px">Koje boje je bio auto? Ne vidi se.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:96px">ColorVu:</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:96px">boja i noću.</div>
    ''' + NIGHT % ('yb', fence, '''<defs><radialGradient id="wl" cx="0" cy="0" r="1"><stop offset="0" stop-color="#fff6dc" stop-opacity=".6"/><stop offset="1" stop-color="#fff6dc" stop-opacity="0"/></radialGradient></defs>
      <text x="30" y="795" font-family="Poppins" font-weight="500" font-size="26" fill="#9db5aa">Primer, ilustracija</text>
      <path id="beam" d="M480 340 L920 480 L920 820 L480 820 Z" fill="url(#wl)" opacity="0"/>''' + CAR % ('carB', '#8a8f8c') + '''
      <g transform="translate(480 340)"><circle r="26" fill="#fff" stroke="#2f7a50" stroke-width="8"/><circle id="led" r="9" fill="#6cc08f"/></g>''') + '''
    <div class="chip" id="b3" style="left:80px;top:1270px">Belo LED svetlo do 40 m</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="cc1" style="left:80px;top:190px;font-size:96px">Ulaz, hodnik,</div>
    <div class="abs h1 green" id="cc2" style="left:80px;top:295px;font-size:96px">manje dvorište.</div>
    ''' + GA % (1, 80, 480, 1, 1, '0 m', 'Belo svetlo', 'boja noću') + GA % (2, 555, 480, 2, 2, '0 MP', 'Rezolucija', '1920 × 1080') + '''
    <div class="chip" id="cc3" style="left:80px;top:1000px">2.8 mm, širok ugao</div>
    <div class="chip" id="cc4" style="left:520px;top:1000px">IP67</div>
    <div class="chip" id="cc5" style="left:710px;top:1000px">mikrofon</div>
    <div class="abs note" id="cc6" style="left:80px;top:1130px;width:920px">Radi od −40 do 60 °C. Audio je jednosmeran, zvučnika nema.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Ide na</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">DVR ili XVR.</div>
    <div class="tile" id="d3" style="left:230px;top:440px;width:620px;height:560px"><img src="assets/cam.jpg" style="left:40px;top:10px;width:540px;height:540px"></div>
    <div class="chip" id="d4" style="left:80px;top:1060px">koaksijalni kabl</div>
    <div class="chip" id="d5" style="left:470px;top:1060px">TVI · AHD · CVI · CVBS</div>
    <div class="abs note" id="d6" style="left:80px;top:1190px;width:920px">NVR i PoE svič ne trebaju. Hikvision DS-2CE12DF3T-LFS.</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.6){$('dark').style.opacity=.8;pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.5);
    {const p=P(t,0,.6);$('ya').style.opacity=p;}
    $('carA').setAttribute('transform',`translate(${lerp(940,560,eoc(P(t,.6,1.2)))} 560)`);
    ['q1','q2'].forEach((id,i)=>{const p=eob(P(t,1.8+i*.5,.35));const el=$(id);el.style.opacity=clamp(p*2,0,1);el.style.transform=`translateY(${Math.sin(t*3+i)*8}px)`;});
    pop($('a3'),t,2.9,{dy:24,s0:1});}
  if(t>=4.4&&t<9.1){$('dark').style.opacity=.6;pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,5.0);
    const on=P(t,5.6,.4);$('beam').style.opacity=on*(.9+.1*Math.sin(t*7));$('led').setAttribute('fill',on>0?'#fff6dc':'#6cc08f');
    const c=eio(P(t,5.8,.8));const r=Math.round(lerp(138,214,c)),gg=Math.round(lerp(143,69,c)),b=Math.round(lerp(140,69,c));
    $('carB').querySelector('path').setAttribute('fill',`rgb(${r},${gg},${b})`);
    $('carB').setAttribute('transform',`translate(560 ${560+Math.sin(t*2)*3})`);
    pop($('b3'),t,6.6,{dy:30,s0:.9});}
  if(t>=8.9&&t<12.6){pop($('cc1'),t,9.05,{dx:-90,dy:0,s0:1});slam($('cc2'),t,9.3);
    [[9.6,.8],[10.1,.5]].forEach(([a,f],i)=>{pop($('g'+(i+1)),t,a,{dy:80,s0:.8,d:.4});const p=gauge('ga'+(i+1),t,a+.15,f);
      if(i==0)$('gv1').textContent=Math.round(p*40)+' m';if(i==1)$('gv2').textContent=Math.round(p*2)+' MP';});
    ['cc3','cc4','cc5'].forEach((id,i)=>pop($(id),t,10.7+i*.3,{dy:40,s0:.8}));pop($('cc6'),t,11.6,{dy:20,s0:1});}
  if(t>=12.4&&t<15.6){pop($('d1'),t,12.55,{dx:-90,dy:0,s0:1});slam($('d2'),t,12.8);
    pop($('d3'),t,12.7,{dy:200,s0:.8,d:.5,ry0:30});$('d3').style.transform+=` translateY(${Math.sin(t*2)*8}px)`;
    ['d4','d5'].forEach((id,i)=>pop($(id),t,13.4+i*.3,{dy:40,s0:.7}));pop($('d6'),t,14.1,{dy:20,s0:1});}
}''',
  pops=[.05, 1.8, 2.3, 2.9, 4.6, 6.6, 9.05, 9.6, 10.1, 10.7, 11.0, 11.3, 11.6, 12.55, 13.4, 13.7, 14.1], impacts=[.5, 5.0, 9.3, 12.8],
  extra=[('riser', 5.6, .14, 1.0), ('confirm', 6.4, .2)])

FD = '/tmp/fnt/package/files'
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
