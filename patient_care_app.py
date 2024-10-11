# main.py

import os
import time
import base64
import logging
import requests
import pandas as pd
import streamlit as st
from openai import OpenAI
from PIL import Image

from patient_care_prompts import (
    data_collection_prompt,
    health_assessment_prompt,
    health_awareness_prompt,
    counseling_prompt,
    advocacy_prompt,
    family_planning_prompt,
    sexual_education_prompt,
    community_visits_prompt,
    report_extraction_prompt,
    report_analysis_prompt,
    error_handling_prompt
)
from utils import sanitize_input, encode_image, validate_image
from config import AIML_API_KEY, BASE_URL

# Configure logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Function to call OpenAI API with caching
@st.cache_data(show_spinner=False)
def cached_get_ai_response(prompt):
    return get_ai_response(prompt)

def get_ai_response(prompt):
    logging.info("Generating AI response for prompt.")
    client = OpenAI(api_key=AIML_API_KEY, base_url=BASE_URL)

    try:
        chat_completion = client.chat.completions.create(
            model="o1-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10000,
            timeout=100  # Set a timeout for the API call
        )
        logging.info("AI response generated successfully.")
        return chat_completion.choices[0].message.content
    except requests.Timeout:
        logging.error("API request timed out.")
        return "Error: The request timed out. Please try again later."
    except Exception as e:
        logging.error(f"Error generating AI response: {str(e)}")
        return f"Error: {str(e)}"

# Streamlit app structure
st.set_page_config(page_title="Patient Care and Medical Report Analyzer App", layout="wide")
st.title("Patient Care and Medical Report Analyzer App")

# Navigation using Tabs
tabs = st.tabs([
    "Report Analyzer", "Data Collection", "Health Assessment", "Health Awareness",
    "Counseling", "Advocacy", "Family Planning", "Sexual Education", "Community Visits"
])

# Section 1: Report Analyzer
with tabs[0]:
    st.header("Medical Report Analyzer")
    uploaded_file = st.file_uploader("Upload a medical report image (.jpg or .jpeg)", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        if not validate_image(uploaded_file):
            st.error("Invalid image file. Please upload a valid .jpg/.jpeg image.")
            logging.warning("User uploaded an invalid image file.")
        else:
            # Encode the uploaded image to base64
            base64_image = encode_image(uploaded_file)
            logging.info("Image uploaded and encoded successfully.")

            prompt = report_extraction_prompt()  # Use prompt from prompts.py
            payload = {
                "model": "gpt-4o",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                        ]
                    }
                ],
                "max_tokens": 2000
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {AIML_API_KEY}"
            }

            response_data = None
            # Show loader animation while processing
            with st.spinner('Extracting data from the medical report...'):
                try:
                    response = requests.post(f"{BASE_URL}/v1/chat/completions", headers=headers, json=payload, timeout=30)
                    response.raise_for_status()  # This will raise an HTTPError for bad responses
                    response_data = response.json()  # Only set response_data if the request is successful
                    logging.info("Data extracted from medical report successfully.")
                except requests.Timeout:
                    st.error("The request timed out. Please try again later.")
                    logging.error("Report extraction request timed out.")
                except requests.HTTPError as http_err:
                    st.error(f"HTTP error occurred: {http_err}")
                    logging.error(f"HTTP error during report extraction: {http_err}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logging.error(f"Error during report extraction: {str(e)}")
            

            # Function to format extracted data
            def format_extracted_data(json_data):
                extracted_data = ""
                if json_data.get('choices') and len(json_data['choices']) > 0:
                    content = json_data['choices'][0]['message']['content']
                    extracted_data += content
                return extracted_data

            formatted_data = format_extracted_data(response_data)
            if formatted_data:
                st.subheader("Formatted Medical Report Data:")
                st.text_area("Extracted Data", formatted_data, height=300)

                # Ask user if they want to analyze the report
                if st.button("Analyze Report"):
                    with st.spinner('Analyzing report, please wait...'):
                        extracted_report = formatted_data.strip()
                        next_prompt = report_analysis_prompt(extracted_report)  # Use prompt from prompts.py

                        analysis_response = cached_get_ai_response(next_prompt)
                        st.subheader("Analysis Report:")
                        st.write(analysis_response)
            else:
                st.error("Failed to extract data from the medical report.")
                logging.error("No data extracted from the medical report.")

# Section 2: Data Collection
with tabs[1]:
    st.header("Data Collection")
    with st.expander("Enter the following health details"):
        health_history = sanitize_input(st.text_input("Health History", key="health_history"))
        family_history = sanitize_input(st.text_input("Family History", key="family_history"))
        medical_history = sanitize_input(st.text_input("Medical History", key="medical_history"))
        living_style = sanitize_input(st.text_input("Living Style", key="living_style"))

    if st.button("Submit Data"):
        if not all([health_history, family_history, medical_history, living_style]):
            st.warning("Please provide all the required information.")
            logging.warning("Incomplete data submitted in Data Collection.")
        else:
            prompt = data_collection_prompt(health_history, family_history, medical_history, living_style)
            response = cached_get_ai_response(prompt)
            st.subheader("Data Collection Analysis:")
            st.write(response)

# Section 3: Health Assessment
with tabs[2]:
    st.header("Health Assessment")
    with st.expander("Provide health details for assessment"):
        health_history_assessment = sanitize_input(st.text_input("Health History", key="health_history_assessment"))
        family_history_assessment = sanitize_input(st.text_input("Family History", key="family_history_assessment"))
        medical_history_assessment = sanitize_input(st.text_input("Medical History", key="medical_history_assessment"))
        living_style_assessment = sanitize_input(st.text_input("Living Style", key="living_style_assessment"))

    if st.button("Get Assessment"):
        if not all([health_history_assessment, family_history_assessment, medical_history_assessment, living_style_assessment]):
            st.warning("Please provide all the required information.")
            logging.warning("Incomplete data submitted in Health Assessment.")
        else:
            prompt = health_assessment_prompt(health_history_assessment, family_history_assessment, medical_history_assessment, living_style_assessment)
            response = cached_get_ai_response(prompt)
            st.subheader("Health Assessment Report:")
            st.write(response)
# Section 4: Health Awareness
with tabs[3]:
    st.header("Health Awareness")
    name = sanitize_input(st.text_input("Name"))
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    health_goal = sanitize_input(st.text_input("Health Goal"))

    if st.button("Generate Tips"):
        if not all([name, age, health_goal]):
            st.warning("Please provide all the required information.")
            logging.warning("Incomplete data submitted in Health Awareness.")
        else:
            prompt = health_awareness_prompt(name, age, health_goal)
            response = cached_get_ai_response(prompt)
            st.subheader("Personalized Health Tips:")
            st.write(response)

# Section 5: Counseling
with tabs[4]:
    st.header("Counseling")
    question = sanitize_input(st.text_input("What would you like counseling on?"))

    if st.button("Get Advice"):
        if not question:
            st.warning("Please enter your counseling question.")
            logging.warning("Empty counseling question submitted.")
        else:
            prompt = counseling_prompt(question)
            response = cached_get_ai_response(prompt)
            st.subheader("Counseling Advice:")
            st.write(response)

# Section 6: Advocacy
with tabs[5]:
    st.header("Advocacy")
    if st.button("Get Advocacy Resources"):
        prompt = advocacy_prompt()
        response = cached_get_ai_response(prompt)
        st.subheader("Advocacy Resources:")
        st.write(response)

# Section 7: Family Planning
with tabs[6]:
    st.header("Family Planning")
    with st.expander("Provide necessary health details"):
        health_history = sanitize_input(st.text_input("Health History"))
        family_history = sanitize_input(st.text_input("Family History"))
        medical_history = sanitize_input(st.text_input("Medical History"))
    
    if st.button("Get Family Planning Advice"):
        if not all([health_history, family_history, medical_history]):
            st.warning("Please provide all the required information.")
            logging.warning("Incomplete data submitted in Family Planning.")
        else:
            prompt = family_planning_prompt(health_history, family_history, medical_history)
            response = cached_get_ai_response(prompt)
            st.subheader("Family Planning Advice:")
            st.write(response)

# Section 8: Sexual Education
with tabs[7]:
    st.header("Sexual Education")
    sex_question = sanitize_input(st.text_input("Ask a question regarding sexual education"))

    if st.button("Get Information"):
        if not sex_question:
            st.warning("Please ask a sexual education question.")
            logging.warning("Empty sexual education question submitted.")
        else:
            prompt = sexual_education_prompt(sex_question)
            response = cached_get_ai_response(prompt)
            st.subheader("Sexual Education Information:")
            st.write(response)

# Section 9: Community Visits
with tabs[8]:
    st.header("Community Visits")
    location = sanitize_input(st.text_input("Enter the location for community visit"))

    if st.button("Plan Community Visit"):
        if not location:
            st.warning("Please provide a location.")
            logging.warning("Empty location provided for Community Visit.")
        else:
            prompt = community_visits_prompt(location)
            response = cached_get_ai_response(prompt)
            st.subheader("Community Visit Plan:")
            st.write(response)
