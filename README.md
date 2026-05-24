# 🌡️ Smart Climate-Resilient Heat Pump ML Predictor

> An interactive Machine Learning dashboard that optimizes dual-cascade heat pump efficiency under extreme sub-zero conditions using the **NASA POWER satellite dataset**.

[![Streamlit App](https://static.streamlit.io/badge_gradient.svg)](YOUR_STREAMLIT_DASHBOARD_LINK_HERE)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 💡 Research Inspiration
This project is inspired by the pioneering work of **Dr. Muhammad Imran** (Reader in Energy Systems at **Aston University, UK**) on his flagship **"Dual Heat Pumps Project for Ukraine."** This software prototype translates his conceptual framework of utilizing dynamic climate features (Solar, Wind, and Ambient Temperature) to protect vulnerable district heating grids into a live predictive application.

---

## 🚀 Live Interactive Demo
Experience the trained Machine Learning simulation directly in your browser:

👉 **[Click Here to Open the Live Dashboard](YOUR_STREAMLIT_DASHBOARD_LINK_HERE)**

### 🖥️ Core ML Features Evaluated
* 🔹 **Outside Ambient Temperature** (Simulated down to -25°C)
* 🔹 **All-Sky Surface Solar Radiation** (W/m²)
* 🔹 **Wind Speed Multipliers** (m/s)
* 🟢 **Target Outcome:** Predicts the Coefficient of Performance (COP) using a trained **Random Forest Regressor** model.

---

## 📊 Data Pipeline & Architecture
The project structure cleanly splits the data science research environment from the front-end production script:

```text
smart-heatpump-predictor/
├── nasa_data_analysis.ipynb   # Backend: NASA API Pipeline, Data Cleaning & ML Training
├── model.pkl                  # Serialized Random Forest Regressor Model File
├── app.py                     # Frontend: Interactive Streamlit UI 
└── requirements.txt           # Environment Dependencies Map
```

## 🛠️ Local Setup Instruction
Run this project locally on your machine in seconds:

```bash
# 1. Clone this repository
git clone [https://github.com/Ftz-AI/smart-heatpump-predictor.git](https://github.com/Ftz-AI/smart-heatpump-predictor.git)

# 2. Enter into the root directory
cd smart-heatpump-predictor

# 3. Install virtual dependencies
pip install -r requirements.txt

# 4. Run the local Streamlit instance
streamlit run app.py
```


📄 Contact & Collaboration
I am an aspiring AI & Data Science Engineer focused on developing software-driven solutions for real-world sustainability and engineering challenges.

Developer: Fatema Tuz Zohora
Linkedin: https://www.linkedin.com/in/f-tuhora-4425353a9?utm_source=share_via&utm_content=profile&utm_medium=member_android
Email:fatematuzzohora133@gmail.com
