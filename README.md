---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.20.0
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

# Titanic Passenger Data Analysis

---
A modular Python project exploring the Titanic dataset through data cleaning, exploratory data analysis, and visualization.

This project investigates how different factors such as gender, age group, embarkation port, and passenger class influenced survival rates during the Titanic disaster.

---

# Project Structure

```text
Titanic/
├── data/
│   └── Titanic.csv
│
├── outputs/
│   ├── survival_by_cabin.png
│   ├── survival_by_gender.png
│   └── survival_by_port.png
│
├── data_loader.py
├── gender.py
├── children.py
├── port.py
├── cabin.py
├── main.py
│
├── REPORT_fr.ipynb
└── running.ipynb
```

---

# Features

- Modular Python project structure
- Data loading and preprocessing
- Survival analysis by:
  - Gender
  - Age group
  - Embarkation port
  - Passenger class
- Automatic chart generation with Matplotlib
- Separation between analysis logic and execution workflow

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

# How to Run

## 1. Install dependencies

```bash
pip install pandas numpy matplotlib
```

## 2. Run the analysis

```bash
python main.py
```

---

# Example Analyses

## Survival Rate by Gender

The project compares male and female survival rates and visualizes the results using bar charts.

## Survival Rate by Passenger Class

The analysis investigates how ticket class influenced survival probability.

## Survival Rate by Embarkation Port

Passenger survival is compared across embarkation locations (`C`, `Q`, `S`).

---

# Output

Generated visualizations are automatically saved inside the `outputs/` directory.

Example:

![outputs/survival_by_gender.png]
![outputs/survival_by_port.png]
![outputs/survival_by_cabin.png]

---

# Purpose of the Project

This project was created as a practice exercise in:
- exploratory data analysis (EDA),
- Python project organization,
- data visualization,
- and modular programming.

The original notebook-based workflow was progressively refactored into reusable Python modules to improve code readability and maintainability.

---

# Author

Jess Swift  
Mathematics & Economics Student — Université Paris-Saclay
