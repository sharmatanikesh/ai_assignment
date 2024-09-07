from dotenv import load_dotenv
load_dotenv()  # Load the environment variables

import streamlit as st 
import os
import google.generativeai as genai 
from PIL import Image

# Configure the generative model with your API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get a response from the Gemini model
def get_gemini_response(user_input, images, testing_type, code_generate):
    # Base prompt to be appended to every input
    base_prompt = (f"Given the provided screenshots of a digital product, "
                   f"generate detailed testing instructions for each feature visible in the images. "
                   f"Each test case should include the following:\n"
                   f"Description: A brief overview of what the feature or functionality being tested is.\n"
                   f"Pre-conditions: List any conditions or setups that must be in place before testing can occur, "
                   f"such as user login, specific settings, or required data.\n"
                   f"Testing Steps: Step-by-step instructions for how to test the feature, including where to navigate, "
                   f"what buttons to press, and what actions to perform.\n"
                   f"Expected Result: Clearly describe what should happen if the feature is working as intended, "
                   f"such as UI updates, system messages, or successful data submission.\n\n")

    # Append testing type and code generation details if they are not null
    if testing_type and code_generate:
        full_prompt = (f"{base_prompt}"
                       f"For testing type: {testing_type}\n"
                       f"Also Generate Code  Framework/Language: {code_generate}\n\n"
                       f"Additional Details: {user_input}")
    elif testing_type:
        full_prompt = (f"{base_prompt}"
                       f"Testing Type: {testing_type}\n\n"
                       f"Additional Details: {user_input}")
    else:
        full_prompt = f"{base_prompt}{user_input}"

    # If there are images, include them in the request
    if images:
        response = model.generate_content([full_prompt] + images)
    else:
        response = model.generate_content(full_prompt)
    
    return response.text

# Streamlit frontend setup
st.set_page_config(page_title="Myracle Assignment by Tanikesh Sharma")
st.header("Myracle Assignment")

testing_type = st.selectbox("Select testing type (OPTIONAL):", ["", "Android", "IOS", "Web"])

code_generate = ""
if testing_type!="":
    if testing_type == "Android":
        code_generate = st.selectbox("Select testing framework (OPTIONAL)", ["JUnit", "Espresso", "Web"])
    elif testing_type == "IOS":
        code_generate = st.selectbox("Select testing language (OPTIONAL)", ["XCTest", "XCUITest", "KIF (Keep It Functional)"])
    elif testing_type == "Web":
        code_generate = st.selectbox("Select testing framework (OPTIONAL)", ["Jest", "Cypress", "Selenium"])

uploaded_images = st.file_uploader("Choose one or more images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
images = []

if uploaded_images:
    # Resize and store the uploaded images
    for uploaded_image in uploaded_images:
        img = Image.open(uploaded_image)
        resized_img = img.resize((200, 200))  # Resize the image to 200x200 pixels
        images.append(resized_img)

    # Display images in rows, 3 per row
    for i in range(0, len(images), 3):
        cols = st.columns(3)
        for j, img in enumerate(images[i:i+3]):
            with cols[j]:
                st.image(img, caption=f"Image {i + j + 1}", use_column_width=True)

# Text input field for user query
user_input = st.text_input("Enter a query (OPTIONAL):")

# Submit button
submit = st.button("Generate Test Instructions")

if submit:
    if not uploaded_images:
        st.warning("Please upload at least one image to generate test instructions.")
    else:
        response = get_gemini_response(user_input, images, testing_type, code_generate)
        st.subheader("Generated Test Instructions")
        st.write(response)
