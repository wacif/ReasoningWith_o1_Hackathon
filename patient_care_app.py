import streamlit as st
import os
import base64
import requests
import time
from openai import OpenAI
from patient_care_prompts import (data_collection_prompt, health_assessment_prompt, health_awareness_prompt,
                                  counseling_prompt, advocacy_prompt, family_planning_prompt, sexual_education_prompt,
                                  community_visits_prompt, error_handling_prompt, report_extraction_prompt, report_analysis_prompt)

# Function to call OpenAI API
def get_ai_response(prompt):
    aiml_api_key = os.getenv('AIML_API')
    client = OpenAI(
        api_key=aiml_api_key,
        base_url="https://api.aimlapi.com/",
    )

    try:
        chat_completion = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5000
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Function to encode the image
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')


# Streamlit app structure
st.title("Patient Care and Medical Report Analyzer App")

# Sidebar for navigation
menu = st.sidebar.selectbox(
    "Choose an option", 
    ["Report Analyzer", "Data Collection", "Health Assessment", "Health Awareness", "Counseling",
     "Advocacy", "Family Planning", "Sexual Education", "Community Visits"]
)

# Section 1: Report Analyzer
if menu == "Report Analyzer":
    st.title("Medical Report Analyzer")
    uploaded_file = st.file_uploader("Upload a medical report image (in .jpg format)", type="jpg")

    if uploaded_file is not None:
        # Encode the uploaded image to base64
        base64_image = encode_image(uploaded_file)

        # Set headers (adjust according to AIML API documentation)
        api_key = os.getenv('AIML_API')
        base_url = "https://api.aimlapi.com/"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Payload structure based on AIML API documentation
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

        # Show loader animation while processing
        with st.spinner('Extracting data from the medical report...'):
            time.sleep(2)
            response = requests.post(f"{base_url}/v1/chat/completions", headers=headers, json=payload)
            response_data = response.json()

        # Function to format extracted data
        def format_extracted_data(json_data):
            extracted_data = ""
            if json_data['choices'] and len(json_data['choices']) > 0:
                content = json_data['choices'][0]['message']['content']
                extracted_data += content
            return extracted_data

        formatted_data = format_extracted_data(response_data)
        st.subheader("Formatted Medical Report Data:")
        st.write(formatted_data)

        # Ask user if they want to analyze the report
        if st.button("Analyze Report"):
            with st.spinner('Analyzing report, please wait...'):
                time.sleep(2)

                # Prepare the next prompt using the extracted data
                extracted_report = formatted_data.strip()
                next_prompt = report_analysis_prompt(extracted_report)  # Use prompt from prompts.py

                try:
                    chat_completion = get_ai_response(next_prompt)
                    st.subheader("Analysis Report:")
                    st.write(chat_completion)

                except Exception as e:
                    st.error(f"Error during the analysis: {e}")

# Section 2: Other Services (e.g., Data Collection, Health Assessment, etc.)
else:
    if menu == "Data Collection":
        st.title("Data Collection")
        health_history = st.text_input("Health History")
        family_history = st.text_input("Family History")
        medical_history = st.text_input("Medical History")
        living_style = st.text_input("Living Style")
        
        if st.button("Submit Data"):
            prompt = data_collection_prompt(health_history, family_history, medical_history, living_style)
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Health Assessment":
        st.title("Health Assessment")
        health_history = st.text_input("Health History")
        family_history = st.text_input("Family History")
        medical_history = st.text_input("Medical History")
        living_style = st.text_input("Living Style")
        
        if st.button("Get Assessment"):
            prompt = health_assessment_prompt(health_history, family_history, medical_history, living_style)
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Health Awareness":
        st.title("Health Awareness")
        name = st.text_input("Name")
        age = st.number_input("Age", 0, 100)
        health_goal = st.text_input("Health Goal")
        
        if st.button("Generate Tips"):
            prompt = health_awareness_prompt(name, age, health_goal)
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Counseling":
        st.title("Counseling")
        question = st.text_input("What would you like counseling on?")
        
        if st.button("Get Advice"):
            prompt = counseling_prompt(question)
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Advocacy":
        st.title("Advocacy")
        if st.button("Get Advocacy Resources"):
            prompt = advocacy_prompt()
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Family Planning":
        st.title("Family Planning")
        health_history = st.text_input("Health History")
        family_history = st.text_input("Family History")
        medical_history = st.text_input("Medical History")
        
        if st.button("Get Family Planning Advice"):
            prompt = family_planning_prompt(health_history, family_history, medical_history)
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Sexual Education":
        st.title("Sexual Education")
        sex_question = st.text_input("Ask a question about sexual education")
        
        if st.button("Get Answer"):
            prompt = sexual_education_prompt(sex_question)
            response = get_ai_response(prompt)
            st.write(response)

    elif menu == "Community Visits":
        st.title("Community Visits")
        location = st.text_input("Location for the community visit")
        
        if st.button("Plan Visit"):
            prompt = community_visits_prompt(location)
            response = get_ai_response(prompt)
            st.write(response)
