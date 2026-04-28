#  Medical Insurance Cost Prediction

A Machine Learning project that predicts **medical insurance costs** based on user attributes such as age, BMI, smoking habits, and more.

---

##  Project Overview

Medical insurance pricing depends on multiple personal and lifestyle factors.  
This project builds a predictive model that estimates insurance charges using machine learning techniques.

The goal is to:
- Understand key factors affecting insurance costs
- Perform data analysis & visualization
- Build and evaluate regression models
- Predict insurance charges for new users

---

##  Features

-  Exploratory Data Analysis (EDA)
-  Data preprocessing & feature engineering
-  Encoding categorical variables
-  Model training using regression algorithms
-  Model evaluation (R²)
-  Insurance cost prediction system

---

##  Dataset

- Source: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- Features:
  - `age` – Age of the person
  - `sex` – Gender
  - `bmi` – Body Mass Index
  - `children` – Number of dependents
  - `smoker` – Smoking status
  - `region` – Residential region
  - `charges` – Insurance cost (target)

---

## ⚙️ Tech Stack

- Python 
- NumPy
- Pandas
- Matplotlib / Seaborn
- Scikit-learn

---

##  Machine Learning Models Used

- Linear Regression
- Decision Tree Regressor

---

##  Workflow

1. Data Collection  
2. Data Cleaning  
3. Exploratory Data Analysis  
4. Feature Engineering  
5. Train-Test Split  
6. Model Training  
7. Model Evaluation  
8. Prediction  

---

##  Model Performance

| Metric | Value |
|-------|------|
| R² Score | 0.751505643411174 |

---

## 🖥️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/devkumar3631/medical-insurance-cost-prediction.git

# Navigate to project folder
cd medical-insurance-cost-prediction

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py
