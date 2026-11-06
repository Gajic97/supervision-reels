"""Gradi 2 reela za 01.11.2026 na osnovu templates/formati-demo (base.html + pomoćne funkcije iz gen.py)."""
import json, os, sys
GEN = os.path.expanduser('~/sr/templates/formati-demo/gen.py')
src = open(GEN, encoding='utf-8').read()
head, build = src.split('# ---------------------------------------------------------------- build')
g = {'__file__': GEN}
exec(head, g)
exec(build.split('for k, f in F.items():')[0], g)
hook, BASE, sfx_for = g['hook'], g['BASE'], g['sfx_for']

R = {}

# ============================================================ KOMPLET (f6, Šta dobiješ)
R['kit'] = dict(
  tag='KOMPLET VIDEO NADZORA', hook=hook('4 kamere, snimač, disk i napajanje. Jedna cena.', (6, 7), 7), hsize=112, subtop=1140,
  sub='Brojimo deo po deo.', p=('Sve ovo', 'u kompletu'),
  inc='✓  Uštedite u kompletu 12.790 RSD (30%)', price='29.800', img='assets/kit.webp',
  scn=[['a', 0, 11.5], ['d', 11.5, 15.5]],
  slams=[0, 1.2, 1.9, 2.6, 3.3, 5.3, 7.3, 9.3, 11.5, 13.6, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="al" style="left:80px;top:200px;width:680px;font-size:50px;height:220px;line-height:1.15"></div>
    <div class="abs" id="ac" style="left:790px;top:190px;width:210px;height:210px;border-radius:50%;background:#2f7a50;border:6px solid #6cc08f;display:flex;align-items:center;justify-content:center;font-size:110px;font-weight:800">0</div>
    <div class="tile" id="i1" style="left:80px;top:450px;width:210px;height:210px"><img src="assets/cam.png" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i2" style="left:316px;top:450px;width:210px;height:210px"><img src="assets/cam.png" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i3" style="left:552px;top:450px;width:210px;height:210px"><img src="assets/cam.png" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i4" style="left:788px;top:450px;width:210px;height:210px"><img src="assets/cam.png" style="left:5px;top:5px;width:200px;height:200px"></div>
    <div class="tile" id="i5" style="left:80px;top:700px;width:400px;height:400px"><img src="assets/dvr.jpg" style="left:10px;top:10px;width:380px;height:380px"></div>
    <div class="tile" id="i6" style="left:510px;top:700px;width:240px;height:400px"><img src="assets/hdd.webp" style="left:0;top:80px;width:240px;height:240px"></div>
    <div class="tile" id="i7" style="left:780px;top:700px;width:220px;height:400px"><img src="assets/psu.webp" style="left:0;top:90px;width:220px;height:220px"></div>
    <div class="abs note" id="an" style="left:80px;top:1150px;width:920px">Uz to 4 DC i 4 BNC konektora. Kabl se kupuje po metru.</div>
  </div>
  <div class="scene" id="d">
    <div class="abs note" id="d0" style="left:80px;top:220px;font-size:40px">Kupljeno pojedinačno</div>
    <div class="abs h1" id="d1" style="left:80px;top:280px;font-size:130px;color:#c9dbd0"><span id="d1v">0</span> RSD<div id="strike" class="abs" style="left:-10px;top:68px;height:14px;width:0;background:#ff7b7b;border-radius:7px"></div></div>
    <div class="abs note" id="d2" style="left:80px;top:520px;font-size:40px">Komplet video nadzora</div>
    <div class="abs h1 green" id="d3" style="left:80px;top:580px;font-size:160px">29.800 RSD</div>
    <div class="abs" id="d4" style="left:80px;top:860px;width:920px;height:260px;border-radius:34px;background:#fff;color:#123528;display:flex;flex-direction:column;justify-content:center;padding:0 50px"><div style="font-size:40px;font-weight:600;color:#5d6b64">Uštedite u kompletu</div><div style="font-size:96px;font-weight:800;color:#2f7a50;letter-spacing:-2px"><span id="d4v">0</span> RSD <span style="font-size:60px">(30%)</span></div></div>
    <div class="abs note" id="d5" style="left:80px;top:1170px;width:920px">Cene sa super-vision.rs, sa PDV-om.</div>
  </div>''',
  js='''const LBL=[[1.2,'Kamera DS-2CE76D0T-LMFS','2 MP, 2.8 mm, mikrofon'],[5.3,'Snimač iDS-7104HQHI-M1/S','4 kanala, AcuSense'],[7.3,'Hard disk WD Purple','1 TB'],[9.3,'Napajanje XED-5013S','12 V 5 A, za sve kamere']];
function renderF(t){
  if(t<11.6){let cur=null;for(const x of LBL)if(t>=x[0]-.1)cur=x;$('al').innerHTML=cur?cur[1]+'<br><span class="green">'+cur[2]+'</span>':'';
    pop($('al'),t,cur?cur[0]:99,{dx:-60,dy:0,s0:1});
    const B=[1.2,1.9,2.6,3.3,5.3,7.3,9.3];let n=0;for(const b of B)if(t>=b)n++;$('ac').textContent=n;
    {let pulse=0;for(const b of B){const d=t-b;if(d>=0&&d<.3)pulse=Math.max(pulse,(1-d/.3)*.25);}tf($('ac'),{s:(t<.8?eob(P(t,.3,.4)):1)+pulse,o:clamp((t-.3)*4,0,1)});}
    fly($('i1'),t,1.2,{y0:-700,r0:-30});fly($('i2'),t,1.9,{y0:-700,r0:25});fly($('i3'),t,2.6,{y0:-700,r0:-20});fly($('i4'),t,3.3,{y0:-700,r0:30});
    fly($('i5'),t,5.3,{x0:-900,y0:0,r0:-10,d:.6});fly($('i6'),t,7.3,{x0:0,y0:900,r0:12,d:.6});fly($('i7'),t,9.3,{x0:900,y0:0,r0:15,d:.6});
    ['i1','i2','i3','i4','i5','i6','i7'].forEach((id,i)=>{if(t>[1.2,1.9,2.6,3.3,5.3,7.3,9.3][i]+.6)$(id).style.transform+=` translateY(${Math.sin(t*2.2+i)*5}px)`;});
    pop($('an'),t,10.0,{dy:20,s0:1});
    if(t>=11){const q=eio(P(t,11,.5));['i1','i2','i3','i4','i5','i6','i7'].forEach(id=>{$(id).style.transform+=` scale(${1-q*.3})`;$(id).style.opacity=String(1-q);});}}
  if(t>=11.4&&t<15.6){pop($('d0'),t,11.6,{dx:-60,dy:0,s0:1});pop($('d1'),t,11.7,{dx:-60,dy:0,s0:1});$('d1v').textContent=fmt(count(t,11.8,1.0,42590));
    $('strike').style.width=(eio(P(t,13.0,.35))*680)+'px';
    pop($('d2'),t,13.4,{dx:-60,dy:0,s0:1});slam($('d3'),t,13.6,{s0:1.8,d:.3});
    pop($('d4'),t,14.2,{dy:80,s0:.85});$('d4v').textContent=fmt(count(t,14.3,.8,12790));pop($('d5'),t,14.6,{dy:20,s0:1});}
}''',
  pops=[1.2, 1.9, 2.6, 3.3, 5.3, 7.3, 9.3, 10.0, 11.6, 11.7, 13.4, 14.2], impacts=[1.2, 5.3, 7.3, 9.3, 13.6], extra=[('swish', 13.0, .3), ('confirm', 15.0, .2)])

# ============================================================ KAMERA (f8, Greška pre kupovine)
GA = '''<div class="gauge" id="g%d" style="left:%dpx;top:%dpx"><svg viewBox="-60 -60 120 120"><circle r="50" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="9"/><circle id="ga%d" r="50" fill="none" stroke="#6cc08f" stroke-width="9" stroke-linecap="round" stroke-dasharray="314" stroke-dashoffset="314" transform="rotate(-90)"/></svg><div class="gv" id="gv%d">%s</div><div class="gl">%s</div><div class="gs">%s</div></div>'''
R['cam'] = dict(
  tag='KAMERA ZA DVORIŠTE', hook=hook('Pre nego što kupiš kameru, proveri snimač.', (4, 6), 6), hsize=118, subtop=1180,
  sub='Ne ide svaka kamera na svaki snimač.', p=('Kamera za', 'dvorište'),
  inc='✓  Na stanju · isporuka za 2 radna dana', price='3.260', img='assets/cam.jpg',
  scn=[['a', 0, 4.5], ['b', 4.5, 8.5], ['c', 8.5, 12], ['d', 12, 15.5]],
  slams=[0, 2.0, 4.5, 8.5, 12, 15.5, 18.5],
  html='''
  <div class="scene" id="a">
    <div class="abs h1" id="a1" style="left:80px;top:190px;font-size:104px">Greška:</div>
    <div class="abs h1 red" id="a2" style="left:80px;top:300px;font-size:104px">NVR snimač.</div>
    <div class="tile" id="aA" style="left:80px;top:500px;width:440px;height:440px"><img src="assets/cam.jpg" style="left:20px;top:20px;width:400px;height:400px"></div>
    <div class="abs" id="aB" style="left:580px;top:560px;width:420px;height:320px;border-radius:34px;background:rgba(255,255,255,.06);border:5px dashed #ff8a80;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:120px;font-weight:800;color:#ff8a80;letter-spacing:2px">NVR</div><div style="font-size:30px;color:#c9dbd0;font-weight:600">mrežni snimač</div></div>
    <div class="abs" id="ax" style="left:740px;top:440px;width:110px;height:110px;border-radius:50%;background:#d64545;border:6px solid #fff;display:flex;align-items:center;justify-content:center;font-size:70px;font-weight:800">✕</div>
    <div class="abs sub" id="a3" style="left:80px;top:1010px;width:920px">THC-B220-M ne radi na NVR snimaču.</div>
  </div>
  <div class="scene" id="b">
    <div class="abs h1" id="b1" style="left:80px;top:190px;font-size:104px">Ide na</div>
    <div class="abs h1 green" id="b2" style="left:80px;top:300px;font-size:104px">DVR ili XVR.</div>
    <svg class="abs" id="coax" style="left:80px;top:470px" width="920" height="160" viewBox="0 0 920 160"><path id="cx" d="M20 80 C 250 -10, 520 170, 900 80" fill="none" stroke="#6cc08f" stroke-width="16" stroke-linecap="round" stroke-dasharray="1000" stroke-dashoffset="1000"/><circle id="cxd" r="14" fill="#fff"/></svg>
    <div class="abs note" id="b0" style="left:80px;top:650px;font-size:40px">Koaksijalni kabl. Izlaz 4 u 1:</div>
    <div class="chip" id="c1x" style="left:80px;top:760px">TVI</div>
    <div class="chip" id="c2x" style="left:310px;top:760px">AHD</div>
    <div class="chip" id="c3x" style="left:540px;top:760px">CVI</div>
    <div class="chip" id="c4x" style="left:770px;top:760px">CVBS</div>
    <div class="abs sub" id="b3" style="left:80px;top:930px;width:920px">Radi sa gotovo svakim postojećim analognim snimačem. PoE ne treba.</div>
  </div>
  <div class="scene" id="c">
    <div class="abs h1" id="cc1" style="left:80px;top:190px;font-size:104px">Za dvorište:</div>
    <div class="abs h1 green" id="cc2" style="left:80px;top:300px;font-size:104px">IR do 40 m.</div>
    ''' + GA % (1, 80, 480, 1, 1, '0 m', 'Noćni vid', 'infracrveno') + GA % (2, 555, 480, 2, 2, '0°', 'Ugao', '2.8 mm objektiv') + '''
    <div class="chip" id="cc3" style="left:80px;top:1000px">2 MP</div>
    <div class="chip" id="cc4" style="left:300px;top:1000px">IP66</div>
    <div class="chip" id="cc5" style="left:520px;top:1000px">metal</div>
  </div>
  <div class="scene" id="d">
    <div class="abs h1" id="d1" style="left:80px;top:190px;font-size:96px">Pre kupovine</div>
    <div class="abs h1 green" id="d2" style="left:80px;top:295px;font-size:96px">proveri:</div>
    <div class="row" id="r1" style="top:500px"><span class="chk">1</span><span>Snimač <span class="green">· DVR ili XVR</span></span></div>
    <div class="row" id="r2" style="top:640px"><span class="chk">2</span><span>Kabl <span class="green">· koaksijalni</span></span></div>
    <div class="row" id="r3" style="top:780px"><span class="chk">3</span><span>Napajanje <span class="green">· 12 VDC</span></span></div>
    <div class="row" id="r4" style="top:920px"><span class="chk">4</span><span>Mikrofon <span class="green">· nema</span></span></div>
    <div class="abs note" id="d3" style="left:80px;top:1090px;width:920px">Vrednosti za HiLook THC-B220-M.</div>
  </div>''',
  js='''function renderF(t){
  if(t<4.6){pop($('a1'),t,.05,{dx:-90,dy:0,s0:1});slam($('a2'),t,.4);
    fly($('aA'),t,.6,{x0:-600,y0:0,r0:-15});fly($('aB'),t,.9,{x0:600,y0:0,r0:15});
    if(t>1.6)$('aA').style.transform+=` translateY(${Math.sin(t*2.4)*8}px)`;
    const s=Math.sin(t*14)*6*(t>2.0&&t<2.6?1:0);$('aB').style.transform+=` translateX(${s}px)`;
    slam($('ax'),t,2.0,{s0:2.4});$('ax').style.transform+=` rotate(${Math.sin(t*5)*8}deg)`;pop($('a3'),t,2.8,{dy:24,s0:1});}
  if(t>=4.4&&t<8.6){pop($('b1'),t,4.6,{dx:-90,dy:0,s0:1});slam($('b2'),t,4.9);
    const cp=eio(P(t,5.2,1.0));$('cx').style.strokeDashoffset=String(1000*(1-cp));const path=$('cx');const L=path.getTotalLength();const pt=path.getPointAtLength(L*cp);$('cxd').setAttribute('cx',pt.x);$('cxd').setAttribute('cy',pt.y);$('cxd').style.opacity=cp>0&&cp<1?1:0;
    pop($('b0'),t,5.5,{dy:24,s0:1});['c1x','c2x','c3x','c4x'].forEach((id,i)=>{pop($(id),t,6.0+i*.3,{dy:60,s0:.7});if(t>6.6+i*.3)$(id).style.transform+=` translateY(${Math.sin(t*3+i)*5}px)`;});
    pop($('b3'),t,7.3,{dy:24,s0:1});}
  if(t>=8.4&&t<12.1){pop($('cc1'),t,8.55,{dx:-90,dy:0,s0:1});slam($('cc2'),t,8.85);
    [[9.3,.8],[9.9,.57]].forEach(([a,f],i)=>{pop($('g'+(i+1)),t,a,{dy:80,s0:.8,d:.4});const p=gauge('ga'+(i+1),t,a+.15,f);
      if(i==0)$('gv1').textContent=Math.round(p*40)+' m';if(i==1)$('gv2').textContent=Math.round(p*103)+'°';});
    ['cc3','cc4','cc5'].forEach((id,i)=>pop($(id),t,10.7+i*.3,{dy:40,s0:.8}));}
  if(t>=11.9&&t<15.6){pop($('d1'),t,12.05,{dx:-90,dy:0,s0:1});pop($('d2'),t,12.25,{dx:-90,dy:0,s0:1});
    ['r1','r2','r3','r4'].forEach((id,i)=>pop($(id),t,12.7+i*.5,{dx:-80,dy:0,s0:1}));pop($('d3'),t,14.8,{dy:20,s0:1});}
}''',
  pops=[.05, .6, .9, 2.8, 4.6, 5.5, 6.0, 6.3, 6.6, 6.9, 7.3, 8.55, 9.3, 9.9, 10.7, 11.0, 11.3, 12.05, 12.25, 12.7, 13.2, 13.7, 14.2], impacts=[.4, 2.0, 4.9, 8.85], extra=[('riser', 5.2, .1, 1.0)])

for k in sys.argv[1:] or R:
    f = R[k]; out = os.path.expanduser(f'~/work/{k}')
    h = BASE
    for tok, val in [('%%TAG%%', f['tag']), ('%%HOOK%%', f['hook']), ('%%HSIZE%%', str(f['hsize'])), ('%%SUBTOP%%', str(f['subtop'])),
                     ('%%SUB%%', f['sub']), ('%%SCENES%%', f['html']), ('%%P1%%', f['p'][0]), ('%%P2%%', f['p'][1]),
                     ('%%INC%%', f['inc']), ('%%PRICE%%', f['price']),
                     ('%%SCN%%', json.dumps(f['scn'])), ('%%SLAMS%%', json.dumps(f['slams'])), ('%%JS%%', f['js'])]:
        h = h.replace(tok, val)
    h = h.replace('src="assets/kit.jpg"', f'src="{f["img"]}"')
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    json.dump(sfx_for(f), open(os.path.join(out, 'sfx.json'), 'w'))
print('ok')
