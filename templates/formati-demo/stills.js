const { chromium } = require('playwright');
(async()=>{const [dir,out,...ts]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('file://'+require('path').resolve(dir,'index.html'));await p.evaluate(()=>window.ready);
for(const t of ts){await p.evaluate(t=>render(t),Number(t));await p.screenshot({path:`${out}_${t}.jpg`,type:'jpeg',quality:70});}
console.log(dir,errs.length?errs:'no errors');await b.close();})();
