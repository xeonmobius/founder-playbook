# founder-playbook

**A Claude Code / OpenCode skill that turns 295 StarterStory transcripts into actionable product & distribution plans — modeled on `/make-playbook`'s style/format, not its content.**

Idea → Build → Launch → Distribution → Monetize → Automate → Exit.

Seven stages, seven checklists, one diagnostic system — plus `scripts/query_transcripts.py` to ground every claim in real founder transcripts (`data/master.jsonl` 295 lines: `starterstory 179 + superwallhq 52 + starterstorybuild 64`).

## Why this exists

`make-playbook` gives you the *framework* (Pieter Levels' MAKE). `founder-playbook` gives you the *evidence* — 295 EN transcripts you already transcribed with `yt-dlp` + `youtube-transcript-api` + `faster-whisper` fallback. Ask "how did founders get first users on Reddit?" and get `R4BS_UiTBPw [11.0s]` + `pvjalHFNM9Q [2.2s]` with timestamps, not generic advice.

Style/format is copied from `make-playbook` (blockquote header, Core principles → Diagnostic questions → A week of practice, `FOUNDER.md` tracker template). All content in `references/` is original synthesis from your transcripts — no verbatim MAKE text.

## What's inside

```
founder-playbook/
├── SKILL.md                     # entry point — workflow + stage diagnostic + transcript query step
├── references/
│   ├── ethos.md                 # bootstrapping-first, deen-aware ethics (no fake engagement)
│   ├── idea.md                  # sizing niche via real MRR stories
│   ├── build.md                 # AI-assisted build (17-min boilerplate etc.)
│   ├── launch.md                # pre-launch checklist + where *your* niche gathers
│   ├── distribution.md          # ★ NEW — ranked channel map from 241 launch / 235 ads / 152 twitter / 134 tiktok / 93 reddit hits
│   ├── monetize.md              # paywall/pricing from 4k paywall experiments
│   ├── automate.md              # founder bottleneck patterns
│   └── exit.md                  # app-flipping playbook
├── scripts/
│   └── query_transcripts.py     # search data/master.jsonl: uv run python scripts/query_transcripts.py "reddit first users" --top 5
└── templates/
    └── founder-tracker.md       # per-product FOUNDER.md tracker (like MAKE.md)
```

## Install — one line (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/xeonmobius/founder-playbook/main/install.sh | bash
```
Installs to **both** `~/.config/opencode/skills/founder-playbook` and `~/.claude/skills/founder-playbook` (creates dirs if missing, `git pull` if exists, `--force` to re-clone). Then restart agent:

```
/founder-playbook
/founder-playbook design my distribution for Sakina (Muslim screen-time app)
```

**Manual (if curl is blocked):**

```bash
git clone https://github.com/xeonmobius/founder-playbook.git ~/.config/opencode/skills/founder-playbook
git clone https://github.com/xeonmobius/founder-playbook.git ~/.claude/skills/founder-playbook
# update later: bash install.sh  (or install.sh --force to re-clone)
```

Or just ask naturally: "how do I get first users", "help price my family app", "Product Hunt launch?".

## Requires your transcripts

This skill expects `data/master.jsonl` + `data/*/transcripts/*.md` from [`Youtube Transcript`](../Youtube%20Transcript) (the `yt-dlp` pipeline in this org). Point `query_transcripts.py --data /path/to/master.jsonl` if elsewhere.

## Example

```
you: /founder-playbook — screen blocking app for Muslims in the west, launch stage

agent: Loads launch.md + distribution.md, runs
       query_transcripts.py "reddit first users" → R4BS_UiTBPw [11.0s] Reddit+SEO playbook
       and builds your 14-day Reddit + TikTok experiment plan with citations
       + updates FOUNDER.md
```

## Attribution

Format/style mirrors [`make-playbook`](https://github.com/tamdogood/make-playbook) (MIT). Content here is original transcript synthesis, not MAKE excerpts. If `make-playbook` is useful, [buy MAKE](https://readmake.com).

## License

MIT — see LICENSE.
