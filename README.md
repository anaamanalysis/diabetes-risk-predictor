# 🩺 Diabetes Risk Predictor

A machine learning web app that predicts diabetes risk based on 
patient health indicators. Built with Random Forest classification 
and deployed as an interactive Streamlit application.

## 🔍 What It Does
- Takes 8 patient health inputs (glucose, BMI, age, insulin etc.)
- Runs a trained Random Forest model (100 decision trees)
- Returns diabetes risk prediction with probability percentage
- Gives a health recommendation based on the result

## 📊 Model Performance
- Algorithm: Random Forest Classifier
- Dataset: Pima Indians Diabetes Database (768 patients)
- Train/Test Split: 80/20
- Accuracy: ~76% on unseen test data
- Most important feature: Glucose level

## 🛠️ Tech Stack
- Python
- Scikit-learn — Random Forest model
- Pandas & NumPy — data processing
- Matplotlib & Seaborn — visualisations
- Streamlit — interactive web UI
- joblib — model saving and loading
- Deployed on Streamlit Cloud

## 🚀 Live App
👉 [diabetes-risk-predictor101.streamlit.app](https://diabetes-risk-predictor101.streamlit.app)

## 📁 Dataset
[Pima Indians Diabetes Database — Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

## 👩‍💻 Author
**Anaam Bind Hussain** — BTech AI & Data Science Student, Final Year  
[GitHub](https://github.com/anaamanalysis)
