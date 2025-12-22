import streamlit as st

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

if option == "Medical Prediction":
    st.header("Medical Risk Prediction")
    st.info("Model demo coming next.")

elif option == "House Price Forecasting":
    st.header("House Price Sales Forecasting")
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
