import streamlit as st
import numpy as np
from joblib import load

st.set_page_config(
    page_title="AI Portfolio",
    layout="wide"
)

st.title("Artificial Intelligence Portfolio")
st.write("Select a project from the menu to explore live AI demos.")

st.sidebar.title("Project Menu")

option = st.sidebar.selectbox(
    "Choose a Project",
    (
        "Medical Prediction",
        "House Price Forecasting",
        "Chatbot",
        "Movie Recommendation",
        "Best Seller Inventory Prediction",
        "Language Translation",
        "Smart Email Assistant (GenAI)"
    )
)

# -------------------------
# MEDICAL PREDICTION
# -------------------------
if option == "Medical Prediction":
    st.header("🩺 Medical Risk Prediction (Diabetes Progression)")

    @st.cache_resource
    def load_medical_model():
        return load("models/diabetes_model.pk1")

    model = load_medical_model()

    st.subheader("Enter Patient Information")

    # ---- FEATURE PROMPTS & RANGES (EXACT ORDER) ----
    age = st.number_input(
        "Enter Age (e.g., 19–95 years)",
        min_value=19,
        max_value=95,
        value=45
    )

    sex = st.number_input(
        "Enter Sex (0 = Female, 1 = Male)",
        min_value=0,
        max_value=1,
        value=0,
        step=1
    )

    bmi = st.number_input(
        "Enter Body Mass Index (BMI, e.g., 18–40 kg/m²)",
        min_value=18.0,
        max_value=40.0,
        value=25.0
    )

    bp = st.number_input(
        "Enter Average Blood Pressure (e.g., 80–180 mmHg)",
        min_value=80.0,
        max_value=180.0,
        value=120.0
    )

    s1 = st.number_input(
        "Enter Total Cholesterol (TC, e.g., 120–240 mg/dL)",
        min_value=120.0,
        max_value=240.0,
        value=200.0
    )

    s2 = st.number_input(
        "Enter LDL (low-density lipoproteins, e.g., 70–160 mg/dL)",
        min_value=70.0,
        max_value=160.0,
        value=130.0
    )

    s3 = st.number_input(
        "Enter HDL (high-density lipoproteins, e.g., 40–70 mg/dL)",
        min_value=40.0,
        max_value=70.0,
        value=50.0
    )

    s4 = st.number_input(
        "Enter TC/HDL ratio (e.g., 2–6)",
        min_value=2.0,
        max_value=6.0,
        value=4.0
    )

    s5 = st.number_input(
        "Enter Glucose (GLU, e.g., 70–130 mg/dL)",
        min_value=70.0,
        max_value=130.0,
        value=100.0
    )

    s6 = st.number_input(
        "Enter Blood Sugar Level (e.g., 80–150 mg/dL)",
        min_value=80.0,
        max_value=150.0,
        value=110.0
    )

    if st.button("Predict Diabetes Risk"):
        # ⚠️ EXACT FEATURE ORDER USED DURING TRAINING
        features = np.array([[
            age,
            sex,
            bmi,
            bp,
            s1,
            s2,
            s3,
            s4,
            s5,
            s6
        ]])

        prediction = model.predict(features)

        if prediction[0] == 1:
            st.error("⚠️ High risk of diabetes progression detected.")
        else:
            st.success("✅ Low risk of diabetes progression.")



# -------------------------
# HOUSE VALUE PREDICTION
# -------------------------
elif option == "House Price Forecasting":
    st.header("🏠 Predict California House Value")

    @st.cache_resource
    def load_house_model():
        return load("models/California_house_value_model.pk1")

    model = load_house_model()

    st.subheader("Enter Housing Information")

    # User inputs with exact Colab ranges
    housing_median_age = st.number_input(
        "House Age (years, 1–60)",
        min_value=1.0,
        max_value=60.0,
        value=20.0
    )

    AveRooms = st.number_input(
        "Average Rooms per Household (1–15)",
        min_value=1.0,
        max_value=15.0,
        value=5.0
    )

    AveBedrms = st.number_input(
        "Average Bedrooms (0.1–5)",
        min_value=0.1,
        max_value=5.0,
        value=1.0
    )

    population = st.number_input(
        "Population (1–10,000)",
        min_value=1.0,
        max_value=10000.0,
        value=1000.0
    )

    AveOccup = st.number_input(
        "Average Occupancy (0.1–20)",
        min_value=0.1,
        max_value=20.0,
        value=3.0
    )

    latitude = st.number_input(
        "Latitude (30–45)",
        min_value=30.0,
        max_value=45.0,
        value=34.0
    )

    longitude = st.number_input(
        "Longitude (-125 to -113)",
        min_value=-125.0,
        max_value=-113.0,
        value=-118.0
    )

    median_income = st.number_input(
        "Median Income (scaled, e.g., 0.5–15)",
        min_value=0.1,
        max_value=15.0,
        value=5.0
    )

    if st.button("Predict House Value"):
        # ⚠️ EXACT FEATURE ORDER REQUIRED BY TRAINED MODEL
        features = np.array([[
            longitude,
            latitude,
            housing_median_age,
            population,
            median_income,
            AveRooms,
            AveBedrms,
            AveOccup
        ]])

        prediction = model.predict(features)

        st.success(
            f"🏡 Estimated Median House Value: **${prediction[0]:,.2f}**"
        )

# -------------------------
# PLACEHOLDERS
# -------------------------
elif option == "Predict House Value":
    st.header("Predict House Value")
    st.info("Model demo coming next.")

elif option == "Chatbot":
    st.header("AI Chatbot")
    st.info("NLP chatbot demo coming next.")

elif option == "Movie Recommendation":
    st.header("Movie Recommendation System")
    st.info("Recommender system demo coming next.")

elif option == "Best Seller Inventory Prediction":
    st.header("Inventory Prediction")
    st.info("Forecasting demo coming next.")

elif option == "Language Translation":
    st.header("Language Translation")
    st.info("Translation demo coming next.")

elif option == "Smart Email Assistant (GenAI)":
    st.header("Smart Email Assistant")
    st.info("Generative AI demo coming next.")
