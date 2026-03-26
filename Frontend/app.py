import streamlit as st
import requests

st.set_page_config(page_title="Manufacturing Output Prediction", layout="wide")
st.title("Manufacturing Equipment Output Prediction")
st.write("Enter machine parameters to predict hourly output:")

# --------------------------
# Machine parameters input
# --------------------------
injection_temp = st.number_input("Injection Temperature (°C)", min_value=0.0, max_value=400.0, value=215.0)
injection_pressure = st.number_input("Injection Pressure (bar)", min_value=0.0, max_value=200.0, value=116.0)
cycle_time = st.number_input("Cycle Time (seconds)", min_value=0.0, max_value=100.0, value=36.0)
cooling_time = st.number_input("Cooling Time (seconds)", min_value=0.0, max_value=100.0, value=12.0)
material_viscosity = st.number_input("Material Viscosity (Pa-s)", min_value=0.0, max_value=1000.0, value=250.0)
ambient_temp = st.number_input("Ambient Temperature (°C)", min_value=0.0, max_value=50.0, value=22.0)
machine_age = st.number_input("Machine Age (years)", min_value=0.0, max_value=50.0, value=8.0)
operator_exp = st.number_input("Operator Experience (months)", min_value=0.0, max_value=600.0, value=30.0)
hours_since_maintenance = st.number_input("Hours Since Last Maintenance", min_value=0.0, max_value=1000.0, value=50.0)
temperature_pressure_ratio = st.number_input("Temperature / Pressure Ratio", min_value=0.0, max_value=10.0, value=1.88)
total_cycle_time = st.number_input("Total Cycle Time (seconds)", min_value=0.0, max_value=200.0, value=48.0)
efficiency_score = st.number_input("Efficiency Score", min_value=0.0, max_value=1.0, value=0.2)
machine_utilization = st.number_input("Machine Utilization", min_value=0.0, max_value=1.0, value=0.35)

# --------------------------
# Categorical inputs
# --------------------------
shift = st.selectbox("Shift", ["Day", "Night"])
machine_type = st.selectbox("Machine Type", ["Type_A", "Type_B", "Type_C"])
material_grade = st.selectbox("Material Grade", ["Economy", "Premium"])
day_of_week = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# --------------------------
# Predict button
# --------------------------
if st.button("Predict"):
    try:
        # Send input data as JSON to FastAPI backend
        data = {
            "injection_temperature": injection_temp,
            "injection_pressure": injection_pressure,
            "cycle_time": cycle_time,
            "cooling_time": cooling_time,
            "material_viscosity": material_viscosity,
            "ambient_temperature": ambient_temp,
            "machine_age": machine_age,
            "operator_experience": operator_exp,
            "hours_since_last_maintenance": hours_since_maintenance,
            "temperature_pressure_ratio": temperature_pressure_ratio,
            "total_cycle_time": total_cycle_time,
            "efficiency_score": efficiency_score,
            "machine_utilization": machine_utilization,
            "shift": shift,
            "machine_type": machine_type,
            "material_grade": material_grade,
            "day_of_week": day_of_week
        }

        response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code == 200:
            st.success(f"Predicted hourly output: {response.json()['predicted_hours']:.2f} hours")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to backend: {e}")