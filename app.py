import streamlit as st
import numpy as np
import joblib

# Load the Pickle file
with open('best_model.pkl' , 'rb') as file:
    model = joblib.load(file)

#Title of Project
st.title("🏢 Building Energy Efficiency Predictor")

st.divider()

st.subheader("Enter Building Parameters")

col1 , col2 = st.columns(2)

with col1:
    relative_compactness = st.number_input(
        "Relative Compactness", min_value=0.0,max_value=1.0,value=0.75
    )
    surface_area = st.number_input(
        "Surface Area (m²)", value=750.0
    )
    wall_area = st.number_input(
        "Wall Area (m²)", value=300.0
    )
    roof_area = st.number_input(
        "Roof Area (m²)", value=150.0
    )

with col2:
    overall_height = st.number_input(
        "Overall Height (m)", min_value=0.0,max_value=7.0,value=0.0
    )
    orientation = st.number_input(
        "Orientation", min_value=1,max_value=5,value=1
    )
    glazing_area = st.slider(
        "Glazing Area", 0.0, 0.4, 0.2
    )
    glazing_area_distribution = st.slider("glazing area distribution",0.0,5.0,0.2)

st.divider()

if st.button("Predict Energy Efficiency"):

    

    input_data = np.array([[relative_compactness,
        surface_area,
        wall_area,
        roof_area,
        overall_height,
        orientation,
        glazing_area,
        glazing_area_distribution
        ]])
    

        # Dummy prediction (remove after model is ready)
    # heating_load = round(20 + wall_area / 50 + overall_height, 2)
    # cooling_load = round(15 + glazing_area * 20 + surface_area / 300, 2)

    # real model prediction
    prediction = model.predict(input_data)
    heating_load = round(prediction[0][0], 2)
    cooling_load = round(prediction[0][1],2)
   
      
    c1 , c2 = st.columns(2)
    with c1:
        st.metric(
            label = "Heating Load (kWh/m^2)",
            value = heating_load
        )
    
    with c2:
        st.metric(
            label = "Cooling Load (kWh/m^2)",
            value = cooling_load
        )
    
    