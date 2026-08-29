#!/usr/bin/env python3
"""
query_transcripts.py — search 295 EN transcripts (data/master.jsonl + data/*/transcripts/*.md)
Usage: uv run python scripts/query_transcripts.py "reddit first users" --top 5 --channel starterstory
       uv run python scripts/query_transcripts.py "SEO" --top 3 --raw
"""
import argparse, json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]  # skills/founder-playbook/scripts -> project root is not fixed; search upwards for data/master.jsonl
# Try multiple data locations
CANDIDATES = [
    pathlib.Path.cwd() / "data" / "master.jsonl",
    pathlib.Path(__file__).resolve().parents[2] / "data" / "master.jsonl",  # shouldn't
    pathlib.Path("/Users/shannonchowdhury/Documents/Youtube Transcript/data/master.jsonl"),
]

def find_data():
    for p in CANDIDATES:
        if p.exists():
            return p
    # fallback search
    for p in pathlib.Path.cwd().rglob("master.jsonl"):
        if p.exists():
            return p
    raise FileNotFoundError("data/master.jsonl not found — run from project root or set DATA_PATH")

def load_entries(master_path):
    entries=[]
    for line in open(master_path, encoding="utf-8"):
        if not line.strip(): continue
        j=json.loads(line)
        entries.append(j)
    return entries

def score(text, terms):
    txt=text.lower()
    s=0
    for t in terms:
        s+= txt.count(t.lower())* (3 if len(t)>3 else 1)
        # bonus for phrase
        if t.lower() in txt:
            s+=2
    # proximity bonus: multiple terms close
    return s

def main():
    ap=argparse.ArgumentParser(description="Query 295 transcripts — also tech stack: --tech \"Stripe\"")
    ap.add_argument("query", nargs="*", help="search terms, e.g. \"reddit SEO\" (or use --tech for exact tool)")
    ap.add_argument("--tech", default=None, help="exact tool name, e.g. \"Stripe\", \"Cursor\", \"Supabase\" — word-boundary match, use with --top")
    ap.add_argument("--top", type=int, default=5, help="top N results")
    ap.add_argument("--channel", default=None, help="filter channel: starterstory / superwallhq / starterstorybuild")
    ap.add_argument("--raw", action="store_true", help="print raw jsonl entries")
    ap.add_argument("--data", default=None, help="path to master.jsonl")
    ap.add_argument("--inventory", action="store_true", help="show tech inventory summary (12 categories, 86 tools)")
    args=ap.parse_args()
    if args.inventory:
        inv_candidates = [
            pathlib.Path(__file__).resolve().parents[1] / "data" / "tech_inventory.json",
            pathlib.Path(__file__).resolve().parents[1] / "references" / "tech_inventory.json",
            pathlib.Path("/Users/shannonchowdhury/.config/opencode/skills/founder-playbook/data/tech_inventory.json"),
            pathlib.Path("/Users/shannonchowdhury/.config/opencode/skills/founder-playbook/references/tech_inventory.json"),
        ]
        for p in inv_candidates:
            if p.exists():
                import json as _js
                data=_js.loads(open(p).read())
                print(f"Tech inventory from {p}: {data.get('total_distinct_tools')} tools in {len(data.get('categories',{}))} categories")
                for cat, tools in data.get("categories",{}).items():
                    line=", ".join([f"{t['tool']} ({t['mentions']})" for t in tools[:5]])
                    print(f"  {cat}: {line}")
                return
        print("No tech_inventory.json found next to skill — see references/tech-stack.md")
        return
    if args.tech:
        q=args.tech
        terms=[q]
        # word-boundary exact match will be used in scoring below
    else:
        if not args.query:
            ap.print_help()
            return
        q=" ".join(args.query)
        terms=re.split(r"\s+", q.strip())
    master = pathlib.Path(args.data) if args.data else find_data()
    entries=load_entries(master)
    if args.channel:
        entries=[e for e in entries if e.get("channel_handle")==args.channel or e.get("channel")==args.channel]
    scored=[]
    for e in entries:
        txt=e.get("transcript","") + " " + e.get("title","")
        # also scan timestamped version if present
        if e.get("transcript_ts"):
            txt += " " + " ".join([s.get("text","") for s in e["transcript_ts"]][:200])
        if args.tech:
            # exact tool: word-boundary or multi-word exact
            s=1 if re.search(r'\b' + re.escape(args.tech.lower()) + r'\b', txt.lower()) else 0
        else:
            s=score(txt, terms)
        if s>0:
            scored.append((s,e))
    scored.sort(key=lambda x: x[0], reverse=True)
    top=scored[:args.top]
    if not top:
        print(f"No matches for '{q}' (tried {len(entries)} entries). Try broader terms: e.g. 'audience', 'launch', 'distribution'")
        return
    for rank,(s,e) in enumerate(top,1):
        vid=e.get("video_id")
        title=e.get("title","")[:70]
        handle=e.get("channel_handle") or e.get("channel","")
        url=e.get("url") or f"https://www.youtube.com/watch?v={vid}"
        # find best snippet
        transcript=e.get("transcript","")
        # find sentence containing any term
        snippet=""
        lower=transcript.lower()
        for t in terms:
            idx=lower.find(t.lower())
            if idx!=-1:
                start=max(0, idx-180)
                snippet=transcript[start: idx+280].replace("\n"," ")
                break
        if not snippet:
            snippet=transcript[:300].replace("\n"," ")
        # find timestamp for snippet
        ts=""
        if e.get("transcript_ts"):
            for seg in e["transcript_ts"]:
                if any(t.lower() in seg.get("text","").lower() for t in terms):
                    ts=f"[{seg.get('start',0):.1f}s]"
                    break
        print(f"\n[{rank}] {title} ({handle}/{vid}) score={s} {ts}")
        print(f"    {url}")
        print(f"    ...{snippet.strip()[:420]}...")
        if args.raw:
            print(json.dumps(e, ensure_ascii=False)[:1000])
    print(f"\n— {len(top)} cited results for '{q}' from {master} (use --raw for full json)")

if __name__=="__main__":
    main()
