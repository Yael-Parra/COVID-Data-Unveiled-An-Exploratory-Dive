# COVID Data Unveiled: An Exploratory Dive

##  Index
-  [About the Project](#-about-the-project)  
-  [Main Features](#-main-features)  
-  [Current Issues](#-current-issues)
-  [Folder Structure](#-folder-structure)
-  [Possible Improvements](#-possible-improvements)   
-  [Technologies Used](#-technologies-used)   
-  [Installation and Usage](#-installation-and-usage)   
-  [Author](#-author)   

---

##  About the Project  

This project focuses on **Exploratory Data Analysis (EDA)** of historical COVID-19 data for the United States, compiled from the states_daily.csv dataset provided by the [COVID Tracking Project API](https://covidtracking.com/data/api). The dataset covers the period from January 13, 2020 to March 7, 2021. To enhance the analysis, population data from the year 2020 was obtained from [1KeyData](https://state.1keydata.com/state-population-density.php) and merged with the COVID-19 dataset.

---

##  Main Features  
✅ Fetches and cleans COVID-19 case, testing, and hospitalization data.  
✅ Integrates state population data for per-capita analysis.  
✅ Generates visualizations to uncover trends and anomalies.  
✅ Provides insights into state-wise and national-level impacts.  
✅ Jupyter Notebook-based analysis for easy reproducibility.  

---

##  Current Issues  
❌ API data is static (no updates beyond 2021).  
❌ Some states may have missing or inconsistent data.  
❌ Population data does not account for yearly changes.  

---

##  Possible Improvements  
✅ Include additional data sources for a more comprehensive analysis.  
✅ Implement automated data cleaning scripts.  
✅ Enhance visualizations with interactive dashboards (e.g., Plotly).  
✅ Apply machine learning models to forecast trends.  

---
## Folder Structure

📂 COVID-Data-Unveiled-An-Exploratory-Dive/  
├── 📂 data/                
│   ├── backup/       
│   ├── states.daily.csv  
│  
├── 📂 eda/                 
│   ├── analysis_data.ipynb 
│   ├── cleaning_data.ipynb  
│   └── clean_data_states_daily.csv  
│  
├── 📂 scrap_from_api/    
│   ├── extracting_data.py 
│  
├── 📜 requirements.txt      
├── 📜 README.md    
├── 📜 COVID Data Analysis Report.pdf
└── 📜 .gitignore           

---

## Technologies Used

- **Python**  
- **Pandas** - Data manipulation and analysis  
- **Matplotlib & Seaborn** - Data visualization and plotting  
- **Requests** - Making API calls for data retrieval  
- **Jupyter Notebook** - Interactive analysis and visualization  

### Dependencies
- `jupyter`  
- `matplotlib`  
- `notebook`  
- `numpy`  
- `pandas`  
- `plotly`  
- `scikit-learn`  
- `scipy`  
- `seaborn`

---

## ⚙ Installation and Usage  

### 1️⃣ Clone the Repository  
```bash
 git clone https://github.com/Yael-Parra/COVID-Data-Unveiled-An-Exploratory-Dive.git # Better check the url in the code section
 cd COVID-Data-Unveiled-An-Exploratory-Dive
```

### 2️⃣ Setting up the environment and dependencies  

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the code
```bash
python scrap_from_api/extracting_data.py 
jupyter notebook cleaning_data.ipynb
jupyter notebook analysis_data.ipynb
```

---
## 🧑‍💻 Author  
This project was fully developed by - [Yael Parra](https://www.linkedin.com/in/yael-parra/).  
If you find this project helpful or have any suggestions, feel free to reach out!

