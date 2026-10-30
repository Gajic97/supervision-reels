"""Pravi stranicu sa nalozima za ručno praćenje: follow_page.py <out_dir>
Čita data/follow.json (lista: date, network, name, handle, url, city, reason)."""
import json, sys, os, html
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(root, 'data', 'follow.json'), encoding='utf-8'))
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
NETS = [('instagram', 'Instagram'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn')]
e = html.escape

def row(x):
    key = e(f"{x['network']}|{x['name']}")
    if x.get('url'):
        link = f'<a href="{e(x["url"])}" target="_blank" rel="noopener">{e(x.get("handle") or "Otvori profil")}</a>'
    else:
        link = f'<span class="nolink">nema linka, potraži po imenu{(" (" + e(x["handle"]) + ")") if x.get("handle") else ""}</span>'
    return (f'<li data-k="{key}"><label><input type="checkbox"><span class="n">{e(x["name"])}</span></label>'
            f'<div class="l">{link}</div><div class="m">{e(x.get("city",""))} · {e(x.get("reason",""))}</div></li>')

secs = []
for net, label in NETS:
    items = [x for x in data if x['network'] == net]
    dates = sorted({x['date'] for x in items}, reverse=True)
    body = ''
    for d in dates:
        day = [x for x in items if x['date'] == d]
        body += f'<h3>{e(d)} <small>({len(day)})</small></h3><ul>' + ''.join(row(x) for x in day) + '</ul>'
    if not body: body = '<p class="empty">Još nema naloga za ovu mrežu.</p>'
    secs.append(f'<section id="{net}"><h2>{label} <small>ukupno {len(items)}</small></h2>{body}</section>')

nav = ''.join(f'<a href="#{n}">{l}</a>' for n, l in NETS)
page = f'''<!doctype html><html lang="sr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nalozi za praćenje</title><style>
:root{{--bg:#f6f8f7;--card:#fff;--ink:#123528;--mut:#5b6f66;--acc:#2f7a50;--line:#dfe7e2}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0e1a15;--card:#15251e;--ink:#e6f2ec;--mut:#9db5aa;--acc:#6cc08f;--line:#24392f}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
main{{max-width:760px;margin:0 auto;padding:16px}}h1{{font-size:22px;margin:8px 0}}
nav{{position:sticky;top:0;background:var(--bg);padding:8px 0;display:flex;gap:8px;z-index:2}}
nav a{{flex:1;text-align:center;padding:8px;border:1px solid var(--line);border-radius:10px;color:var(--ink);text-decoration:none;background:var(--card)}}
h2{{margin:24px 0 4px}}h2 small,h3 small{{color:var(--mut);font-weight:400;font-size:13px}}h3{{font-size:14px;color:var(--mut);margin:14px 0 6px}}
ul{{list-style:none;padding:0;margin:0}}li{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 12px;margin:6px 0}}
li.done{{opacity:.45}}label{{display:flex;gap:10px;align-items:center;font-weight:600}}input{{width:20px;height:20px;accent-color:var(--acc)}}
.l{{margin:4px 0 0 30px}}.l a{{color:var(--acc);font-weight:600;word-break:break-all}}.nolink{{color:#c0392b}}
.m{{margin:2px 0 0 30px;color:var(--mut);font-size:13px}}.empty{{color:var(--mut)}}p.note{{color:var(--mut);font-size:13px}}
</style></head><body><main><h1>Nalozi za praćenje</h1>
<p class="note">Samo instalateri i firme za video nadzor iz Srbije. Štikliraj kad zapratiš (pamti se na ovom telefonu).</p>
<nav>{nav}</nav>{''.join(secs)}</main><script>
document.querySelectorAll('li[data-k]').forEach(li=>{{const k='f:'+li.dataset.k,c=li.querySelector('input');
let v=null;try{{v=localStorage.getItem(k)}}catch(e){{}}if(v){{c.checked=true;li.classList.add('done')}}
c.onchange=()=>{{li.classList.toggle('done',c.checked);try{{c.checked?localStorage.setItem(k,'1'):localStorage.removeItem(k)}}catch(e){{}}}}}});
</script></body></html>'''
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
print('ok', len(data))
