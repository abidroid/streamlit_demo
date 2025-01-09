import streamlit as st
import requests

def get_all_fruits():
    url = 'https://fruityvice.com/api/fruit/all'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.write(str(e))
        return {"mistake": str(e)}
    
st.title("Fruit and Nutritions")
st.write("url = 'https://fruityvice.com/api/fruit/all'")

if st.button("Fetch Fruits"):
    with st.spinner("Fetching..."):
        data = get_all_fruits()

    if "mistake" in data:
        st.error(f"Error")
    else:
        st.success("Fruits fetched successfully!")
        st.json(data)

