import streamlit as st
import pandas as pd
import joblib
import numpy as np
from PIL import Image
import pytesseract
import re
import cv2
from streamlit_option_menu import option_menu
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from openai import OpenAI

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(page_title="AI Healthcare System", layout="wide")

# ---------------------------
# OPENAI
# ---------------------------
client = OpenAI(api_key="OPENAI_API_KEY")
# ---------------------------
# STYLE
# ---------------------------
st.markdown("""
<style>
.stApp { background-color: #0e1117; color: white; }
h1, h2, h3 { text-align:center; }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# LOAD MODEL
# ---------------------------
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("model_columns.pkl")

def predict_heart(data):
    df = pd.DataFrame(data)
    df = pd.get_dummies(df)

    for col in model_columns:
        if col not in df:
            df[col] = 0

    df = df[model_columns]
    scaled = scaler.transform(df)

    return round(model.predict_proba(scaled)[0][1] * 100, 2)

# ---------------------------
# PDF FUNCTION
# ---------------------------
def create_pdf(age, sex, bmi, sleep, risk, rec, advice):
    file_path = "heart_report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("<b>AI HEALTHCARE REPORT</b>", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph("<b>Patient Details</b>", styles['Heading2']))
    content.append(Paragraph(f"Age: {age}", styles['Normal']))
    content.append(Paragraph(f"Sex: {sex}", styles['Normal']))
    content.append(Paragraph(f"BMI: {bmi}", styles['Normal']))
    content.append(Paragraph(f"Sleep Hours: {sleep}", styles['Normal']))
    content.append(Spacer(1, 15))

    content.append(Paragraph("<b>Heart Risk Analysis</b>", styles['Heading2']))
    content.append(Paragraph(f"Risk Percentage: {risk}%", styles['Normal']))
    content.append(Spacer(1, 15))

    content.append(Paragraph("<b>Recommendations</b>", styles['Heading2']))
    content.append(Paragraph(rec, styles['Normal']))
    content.append(Spacer(1, 15))

    content.append(Paragraph("<b>Personal Advice</b>", styles['Heading2']))
    content.append(Paragraph(advice if advice else "No major issues", styles['Normal']))

    doc.build(content)
    return file_path

# ---------------------------
# NAVBAR
# ---------------------------
selected = option_menu(
    menu_title=None,
    options=["Home", "Prediction", "Chatbot"],
    icons=["house", "heart", "chat"],
    orientation="horizontal"
)

# ===========================
# 🏠 HOME
# ===========================
if selected == "Home":

    st.title(" AI Heart Disease System")

    st.markdown("""
    ### Features
    - Heart Disease Prediction  
    - ECG Image Analysis  
    - Medical Report OCR  
    - AI Chatbot Support  
    """)

# ===========================
#  PREDICTION
# ===========================
elif selected == "Prediction":

    st.header("🧍 Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.selectbox("Age Category", ["Age 18 to 24","Age 25 to 29"])
        sex = st.selectbox("Sex", ["Male","Female"])
        bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
        sleep = st.slider("Sleep Hours", 0, 24, 7)
        physical_days = st.slider("Physical Health Days", 0, 30, 0)

    with col2:
        smoker = st.selectbox("Smoking Status", ["Never smoked","Current smoker"])
        alcohol = st.selectbox("Alcohol", ["Yes","No"])
        activity = st.selectbox("Physical Activity", ["Yes","No"])
        diabetes = st.selectbox("Diabetes", ["No","Yes"])
        kidney = st.selectbox("Kidney Disease", ["Yes","No"])
        copd = st.selectbox("COPD", ["Yes","No"])
        depression = st.selectbox("Depression", ["Yes","No"])
        walking = st.selectbox("Difficulty Walking", ["Yes","No"])

    st.subheader(" Heart Disease Prediction")

    if st.button("Predict Heart Risk"):

        data = {
            "AgeCategory":[age],
            "Sex":[sex],
            "BMI":[bmi],
            "SleepHours":[sleep],
        }

        risk = predict_heart(data)
        st.session_state["risk"] = risk

        st.success(f" Heart Risk: {risk}%")

        if risk > 70:
            rec = "Consult doctor immediately"
        elif risk > 40:
            rec = "Exercise & reduce stress"
        else:
            rec = "Healthy lifestyle"

        advice = "Reduce alcohol" if alcohol == "Yes" else ""

        pdf = create_pdf(age, sex, bmi, sleep, risk, rec, advice)

        with open(pdf, "rb") as f:
            st.download_button("📥 Download Report", f, "report.pdf")

    # ---------------- ECG ----------------
    st.markdown("---")
    st.subheader("📈 ECG Prediction")

    ecg_file = st.file_uploader("Upload ECG Image", type=["jpg","png","jpeg"])

    if ecg_file is not None:

        img = Image.open(ecg_file)
        st.image(img, use_container_width=True)

        if st.button("Analyze ECG"):

            gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)

            edge_density = np.sum(edges) / edges.size
            contrast = gray.std()

            if edge_density < 0.015:
                st.error("🚨 ECG Result: Abnormal")
            elif contrast < 30:
                st.warning("⚠ ECG Result: Irregular")
            else:
                st.success("✅ ECG Result: Normal")

# ===========================
# 🤖 CHATBOT
# ===========================
elif selected == "Chatbot":

    st.title("🤖 Seven AI Assistant")
    st.info("For guidance only. Consult doctor.")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    for msg in st.session_state.chat:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask Seven AI...")

    if user_input:

        st.session_state.chat.append({"role":"user","content":user_input})

        risk_info = ""
        if "risk" in st.session_state:
            risk_info = f"User heart risk is {st.session_state['risk']}%."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":"You are Seven AI, a healthcare assistant."},
                {"role":"user","content": risk_info + user_input}
            ]
        )

        reply = response.choices[0].message.content

        st.session_state.chat.append({"role":"assistant","content":reply})

        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(reply)