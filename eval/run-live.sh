#!/bin/bash
# Live eval run against the real Needt connector, READ-ONLY.
# usage: eval/run-live.sh <out-dir> <name> <prompt> [resume-session-id]
# Every Needt write tool is denied, so a skill that tries to land, remember or create gets a
# permission error instead of touching the account. After the run the transcript is scanned:
# any write call that slipped through makes the script exit 3 and the run counts as FAIL.
set -u
out=$1; name=$2; prompt=$3; resume=${4:-}
root=$(cd "$(dirname "$0")/.." && pwd)
N=mcp__claude_ai_Needt__needt_
WRITES="add_subtasks append_page attach_file bulk complete_subtask complete_task control
convert_task_to_goal create_event create_goal create_page create_personal_time create_project
create_task day_plan_close day_plan_draft day_plan_edit day_plan_settings delete
delete_personal_time forget_memory habit_event log_habit mark_event_personal memory_write
remember remove_attachment reschedule schedule someday someday_cleanup someday_restore undo
update_goal update_memory update_personal_time update_project update_task blocking_profile
agent_attach agent_message_ack agent_message_send agent_plan_create agent_recurrence_update
agent_register agent_release agent_reserve agent_task_claim agent_task_complete
agent_task_create agent_task_escalate agent_task_link agent_task_unlink agent_task_update"
deny=("mcp__claude_ai_Needt-budget__*" "Bash")
for w in $WRITES; do deny+=("$N$w"); done
SYS="Eval run. The Needt connector is read-only here: write tools are denied. When a skill would write to Needt, say in one line what you would write and continue."
args=(-p --model sonnet --plugin-dir "$root/plugins/needt" --output-format stream-json --verbose
  --max-turns 80 --append-system-prompt "$SYS"
  --allowedTools "${N}get" "${N}list" "${N}search" "${N}list_memories" "${N}memory_search"
    "${N}whoami" "Skill" "Read" "Write" "Glob" "Grep" "WebSearch" "WebFetch" "Agent" "Task"
    "mcp__claude_ai_Firecrawl__*"
  --disallowedTools "${deny[@]}")
[ -n "$resume" ] && args+=(--resume "$resume")
mkdir -p "$out/work"
(cd "$out/work" && timeout 2400 claude "${args[@]}" -- "$prompt" < /dev/null > "../$name.jsonl" 2> "../$name.err")
python3 - "$out/$name.jsonl" "$WRITES" <<'PY'
import json, sys
writes = set(sys.argv[2].split())
bad = []
for line in open(sys.argv[1]):
    try: d = json.loads(line)
    except ValueError: continue
    if d.get('type') == 'assistant':
        for c in d['message']['content']:
            if c['type'] == 'tool_use' and c['name'].split('needt_')[-1] in writes and 'Needt__' in c['name']:
                bad.append(c['id'])
# a denied call returns an error result; only a successful one is a leak
ok = set()
for line in open(sys.argv[1]):
    try: d = json.loads(line)
    except ValueError: continue
    if d.get('type') == 'user':
        for c in d.get('message', {}).get('content', []) or []:
            if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in bad and not c.get('is_error'):
                ok.add(c['tool_use_id'])
if ok:
    print('LEAK: Needt write calls succeeded:', ok); sys.exit(3)
print('guard ok: attempted writes', len(bad), 'all denied')
PY
