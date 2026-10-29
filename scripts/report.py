#!/usr/bin/env python3
"""Izveštaj o rezultatima reelova: Buffer API metrike + data/posted.json, pa statička HTML stranica.

Upotreba:
  BUFFER_TOKEN=... python3 scripts/report.py <izlazni_folder> [--days 60]
Pravi <izlazni_folder>/index.html i data.json. Na grani `media` folder je `izvestaj/`, a javni link je
https://gajic97.github.io/supervision-reels/izvestaj/
"""
import html, json, os, sys, urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

API = "https://api.buffer.com"
TOKEN = os.environ.get("BUFFER_TOKEN", "")
BG = ZoneInfo("Europe/Belgrade")

def gql(q, v=None):
    req = urllib.request.Request(API, data=json.dumps({"query": q, "variables": v or {}}).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"})
    try: body = urllib.request.urlopen(req, timeout=120).read()
    except urllib.error.HTTPError as e: body = e.read()
    out = json.loads(body)
    if out.get("errors"): sys.exit("Buffer greška: " + json.dumps(out["errors"], ensure_ascii=False))
    return out["data"]

POSTS = """query($o:OrganizationId!, $s:DateTime!, $after:String) {
  posts(input:{organizationId:$o, filter:{status:[sent], createdAt:{start:$s}}}, first:50, after:$after) {
    edges { node { id channelService sentAt text externalLink metadata { __typename } metrics { name value } } }
    pageInfo { hasNextPage endCursor } } }"""

def fetch(days):
    org = gql("{ account { organizations { id } } }")["account"]["organizations"][0]["id"]
    start = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    posts, after = [], None
    while True:
        d = gql(POSTS, {"o": org, "s": start, "after": after})["posts"]
        posts += [e["node"] for e in d["edges"]]
        if not d["pageInfo"]["hasNextPage"]: break
        after = d["pageInfo"]["endCursor"]
    return posts

def metric(p, *names):
    m = {x["name"]: x["value"] for x in (p.get("metrics") or [])}
    for n in names:
        if n in m and m[n] is not None: return float(m[n])
    return 0.0

def views(p):   return metric(p, "Video Views", "Views", "Plays", "Impressions")
def reach(p):   return metric(p, "Reach", "Impressions")
def eng(p):     return metric(p, "Reactions", "Likes") + metric(p, "Comments") + metric(p, "Shares") + metric(p, "Saves")
def watch(p):   return metric(p, "Avg. Watch Time (sec)", "Average Watch Time")

def esc(s): return html.escape(str(s))

def main():
    out_dir = sys.argv[1]; days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 60
    os.makedirs(out_dir, exist_ok=True)
    posts = fetch(days)
    by_id = {p["id"]: p for p in posts}
    posted = json.load(open("data/posted.json"))
    reels = []
    for e in posted:
        ids = dict(e.get("buffer_posts") or {})
        for k, svc in (("buffer_post_id", "instagram"), ("buffer_post_id_tiktok", "tiktok"), ("buffer_post_id_linkedin", "linkedin")):
            if e.get(k): ids.setdefault(svc, e[k])
        ch = {}
        for svc, pid in ids.items():
            p = by_id.get(pid)
            if p: ch[svc] = {"views": views(p), "reach": reach(p), "eng": eng(p), "watch": watch(p), "link": p.get("externalLink")}
        tot_v = sum(c["views"] for c in ch.values()); tot_e = sum(c["eng"] for c in ch.values())
        reels.append({**{k: e.get(k) for k in ("date", "product", "category", "keyword", "hook_type", "hook_text", "music_style", "video", "scheduled")},
                      "channels": ch, "views": tot_v, "eng": tot_e})
    reels.sort(key=lambda r: r.get("scheduled") or r.get("date") or "", reverse=True)

    def group(key):
        g = defaultdict(lambda: [0, 0.0, 0.0])
        for r in reels:
            k = r.get(key) or "—"; g[k][0] += 1; g[k][1] += r["views"]; g[k][2] += r["eng"]
        return sorted(((k, n, v / n, e / n) for k, (n, v, e) in g.items()), key=lambda x: -x[2])
    svc_tot = defaultdict(lambda: [0, 0.0, 0.0])
    for r in reels:
        for s, c in r["channels"].items(): svc_tot[s][0] += 1; svc_tot[s][1] += c["views"]; svc_tot[s][2] += c["eng"]
    other = [p for p in posts if p["id"] not in {pid for r in posted for pid in list((r.get("buffer_posts") or {}).values()) + [r.get("buffer_post_id"), r.get("buffer_post_id_tiktok"), r.get("buffer_post_id_linkedin")] if pid}]

    weekly = ""
    wdir = "data/weekly"
    if os.path.isdir(wdir):
        files = sorted(f for f in os.listdir(wdir) if f.endswith(".md"))
        if files: weekly = open(os.path.join(wdir, files[-1]), encoding="utf-8").read()

    now = datetime.now(BG).strftime("%d.%m.%Y. %H:%M")
    json.dump({"generated": now, "reels": reels}, open(os.path.join(out_dir, "data.json"), "w"), ensure_ascii=False, indent=1)

    maxv = max([r["views"] for r in reels] + [1])
    def tbl(rows, head):
        h = "".join(f"<th>{esc(x)}</th>" for x in head)
        b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
        return f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
    def n(x): return f"{x:,.0f}".replace(",", ".")
    reel_rows = []
    for r in reels:
        chs = " ".join(f'<a class="pill {s}" href="{esc(c["link"] or "#")}" target="_blank">{s[:2].upper()} {n(c["views"])}</a>' for s, c in sorted(r["channels"].items()))
        bar = f'<div class="bar"><span style="width:{100 * r["views"] / maxv:.0f}%"></span></div>'
        reel_rows.append([esc((r.get("scheduled") or r.get("date") or "")[:16]), f'<b>{esc(r.get("product") or "")}</b><br><small>{esc(r.get("keyword") or "")}</small>',
                          esc(r.get("hook_type") or "—"), esc(r.get("music_style") or "—"), f"{n(r['views'])}{bar}", n(r["eng"]), chs])
    kpis = "".join(f'<div class="kpi"><small>{esc(s.capitalize())}</small><b>{n(v)}</b><span>pregleda · {n(e)} interakcija · {k} reel(a)</span></div>' for s, (k, v, e) in sorted(svc_tot.items()))
    page = f"""<!doctype html><html lang="sr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SuperVision reelovi: izveštaj</title><style>
:root{{--bg:#0f2a20;--card:#163a2d;--tx:#eef5f0;--mu:#a9c4b4;--ac:#6cc08f;--ac2:#439665}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.45 Poppins,system-ui,sans-serif;padding:16px}}
main{{max-width:1100px;margin:0 auto}}h1{{font-size:26px;margin:8px 0 2px}}h2{{font-size:18px;margin:28px 0 10px;color:var(--ac)}}
.mu{{color:var(--mu)}}.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
.kpi{{background:var(--card);border-radius:14px;padding:14px}}.kpi b{{display:block;font-size:28px}}.kpi small,.kpi span{{color:var(--mu)}}
.tw{{overflow-x:auto;background:var(--card);border-radius:14px}}table{{border-collapse:collapse;width:100%;min-width:640px}}
th,td{{text-align:left;padding:9px 12px;border-bottom:1px solid #24503f;vertical-align:top}}th{{color:var(--mu);font-weight:600;font-size:13px}}
.bar{{height:6px;background:#24503f;border-radius:3px;margin-top:4px;min-width:80px}}.bar span{{display:block;height:6px;background:var(--ac);border-radius:3px}}
.pill{{display:inline-block;padding:2px 8px;border-radius:999px;background:#24503f;color:var(--tx);text-decoration:none;font-size:12px;margin:2px}}
.wk{{background:var(--card);border-radius:14px;padding:14px;white-space:pre-wrap}}small{{color:var(--mu)}}
</style></head><body><main>
<h1>SuperVision reelovi: izveštaj</h1><div class="mu">Ažurirano {esc(now)} · Buffer metrike kasne nekoliko sati · poslednjih {days} dana</div>
<h2>Ukupno po mreži</h2><div class="kpis">{kpis or '<div class="kpi">Još nema podataka</div>'}</div>
<h2>Nedeljni zaključak</h2><div class="wk">{esc(weekly) if weekly else 'Prvi nedeljni zaključak stiže u ponedeljak.'}</div>
<h2>Svi reelovi</h2>{tbl(reel_rows, ["Vreme", "Proizvod / ključna reč", "Hook", "Muzika", "Pregledi", "Interakcije", "Po mreži"])}
<h2>Po tipu hook-a</h2>{tbl([[esc(k), c, n(v), n(e)] for k, c, v, e in group("hook_type")], ["Hook", "Reelova", "Ø pregleda", "Ø interakcija"])}
<h2>Po muzici</h2>{tbl([[esc(k), c, n(v), n(e)] for k, c, v, e in group("music_style")], ["Stil", "Reelova", "Ø pregleda", "Ø interakcija"])}
<h2>Po kategoriji</h2>{tbl([[esc(k), c, n(v), n(e)] for k, c, v, e in group("category")], ["Kategorija", "Reelova", "Ø pregleda", "Ø interakcija"])}
<h2>Ostale objave na kanalima</h2>{tbl([[esc((p.get("sentAt") or "")[:10]), esc(p["channelService"]), esc((p.get("text") or "")[:90]), n(views(p)), n(eng(p))] for p in other[:40]], ["Datum", "Mreža", "Tekst", "Pregledi", "Interakcije"])}
</main></body></html>"""
    open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(page)
    print(f"OK {len(reels)} reelova, {len(posts)} objava ukupno", file=sys.stderr)

if __name__ == "__main__":
    main()
