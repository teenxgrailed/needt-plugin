#!/usr/bin/env bash
# Release gate + build for the needt plugin.
# Usage: ./release.sh <version>   (versions in plugin.json files must already be bumped)
set -euo pipefail
cd "$(dirname "$0")"
V="${1:?version, e.g. 0.13.0}"

# 1. gate: eval results for this version, no FAIL
R="eval/results-$V.md"
[ -f "$R" ] || { echo "no $R — run the eval first (eval/README.md)"; exit 1; }
grep -q "· FAIL" "$R" && { echo "$R holds a FAIL — fix the skill, re-run"; exit 1; }
grep -q "PASS" "$R" || { echo "$R has no PASS lines"; exit 1; }

# 2. versions agree
for f in needt/plugin.json needt/.claude-plugin/plugin.json; do
  grep -q "\"version\": \"$V\"" "$f" || { echo "$f is not $V"; exit 1; }
done

# 3. validate, scan, size caps
claude plugin validate needt | grep -q "Validation passed"
score=$(skillspector scan needt --no-llm 2>/dev/null | grep -o 'Score *[0-9]*' | grep -o '[0-9]*$')
[ "${score:-100}" -le 50 ] || { echo "SkillSpector $score > 50"; exit 1; }
for f in needt/skills/*/SKILL.md; do
  [ "$(wc -c < "$f")" -le 8000 ] || { echo "$f over 8000 bytes"; exit 1; }
  d=$(sed -n 's/^description: //p' "$f" | python3 -c 'import sys;print(len(sys.stdin.read().rstrip()))')
  [ "$d" -le 600 ] || { echo "$f description $d > 600 chars"; exit 1; }
done

# 4. build
python3 build-standalone.py > /dev/null
rm -f needt.plugin
(cd needt && zip -qr ../needt.plugin . -x '.DS_Store' '*/.DS_Store')
mkdir -p "dist-$V"
cp needt.plugin skills-standalone/*.zip "dist-$V/"
echo "built dist-$V: $(ls "dist-$V" | wc -l | tr -d ' ') files, scan $score/100"
