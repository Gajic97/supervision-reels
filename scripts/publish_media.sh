#!/usr/bin/env bash
# Objavljuje videe i stranice na granu media (GitHub Pages), BEZ force push-a.
# Upotreba: GH_TOKEN=... BUFFER_TOKEN=... bash scripts/publish_media.sh <mp4> [<mp4> ...]
# Svaki mp4 mora već imati konačno ime (npr. ~/work/x/2026-11-04-slug.mp4); uz njega se kopira i .jpg ako postoji.
set -euo pipefail
SR="$(cd "$(dirname "$0")/.." && pwd)"
AUTH="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)"
M="$HOME/media"
if [ ! -d "$M/.git" ]; then git -c http.extraHeader="$AUTH" clone -q --depth 1 --branch media https://github.com/Gajic97/supervision-reels.git "$M"; fi
mkdir -p "$M/v"
for f in "$@"; do cp "$f" "$M/v/"; j="${f%.mp4}.jpg"; [ -f "$j" ] && cp "$j" "$M/v/" || true; done
# stari videi (više od 14 dana po datumu u imenu) se uklanjaju običnim commit-om
cut=$(date -d '-14 days' +%F)
for f in "$M"/v/*; do b=$(basename "$f"); d=${b:0:10}; if [[ "$d" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && [[ "$d" < "$cut" ]]; then git -C "$M" rm -q "v/$b"; fi; done
python3 "$SR/scripts/follow_page.py" "$M/nalozi"
if [ -n "${BUFFER_TOKEN:-}" ]; then (cd "$SR" && python3 scripts/report.py "$M/izvestaj" --days 60) || echo "izveštaj nije osvežen"; fi
git -C "$M" add -A
git -C "$M" -c user.name="supervision-bot" -c user.email="bot@users.noreply.github.com" commit -qm "media $(date +%F)" || echo "nema promena"
git -C "$M" -c http.extraHeader="$AUTH" push -q origin media
echo "OK media"
