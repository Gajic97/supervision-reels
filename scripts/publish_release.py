#!/usr/bin/env python3
"""Postavlja gotov MP4 (i poster) kao GitHub Release asset i ispisuje javni link za Buffer.

Upotreba:
  GH_TOKEN=... python3 scripts/publish_release.py <tag> <video.mp4> [poster.jpg]
Javni link ima oblik:
  https://github.com/Gajic97/supervision-reels/releases/download/<tag>/<ime-fajla>
"""
import json, mimetypes, os, sys, urllib.request

REPO = os.environ.get("SV_REPO", "Gajic97/supervision-reels")
TOKEN = os.environ["GH_TOKEN"]

def api(method, url, data=None, ctype="application/json"):
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "Content-Type": ctype})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)

def main():
    tag, files = sys.argv[1], sys.argv[2:]
    try:
        rel = api("GET", f"https://api.github.com/repos/{REPO}/releases/tags/{tag}")
    except urllib.error.HTTPError as e:
        if e.code != 404: raise
        rel = api("POST", f"https://api.github.com/repos/{REPO}/releases",
                  json.dumps({"tag_name": tag, "name": tag, "body": "Automatski reel"}).encode())
    upload = rel["upload_url"].split("{")[0]
    for f in files:
        name = os.path.basename(f)
        ctype = mimetypes.guess_type(name)[0] or "application/octet-stream"
        with open(f, "rb") as fh:
            a = api("POST", f"{upload}?name={name}", fh.read(), ctype)
        print(a["browser_download_url"])

if __name__ == "__main__":
    main()
