import requests
import streamlit as st


def get_all_countries():
    url = 'https://countriesnow.space/api/v0.1/countries/flag/images'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.write(str(e))
        return {"mistake": str(e)}
    

st.title("Fetching All Countries")

if st.button("Fetch All Countries"):
    with st.spinner("Fetching..."):
        data = get_all_countries()

    if "mistake" in data:
        st.error(f"Error: {data['error']}")
    else:
        st.success("Data fetched successfully!")
        st.json(data)
        st.write(len(data['data']))
