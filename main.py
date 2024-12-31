import streamlit as st

# Write and magic
st.write("Hello **world**!")
st.write("Hello, *World!* :sunglasses:")



st.title("Streamlit Widgets Example")
st.header("Basic Widgets")
st.subheader("Sub Heading")
st.caption("Small Text")
st.code(""" 
a = 24
print(a)
""")




# name = st.text_input("What's your name")
# age = st.number_input("What's your age?", min_value=0, max_value=120, value=18)

# if st.button("Submit"):
#     st.write(f"Hello, {name}! You are {age} years old")