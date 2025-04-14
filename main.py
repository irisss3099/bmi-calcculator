import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

# CSS for background, inputs, button, and styling
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=1950&q=80");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .title {
            text-align: center;
            color: #00BFA6;
            font-size: 46px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .result {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            padding-top: 25px;
        }
        .stNumberInput > div > input {
            border-radius: 8px;
        }
        div.stButton > button {
            background-color: #87CEEB !important; /* Sky Blue */
            color: white !important;
            border: none !important;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-size: 16px;
            transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 0 4px 12px rgba(135, 206, 235, 0.4);
        }
        div.stButton > button:hover {
            background-color: #76bcd9 !important;
            transform: scale(1.03);
            box-shadow: 0 6px 16px rgba(135, 206, 235, 0.5);
        }
        div.stButton > button:active {
            transform: scale(0.96);
            box-shadow: inset 0 3px 6px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar - BMI Chart
with st.sidebar:
    st.markdown("## 📊 BMI Chart")
    bmi_data = pd.DataFrame({
        "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
        "BMI Range": ["< 18.5", "18.5 – 24.9", "25 – 29.9", "30 or more"],
        "Color": ["🟠", "🟢", "🟧", "🔴"]
    })
    st.dataframe(bmi_data, hide_index=True, use_container_width=True)

# Main content
st.markdown("<h1 class='title'>💪 BMI Calculator</h1>", unsafe_allow_html=True)

# Inputs
height = st.number_input("📏 Enter your height (in cm):", min_value=50, max_value=250, value=170)
weight = st.number_input("⚖️ Enter your weight (in kg):", min_value=10, max_value=300, value=70)

# BMI Calculation
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 18.5:
        status = "Underweight"
        color = "orange"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
        color = "green"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
        color = "darkorange"
    else:
        status = "Obese"
        color = "red"

    # Result with white background card
    st.markdown(f"""
        <div style='
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 16px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            text-align: center;
        '>
            <div class='result' style='color:{color};'>
                Your BMI is: {bmi}<br>
                Category: <strong>{status}</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='
        margin-top: 60px;
        background: linear-gradient(90deg, rgba(0,191,166,0.12), rgba(0,191,166,0.05));
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #00796B;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    '>
        🚀 Created by Sabila Aleem ❤
    </div>
""", unsafe_allow_html=True)



