#!/usr/bin/env bash
# Preuzima evidenciju (posted.json, follow.json, postponed.json, weekly/) sa grane media (folder state/) u ~/sr/data/.
# Evidencija živi na grani media jer zakazani zadaci pouzdano pišu samo tamo.
# Upotreba (odmah posle kloniranja): GH_TOKEN=... bash scripts/state_pull.sh
set -euo pipefail
SR="$(cd "$(dirname "$0")/.." && pwd)"
AUTH="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)"
M="$HOME/media"
if [ ! -d "$M/.git" ]; then git -c http.extraHeader="$AUTH" clone -q --depth 1 --branch media https://github.com/Gajic97/supervision-reels.git "$M"; else git -C "$M" -c http.extraHeader="$AUTH" pull -q --rebase origin media; fi
if [ -d "$M/state" ]; then
  mkdir -p "$SR/data"
  for f in posted.json follow.json postponed.json; do [ -f "$M/state/$f" ] && cp "$M/state/$f" "$SR/data/$f"; done
  [ -d "$M/state/weekly" ] && mkdir -p "$SR/data/weekly" && cp -r "$M/state/weekly/." "$SR/data/weekly/"
  echo "OK state: $(python3 -c "import json;print(len(json.load(open('$SR/data/posted.json'))))") objava u evidenciji"
else
  echo "state/ još ne postoji na grani media, koristim data/ iz main"
fi
