import streamlit as st

st.title("Machine Learning Prediction Tool")

st.write("Enter the explanatory variables below.")

area = st.number_input("Area", min_value=0.0)
bedrooms = st.number_input("Number of bedrooms", min_value=0)
age = st.number_input("Age of house", min_value=0.0)
distance = st.number_input("Distance from city center", min_value=0.0)

if st.button("Predict"):
    # Temporary example model
    prediction = (
        1000
        + area * 150
        + bedrooms * 10000
        - age * 2000
        - distance * 1000
    )

    st.success(f"Predicted value: {prediction:,.2f}")
