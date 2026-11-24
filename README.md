# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b52-front-page-dense/rank.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b52-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page newspaper front page summing up **23 November 2026** in a single
1024×1024 image: an AI rout hits Asian markets, the UN chief urges AI rules at
the Bridgetown summit, and the US lead over China hits a record low.

## What's inside

- **3 hero scenes** — Kospi −3.3% (4,708.54), Guterres: regulate AI before it's
  too late (150 delegates back a risk framework), Asia Power Index 2026
  (US 78.9 vs China 73.6, gap 5.3).
- **10 cards** — Bessent/Nvidia, FBI NCIC hack, Trump on Iran, Nasdaq futures,
  Skubal's $450M Mets deal, Tom Jackson, states vs SpaceX, Anthropic IPO
  ($107.3B, raised at $83/share), Poland missile claim, Russian nuclear satellite.
- **18 more stories** in ALSO ON MONDAY, plus a world map with 13 numbered pins.
- **DATE CHECK** — stories dated 22/21/19 Nov are explicitly left out, so nothing
  from another day sneaks in as 23 Nov news.

## How it is built

`draw.py` (Pillow) renders `entry.png`. `main.py` is **stdlib-only**: it verifies
the PNG header and copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `out/`). It never writes next to itself, so it also runs from a
read-only copy of this repo.

```sh
python3 draw.py          # render entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # verify + copy
```

## Sources

Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN · Lowy Institute
(Asia Power Index 2026). All figures as reported 23 Nov 2026. Scenes are drawn
illustrations, not photographs. CHIPS: REPORTED = confirmed by wires ·
CLAIM = one side's claim, not independently confirmed.
