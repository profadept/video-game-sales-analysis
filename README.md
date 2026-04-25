# Video Game Sales Analysis

Exploratory analysis of global video game sales across genres, platforms, and
regions from 1980 to 2016, using data sourced from VGChartz via Kaggle.

---

## Key Findings

- **Action dominates by volume but not efficiency.** Platform and Shooter titles
  yield a higher average revenue per release, making them more viable targets for
  studios entering a saturated market.
- **Sony and Microsoft control the commercial ceiling.** The PS2, Xbox 360, and PS3
  account for the highest cumulative software revenue of any hardware in the dataset.
- **Critic scores are weakly correlated with sales.** Titles scoring in the 60–80
  range regularly achieve blockbuster commercial results, indicating that marketing,
  bundling, and brand recognition are stronger drivers than critical reception.
- **Regional tastes diverge sharply.** North America and Europe follow broadly
  similar genre preferences, while Japan shows a disproportionate concentration in
  Role-Playing Games relative to both western markets.

---

## Dataset

| Field   | Detail                                                                 |
|---------|------------------------------------------------------------------------|
| Source  | [VGChartz via Kaggle](https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings) |
| Records | 16,719 titles (post-cleaning: 16444)                                 |
| Period  | 1980 – 2016                                                            |
| License | CC0 Public Domain                                                      |

See [`data/README.md`](data/README.md) for download instructions.

---

## How to Run

```bash
git clone https://github.com/profadept/video-game-sales-analysis.git
cd video-game-sales-analysis
uv sync
uv run python scripts/download_data.py
jupyter notebook notebooks/Video_Game_Sales_EDA.ipynb
```

---

## Project Structure

```
├── data/
│   └── README.md               ← download instructions
├── notebooks/
│   └── Video_Game_Sales_EDA.ipynb
├── outputs/
│   └── figures/                ← saved charts (generated on run)
├── scripts/
│   └── download_data.py
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## Limitations

Coverage becomes sparse after 2016. The dataset reflects physical and early-digital
sales only and does not account for mobile, free-to-play, or post-2016 digital
storefronts. Critic and user score data is missing for approximately 40% of titles,
so score-based findings apply to the reviewed subset only.