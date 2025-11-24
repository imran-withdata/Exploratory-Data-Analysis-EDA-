# Exploratory-Data-Analysis-EDA-
# House Prices EDA Project

This repository contains an Exploratory Data Analysis (EDA) for the `kc_house_data.csv` dataset.

**Contents**
- `data/` : (Not included here) Original CSV placed in repository root as `kc_house_data.csv`
- `EDA.ipynb` : Jupyter notebook with step-by-step EDA
- `eda.py` : A script that reproduces key EDA steps and saves summary files & plots
- `summary_statistics.csv` : Summary statistics produced by pandas
- `missing_values.csv` : Missing value counts per column
- `data_info.txt` : Output of `df.info()`
- PNG plots: histogram, scatter, correlation heatmap

## How to use

1. Clone the repository.
2. Put `kc_house_data.csv` in the project root (or update the path in the notebook/script).
3. Create a virtual environment and install requirements:
```
pip install -r requirements.txt
```
4. Run the notebook `EDA.ipynb` or run the script:
```
python eda.py
```

## Notes
- The notebook includes visualizations and short commentary for each step.
- This project is ready to upload to GitHub; include the dataset or link to a data source if the dataset is large.
