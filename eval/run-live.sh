#!/bin/bash
# Live eval run against the real Needt connector, READ-ONLY.
# usage: eval/run-live.sh <out-dir> <name> <prompt> [resume-session-id]
# Every Needt write tool is denied under both names the connector can have (claude.ai's
# `mcp__claude_ai_Needt__` and the plugin's own `mcp__plugin_needt_needt__`). After the run
# the transcript is scanned: a successful call to any Needt tool outside the read list, a
# failed claude run or a transcript with no result makes the script exit non-zero (FAIL).
set -u
out=$1; name=$2; prompt=$3; resume=${4:-}
root=$(cd "$(dirname "$0")/.." && pwd)
PREFIXES="mcp__claude_ai_Needt__needt_ mcp__plugin_needt_needt__needt_"
READS="get list search list_memories memory_search whoami"
WRITES="add_subtasks append_page attach_file bulk complete_subtask complete_task control
convert_task_to_goal create_event create_goal create_idea create_page create_personal_time
create_project create_task day_plan_close day_plan_draft day_plan_edit day_plan_settings delete
delete_personal_time forget_memory habit_event log_habit mark_event_personal memory_write
remember reminders remove_attachment reschedule schedule skip_idea someday someday_cleanup
someday_restore take_idea undo update_goal update_memory update_personal_time update_project
update_task blocking blocking_profile agent_attach agent_message_ack agent_message_send
agent_plan_create agent_recurrence_update agent_register agent_release agent_reserve
agent_task_claim agent_task_complete agent_task_create agent_task_escalate agent_task_link
agent_task_unlink agent_task_update"
deny=("mcp__claude_ai_Needt-budget__*" "Bash")
allow=("Skill" "Read" "Write" "Glob" "Grep" "WebSearch" "WebFetch" "Agent" "Task" "mcp__claude_ai_Firecrawl__*")
for p in $PREFIXES; do
  for w in $WRITES; do deny+=("$p$w"); done
  for r in $READS; do allow+=("$p$r"); done
done
SYS="Eval run: Needt write tools are unavailable in this session. Behave exactly as you would with them. Only at the point where you would actually call one, write one line [would call: <tool>(<short args>)] instead and continue; an offer stays an offer."
# --setting-sources project,local: the runner's own ~/.claude/CLAUDE.md and user settings stay
# out, so a personal "always create tasks" rule cannot pass for skill behaviour.
args=(-p --model sonnet --setting-sources project,local --plugin-dir "$root/plugins/needt" --output-format stream-json --verbose
  --max-turns 80 --append-system-prompt "$SYS" --allowedTools "${allow[@]}" --disallowedTools "${deny[@]}")
[ -n "$resume" ] && args+=(--resume "$resume")
mkdir -p "$out/work"
(cd "$out/work" && timeout 2400 claude "${args[@]}" -- "$prompt" < /dev/null > "../$name.jsonl" 2> "../$name.err")
rc=$?
python3 - "$out/$name.jsonl" "$READS" "$rc" <<'PY'
import json, sys
path, reads, rc = sys.argv[1], set(sys.argv[2].split()), int(sys.argv[3])
calls, ok, result = {}, set(), None
for line in open(path):
    try: d = json.loads(line)
    except ValueError: continue
    if d.get('type') == 'result': result = d
    if d.get('type') == 'assistant':
        for c in d['message']['content']:
            if c['type'] == 'tool_use' and 'needt_' in c['name'] and 'Needt-budget' not in c['name']:
                tool = c['name'].split('needt_', 1)[1] if '__needt_' in c['name'] else c['name']
                if tool not in reads: calls[c['id']] = c['name']
    if d.get('type') == 'user':
        for c in d.get('message', {}).get('content', []) or []:
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in calls and not c.get('is_error'):
                ok.add(calls[c['tool_use_id']])
if ok:
    print('LEAK: Needt write calls succeeded:', sorted(ok)); sys.exit(3)
if rc != 0 or result is None or result.get('is_error') or result.get('subtype') != 'success':
    print('RUN FAILED: claude exit', rc, 'result', None if result is None else result.get('subtype')); sys.exit(4)
print('guard ok: non-read Needt calls', len(calls), '- none succeeded')
PY
