# AI Heart Disease Prediction and Risk Analysis

An AI-powered healthcare screening system that predicts heart disease risk using Machine Learning and classifies ECG images using Deep Learning, deployed as an interactive web application.

**Module:** Data Analytics & Algorithms — MSc in Data Science  
**Authors:** Naga Sai Kedasu & AR Fardin Shaik

---

## Project Overview

This system combines multiple AI components into a single Streamlit web application:

- A **Machine Learning model** (Random Forest) that predicts heart disease risk from clinical health indicators
- A **Deep Learning model** (CNN) that classifies ECG images as Normal or Abnormal
- An **AI Chatbot** (Seven AI) that provides personalised health guidance based on prediction results
- **PDF Report Generation** with patient details, risk score, and recommendations

The project focuses on **preventive healthcare for underserved populations** — making cardiac screening accessible through any web browser without specialist equipment.

---

## Features

### Heart Disease Prediction
Takes 13 health inputs (age, BMI, sleep, smoking, diabetes, etc.) and returns a risk percentage using a trained Random Forest classifier. The model was trained on the CDC BRFSS 2022 dataset with 445,132 records.

### ECG Image Analysis
Upload an ECG image and the system analyses it for abnormalities using image processing techniques (edge detection and contrast analysis via OpenCV).

### Seven AI Chatbot
An AI assistant powered by OpenAI GPT-4o-mini that answers health-related questions. It has context about the user's risk score, so responses are personalised. Includes a disclaimer: *"For guidance only. Consult doctor."*

### PDF Report Download
After prediction, users can download a PDF report containing their details, risk percentage, and health recommendations — generated using ReportLab.

---

## Tech Stack

| Category | Technologies |
|----------|-------------|
| Language | Python 3.x |
| Web Framework | Streamlit, streamlit-option-menu |
| ML Libraries | Scikit-learn, XGBoost, Imbalanced-learn (SMOTE) |
| Deep Learning | TensorFlow, Keras |
| Data Processing | Pandas, NumPy, Matplotlib, Seaborn |
| Image Processing | OpenCV, Pillow |
| AI Chatbot | OpenAI API (GPT-4o-mini) |
| PDF Generation | ReportLab |
| Model Serialisation | Joblib |

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key

The chatbot requires an OpenAI API key. **Never hardcode API keys in your code.** Set it as an environment variable:

**On Mac/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**On Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

**Using a `.env` file (recommended):**

Create a file called `.env` in the project root:
```
OPENAI_API_KEY=your-api-key-here
```

Then load it in Python using `python-dotenv`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

> **Why not hardcode the key?** If you push code with an API key to GitHub, anyone can see it and use your account. OpenAI will also automatically revoke exposed keys. Using environment variables keeps your key private and is industry standard practice.

### 4. Run the application

```bash
streamlit run arfardin.py
```

The app will open at `http://localhost:8501`

---

## Project Structure

```
heart-disease-prediction/
│
├── arfardin.py                  # Main Streamlit application
├── Heart_Diseases.ipynb         # ML model training notebook (EDA, LR, RF, XGBoost)
├── Untitled32.ipynb             # CNN model training notebook (ECG classification)
│
├── heart_model.pkl              # ⚠️ Not in repo — trained Random Forest model
├── scaler.pkl                   # ⚠️ Not in repo — fitted StandardScaler
├── model_columns.pkl            # ⚠️ Not in repo — column order after encoding
├── ecg_model.h5                 # ⚠️ Not in repo — trained CNN model
│
├── requirements.txt             # Python dependencies
├── .env                         # ⚠️ Not in repo — API keys (create your own)
├── .gitignore                   # Files excluded from Git
└── README.md                    # This file
```

---

## Files in This Repository

These are the files included and available in the GitHub repository:

| File | Description |
|------|-------------|
| `arfardin.py` | Main Streamlit application — contains the full web app with Home, Prediction, and Chatbot pages |
| `Heart_Diseases.ipynb` | Jupyter notebook for ML model training — includes EDA, data preprocessing, SMOTE balancing, Logistic Regression, Random Forest, XGBoost training and evaluation |
| `Untitled32.ipynb` | Jupyter notebook for CNN model training — includes ECG signal-to-image conversion, CNN architecture, training (15 epochs), and evaluation |
| `heart_disease_presentation.pptx` | Project presentation slides (14 slides) covering problem statement, architecture, model comparison, deployment screenshots, and results |
| `requirements.txt` | List of all Python packages needed to run the project |
| `.gitignore` | Specifies which files Git should ignore (model files, datasets, API keys, cache) |
| `README.md` | This file — project documentation and setup instructions |

> **How to use:** Clone the repo, install dependencies from `requirements.txt`, download the datasets from the links below, run both notebooks to generate the model files, set your API key, then launch the app with `streamlit run arfardin.py`.

---

## Files Not Included in This Repository

Some files are intentionally excluded from GitHub. Here is why and how to get them:

### Model Files (`.pkl`, `.h5`)

| File | Size | Why Excluded | How to Get It |
|------|------|-------------|---------------|
| `heart_model.pkl` | ~4 MB | GitHub has a 100MB file limit; best practice is to not store binary models in Git | Run `Heart_Diseases.ipynb` to regenerate |
| `scaler.pkl` | ~1 KB | Generated during training | Run `Heart_Diseases.ipynb` to regenerate |
| `model_columns.pkl` | ~1 KB | Generated during training | Run `Heart_Diseases.ipynb` to regenerate |
| `ecg_model.h5` | ~15 MB | Binary model file | Run `Untitled32.ipynb` to regenerate |

> **To regenerate all models:** Open the Jupyter notebooks and run all cells. The `.pkl` and `.h5` files will be saved automatically.

### Dataset Files

| Dataset | Size | Source |
|---------|------|--------|
| CDC BRFSS 2022 | ~200 MB | [Kaggle — Indicators of Heart Disease](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) |
| MIT-BIH Arrhythmia | ~100 MB | [Kaggle — ECG Heartbeat Categorization](https://www.kaggle.com/datasets/shayanfazeli/heartbeat) |

> **Why not include datasets?** They are several hundred MB combined. GitHub is not designed for large data storage. Download them from the links above and place them in the project folder before running the notebooks.

### API Keys and Secrets

| File | Why Excluded |
|------|-------------|
| `.env` | Contains the OpenAI API key — **never commit secrets to Git** |

> See the "Set up your OpenAI API key" section above for setup instructions.

### `.gitignore`

The following `.gitignore` is used to prevent accidental commits of large or sensitive files:

```
# API keys and secrets
.env
*.key

# Model files
*.pkl
*.h5
*.pt

# Datasets
*.csv
*.zip
*.gz

# Python
__pycache__/
*.pyc
.ipynb_checkpoints/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## Model Performance

| Model | Accuracy | ROC-AUC | Task |
|-------|----------|---------|------|
| Logistic Regression | 75.6% | 60.9% | Heart disease risk (baseline) |
| **Random Forest** | **84.8%** | 53.9% | Heart disease risk (deployed) |
| XGBoost | 76.8% | 61.1% | Heart disease risk (best ROC-AUC) |
| **CNN** | **88%** | — | ECG classification (Normal/Abnormal) |

> **Note:** Random Forest was selected for deployment due to highest accuracy. XGBoost had better ROC-AUC (class discrimination). See the project report for detailed analysis.

---

## System Output

When a user completes a prediction, they receive:

- **Heart Risk Percentage** — e.g., "Heart Risk: 94.0%"
- **Risk Level** — Low (below 40%), Medium (40–70%), or High (above 70%)
- **Health Recommendations** — based on risk level
- **Personalised Advice** — based on lifestyle factors (alcohol, smoking)
- **Downloadable PDF Report** — with all details for doctor consultation
- **ECG Result** — Normal, Irregular, or Abnormal (if ECG image uploaded)
- **AI Chatbot Responses** — context-aware health guidance

---

## Sustainability and Resilience

This project addresses healthcare sustainability through:

- **Accessibility** — cardiac screening via any web browser, no specialist equipment needed
- **Cost reduction** — near-zero cost per screening vs €150–€500 traditional consultation
- **Environmental impact** — digital reports replace paper; remote screening reduces patient travel
- **Resource efficiency** — lightweight models (4MB + 15MB) run on any laptop without GPU
- **System resilience** — dual independent models; ML prediction works fully offline

Aligned with **UN SDGs**: SDG 3 (Good Health), SDG 9 (Innovation), SDG 10 (Reduced Inequalities).

---

## Use Cases

- Early heart disease screening in primary care and rural clinics
- Health monitoring and risk tracking over time
- AI-assisted patient triage in resource-limited settings
- Educational demonstration of ML/DL in healthcare

---

## Disclaimer

> **This application is for educational and screening purposes only.** It is not a substitute for professional medical diagnosis, advice, or treatment. Always consult a qualified healthcare provider for medical decisions.

---

## Future Enhancements

- Real-time ECG monitoring from wearable devices (Apple Watch, Fitbit)
- Cloud deployment on AWS/Azure with authentication
- 1D-CNN on raw ECG signals (more efficient than image conversion)
- Mobile application for broader accessibility
- Federated learning for privacy-preserving model training
- Integration with hospital EHR systems

---

## Authors

**Naga Sai Kedasu** — Machine Learning (Logistic Regression, Random Forest, XGBoost, preprocessing, backend)  
**AR Fardin Shaik** — Deep Learning (CNN architecture, ECG processing, Streamlit frontend, chatbot integration)

MSc in Data Science — Data Analytics & Algorithms — 2026
