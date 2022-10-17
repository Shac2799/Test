import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Shac's streamlit test")
    st.text("My attempt at a streamlit app")
    
with dataset:
    st.header("Dataset")

with features:
    st.header("My features")

with model_training:
    st.header("Model training time!")
