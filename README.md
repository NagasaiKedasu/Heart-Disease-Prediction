Heart Disease Prediction and Risk Analysis

🌟 Project Overview

AI Healthcare System is an intelligent application that predicts the risk of heart disease using machine learning. It integrates multiple components such as ECG analysis, OCR-based report reading, and an AI-powered assistant (Seven AI) to provide basic health guidance.

This project demonstrates the real-world application of Artificial Intelligence in healthcare.

🚀 Key Features

Heart Disease Prediction
	•	Predicts heart risk percentage based on user health data
	•	Uses trained machine learning model

📈 ECG Image Analysis
	•	Upload ECG images
	•	Detect abnormalities using image processing

📄 Medical Report OCR
	•	Extracts text from medical reports
	•	Identifies values like BP and cholesterol

💡 Personalized Recommendations
	•	Provides suggestions based on risk level

🤖 Seven AI Assistant
	•	AI chatbot for basic health queries
	•	Powered by OpenAI (secured implementation)

🛠 Tech Stack

Category	Technologies Used
Frontend	Streamlit
Backend	Python
ML Models	Scikit-learn
Image Processing	OpenCV
OCR	Tesseract
AI Chatbot	OpenAI API
Deployment	Streamlit / Local

🔐 Security Best Practices

API Key Handling
	•	API keys are NOT stored in the repository
	•	Uses environment variables / secrets

OPENAI_API_KEY=

👉 This follows industry standards for secure applications.

📂 Excluded Files

The following files are not included intentionally:
	•	❌ Large model files (.pkl, .h5)
	•	❌ Dataset files
	•	❌ API keys / secrets

Reason:
	•	GitHub file size limit (100MB)
	•	Security concerns
	•	Real-world practice uses cloud storage

▶️ How to Run

pip install -r requirements.txt
streamlit run app.py

📊 System Output
	•	Heart Risk Percentage
	•	Risk Level (Low / Medium / High)
	•	Health Recommendations
	•	Personalized Advice
	•	ECG Result
	•	AI Chatbot Response

🎯 Use Cases
	•	Early heart disease detection
	•	Health monitoring systems
	•	AI-based healthcare apps
	•	Educational AI projects

⚠️ Disclaimer

This application is for educational purposes only and should not be used as a substitute for professional medical advice.

👨‍💻 Author

Naga Sai Kedasu

A R Fardin Shaik

⭐ Future Enhancements
	•	Real-time wearable data integration
	•	Cloud deployment (AWS / Azure)
	•	Advanced deep learning models
	•	Mobile app integration




