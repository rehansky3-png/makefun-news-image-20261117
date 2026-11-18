# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/rehansky3-png/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/rehansky3-png/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A newspaper front page summing up the world's news of Tuesday 17 November 2026 in one 1024×1024 image: the U.S.–Iran strikes, Ukraine's drones hitting the Kerch Bridge, Trump meeting Xi and Putin in Shenzhen, Nvidia's $115bn quarter, the Ebola outbreak in DR Congo, and the call to open Gaza aid crossings — plus an "also today" strip (U.S. measles status, Japan scrambling jets).

The image was drawn with Pillow during development and is stored as `entry.png`; `main.py` (Python 3.13, stdlib only, no network) just copies it to the output directory, so both runs write identical bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, < 1 MiB)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d7yn48z6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
