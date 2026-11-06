"""Gradi 2 reela za 04.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
import json, os, sys, shutil
GEN = os.path.expanduser('~/sr/templates/formati-demo/gen.py')
src = open(GEN, encoding='utf-8').read()
head, build = src.split('# ---------------------------------------------------------------- build')
g = {'__file__': GEN}
exec(head, g)
exec(build.split('for k, f in F.items():')[0], g)
hook, BASE, sfx_for, CAMDOT = g['hook'], g['BASE'], g['sfx_for'], g['CAMDOT']

FONTS = ''.join(
    f"@font-face{{font-family:'Poppins';font-weight:{w};src:url(assets/fonts/poppins-{s}-{w}-normal.woff2) format('woff2');unicode-range:{r}}}"
    for w in (400, 500, 600, 700, 800)
    for s, r in (('latin', 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD,U+2713,U+2715'),
                 ('latin-ext', 'U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF')))
IMGDIR = os.path.expanduser('~/img')
R = {}

# ============================================================ IP KOMPLETI turret vs bullet (f4, A ili B)
def rowscene(sid, head, a_big, a_small, b_big, b_small, extra='', bsize=66):
    box = 'position:absolute;top:470px;width:445px;height:620px;border-radius:34px;padding:40px 34px;display:flex;flex-direction:column;justify-content:center'
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs h1" id="{sid}h" style="left:80px;top:220px;font-size:110px">{head}</div>
    <div id="{sid}A" style="{box};left:80px;background:#fff;color:#123528"><div style="font-size:30px;font-weight:800;color:#2f7a50;letter-spacing:3px">A · TURRET</div><div id="{sid}Av" style="font-size:{bsize}px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{a_big}</div><div id="{sid}A2" style="font-size:32px;color:#5d6b64;font-weight:500;margin-top:22px;line-height:1.3">{a_small}</div></div>
    <div id="{sid}B" style="{box};left:555px;background:rgba(255,255,255,.08);border:3px solid #6cc08f"><div style="font-size:30px;font-weight:800;color:#6cc08f;letter-spacing:3px">B · BULLET</div><div id="{sid}Bv" style="font-size:{bsize}px;font-weight:800;line-height:1.05;margin-top:26px;letter-spacing:-1px">{b_big}</div><div id="{sid}B2" style="font-size:32px;color:#c9dbd0;font-weight:500;margin-top:22px;line-height:1.3">{b_small}</div></div>
    {extra}
  </div>'''

SAME = [('4 kamere', '2 MP, objektiv 2.8 mm'), ('Snimač NVR-104H-D', '4 kanala, kamere do 6 MP'), ('PoE svič', 'slika i struja kroz 1 mrežni kabl'),
        ('Disk WD Purple 1 TB', 'snimač prima disk do 6 TB'), ('IP67 i mikrofon', 'na kamerama oba kompleta')]
same_html = ''.join(
    f'<div class="row" id="cr{i}" style="top:{430 + i * 150}px"><span class="chk">✓</span><div><div style="font-size:46px;font-weight:800;line-height:1.1">{a}</div><div style="font-size:30px;color:#c9dbd0;font-weight:500">{b}</div></div></div>'
    for i, (a, b) in enumerate(SAME))

R['poredjenje-ip-kompleta-turret-bullet'] = dict(
  tag='IP KOMPLET VIDEO NADZORA', hook=hook('Biraš IP komplet sa 4 kamere?', (1, 2, 4), 2), hsize=128, subtop=1080,
  sub='Ista cena, isti snimač. Razlika je u kameri.', p=('Komplet A', '4x turret IP'),
  inc='✓  Uštedite u kompletu 10.610 RSD (22%)', price='38.100', img='assets/kit.jpg',
  imgs={'a.jpg': '888.jpg', 'b.jpg': '777.jpg', 'kit.jpg': 'komplet-video-nadzora-hilook-4-turret-ip-ipc-t220ha-luc-nvr-104h-d.jpg'},
  scn=[['a', 0, 3.5], ['b', 3.5, 8], ['c', 8, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.0, 3.5, 8, 11.5, 13.4, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="tile" id="aA" style="left:60px;top:330px;width:460px;height:560px"><img src="assets/a.jpg" style="left:30px;top:20px;width:400px;height:400px"><div class="abs" style="left:0;top:445px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">A · Turret</div><div class="abs" style="left:0;top:498px;width:460px;text-align:center;font-size:26px;color:#5d6b64">4x IPC-T220HA-LUC</div></div>
    <div class="tile" id="aB" style="left:560px;top:330px;width:460px;height:560px"><img src="assets/b.jpg" style="left:30px;top:20px;width:400px;height:400px"><div class="abs" style="left:0;top:445px;width:460px;text-align:center;font-size:40px;font-weight:800;color:#123528">B · Bullet</div><div class="abs" style="left:0;top:498px;width:460px;text-align:center;font-size:26px;color:#5d6b64">4x IPC-B120HA-LUC</div></div>
    <div class="abs" id="vs" style="left:420px;top:520px;width:240px;height:240px;border-radius:50%;background:#2f7a50;border:8px solid #fff;display:flex;align-items:center;justify-content:center;font-size:96px;font-weight:800;box-shadow:0 20px 50px rgba(0,0,0,.5)">VS</div>
    <div class="abs h1" id="a3" style="left:0;width:1080px;text-align:center;top:970px;font-size:64px">IP komplet video nadzora</div>
    <div class="abs note" id="a4" style="left:0;width:1080px;text-align:center;top:1060px">HiLook · 4 kamere · oba na stanju</div>
  </div>
  ''' + rowscene('b', 'Noću', 'Bez odsjaja', 'nema staklenu kupolu, IC svetlo ne odsjaji u snimku', 'Smart Hybrid Light', 'osvetljenje na kameri', bsize=56)
      + '''
  <div class="scene" id="c">
    <div class="abs h1" id="ch" style="left:80px;top:220px;font-size:110px">Isto u <span class="green">oba</span></div>
    ''' + same_html + '''
  </div>'''
      + rowscene('d', 'Cena', '38.100', 'RSD sa PDV-om', '38.100', 'RSD sa PDV-om',
                 '<div class="abs note" id="dn" style="left:0;width:1080px;text-align:center;top:1120px">U oba kompleta ušteda je 10.610 RSD (22%).</div>'
                 '<div class="abs h1" id="dq" style="left:0;width:1080px;text-align:center;top:1200px;font-size:76px">Napiši u komentar: <span class="green">A ili B?</span></div>'),
  js='''function rowS(p,t,a){pop($(p+'h'),t,a,{dx:-90,dy:0,s0:1});pop($(p+'A'),t,a+.4,{dx:-300,dy:0,s0:.95,ry0:-30});pop($(p+'B'),t,a+.9,{dx:300,dy:0,s0:.95,ry0:30});}
function renderF(t){
  if(t<3.6){fly($('aA'),t,.05,{x0:-700,y0:0,r0:-12});fly($('aB'),t,.35,{x0:700,y0:0,r0:12});const q=P(t,1.0,.3);tf($('vs'),{s:lerp(3,1,eoc(q))+.04*Math.sin(t*6),o:clamp(q*3,0,1),r:lerp(-90,0,eoc(q))});
    if(t>1)['aA','aB'].forEach((id,i)=>$(id).style.transform+=` translateY(${Math.sin(t*2.2+i*2)*7}px)`);
    pop($('a3'),t,1.6,{dy:40,s0:.9});pop($('a4'),t,2.1,{dy:20,s0:1});}
  if(t>=3.4&&t<8.1){rowS('b',t,3.6);pop($('bA2'),t,5.3,{dy:30,s0:.9});pop($('bB2'),t,5.8,{dy:30,s0:.9});}
  if(t>=7.9&&t<11.6){pop($('ch'),t,8.05,{dx:-90,dy:0,s0:1});
    for(let i=0;i<5;i++){const a=8.4+i*.42;pop($('cr'+i),t,a,{dx:-160,dy:0,s0:.95});const k=$('cr'+i).querySelector('.chk');const q=eob(P(t,a+.15,.3));k.style.transform=`scale(${q})`;}}
  if(t>=11.4&&t<15.6){rowS('d',t,11.6);
    const a=count(t,12.0,.9,38100),b=count(t,12.5,.9,38100);$('dAv').textContent=fmt(a);$('dBv').textContent=fmt(b);
    pop($('dn'),t,13.0,{dy:20,s0:1});
    const q=P(t,13.4,.4);tf($('dq'),{s:lerp(1.5,1,eoc(q))+.03*Math.sin(t*5),o:clamp(q*3,0,1)});}
}''',
  pops=[.05, .35, 1.6, 3.6, 4.0, 4.5, 5.3, 5.8, 8.05, 8.4, 8.82, 9.24, 9.66, 10.08, 11.6, 12.0, 12.5, 13.0], impacts=[1.0, 13.4])

# ============================================================ EZVIZ CS-H5 4G (f5, Za koga je)
def persona(sid, label, title, sub, svg):
    return f'''
  <div class="scene" id="{sid}">
    <div class="abs tag" id="{sid}l" style="left:80px;top:200px;font-size:44px">{label}</div>
    <div class="abs h1" id="{sid}t" style="left:80px;top:270px;width:920px;font-size:92px">{title}</div>
    <div class="card" id="{sid}c" style="left:80px;top:520px;width:920px;height:640px;background:#e6f2ea">{svg}</div>
    <div class="abs sub" id="{sid}s" style="left:80px;top:1210px;width:920px">{sub}</div>
  </div>'''
TOWER = '<g transform="translate(760 150)"><path d="M0 0 L-40 320 M0 0 L40 320 M-30 240 L30 240 M-20 160 L20 160 M-10 80 L10 80" stroke="#123528" stroke-width="8" fill="none"/><circle r="12" fill="#2f7a50"/><g id="sig" fill="none" stroke="#2f7a50" stroke-width="8" stroke-linecap="round"><path d="M-40 -30 A50 50 0 0 1 40 -30"/><path d="M-70 -55 A90 90 0 0 1 70 -55"/><path d="M-100 -80 A130 130 0 0 1 100 -80"/></g></g>'
WARE = ('<svg width="920" height="640" viewBox="0 0 920 640"><rect y="500" width="920" height="140" fill="#cfe6d8"/>'
        '<path d="M80 500 L80 270 L330 170 L580 270 L580 500 Z" fill="#fff" stroke="#123528" stroke-width="8"/>'
        '<rect x="230" y="340" width="200" height="160" fill="#2f7a50"/>' + ''.join(f'<line x1="230" y1="{y}" x2="430" y2="{y}" stroke="#6cc08f" stroke-width="5"/>' for y in (370, 400, 430, 460))
        + '<g id="aC">' + CAMDOT % (560, 285) + '</g>'
        + '<g transform="translate(150 110)"><g id="nowifi"><circle r="46" fill="#fff" stroke="#d64545" stroke-width="7"/><path d="M-22 4 A30 30 0 0 1 22 4 M-10 16 A14 14 0 0 1 10 16" stroke="#123528" stroke-width="7" fill="none" stroke-linecap="round"/><line x1="-30" y1="-30" x2="30" y2="30" stroke="#d64545" stroke-width="8" stroke-linecap="round"/></g></g>'
        + TOWER + '<text x="30" y="620" font-family="Poppins" font-weight="500" font-size="26" fill="#5d6b64">Primer, ilustracija</text></svg>')
FARM = ('<svg width="920" height="640" viewBox="0 0 920 640"><rect y="500" width="920" height="140" fill="#b9dcc6"/>'
        '<path d="M260 500 L260 290 L460 170 L660 290 L660 500 Z" fill="#fff" stroke="#123528" stroke-width="8"/>'
        '<rect x="390" y="360" width="140" height="140" fill="#2f7a50"/><path d="M390 360 L530 500 M530 360 L390 500" stroke="#6cc08f" stroke-width="7"/>'
        '<rect x="420" y="230" width="80" height="60" fill="#6cc08f"/>' + CAMDOT % (640, 300)
        + '<g id="rain" stroke="#439665" stroke-width="6" stroke-linecap="round">' + ''.join(f'<line x1="{x}" y1="{y}" x2="{x - 14}" y2="{y + 40}"/>' for x, y in
          [(60, 40), (140, 120), (220, 20), (300, 90), (380, 50), (560, 70), (640, 20), (720, 110), (800, 40), (870, 140), (100, 230), (760, 230), (860, 300), (40, 330)]) + '</g>'
        + '<g transform="translate(150 300)"><rect x="-70" y="-46" width="140" height="92" rx="20" fill="#2f7a50"/><text y="16" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="44" fill="#fff">IP67</text></g>'
        + '<text x="30" y="620" font-family="Poppins" font-weight="500" font-size="26" fill="#5d6b64">Primer, ilustracija</text></svg>')
BUILD = ('<svg width="920" height="640" viewBox="0 0 920 640"><rect width="920" height="640" fill="#0f241b"/>'
        '<circle cx="800" cy="90" r="42" fill="#e9f3ec"/><circle cx="782" cy="78" r="42" fill="#0f241b"/>'
        '<g id="stars" fill="#e9f3ec">' + ''.join(f'<circle cx="{x}" cy="{y}" r="4"/>' for x, y in [(120, 60), (260, 120), (420, 50), (560, 100), (660, 40), (340, 190)]) + '</g>'
        '<rect y="520" width="920" height="120" fill="#1b4636"/>'
        '<defs><linearGradient id="bm" x1="0" x2="1"><stop offset="0" stop-color="#fff6dc" stop-opacity=".55"/><stop offset="1" stop-color="#fff6dc" stop-opacity="0"/></linearGradient></defs>'
        '<path id="beam" d="M150 250 L880 360 L880 620 L150 330 Z" fill="url(#bm)" opacity="0"/>'
        '<g stroke="#9db5aa" stroke-width="7" fill="none"><rect x="420" y="300" width="300" height="220"/><path d="M420 300 L570 200 L720 300"/><line x1="420" y1="410" x2="720" y2="410"/><line x1="520" y1="300" x2="520" y2="520"/><line x1="620" y1="300" x2="620" y2="520"/></g>'
        '<g transform="translate(150 250)"><rect x="-26" y="-20" width="70" height="40" rx="10" fill="#fff"/><circle cx="40" r="12" fill="#6cc08f" id="led"/><line x1="0" y1="20" x2="0" y2="270" stroke="#9db5aa" stroke-width="10"/></g>'
        '<g id="ruler" transform="translate(150 560)"><line x1="0" y1="0" x2="0" y2="0" id="rl" stroke="#6cc08f" stroke-width="8" stroke-linecap="round"/><text id="rt" x="10" y="50" font-family="Poppins" font-weight="800" font-size="40" fill="#6cc08f">0 m</text></g>'
        '<text x="30" y="40" font-family="Poppins" font-weight="500" font-size="26" fill="#9db5aa">Primer, ilustracija</text></svg>')

R['ezviz-cs-h5-4g'] = dict(
  tag='KAMERA SA SIM KARTICOM', hook=hook('Ako nemaš internet, kamera nosi svoj.', (2, 4, 5), 4), hsize=112, subtop=1110,
  sub='Bez rutera i fiksnog priključka. Ide preko 4G.', p=('EZVIZ CS-H5', '4G kamera 3 MP'),
  inc='✓  Treba joj struja (12 V DC) i nano SIM', price='9.399', img='assets/cam.jpg',
  imgs={'cam.jpg': 'cs-h5-4g.jpg'},
  scn=[['a', 0, 4.5], ['b', 4.5, 9], ['c', 9, 13], ['d', 13, 15.5]],
  slams=[0, 4.5, 9, 13, 15.5, 18.5],
  html=persona('a', '1 · MAGACIN NA PERIFERIJI', 'Struja ima, <span class="green">interneta nema.</span>', 'Nano SIM umesto rutera i fiksnog priključka.', WARE)
    + persona('b', '2 · FARMA', 'Kiša i blato? <span class="green">IP67.</span>', 'Kućište podnosi i jaču kišu.', FARM)
    + persona('c', '3 · KUĆA U IZGRADNJI', 'Noću vidi <span class="green">do 30 m.</span>', 'Tri režima: puna boja, crno-belo i pametni.', BUILD)
    + '''
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:104px">Ista kamera.</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:300px;font-size:104px">Za sva tri.</div>
    <div class="disc" id="d3" style="left:250px;top:470px;width:580px;height:580px"><img src="assets/cam.jpg" style="left:40px;top:40px;width:500px;height:500px"></div>
    <div class="chip" id="d4" style="left:80px;top:1120px">Magacin</div><div class="chip" id="d5" style="left:330px;top:1120px">Farma</div><div class="chip" id="d6" style="left:540px;top:1120px">Kuća u izgradnji</div>
  </div>''',
  js='''function per(p,t,a){pop($(p+'l'),t,a,{dx:-60,dy:0,s0:1});slam($(p+'t'),t,a+.3,{s0:1.3});pop($(p+'c'),t,a+.5,{dy:200,s0:.85,d:.5,ry0:20});pop($(p+'s'),t,a+1.5,{dy:24,s0:1});}
function renderF(t){
  if(t<4.6){per('a',t,0);
    {const q=eob(P(t,1.2,.35));const n=$('nowifi');n.style.transformBox='fill-box';n.style.transformOrigin='center';n.style.transform=`scale(${q})`;}
    [...$('sig').children].forEach((c,i)=>{const on=t>1.9?(.25+.75*Math.max(0,Math.sin((t-1.9)*6-i*.9))):0;c.style.opacity=on;});
    {const g=$('aC');const q=eob(P(t,2.3,.3));g.style.transformBox='fill-box';g.style.transformOrigin='center';g.style.transform=`scale(${q})`;}}
  if(t>=4.4&&t<9.1){per('b',t,4.6);[...$('rain').children].forEach((c,i)=>c.setAttribute('transform',`translate(${-((t*90+i*37)%160)/4} ${((t*260+i*53)%300)})`));}
  if(t>=8.9&&t<13.1){per('c',t,9.1);
    const on=P(t,10.0,.4);$('beam').style.opacity=on*(.85+.15*Math.sin(t*6));$('led').setAttribute('fill',on>0?'#fff6dc':'#6cc08f');
    const r=eio(P(t,10.3,1.0));$('rl').setAttribute('x2',String(r*700));$('rt').textContent=Math.round(r*30)+' m';$('rt').setAttribute('x',String(10+r*560));
    [...$('stars').children].forEach((s,i)=>s.style.opacity=.35+.65*Math.abs(Math.sin(t*2+i)));}
  if(t>=12.9&&t<15.6){pop($('d1'),t,13.05,{dx:-90,dy:0,s0:1});slam($('d2'),t,13.3);
    const hp=P(t,13.1,.6),he=eob(hp);tf($('d3'),{y:lerp(300,0,he)+Math.sin(t*2)*10,s:lerp(.5,1,he),o:clamp(hp*3,0,1),ry:lerp(-60,0,eoc(hp))});
    ['d4','d5','d6'].forEach((id,i)=>pop($(id),t,13.8+i*.25,{dy:40,s0:.7}));}
}''',
  pops=[0, .5, 1.2, 2.3, 4.6, 5.1, 9.1, 9.6, 10.6, 13.05, 13.8, 14.05, 14.3], impacts=[.3, 4.9, 9.4, 13.3],
  extra=[('riser', 10.0, .12, .9)])

FD = '/tmp/fnt/package/files'
for k in sys.argv[1:] or R:
    f = R[k]; out = os.path.expanduser(f'~/work/{k}')
    os.makedirs(os.path.join(out, 'assets', 'fonts'), exist_ok=True)
    for w in (400, 500, 600, 700, 800):
        for s in ('latin', 'latin-ext'):
            shutil.copy(f'{FD}/poppins-{s}-{w}-normal.woff2', os.path.join(out, 'assets', 'fonts'))
    shutil.copy(os.path.expanduser('~/sr/templates/reel-v4/assets/supervision-ikonica-512.png'), os.path.join(out, 'assets'))
    for dst, srcf in f['imgs'].items():
        shutil.copy(os.path.join(IMGDIR, srcf), os.path.join(out, 'assets', dst))
    h = BASE.replace('<style>', '<style>' + FONTS, 1)
    for tok, val in [('%%TAG%%', f['tag']), ('%%HOOK%%', f['hook']), ('%%HSIZE%%', str(f['hsize'])), ('%%SUBTOP%%', str(f['subtop'])),
                     ('%%SUB%%', f['sub']), ('%%SCENES%%', f['html']), ('%%P1%%', f['p'][0]), ('%%P2%%', f['p'][1]),
                     ('%%INC%%', f['inc']), ('%%PRICE%%', f['price']),
                     ('%%SCN%%', json.dumps(f['scn'])), ('%%SLAMS%%', json.dumps(f['slams'])), ('%%JS%%', f['js'])]:
        h = h.replace(tok, val)
    h = h.replace('src="assets/kit.jpg"', f'src="{f["img"]}"') if 'kit.jpg' not in f['imgs'] else h
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
print('ok')
