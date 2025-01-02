import streamlit as st
import numpy as np

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

st.subheader('Numpy Understandings')
arr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.
st.write(arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
st.write(arr_2d)
st.write(arr_2d.ndim)
st.write(arr_2d.shape)
st.write(arr_2d.size)


st.write('Simple Operations')
st.write('Numpy addition')
# Array addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
# st.write(array1)
# st.write( array2)
# st.write(result)



col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center", border=False)

col1.write(array1)

col2.write("plus")

col3.write(array2)

col4.write("=")

col5.write(result)


# Scalar multiplication
# arr = np.array([1, 2, 3])
# result2 = arr * 2 # each element of an array is multiplied by 2
# st.write(result2)
# name = st.text_input("What's your name")
# age = st.number_input("What's your age?", min_value=0, max_value=120, value=18)

# if st.button("Submit"):
#     st.write(f"Hello, {name}! You are {age} years old")