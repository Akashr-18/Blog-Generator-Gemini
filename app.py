import streamlit as st
import os
from PIL import Image
from blog_creation import gemini_blog_creation

st.set_page_config("Blog Post Generator")
st.header("Blog Post  Generator")

input = st.text_input("Enter the topic", key='input')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    #To display the image
    st.image(image, caption="Uploaded Image (Resized)", use_column_width=True)

button = st.button("Get Blog content")

if button:
    response = gemini_blog_creation(image, input)
    st.subheader("Response: ")
    st.write(response.text)