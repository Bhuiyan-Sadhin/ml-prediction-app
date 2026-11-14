import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Machine Learning Prediction Tool")

st.write("Enter the explanatory variables below.")

# User inputs
area = st.number_input("Area", min_value=0.0, value=120.0)
bedrooms = st.number_input("Number of bedrooms", min_value=0, value=3)
age = st.number_input("Age of house", min_value=0.0, value=5.0)
distance = st.number_input("Distance from city center", min_value=0.0, value=8.0)


# Prediction
if st.button("Predict"):

    prediction = (
        1000
        + area * 150
        + bedrooms * 10000
        - age * 2000
        - distance * 1000
    )

    st.success(f"Predicted value: {prediction:,.2f}")

    # -----------------------------
    # Graph: Area vs Predicted value
    # -----------------------------

    areas = range(20, 301, 10)

    predictions = []

    for a in areas:

        p = (
            1000
            + a * 150
            + bedrooms * 10000
            - age * 2000
            - distance * 1000
        )

        predictions.append(p)

    df = pd.DataFrame({
        "Area": areas,
        "Predicted value": predictions
    })

    st.subheader("Prediction vs Area")

    st.line_chart(
        df,
        x="Area",
        y="Predicted value"
    )
