import streamlit as st

st.title("Streamlist Widgets Example")
st.header("Basic Widgets")

name = st.text_input("What's your name")
age = st.number_input("What's your age?", min_value=0, max_value=120, value=18)

if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old")