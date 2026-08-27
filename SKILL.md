---
name: founder-playbook
description: Turn 295 StarterStory/Superwall/StarterStoryBuild transcripts into actionable product & distribution plans. Use when you want to validate an idea, design distribution, price/monetize, or ask "how did X founder get first users?" — grounded in real transcripts at data/master.jsonl + data/*/transcripts/*.md, modeled on /make-playbook (Idea→Build→Launch→Grow→Monetize→Automate→Exit) but evidence-backed. Trigger on "distribution", "how do i get users", "product idea", "pricing", or /founder-playbook.
user-invocable: true
references: references/ethos.md, references/idea.md, references/build.md, references/launch.md, references/distribution.md, references/monetize.md, references/automate.md, references/exit.md
templates: templates/founder-tracker.md
scripts: scripts/query_transcripts.py
---

# Founder Playbook — transcript-backed

Modeled on `/make-playbook` (Pieter Levels' *MAKE* framework: Idea→Build→Launch→Grow→Monetize→Automate→Exit) but every piece of advice is grounded in your **295 EN transcripts** (`data/master.jsonl` 295 lines, `data/starterstory 179 + superwallhq 52 + starterstorybuild 64`) — not generic startup lore. The transcripts are the evidence base; the 7 stages are the scaffolding.

## What this gives you that /make-playbook doesn't

- **Evidence on demand:** any distribution/pricing/build claim is cross-checked against 3-5 real founder transcripts (with `video_id` + timestamp citations) via `scripts/query_transcripts.py`
- **Distribution-first:** `references/distribution.md` is a dedicated Grow-stage playbook distilled from 241 launch + 235 ads + 152 twitter + 134 tiktok + 93 reddit + 80 SEO + 23 cold-email transcripts — ask "design my distribution for X" and get a channel-ranked plan with founder quotes
- **Same tracker discipline:** `templates/founder-tracker.md` → `FOUNDER.md` (like `MAKE.md`) so next session picks up where you left off

## Workflow

1. **Identify product + stage.** If `FOUNDER.md` exists read it first. Otherwise ask: what product/idea, who is the first 1k users, what stage are you stuck on? Don't guess — use Quick stage diagnostic below.

2. **Load ethos + relevant stage file(s).** Always `references/ethos.md` first (bootstrapping-first, no fake followers/bots/data-selling). Then the stage file(s) — usually one, but load adjacent on boundaries (e.g. "should I charge?" → build/launch/monetize).

3. **Query transcripts for evidence.** Run `uv run python scripts/query_transcripts.py "<your question>" --top 5` (or `--channel starterstory`) to pull verbatim founder snippets. Surface 2-3 quotes with `video_id` + `[start]` timestamps — never invent tactics without a citation.

4. **Apply to *your* product — don't just restate.** Turn the checklist + transcript evidence into a concrete, numbered 7-day action list for *this* product, this niche, this week.

5. **Push to ship.** Bias to the smallest shippable next step. If stuck theorizing, assign one experiment (e.g. "post 1 raw build-in-public thread on Reddit r/SaaS tomorrow") not more framework.

6. **Create/update FOUNDER.md tracker.** For new product, copy `templates/founder-tracker.md` → `FOUNDER.md` in project root and fill known fields. For existing, update the stage section as decisions are made so next `/founder-playbook` has state.

7. **Flag ethics violations.** Same constraint as `make-playbook`: no fake engagement/upvotes/reviews, no dishonest growth hacks, no dark-pattern monetization. Call it out + suggest honest alternative from references.

## Quick stage diagnostic (same as /make-playbook, transcript-linked)

| Symptom | Revisit | Reference | Transcript query to try |
|---|---|---|---|
| "what should I build / is this idea too big?" | Idea | `references/idea.md` | `query_transcripts.py "how I found my idea"` |
| Stuck on stack/tools or outsourcing before shipping | Build | `references/build.md` | `query_transcripts.py "built in 3 days with AI"` |
| Built but nobody knows it exists | Launch | `references/launch.md` | `query_transcripts.py "Product Hunt launch"` |
| Users plateaued or only when ads run | Distribution/Grow | `references/distribution.md` | `query_transcripts.py "distribution reddit SEO"` |
| Users but no revenue / pricing feels off | Monetize | `references/monetize.md` | `query_transcripts.py "pricing $30k/month"` |
| Revenue but founder is bottleneck | Automate | `references/automate.md` | `query_transcripts.py "automate support"` |
| Considering acquisition | Exit | `references/exit.md` | `query_transcripts.py "sold my app"` |

## Principles (transcript-validated)

- Size niche math: `price × realistic paid customers` must be a business worth building — assume <3% free→paid (transcripts repeatedly show single-digit conversion even at $30k MRR stories like `hCvy-Rt7Naw`).
- Subscription compounds > one-time even with churn — model both (see `monetize.md`).
- Paid ads work *after* organic pull — 235 ads mentions in transcripts show ads as amplifier, not starter (see `distribution.md`).
- Launch infra must survive spike — general startup communities send real traffic (Levels + StarterStory launches).

## Ending on an action

Every answer ends with **one time-boxed next step** (e.g. "next 7 days: log 3 distribution experiments, run 1 Reddit comment test") + citation IDs. No open-ended advice dumps.
