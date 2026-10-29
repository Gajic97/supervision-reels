#!/usr/bin/env python3
"""Zakazuje video objavu preko Buffer API-ja (GraphQL, https://api.buffer.com).

Upotreba:
  BUFFER_TOKEN=... python3 scripts/schedule_buffer.py \
      --service instagram --video https://gajic97.github.io/supervision-reels/v/x.mp4 \
      --text-file opis.txt --at "2026-10-29 20:00" [--dry-run]

--service  instagram | tiktok | linkedin (kanal mora biti povezan u Buffer-u)
--at       lokalno vreme Europe/Belgrade; bez --at objava ide u Buffer red (addToQueue)
"""
import argparse, json, os, sys, urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

API = "https://api.buffer.com"
TOKEN = os.environ.get("BUFFER_TOKEN", "")

def gql(query, variables=None):
    req = urllib.request.Request(API, data=json.dumps({"query": query, "variables": variables or {}}).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"})
    try:
        body = urllib.request.urlopen(req, timeout=120).read()
    except urllib.error.HTTPError as e:
        body = e.read()
    out = json.loads(body)
    if out.get("errors"):
        sys.exit("Buffer greška: " + json.dumps(out["errors"], ensure_ascii=False))
    return out["data"]

def channel_id(service):
    orgs = gql("{ account { organizations { id } } }")["account"]["organizations"]
    for o in orgs:
        chans = gql("query($o:OrganizationId!){ channels(input:{organizationId:$o}) { id name service } }", {"o": o["id"]})["channels"]
        for c in chans:
            if c["service"] == service:
                return c["id"], c["name"]
    sys.exit(f"Kanal '{service}' nije povezan u Buffer-u")

MUTATION = """
mutation($input: CreatePostInput!) {
  createPost(input: $input) {
    ... on PostActionSuccess { post { id dueAt status } }
    ... on MutationError { message }
  }
}"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--service", required=True)
    ap.add_argument("--video", required=True)
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--at")
    ap.add_argument("--thumb-offset", type=int, default=0, help="ms; frejm 0 je poster")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    cid, cname = channel_id(a.service)
    text = open(a.text_file, encoding="utf-8").read().strip()
    inp = {
        "channelId": cid, "text": text, "schedulingType": "automatic", "needsApproval": False,
        "assets": [{"video": {"url": a.video, "metadata": {"thumbnailOffset": a.thumb_offset}}}],
        "mode": "addToQueue",
    }
    if a.at:
        due = datetime.strptime(a.at, "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo("Europe/Belgrade"))
        inp["mode"] = "customScheduled"
        inp["dueAt"] = due.astimezone(ZoneInfo("UTC")).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    if a.service == "instagram":
        inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True, "isAiGenerated": False}}
    elif a.service == "tiktok":
        inp["metadata"] = {"tiktok": {"isAiGenerated": False}}
    if a.dry_run:
        print(json.dumps(inp, ensure_ascii=False, indent=1)); return
    res = gql(MUTATION, {"input": inp})["createPost"]
    if "message" in res:
        sys.exit("Buffer odbio: " + res["message"])
    print(json.dumps({"channel": cname, **res["post"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
