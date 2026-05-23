import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Web page initialization and structure
st.set_page_config(
    page_title="Smart Heat Pump Predictor",
    page_icon="🌡️",
    layout="wide"
)

# dashboard tittle and discription
st.title("🌡️ Smart Dual Heat Pump Efficiency Predictor")
st.markdown("""
This interactive dashboard uses simulation models to demonstrate how smart dual-cascade heat pumps outperform conventional ones.
""")

st.markdown("---")

# User interaction control panel (sidebar input)
st.sidebar.header("📊 Adjust Parameters")
st.sidebar.write("Change these to see how the system reacts in real-time:")

# Setup interactive sliders to modify environmental attributes dynamically
temp_input = st.sidebar.slider("Outside Ambient Temperature (°C)", -25, 15, -10)
wind_input = st.sidebar.slider("Wind Speed (m/s)", 0.0, 15.0, 5.0)
solar_input = st.sidebar.slider("Solar Radiation (W/m²)", 0, 500, 100)
people_input = st.sidebar.slider("Building Occupancy (Number of People)", 1, 100, 20)

# Interactive simulation mathmatical engine
def calculate_live_metrics(temp, wind, solar, people):
    # Buliding heat load logic calculation
    base_load = 20 
    temp_effect = max(0, (18 - temp) * 1.5)
    wind_effect = wind * 0.5
    human_offset = people * 0.1
    heating_load = max(0, base_load + temp_effect + wind_effect - human_offset)
    
    # Efficiency modeling for ambient temperature drops
    if temp > 0:
        conventional_cop = 3.5 + (temp * 0.05)
        dual_pump_cop = 4.0 + (temp * 0.04)
    else:
        conventional_cop = max(1.0, 2.5 + (temp * 0.12))
        dual_pump_cop = max(1.8, 3.2 + (temp * 0.06))
        
    if solar > 0:
        dual_pump_cop += (solar * 0.001)
        
    return heating_load, conventional_cop, dual_pump_cop


heating_load, conv_cop, dual_cop = calculate_live_metrics(temp_input, wind_input, solar_input, people_input)

# Live Dashboard
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Required Heating Load", value=f"{round(heating_load, 1)} kW")
with col2:
    st.metric(label="Conventional Pump COP", value=f"{round(conv_cop, 2)}")
with col3:
    st.metric(label="Smart Dual Pump COP", value=f"{round(dual_cop, 2)}", delta=f"+{round(dual_cop - conv_cop, 2)} Higher")
with col4:
    energy_saved = ((1/conv_cop) - (1/dual_cop)) * heating_load
    st.metric(label="Estimated Power Saved", value=f"{max(0, round(energy_saved, 2))} kW")

st.markdown("---")

# Dynamic line chart
st.subheader("📈 Efficiency Comparison Over a Temperature Range")

# Generate an array vector mapping over cold weather margins to feed the data vector
temp_range = np.linspace(-25, 15, 50)
chart_data = []

for t in temp_range:
    _, c_cop, d_cop = calculate_live_metrics(t, wind_input, solar_input, people_input)
    chart_data.append({"Temperature (°C)": t, "Conventional Heat Pump": c_cop, "Smart Dual Heat Pump": d_cop})

# Render data block arrays safely into structured Pandas tables indexed by temperature
df_chart = pd.DataFrame(chart_data).set_index("Temperature (°C)")

# Build native interactive line visualizations using customized UI color themes
st.line_chart(df_chart, color=["#e74c3c", "#2ecc71"])

st.caption("Notice how the Smart Dual Heat Pump (Green Line) maintains steady performance even when temperatures drop to -20°C, while the conventional pump (Red Line) drops drastically.")