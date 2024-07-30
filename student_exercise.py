import streamlit as st
import requests

st.set_page_config(layout="wide")

api_key = "NgyOtw2ty6wzhcie0jCc5u153cRSmskw6ID5ZUU2"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
content = response.json()

image_url = content['hdurl']
image_response = requests.get(image_url)

with open("APOD.jpg", 'wb') as file:
    file.write(image_response.content)

st.header(content['title'])
st.image("APOD.jpg")
st.write(content['explanation'])