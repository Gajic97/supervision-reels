"""Gradi 2 reela za 09.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
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

# ============================================================ Hikvision DS-2CE16H0T-ITF 5 MP (f8, greška pre kupovine) — BEZ CENE
DVR_SVG = '''<svg class="abs" id="aB" style="left:580px;top:520px" width="420" height="420" viewBox="0 0 420 420">
      <rect x="0" y="0" width="420" height="420" rx="34" fill="rgba(255,255,255,.06)" stroke="#439665" stroke-width="4" stroke-dasharray="14 10"/>
      <rect x="50" y="150" width="320" height="120" rx="18" fill="#dfe8e3"/><rect x="50" y="250" width="320" height="20" rx="6" fill="#b9c7bf"/>
      <circle cx="330" cy="190" r="9" fill="#2f7a50"/><rect x="80" y="182" width="140" height="14" rx="7" fill="#9fb0a7"/>
      <text x="210" y="340" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="46" fill="#ff8a80">1080p</text>
      <text x="210" y="110" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="34" fill="#c9dbd0">stari snimač</text>
    </svg>'''

def pix(gid, n, x0):
    # mreža piksela: n x n kvadrata u polju 380x380
    s = 380 / n
    cells = ''.join(f'<rect x="{x0 + i * s:.1f}" y="{j * s:.1f}" width="{s - 2:.1f}" height="{s - 2:.1f}" rx="2"/>' for i in range(n) for j in range(n))
    return f'<g id="{gid}">{cells}</g>'

R['cam'] = dict(
  style='lofi_chill', key=7, seed=911,
  tag='KAMERA ZA DVORIŠTE', hook=hook('Pre kamere od 5 MP, proveri snimač.', (3, 4, 6), 6), hsize=124, subtop=1180,
  sub='Greška koju je lako napraviti.', p=('Kamera za dvorište', '5 MP · Hikvision'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='', img='assets/cam.jpg', noprice=True,
  scn=[['a', 0, 4.5], ['b', 4.5, 8.5], ['c', 8.5, 12], ['d', 12, 15.5]],
  slams=[0, 2.0, 4.5, 8.5, 9.7, 12, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:100px">Kamera 5 MP,</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:100px">snimač 1080p.</div>
    <div class="tile" id="aA" style="left:80px;top:520px;width:420px;height:420px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:380px;height:380px"></div>
    ''' + DVR_SVG + '''
    <div class="abs h1 red" id="aq" style="left:490px;top:640px;width:100px;text-align:center;font-size:150px">?</div>
    <div class="abs sub" id="a3" style="left:80px;top:1010px;width:920px">Na 1080p snimaču slika se spušta na 2 MP.</div>
    <div class="abs note" id="a4" style="left:80px;top:1150px;width:920px">Snimač je primer, ilustracija.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:100px">Platiš 5 MP,</div>
    <div class="abs h1 red" id="b2" style="left:80px;top:300px;font-size:100px">gledaš 2 MP.</div>
    <svg class="abs" id="bpx" style="left:80px;top:500px" width="920" height="380" viewBox="0 0 920 380">
      <g fill="#6cc08f">''' + pix('pxA', 14, 0) + '''</g>
      <g fill="#ff8a80">''' + pix('pxB', 7, 540) + '''</g>
    </svg>
    <div class="abs h1" id="bl1" style="left:80px;top:900px;width:380px;text-align:center;font-size:64px"><span id="bv1">0</span> MP</div>
    <div class="abs h1 red" id="bl2" style="left:620px;top:900px;width:380px;text-align:center;font-size:64px"><span id="bv2">0</span> MP</div>
    <div class="abs note" id="b3" style="left:80px;top:1030px;width:920px">Primer: kamera 5 MP na 1080p snimaču. Šema je ilustracija.</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="c1" style="left:80px;top:190px;font-size:100px">Rešenje: snimač</div>
    <div class="abs h1 green" id="c2" style="left:80px;top:300px;font-size:100px">sa 5 MP ulazom.</div>
    <div class="tile" id="cA" style="left:330px;top:470px;width:420px;height:420px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:380px;height:380px"></div>
    <div class="abs" id="cok" style="left:660px;top:420px;width:170px;height:170px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:92px;font-weight:800">✓</div>
    <div class="chip" id="c3" style="left:80px;top:960px">ista koaksijalna instalacija</div>
    <div class="chip" id="c4" style="left:80px;top:1070px">bez prelaska na IP i novog kabla</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Pre kupovine</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">proveri:</div>
    <div class="row" id="r1" style="top:480px"><span class="chk">1</span><span>Snimač <span class="green">· 5 MP Turbo HD ulaz</span></span></div>
    <div class="row" id="r2" style="top:620px"><span class="chk">2</span><span>Noću <span class="green">· EXIR do oko 30 m</span></span></div>
    <div class="row" id="r3" style="top:760px"><span class="chk">3</span><span>Zvuk <span class="green">· nema, samo video</span></span></div>
    <div class="row" id="r4" style="top:900px"><span class="chk">4</span><span>Kućište <span class="green">· metal, za spolja</span></span></div>
    <div class="abs note" id="d3" style="left:80px;top:1060px;width:920px">Vrednosti za DS-2CE16H0T-ITF. Noću slika crno-bela.</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.6){pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.4);
    const s=Math.sin(t*14)*6*(t>2.0&&t<2.6?1:0);fly($('aA'),t,.6,{x0:-600,y0:0,r0:-15});fly($('aB'),t,.9,{x0:600,y0:0,r0:15});
    if(t>1.4){$('aA').style.transform+=` translateY(${Math.sin(t*2.2)*7}px) translateX(${s}px)`;$('aB').style.transform+=` translateY(${Math.sin(t*2.2+1.5)*7}px) translateX(${-s}px)`;}
    slam($('aq'),t,2.0,{s0:2.4});$('aq').style.transform+=` rotate(${Math.sin(t*5)*8}deg)`;pop($('a3'),t,2.6,{dy:24,s0:1});pop($('a4'),t,3.1,{dy:20,s0:1});}
  if(t>=4.4&&t<8.6){pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.9);
    const pa=$('pxA').children,pb=$('pxB').children;
    for(let i=0;i<pa.length;i++){const q=P(t,5.2+(i%14)*.03+Math.floor(i/14)*.02,.25);pa[i].style.opacity=clamp(q*2,0,1)*(0.55+0.45*Math.abs(Math.sin(i*1.7+t*2)));}
    for(let i=0;i<pb.length;i++){const q=P(t,5.9+(i%7)*.05+Math.floor(i/7)*.03,.25);pb[i].style.opacity=clamp(q*2,0,1)*(0.55+0.45*Math.abs(Math.sin(i*2.3+t*2)));}
    pop($('bl1'),t,5.6,{dy:40,s0:.9});pop($('bl2'),t,6.3,{dy:40,s0:.9});
    $('bv1').textContent=count(t,5.6,.6,5);$('bv2').textContent=Math.max(2,5-Math.round(eoc(P(t,6.4,.8))*3));
    pop($('b3'),t,7.0,{dy:20,s0:1});}
  if(t>=8.4&&t<12.1){pop($('c1'),t,8.55,{dx:-90,dy:0,s0:1});slam($('c2'),t,8.85);
    pop($('cA'),t,9.0,{dy:120,s0:.8,ry0:30});if(t>9.5)$('cA').style.transform+=` translateY(${Math.sin(t*2.3)*8}px) rotate(${Math.sin(t*1.6)*2}deg)`;
    const q=P(t,9.7,.3);tf($('cok'),{s:lerp(2.5,1,eoc(q))+.04*Math.sin(t*6),o:clamp(q*3,0,1)});
    pop($('c3'),t,10.2,{dx:-80,dy:0,s0:1});pop($('c4'),t,10.7,{dx:-80,dy:0,s0:1});}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.25,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4'].forEach((id,i)=>{pop($(id),t,12.6+i*.45,{dx:-80,dy:0,s0:1});const c=$(id).firstElementChild;c.style.transform=`scale(${eob(P(t,12.75+i*.45,.3))})`;});
    pop($('d3'),t,14.6,{dy:20,s0:1});}
}''',
  pops=[.05, .6, .9, 2.6, 3.1, 4.6, 5.6, 6.3, 7.0, 8.55, 9.0, 10.2, 10.7, 12.05, 12.25, 12.6, 13.05, 13.5, 13.95, 14.6],
  impacts=[.4, 2.0, 4.9, 9.7], extra=[('confirm', 9.75, .22), ('riser', 5.9, .1, 1.2)])

# ============================================================ HiLook NVR-104H-D vs NVR-108H-D (f4)
def rowscene(sid, head, a_big, a_small, b_big, b_small, extra=''):
    box = 'position:absolute;top:470px;width:445px;height:620px;border-radius:34px;padding:40px 34px;display:flex;flex-direction:column;justify-content:center'
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs h1" id="{sid}h" style="left:80px;top:220px;font-size:110px">{head}</div>
    <div id="{sid}A" style="{box};left:80px;background:#fff;color:#123528"><div style="font-size:30px;font-weight:800;color:#2f7a50;letter-spacing:2px">A · NVR-104H-D</div><div id="{sid}Av" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{a_big}</div><div id="{sid}A2" style="font-size:32px;color:#5d6b64;font-weight:500;margin-top:22px;line-height:1.3">{a_small}</div></div>
    <div id="{sid}B" style="{box};left:555px;background:rgba(255,255,255,.08);border:3px solid #6cc08f"><div style="font-size:30px;font-weight:800;color:#6cc08f;letter-spacing:2px">B · NVR-108H-D</div><div id="{sid}Bv" style="font-size:66px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{b_big}</div><div id="{sid}B2" style="font-size:32px;color:#c9dbd0;font-weight:500;margin-top:22px;line-height:1.3">{b_small}</div></div>
    {extra}
  </div>'''

TILE = lambda tid, left, img, lab, sub: f'<div class="tile" id="{tid}" style="left:{left}px;top:330px;width:460px;height:560px"><img src="assets/{img}" style="left:30px;top:20px;width:400px;height:400px"><div class="abs" style="left:0;top:445px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">{lab}</div><div class="abs" style="left:0;top:500px;width:460px;text-align:center;font-size:26px;color:#5d6b64">{sub}</div></div>'

R['nvr'] = dict(
  style='minimal_tech', key=2, seed=2887,
  tag='SNIMAČ ZA VIDEO NADZOR', hook=hook('Imaš 4 IP kamere ili planiraš više?', (1, 2, 3), 6), hsize=118, subtop=1180,
  sub='Dva HiLook NVR snimača, kamere do 6 MP.', p=('Snimač za', '4 IP kamere'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='7.860', img='assets/nvr4.jpg',
  scn=[['a', 0, 3.5], ['b', 3.5, 8], ['c', 8, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.0, 3.5, 8, 11.5, 13.2, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    ''' + TILE('aA', 60, 'nvr4.jpg', 'A · 4 kanala', 'NVR-104H-D') + TILE('aB', 560, 'nvr8.jpg', 'B · 8 kanala', 'NVR-108H-D') + '''
    <div class="abs" id="vs" style="left:420px;top:520px;width:240px;height:240px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:96px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.5)">VS</div>
    <div class="abs h1" id="a3" style="left:0;width:1080px;text-align:center;top:970px;font-size:64px">Snimač za video nadzor</div>
    <div class="abs note" id="a4" style="left:0;width:1080px;text-align:center;top:1060px">HiLook NVR · IP kamere do 6 MP · oba na stanju</div>
  </div>
  ''' + rowscene('b', 'Kanali', '<span id="bAn">0</span>', 'kuće, stanovi i manje firme', '<span id="bBn">0</span>', 'firme, prodavnice, šira pokrivenost kuće')
      + rowscene('c', 'Protok', '<span id="cAn">0</span> Mbps', 'dovoljno za 4 kamere', '<span id="cBn">0</span> Mbps', 'stabilan rad svih 8 kanala',
                 '<div class="abs note" id="cn" style="left:80px;top:1150px;width:920px">Oba: H.265+, HDMI i VGA, 1 ležište za disk, bez PoE.</div>')
      + rowscene('d', 'Cena', '7.860', 'RSD sa PDV-om', '10.000', 'RSD sa PDV-om',
                 '<div class="abs h1" id="dq" style="left:0;width:1080px;text-align:center;top:1160px;font-size:76px">Napiši u komentar: <span class="green">A ili B?</span></div>'),
  js='''function rowS(p,t,a){pop($(p+'h'),t,a,{dx:-90,dy:0,s0:1});pop($(p+'A'),t,a+.4,{dx:-300,dy:0,s0:.95,ry0:-30});pop($(p+'B'),t,a+.9,{dx:300,dy:0,s0:.95,ry0:30});}
function renderF(t){
  if(t<3.6){fly($('aA'),t,.05,{x0:-700,y0:0,r0:-12});fly($('aB'),t,.35,{x0:700,y0:0,r0:12});
    if(t>.6){$('aA').style.transform+=` translateY(${Math.sin(t*2.3)*7}px)`;$('aB').style.transform+=` translateY(${Math.sin(t*2.3+1.5)*7}px)`;}
    const q=P(t,1.0,.3);tf($('vs'),{s:lerp(3,1,eoc(q))+.04*Math.sin(t*6),o:clamp(q*3,0,1),r:lerp(-90,0,eoc(q))});
    pop($('a3'),t,1.6,{dy:40,s0:.9});pop($('a4'),t,2.1,{dy:20,s0:1});}
  if(t>=3.4&&t<8.1){rowS('b',t,3.6);$('bAn').textContent=count(t,4.1,.6,4)+' IP';$('bBn').textContent=count(t,4.6,.8,8)+' IP';
    pop($('bA2'),t,5.5,{dy:30,s0:.9});pop($('bB2'),t,6.0,{dy:30,s0:.9});}
  if(t>=7.9&&t<11.6){rowS('c',t,8.1);$('cAn').textContent=count(t,8.6,.8,40);$('cBn').textContent=count(t,9.1,.8,60);pop($('cn'),t,9.8,{dy:30,s0:1});}
  if(t>=11.4&&t<15.6){rowS('d',t,11.6);
    const a=count(t,12.0,.9,7860),b=count(t,12.5,.9,10000);$('dAv').textContent=fmt(a);$('dBv').textContent=fmt(b);
    const q=P(t,13.2,.4);tf($('dq'),{s:lerp(1.5,1,eoc(q))+.03*Math.sin(t*5),o:clamp(q*3,0,1)});}
}''',
  pops=[.05, .35, 1.6, 2.1, 3.6, 4.0, 4.5, 5.5, 6.0, 8.1, 8.5, 9.0, 9.8, 11.6, 12.0, 12.5], impacts=[1.0, 13.2])

IMGS = {'cam': {'cam.jpg': 'cam.jpg'}, 'nvr': {'nvr4.jpg': 'nvr4.jpg', 'nvr8.jpg': 'nvr8.jpg'}}
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
    if f.get('noprice'):  # Hikvision: Cena na upit (BRAND.md)
        rep = [
          ('<div id="odo" style="display:flex;font-variant-numeric:tabular-nums;line-height:110px;height:110px"></div><span>RSD</span><span style="font-size:34px;color:#5d6b64;font-weight:500;letter-spacing:0">sa PDV-om</span>',
           '<div id="odo" style="display:none"></div><span id="cnu" style="font-size:92px">Cena na upit</span>'),
          ('>Dodaj u korpu</div>', '>Zatraži ponudu</div>'),
          ("$('sPbt').textContent=done?'✓  Dodato u korpu':'Dodaj u korpu'", "$('sPbt').textContent=done?'✓  062/618-736':'Zatraži ponudu'"),
          ("pop($('sPinc'),t,16.5,{dy:30,s0:.9});", "pop($('cnu'),t,15.9,{dx:-60,dy:0,s0:1});pop($('sPinc'),t,16.5,{dy:30,s0:.9});"),
        ]
        for a, b in rep:
            assert a in h, a
            h = h.replace(a, b)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
    json.dump({'style': f['style'], 'key': f['key'], 'seed': f['seed']}, open(os.path.join(out, 'music.json'), 'w'))
print('ok')
