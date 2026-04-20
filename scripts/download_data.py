"""
download_data.py
Run with: uv run python scripts/download_data.py
Requires: ~/.kaggle/kaggle.json
"""

from pathlib import Path
import kaggle

DATASET = "rush4ratio/video-game-sales-with-ratings"
DEST    = Path("data/raw")


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(DATASET, path=DEST, unzip=True)
    print(f"→ {DEST}")
