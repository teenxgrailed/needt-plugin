---
tags: ['critic']
max_turns: 8
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill, AskUserQuestion]
---

review this function for bugs:
```js
function total(items) { let t = 0; for (let i = 0; i <= items.length; i++) t += items[i].price; return t; }
```
