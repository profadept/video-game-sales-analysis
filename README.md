# 🎮 Video Game Sales Analysis

Exploratory Data Analysis (EDA) of global video game sales to uncover trends across **genres**, **platforms**, and **regions** using Python data tools.

---

## 📊 Project Overview

This project explores the **Video Game Sales with Ratings** dataset from Kaggle to answer key analytical questions such as:
- Which game genres and platforms have dominated sales over time?
- How do critic and user ratings relate to global sales?
- Which publishers achieved the highest commercial success?

---

## 🧰 Tools and Libraries

- **Python 3.11**
- **Pandas**, **NumPy** – data cleaning and transformation  
- **Seaborn**, **Matplotlib** – static visualization  
- **Plotly** – interactive charts  
- **Jupyter Notebook** – exploration workflow  
- **Kaggle API** – automated data acquisition  

---

## 🧱 Project Structure

```
video-game-sales-analysis/
├── data/                # Dataset (downloaded via Kaggle API)
├── figures/             # Saved plots and visualizations
├── notebooks/           # Jupyter notebooks for analysis
│   └── Video_Game_Sales_EDA.ipynb
├── environment.yml      # Conda environment file
├── requirements.txt     # Pip dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### For Conda users
```bash
conda env create -f environment.yml
conda activate vg-sales-env
```

### For pip/venv users
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📥 Downloading the Dataset

After activating the environment, run this inside the notebook or terminal:
```bash
kaggle datasets download -d rush4ratio/video-game-sales-with-ratings -p data/ --unzip
```

This will automatically create the `data/` folder (if missing) and extract the CSV file for analysis.

---

## 🔍 EDA Outline

1. **Import & Setup** – Load libraries and set styles  
2. **Data Overview** – Inspect structure, missing values, and summary stats  
3. **Cleaning & Fixes** – Handle missing data and inconsistent values  
4. **Feature Engineering** – Create features like `game_age`  
5. **Univariate Analysis** – Examine distributions of sales, genres, and scores  
6. **Bivariate Analysis** – Explore relationships (e.g., critic score vs global sales)  
7. **Summary & Conclusions** – Highlight insights and findings  

---

## 📈 Key Learning Goals

- Apply complete EDA workflow from setup to visualization  
- Use the Kaggle API for reproducible dataset acquisition  
- Document findings clearly with Markdown and visual summaries  
- Strengthen portfolio presentation for data analysis roles  

---

## 🧾 License

Dataset provided under Kaggle’s data-sharing license.  
Project notebooks and analysis are released under the MIT License.

