#!/usr/bin/env python3
"""Build standalone skill folders + zips from the plugin skills.

Each plugin skill becomes `skills-standalone/needt-<name>/` (the main skill stays `needt`)
with cross-skill links rewritten to "x (the `needt-x` skill)" and every shared reference
file it links copied into its own references/ folder.
"""
import re, shutil, pathlib, zipfile

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "needt" / "skills"
OUT = ROOT / "skills-standalone"

SHARED = {  # link target → source file
    "../setup/references/delegation.md": SRC / "setup/references/delegation.md",
    "../setup/references/tools-help.md": SRC / "setup/references/tools-help.md",
    "../setup/references/widgets.md": SRC / "setup/references/widgets.md",
    "../setup/references/skills-map.md": SRC / "setup/references/skills-map.md",
    "../setup/references/user-skills.md": SRC / "setup/references/user-skills.md",
    "../setup/references/onboarding.md": SRC / "setup/references/onboarding.md",
    "../needt/references/memory.md": SRC / "needt/references/memory.md",
    "../search/references/tools.md": SRC / "search/references/tools.md",
}

def std_name(skill):
    return "needt" if skill == "needt" else f"needt-{skill}"

def rewrite(text):
    # shared references → local references/
    for target, src in SHARED.items():
        base = src.name
        for tgt in (target, "../" + target):  # from SKILL.md and from references/*.md
            text = re.sub(r"\[([^\]]+)\]\(" + re.escape(tgt) + r"\)", r"\1 (references/" + base + ")", text)
            text = text.replace(tgt, f"references/{base}")
    # sister skills: [x](../x/SKILL.md) → x (the `needt-x` skill)
    def sk(m):
        label, skill = m.group(1), m.group(2)
        return f"{label} (the `{std_name(skill)}` skill)"
    text = re.sub(r"\[([^\]]+)\]\((?:\.\./)+([a-z]+)/SKILL\.md\)", sk, text)
    return text

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

for skill_dir in sorted(p for p in SRC.iterdir() if p.is_dir()):
    skill = skill_dir.name
    dest = OUT / std_name(skill)
    shutil.copytree(skill_dir, dest)
    md = dest / "SKILL.md"
    text = md.read_text()
    text = re.sub(r"^name: \+?setup$", f"name: {std_name(skill)}", text, flags=re.M)
    text = re.sub(r"^name: " + re.escape(skill) + r"$", f"name: {std_name(skill)}", text, flags=re.M)
    needed = [t for t in SHARED if t in text]
    text = rewrite(text)
    md.write_text(text)
    for t in needed:
        (dest / "references").mkdir(exist_ok=True)
        shutil.copy(SHARED[t], dest / "references" / SHARED[t].name)
    # references inside the skill may link shared files too
    for ref in (dest / "references").glob("*.md") if (dest / "references").exists() else []:
        ref.write_text(rewrite(ref.read_text()))
    zpath = OUT / f"{std_name(skill)}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(dest.rglob("*")):
            z.write(f, f.relative_to(OUT))
    leftovers = re.findall(r"\]\(\.\./", text)
    print(f"{std_name(skill):16} {len(text):6} chars  refs={sorted(p.name for p in (dest/'references').glob('*')) if (dest/'references').exists() else []}  leftover_links={len(leftovers)}")
