# 🎮 Video Game Sales Analysis
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)

Exploratory Data Analysis (EDA) of global video game sales to uncover trends across **genres**, **platforms**, and **regions** using Python data tools.


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

### 🔑 Setting up the Kaggle API
To use the Kaggle command below, you must first set up your Kaggle API credentials:

1. Go to your [Kaggle Account Settings](https://www.kaggle.com/settings/account) or create one if you don't have.  
2. Click on **Settings** from your Profile Dashborad and Scroll to **API** and click **Create New API Token**. This will download a file named `kaggle.json`.
3. Move the file to your home directory’s hidden `.kaggle` folder:
   ```bash
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```
   - `~/.kaggle/` is where the Kaggle CLI looks for your credentials.  
   - `chmod 600` ensures your key file is private and secure.
4. Verify installation:
   ```bash
   kaggle --version
   ```
   If you see a version number (e.g., `Kaggle API 1.7.4.5`), your setup is correct.

Once configured, run this inside the notebook or terminal:
```bash
kaggle datasets download -d rush4ratio/video-game-sales-with-ratings -p data/ --unzip
```

This command will automatically create the `data/` folder (if missing) and extract the CSV file for analysis.

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

