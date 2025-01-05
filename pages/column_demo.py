import streamlit as st


st.title("Understanding Columns")

abid, zahid, shahid = st.columns(3)

abid.write("Muhammad Abid")
zahid.write("Muhammad Zahid")
shahid.write("Muhammad Shahid")