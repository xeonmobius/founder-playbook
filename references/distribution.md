# Distribution (Grow) — transcript-backed

> Distilled from 295 StarterStory/Superwall/StarterStoryBuild transcripts (Apr 2026): 241 mention "launch", 235 "ads", 190 "audience", 152 "twitter", 134 "tiktok", 93 "reddit", 80 "SEO", 31 "outreach", 23 "cold email", 14 "Product Hunt". This is an original synthesis of *what founders actually did* — cite `video_id` + `[timestamp]` when you claim a channel works, don't just assert it.

## Core principles (transcript-validated)

- **Distribution is built into the product, not bolted on.** Founders who got retention (e.g. `yBjcmMhXSDk` "I Built a $20K/Month Mobile App" — 3 days AI build but 6 months retention work) describe sharing/shareable outputs as the growth lever. If people don't naturally want to come back + tell others, no channel fixes it.
- **Organic before paid.** 235 "ads" hits show ads as *amplifier after* organic pull (boosting winning TikTok/Reddit posts), not cold starter. "Flat organic growth is useful information" — fix product/differentiation before buying traffic.
- **Transparency is a real channel.** Build-in-public across Twitter/TikTok/YouTube (152/134 hits) drives word-of-mouth + press because numbers/mistakes are public. StarterStory itself is the canonical example.
- **Never fake it.** 0 transcripts advocate bought followers/bots — ethics constraint in `ethos.md` overrides any tactic that would require it. Small & real > large & fake.

## Channel map — ranked by transcript evidence + when to use it

1. **Reddit (93 hits) — best for first 1k niche users, fastest feedback loop**
   - Why: highly targeted subreddits, founders report first paying users from a single honest post (no ads). Requires genuine value, not spam.
   - Transcript cue: `query "reddit first users"` → e.g. founders describing r/SaaS, r/SideProject posts
   - Play: 1 helpful comment/day in 2 subreddits where your micro-niche lives + 1 raw "built this" post/week with numbers.

2. **SEO (80 hits) — durable, compounds, slow start**
   - Why: founders at $30k/mo like `hCvy-Rt7Naw` (cooking niche) and `LWPN-PAhtLA` ($35k/mo website built in 3h) credit SEO + programmatic pages for compounding traffic.
   - Play: 10 programmatic SEO pages answering exact niche queries; measure 8-week lag.

3. **TikTok / Short-form (134 hits) — outlier-driven, lottery-like**
   - Why: transcripts warn TikTok is "lottery system" (5 hits verbatim) — but outliers scale fast when you "spy" competitors' viral formats and clone with your product's output.
   - Play: `spy talk` pattern — scroll 500+ competitor TikToks, find 3 outlier formats, clone 1/day for 7 days.

4. **Twitter/X (152 hits) — build-in-public, audience before product**
   - Why: 152 mentions tie Twitter to audience-building *before* launch.
   - Play: 1 build-in-public thread/week with real numbers (MRR, churn) + reply to 5 niche accounts/day.

5. **Cold outreach (23 cold email + 31 outreach) — high effort, high signal**
   - Why: sparse but founder-cited for B2B / first 10 customers. Works when hyper-personalized, fails when templated.
   - Play: 10 hyper-personalized cold emails to micro-niche prospects with a Loom, not a blast.

6. **Product Hunt / Launch communities (14 hits) — spike, not sustain**
   - Why: launch spikes are real but transient; transcripts show re-launching on multiple platforms as product evolves.
   - Play: schedule 2 re-launches (different communities) 30 days apart.

7. **Paid ads (235 hits) — only after organic proof**
   - Why: boost winners, don't create them. "Boosting those videos with paid ads" pattern appears 7× in transcripts.
   - Play: only spend after 1 channel shows organic retention; then $20/day boosting winning creative.

## Distribution design workflow (use this when user says "help design my distribution")

1. **Name the micro-niche** (first 1k — see `idea.md`). Which 2 subreddits / 10 SEO queries / 5 TikTok hashtags does *that exact* person already hang out in?
2. **Pick 2 channels max for next 14 days** from map above — rank by where micro-niche actually lives, not where you *want* them to live. Cite 2 transcripts that used those channels.
3. **Define shareable output.** What does your product *produce* that is personalized + shareable with a preview? (e.g. filtered list, generated image, report). Make that the distribution asset, not the homepage.
4. **Set 14-day experiment.** For each channel: 1 experiment/day (e.g. 7 Reddit comments + 7 TikToks), measure reply rate / CTR / retention at day 7, not installs alone.
5. **Gate.** If no organic pull after 14 days, revisit product differentiation before adding a third channel or any paid spend.

## Measuring competitors (directional)

- Third-party traffic tools = relative trends, not absolute. Use for "what channel are they winning on?" not "how many visits exactly?"
- Traffic ≠ revenue. Cross-check with monetization (see `monetize.md`).

## Diagnostic questions (ask these about *their* product)

1. Is growth right now organic or propped up by something that stops when you stop pushing? (be honest)
2. Retention 2-3 weeks after first visit — does product pull people back without you nudging?
3. Have you posted real numbers/progress publicly in the last 7 days? What would you share if you did?
4. What does your product *output* that could be made personalized + shareable with a preview?
5. Which 2 channels in the map does your micro-niche actually live in — and do you have 2 transcript citations that those channels worked for a similar niche?
6. If you expose an API/embed, have you thought through copy-risk vs distribution upside?

## A week of practice (homework)

Pull every piece of feedback from your last launch (launch-platform comments, Reddit replies, DMs). Ship one product change from it + run 7 distribution experiments (1/day) on your #1 ranked channel. Do not add paid spend until you see organic retention.

## Query helpers

- `uv run python scripts/query_transcripts.py "reddit first users" --top 5`
- `uv run python scripts/query_transcripts.py "SEO programmatic" --top 5`
- `uv run python scripts/query_transcripts.py "tiktok viral outlier" --top 5`
- `uv run python scripts/query_transcripts.py "cold email first 10 customers" --top 5`
