# Data

Raw and processed data are not committed to this repository.

## Source

- **Dataset:** Video Game Sales with Ratings
- **Provider:** Kaggle — rush4ratio
- **URL:** https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings
- **File:** Video_Games_Sales_as_at_22_Dec_2016.csv (~2 MB)
- **License:** CC0 Public Domain

## Download

### Option A — Automated (recommended)

Requires a Kaggle account and API token placed at `~/.kaggle/kaggle.json`.

```bash
uv run python scripts/download_data.py
```

### Option B — Manual

1. Visit the URL above
2. Download `Video_Games_Sales_as_at_22_Dec_2016.csv`
3. Place it at `data/Video_Games_Sales_as_at_22_Dec_2016.csv`

## Notes

Coverage becomes sparse after 2016. Critic and user score data is absent
for approximately 40% of titles — score-based findings apply to the
reviewed subset only.
