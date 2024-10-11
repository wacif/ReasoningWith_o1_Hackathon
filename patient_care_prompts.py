# prompts.py

def data_collection_prompt(health_history, family_history, medical_history, living_style):
    """
    Generates a prompt for data collection analysis based on provided health details.
    """
    return f"""
    Perform a detailed analysis based on the following data:
    - Health History: {health_history}
    - Family History: {family_history}
    - Medical History: {medical_history}
    - Living Style: {living_style}
    
    Provide a summary and insights on the patient's current health status.
    """

def health_assessment_prompt(health_history, family_history, medical_history, living_style):
    """
    Generates a prompt for health assessment based on the provided user input.
    """
    return f"""
    Given the following data:
    - Health History: {health_history}
    - Family History: {family_history}
    - Medical History: {medical_history}
    - Living Style: {living_style}
    
    Provide a health assessment that includes risks, suggestions for improvement, and any necessary follow-ups.
    """

def health_awareness_prompt(name, age, health_goal):
    """
    Generates a prompt for personalized health tips based on user's age and health goals.
    """
    return f"""
    Provide personalized health tips for the following individual:
    - Name: {name}
    - Age: {age}
    - Health Goal: {health_goal}
    
    The tips should focus on achieving the specified health goal, while considering age-related health factors.
    """

def counseling_prompt(question):
    """
    Generates a counseling prompt based on the user's question.
    """
    return f"""
    Provide counseling advice for the following question:
    - Question: {question}
    
    The advice should be detailed and address the user's concerns in a supportive and informative manner.
    """

def advocacy_prompt():
    """
    Generates a prompt for advocacy resources.
    """
    return """
    Provide a list of advocacy resources and explain how they can support patients in terms of health rights, social support, and access to healthcare services.
    """

def family_planning_prompt(health_history, family_history, medical_history):
    """
    Generates a prompt for family planning advice based on user health details.
    """
    return f"""
    Based on the following information:
    - Health History: {health_history}
    - Family History: {family_history}
    - Medical History: {medical_history}
    
    Provide detailed family planning advice, including potential risks and recommendations.
    """

def sexual_education_prompt(sex_question):
    """
    Generates a prompt for sexual education based on the user's question.
    """
    return f"""
    Provide an accurate and clear answer to the following sexual education question:
    - Question: {sex_question}
    
    Ensure that the information is appropriate, scientifically accurate, and helps the user understand the topic.
    """

def community_visits_prompt(location):
    """
    Generates a prompt for planning a community visit based on the specified location.
    """
    return f"""
    Plan a community health visit for the following location:
    - Location: {location}
    
    Include details such as healthcare services that can be provided, outreach strategies, and the impact on community health.
    """

def report_extraction_prompt():

    return """
    Analyze the uploaded medical report and extract important data such as test names, results, and normal ranges.
    Please extract and organize all the details mentioned in the report, including the following parameters:

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
- Present the extracted data in a structured, tabular format.
    """

def report_analysis_prompt(extracted_report):
    """
    Generates a prompt for analyzing the extracted data from a medical report.
    """
    return f"""
    Based on the following extracted report data:
    {extracted_report}
    
    Perform a detailed analysis and provide insights. Include any abnormal results, potential health risks, summary and recommendations for follow-up tests or treatments.
    """

def error_handling_prompt():
    """
    Generates a prompt for handling errors and guiding users through corrections.
    """
    return """
    If an error occurs during data extraction or report analysis, explain it to the user clearly and provide steps to correct the issue. Offer suggestions for improving the input or report quality.
    """
