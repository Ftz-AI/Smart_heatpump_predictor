import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import warnings
warnings.filterwarnings("ignore")


# 1. Page Configuration Setup
st.set_page_config(
    page_title="Smart Heat Pump Predictor",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ Smart Dual Heat Pump Predictor")
st.markdown("""

This interactive web app utilizes a trained **Random Forest Regressor ML Model** to predict heat pump efficiency (COP) based on dynamic real-time climate inputs.
""")
st.markdown("---")

# 2. Sidebar Input Controls
st.sidebar.header("📊 Live Environmental Features")
temp_input = st.sidebar.slider("Ambient Temperature (°C)", -25, 15, -10)
wind_input = st.sidebar.slider("Wind Speed (m/s)", 0.0, 15.0, 5.0)
solar_input = st.sidebar.slider("Solar Radiation (W/m²)", 0, 500, 100)
people_input = st.sidebar.slider("Building Occupancy (People)", 1, 100, 20)

# Thermodynamic calculation for building heating load demand reference
base_load = 20 
heating_load = max(0, base_load + max(0, (18 - temp_input) * 1.5) + (wind_input * 0.5) - (people_input * 0.1))

# 3. ML Model Loader Engine (Deserializing the Pickle File)
@st.cache_resource
def load_ml_predictor():
    if os.path.exists("model.pkl"):
        return joblib.load("model.pkl")  # Loading the exported model file
    return None

model = load_ml_predictor()

# 4. Formatting User Input into Structured Dataframe
input_features = pd.DataFrame([[temp_input, wind_input, solar_input]], columns=['Temperature', 'Wind_Speed', 'Solar_Radiation'])

# 5. Real-Time Predictive Inference using ML Model
if model is not None:
    predicted_cop = float(model.predict(input_features)[0])
    status_msg = "⚡ Powered by Live Random Forest ML Model"
else:
    # Mathematical thermodynamic simulation as a reliable fallback fallback
    predicted_cop = max(1.8, 3.2 + (temp_input * 0.06)) + (solar_input * 0.001)
    status_msg = "⚠️ Running on fallback baseline equations (Upload model.pkl to trigger ML)"

# Conventional single-stage baseline heat pump COP calculation
conventional_cop = max(1.0, 2.5 + (temp_input * 0.12)) if temp_input <= 0 else 3.5 + (temp_input * 0.05)

# 6. Displaying KPI Operational Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Calculated Heating Load", value=f"{round(heating_load, 1)} kW")
with col2:
    st.metric(label="Conventional Pump COP", value=f"{round(conventional_cop, 2)}")
with col3:
    st.metric(label="Predicted Smart Pump COP (ML)", value=f"{round(predicted_cop, 2)}", delta=f"+{round(predicted_cop - conventional_cop, 2)} Efficiency Gain")
with col4:
    energy_saved = ((1/conventional_cop) - (1/predicted_cop)) * heating_load
    st.metric(label="Estimated Grid Power Saved", value=f"{max(0, round(energy_saved, 2))} kW")

st.info(status_msg)
st.markdown("---")

# 7. Rendering Dynamic Predictive Curves Over Temperature Ranges
st.subheader("📈 ML Predictive Curve Over Temperature Margins")
temp_range = np.linspace(-25, 15, 50)
chart_data = []

for t in temp_range:
    c_cop = max(1.0, 2.5 + (t * 0.12)) if t <= 0 else 3.5 + (t * 0.05)
    if model is not None:
        inst_features = pd.DataFrame([[t, wind_input, solar_input]], columns=['Temperature', 'Wind_Speed', 'Solar_Radiation'])
        p_cop = float(model.predict(inst_features)[0])
    else:
        p_cop = max(1.8, 3.2 + (t * 0.06)) + (solar_input * 0.001)
    chart_data.append({"Temperature (°C)": t, "Conventional Heat Pump": c_cop, "Smart ML Dual Heat Pump": p_cop})

df_chart = pd.DataFrame(chart_data).set_index("Temperature (°C)")
st.line_chart(df_chart, color=["#e74c3c", "#2ecc71"])
