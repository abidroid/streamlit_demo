import streamlit as st
import requests

def get_random_user():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.write(str(e))
        return {"mistake": str(e)}
    
st.title("Fetching a random user")

if st.button("Fetch a User"):
    with st.spinner("Fetching..."):
        data = get_random_user()

    if "mistake" in data:
        st.error(f"Error")
    else:
        st.success("User fetched successfully!")
        st.json(data)

        st.header(data['results'][0]['name']['first'])
        st.image(data['results'][0]['picture']['medium'])