import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load('diabetes_model.pkl')

# Page config
st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺")

st.title("🩺 Diabetes Risk Predictor")
st.markdown("Enter patient details below to assess diabetes risk.")
st.markdown("---")

# Input fields — each one matches a feature the model was trained on
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", 0, 20, 1)
    glucose = st.slider("Glucose Level", 0, 200, 120)
    blood_pressure = st.slider("Blood Pressure (mm Hg)", 0, 130, 70)
    skin_thickness = st.slider("Skin Thickness (mm)", 0, 100, 20)

with col2:
    insulin = st.slider("Insulin Level (μU/ml)", 0, 900, 80)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.slider("Age", 1, 100, 25)

st.markdown("---")

if st.button("🔍 Predict Diabetes Risk"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠️ High Risk of Diabetes ({probability:.1f}% probability)")
        st.markdown("**Recommendation:** Please consult a medical professional.")
    else:
        st.success(f"✅ Low Risk of Diabetes ({probability:.1f}% probability)")
        st.markdown("**Recommendation:** Maintain healthy lifestyle habits.")

    st.markdown("---")
    st.caption("⚠️ This tool is for educational purposes only. "
               "Not a substitute for medical advice.")