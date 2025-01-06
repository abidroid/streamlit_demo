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

        col1, col2 = st.columns(2)
        for json_country in data['data'][:5]:
            flag_image_response = requests.get(json_country['flag'])
            if flag_image_response.status_code == 200:
                flag_content = flag_image_response.text
                # Wrap the SVG content in a div with specified width and height
                    # Wrap the SVG content inside a styled <div> with object-fit
                styled_svg = f'''
                <div style="width: 300px; height: 200px; border: 1px solid black; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                    <img src="data:image/svg+xml;base64,{flag_content.encode('utf-8').decode('utf-8')}" style="width: 100%; height: 100%; object-fit: contain;">
                </div>
                '''
                col1.markdown(styled_svg, unsafe_allow_html=True)
            
            country_markdown = f'''
            <div style="width: 300px; height: 200px; border: 1px solid black; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                {json_country["name"]}
                </div>
            '''
            col2.markdown(country_markdown, unsafe_allow_html=True)
