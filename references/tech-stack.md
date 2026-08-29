# Tech Stack — what 295 founders actually used (by use case)

> Distilled from `data/master.jsonl` 295 transcripts (starterstory 179 + superwallhq 52 + starterstorybuild 64). Every tool below has ≥2 mentions with `video_id` citation via `scripts/query_transcripts.py --tech "Cursor"`. Use this when you need a tool and don't know it exists for your use case — pick by *use case*, not by hype.

Generated 2026-08-27. Run `uv run python scripts/query_transcripts.py --tech "<tool>"` for 2-3 founder quotes per tool.

## How to use

1. **Start from your use case**, not the tool list. "I need auth for my Muslim family app" → jump to **Auth** → see `Clerk (4)` vs `Supabase Auth` vs `Firebase Auth` with transcript evidence.
2. **Rank by transcript frequency + fit for solo.** High mentions = battle-tested for indie (e.g. `Cursor 83`, `Stripe 54`). Low mentions but hyper-niche (e.g. `OneSignal 1`) = valid but fewer data points — verify via query.
3. **Always query before committing.** `query_transcripts.py --tech "RevenueCat"` returns founder snippet + `[timestamp]` so you hear *how* they used it, not just that they did.

## Quick selector — "I need a tool for..."

| Your need | Top transcript-backed picks (mentions) | When to choose |
|---|---|---|
| **Build an app fast with AI** | `Cursor 83`, `Claude 41`, `ChatGPT 35`, `Lovable 24`, `Claude Code 12`, `Bolt 8`, `v0 3`, `Replit` | Cursor for full app, Lovable/Bolt for landing + mobile MVP in hours |
| **Frontend / Mobile** | `React 40`, `Swift 25`, `React Native 14`, `Expo 12`, `Next.js 10`, `Remix 9`, `Tailwind 8` | Expo + React Native for your screen blocker (family mode on iOS/Android); Next.js for web companion |
| **Backend & DB** | `Firebase 15`, `Postgres 7`, `Supabase 3`, `Neon 2`, `Upstash Redis 2` | Firebase for auth+realtime family sync; Supabase/Postgres for relational + RLS |
| **Hosting & Infra** | `AWS 13`, `Render 6`, `Vercel 5`, `Heroku 5`, `Railway 4`, `Cloudflare 3` | Vercel for Next.js, Render/Railway for solo cheap backend, Cloudflare for edge |
| **Auth (family / kid accounts)** | `Clerk 4`, `Auth0 1`, `Firebase Auth`, `Supabase Auth` | Clerk for multi-user family auth with kid profiles; Firebase Auth if on Firebase |
| **Payments (App Store + Web)** | `Superwall 61`, `Stripe 54`, `RevenueCat 17`, `Polar 4`, `LemonSqueezy 2`, `Paddle 2` | Superwall/RevenueCat for iOS family subscription + paywall A/B; Stripe for web; Polar for open-source friendly |
| **Analytics & Retention** | `Segment 13`, `Clarity 13`, `Google Analytics 10`, `Mixpanel 6`, `Plausible 5`, `Sentry 4` | Segment to pipe family usage → PostHog/Mixpanel; Clarity for session replay on onboarding |
| **Email & Lifecycle** | `Loops 13`, `Resend 4`, `Postmark 3`, `Beehiiv 3` | Loops/Resend for prayer-time nudges + family weekly report; Beehiiv if newsletter is distribution |
| **Design** | `Figma 46`, `Canva 12`, `Framer 11`, `Sora 5` | Figma for app + family onboarding flows; Canva for TikTok thumbnails |
| **Automation / No-code** | `Bubble 23`, `Zapier 13`, `Webflow 9`, `n8n 2`, `Make.com 1` | Bubble for no-code MVP, Zapier/n8n to automate mosque WhatsApp → email capture |
| **Marketing & Distribution** | `YouTube 167`, `Twitter 152`, `TikTok 130`, `Instagram 123`, `Reddit 89`, `Product Hunt 14` | See `references/distribution.md` for ranked channel map — Reddit + TikTok for your niche |
| **Community** | `Discord 59`, `Slack 33`, `Notion 34` | Discord for family beta community |
| **Mobile Ecosystem** | `App Store 94`, `Play Store 10`, `TestFlight 1`, `OneSignal 1` | OneSignal for prayer-time push (sparingly per `launch.md`) |

## Detailed tables — with citation queries

### AI Coding / Builders (280 mentions)
| Tool | Mentions | Typical transcript phrasing | Query |
|---|---|---|---|
| Cursor | 83 | "I built this app with Cursor in 3 days" `GQ27QVp3SzQ [cursor:42s]` | `--tech "Cursor"` |
| Claude | 41 | "Claude Code built my onboarding" | `--tech "Claude"` |
| ChatGPT | 35 | "started with ChatGPT prototype" | `--tech "ChatGPT"` |
| Lovable | 24 | "Lovable for landing + app in 17 minutes" `COblC3XvuZo` | `--tech "Lovable"` |
| Claude Code | 12 | "Claude Code vs Cursor" `EQfZCe3MkTU` | `--tech "Claude Code"` |
| Bolt.new | 8 | "Bolt for MVP in a day" `8kM-JcKpcDs` | `--tech "Bolt"` |
| Windsurf | 4 | | `--tech "Windsurf"` |
| v0 | 3 | | `--tech "v0"` |

*Use case:* Need to ship MVP solo in days/weeks not months? Start Cursor or Lovable + boilerplate (`COblC3XvuZo` Expo boilerplate). Don't outsource before shipping.

### Backend & Database (37 mentions)
| Tool | Mentions | When founders chose it | Query |
|---|---|---|---|
| Firebase | 15 | Non-technical, real-time sync (family mode) | `--tech "Firebase"` |
| Postgres | 7+3 | Supabase/Neon Postgres for relational + RLS | `--tech "Postgres"` |
| Supabase | 3 | Auth + DB + storage in one | `--tech "Supabase"` |
| Neon | 2 | Serverless Postgres | `--tech "Neon"` |

*Use case:* Family app needs kid profiles + parental controls → Supabase (RLS per family) or Firebase (real-time). For SabrScreen: Supabase Postgres + Row Level Security per family_id.

### Payments & Monetization (144 mentions)
| Tool | Mentions | When | Query |
|---|---|---|---|
| Superwall | 61 | iOS paywall A/B + RevenueCat alternative | `--tech "Superwall"` |
| Stripe | 54 | Web + mobile web checkout | `--tech "Stripe"` |
| RevenueCat | 17 | Mobile subscription infra, $10M apps | `--tech "RevenueCat"` |
| Polar | 4 | OSS-friendly, `XifgHi9R5Rc` $60k/mo in 2 months | `--tech "Polar"` |

*Use case:* Your screen blocker is subscription (`$4.99/mo family`). For App Store family subscriptions → Superwall or RevenueCat (both cited for $10M apps `5u9u8yzPEpA`). Stripe for web companion. Don't use Gumroad for subscriptions.

### Auth (5 mentions — sparse, but critical)
| Tool | Mentions | Note | Query |
|---|---|---|---|
| Clerk | 4 | Family multi-user, kid profiles, `XifgHi9R5Rc` | `--tech "Clerk"` |
| Auth0 | 1 | | `--tech "Auth0"` |
| Firebase Auth | — | implied via Firebase 15 | `--tech "Firebase Auth"` |

*Use case:* Need kid vs parent logins + family invite? Clerk handles this out-of-box; Firebase Auth if already on Firebase. Don't build auth yourself.

### Analytics (57 mentions)
| Tool | Mentions | Use | Query |
|---|---|---|---|
| Segment | 13 | Pipe once → PostHog/Mixpanel | `--tech "Segment"` |
| Clarity | 13 | Free session replay for onboarding fixes | `--tech "Clarity"` |
| Google Analytics | 10 | Traffic, but not product funnel | `--tech "Google Analytics"` |
| Mixpanel | 6 | Retention `pb4JIH8FubE 0.8%→40%` | `--tech "Mixpanel"` |
| Plausible | 5 | Privacy-friendly | `--tech "Plausible"` |
| Sentry | 4 | Crash tracking | `--tech "Sentry"` |

*Use case:* Track family habit formation: Segment → Mixpanel for retention cohorts (`pb4JIH8FubE` study). Clarity to replay where parents drop in onboarding.

### Design (74 mentions)
| Tool | Mentions | Use | Query |
|---|---|---|---|
| Figma | 46 | `P4QodeA_lQ0` exact process | `--tech "Figma"` |
| Canva | 12 | Thumbnails for TikTok | `--tech "Canva"` |
| Framer | 11 | Landing pages | `--tech "Framer"` |

### Hosting (48 mentions)
| Tool | Mentions | Solo-friendly? | Query |
|---|---|---|---|
| AWS | 13 | Overkill early | `--tech "AWS"` |
| Render | 6 | Cheap, simple | `--tech "Render"` |
| Vercel | 5 | Next.js native | `--tech "Vercel"` |
| Railway | 4 | | `--tech "Railway"` |

For SabrScreen web + API: `Vercel` (frontend) + `Render` or `Railway` (API) — avoid AWS until you need it.

## How to pick — 3-question diagnostic

1. **What's your use case verb?** "I need to *collect payments* for families" → Payments table, not Analytics. Don't browse alphabetically.
2. **Solo or team?** Solo → prefer managed (Clerk, Supabase, Superwall) over DIY (AWS, self-hosted Postgres).
3. **Did a similar niche founder use it?** Run `query_transcripts.py --tech "Clerk"` and read 2 snippets — if both are B2C family apps, that's signal; if only B2B SaaS, keep scanning.

## Query helpers

```bash
# All stack
uv run python scripts/query_transcripts.py --tech "Stripe" --top 5
uv run python scripts/query_transcripts.py --tech "Supabase" --top 5
uv run python scripts/query_transcripts.py --tech "Cursor" --top 5
# By use case (via distribution.md + this file)
uv run python scripts/query_transcripts.py "pricing $30k/month" --top 5  # monetize
uv run python scripts/query_transcripts.py "built in 3 days with AI" --top 5  # build
```

## Full inventory (machine-readable)

See `data/tech_inventory.json` (also copied to skill's `references/tech_inventory.json` for offline grep) — 86 distinct tools ≥2 mentions, 12 categories, counts + example video_ids.

## Ethics

Don't pick a tool because it lets you fake growth or harvest family data. Per `ethos.md`: no dark-pattern payments, no selling kid data, no fake reviews — choose the boring, managed tool that respects users.
