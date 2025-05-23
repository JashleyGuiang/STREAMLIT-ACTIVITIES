import streamlit as st

st.title("Hello, Streamlit!")
st.header("Welcome to Your First Streamlit App 🎉")
st.write("This app collects your basic information and greets you personally!")

#Input fields for user information
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)

#Display the input values
if name:
    st.write(f"Hello, {name}! You are {int(age)} years old.")
