# prompts.py

# 1. Data Collection Prompt
def data_collection_prompt(health_history, family_history, medical_history, living_style):
    return f"""
    The user has provided their health, family, and medical history. Please analyze the following data:
    - Health History: {health_history}
    - Family History: {family_history}
    - Medical History: {medical_history}
    - Living Style: {living_style}
    Use this data to identify potential health risks, conditions to monitor, and lifestyle adjustments.
    """

# 2. Health Assessment Prompt
def health_assessment_prompt(health_history, family_history, medical_history, living_style):
    return f"""
    Based on the patient's health history, family history, and lifestyle, provide a comprehensive health assessment.
    - Health History: {health_history}
    - Family History: {family_history}
    - Medical History: {medical_history}
    - Living Style: {living_style}
    Consider potential health risks and provide recommendations for improvement.
    """

# 3. Health Awareness Prompt
def health_awareness_prompt(name, age, health_goal):
    return f"""
    Provide personalized health tips for {name}, age {age}, whose goal is {health_goal}. Tailor these tips to their 
    current health status and lifestyle.
    """

# 4. Counseling Prompt
def counseling_prompt(question):
    return f"Counsel the user on: {question}. Think deeply through the issue and offer holistic advice."

# 5. Advocacy Prompt
def advocacy_prompt():
    return """
    Provide the user with tailored advocacy resources on their healthcare rights. Explain patient rights, informed 
    consent, and how to navigate healthcare systems effectively.
    """

# 6. Family Planning Prompt
def family_planning_prompt(health_history, family_history, medical_history):
    return f"""
    Considering the user's health, family, and medical history, provide personalized family planning advice. Discuss 
    contraceptive options and reproductive health based on their unique health profile.
    """

# 7. Sexual Education Prompt
def sexual_education_prompt(sex_question):
    return f"Provide a comprehensive answer to the user's sexual education question: {sex_question}"

# 8. Community Visits Prompt
def community_visits_prompt(location):
    return f"""
    The user has requested a community health visit in {location}. Plan how the visit could benefit the user's health 
    based on their background data, and explain what services they might expect during the visit.
    """

# General Error Handling Prompt
def error_handling_prompt():
    return "Please provide the missing information to generate an accurate response."

# ---- Report Analyzer Prompts ----

# 9. Medical Report Data Extraction Prompt
def report_extraction_prompt():
    return """I have a medical report containing various test results. Please extract and organize all the details mentioned in the report, including the following parameters:

1. Patient's Name
2. Age
3. Gender
4. Test Report Date
5. Complete Blood Count (CBC) parameters including:
   - Hemoglobin
   - RBC Count
   - Hematocrit
   - MCV
   - MCH
   - MCHC
   - RDW-CV
   - RDW-SD
   - Platelet Count
   - MPV
   - PDW
   - PCT
   - Total WBC Count (WBC)
   - Differential WBC Count (Neutrophils, Lymphocytes, Monocytes, Eosinophils, Basophils) as both percentage and absolute counts
6. Reference ranges for each parameter, if available.
7. Any other relevant information mentioned in the report (e.g., doctor's notes or comments).
The report is structured as follows:
- Header with patient details (Name, Age, Gender, Registration Date, and Report Date)
- Test section listing various blood count parameters with observed values and reference ranges.
- Please extract and organize the details in the following tabular format:
    
    | Test Name          | Result   | Normal Range   |
    |--------------------|----------|----------------|
"""

# 10. Medical Report Analysis Prompt
def report_analysis_prompt(extracted_report):
    return f"""
     
    You are a professional doctor reviewing the following Complete Blood Count (CBC) report details: {extracted_report}

    Step-by-step, perform a thorough analysis of this CBC report by focusing on key components such as White Blood Cell count, Red Blood Cell count, Hemoglobin levels, Hematocrit percentage, Platelet count, and any other relevant indices. Identify any abnormalities or significant findings in these parameters.

    Based on your analysis:
    1. Provide a detailed summary of the patient's current health status.
    2. Offer specific recommendations for lifestyle and dietary improvements that could help optimize their blood health and overall well-being.

    Ensure your response is comprehensive yet clear, maintaining professional language suitable for communicating with both healthcare professionals and patients."""

