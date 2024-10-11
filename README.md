# HealthAI App Documentation

Welcome to the **HealthAI** application! This documentation provides comprehensive information to help you understand, install, configure, and utilize the HealthAI app effectively.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running the App](#running-the-app)
  - [Available Prompts](#available-prompts)
- [Code Structure](#code-structure)
  - [prompts.py](#promptspy)
  - [config.py](#configpy)
- [API Integration](#api-integration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Introduction

**HealthAI** is a healthcare-focused application designed to assist users in various aspects of health management. Leveraging the power of OpenAI's language models, HealthAI provides features such as health assessments, personalized health tips, counseling advice, advocacy resources, family planning advice, sexual education, community health visit planning, medical report extraction, and analysis.

This application is built using Python and Streamlit, making it accessible and user-friendly through a web interface.

## Features

- **Data Collection Analysis:** Gather and analyze health-related data.
- **Health Assessment:** Assess health status, identify risks, and provide improvement suggestions.
- **Personalized Health Tips:** Offer tailored health advice based on user demographics and goals.
- **Counseling Advice:** Provide supportive and informative advice for user queries.
- **Advocacy Resources:** List and explain resources supporting health rights and access.
- **Family Planning Advice:** Offer detailed family planning recommendations.
- **Sexual Education:** Answer sexual health questions with accurate information.
- **Community Health Visit Planning:** Plan and strategize community health initiatives.
- **Medical Report Extraction:** Extract and organize data from medical reports.
- **Report Analysis:** Analyze extracted medical data and provide insights.
- **Error Handling:** Manage and guide users through potential errors effectively.

## Requirements

Before installing HealthAI, ensure you have the following dependencies:

- **Python Libraries:**
  - `streamlit`
  - `openai`
  - `requests`
  - `pandas`
  - `Pillow`
  - `python-dotenv`

These are specified in the `requirements.txt` file.

## Installation

### Prerequisites

- **Python 3.7 or higher** installed on your system.
- **pip** package installer.
- An **OpenAI API key** for accessing OpenAI's language models.
- **Git** (optional) for cloning the repository.

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/healthai.git
   cd healthai
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   AIML_API=your_openai_api_key_here
   ```

   Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Configuration

The `config.py` file manages the application's configuration settings, particularly the API integration.

```python
import os

# Set your API key and base URL here
AIML_API_KEY = os.getenv('AIML_API')  # Make sure to set this in your environment
BASE_URL = "https://api.aimlapi.com/"
```

- **AIML_API_KEY:** Retrieves the OpenAI API key from environment variables.
- **BASE_URL:** The base URL for the AI/ML API endpoint.

Ensure that the `.env` file is correctly set up with your API key for seamless integration.

## Usage

### Running the App

To launch the HealthAI application, use Streamlit's CLI:

```bash
streamlit run app.py
```

Ensure you're in the project's root directory and that all dependencies are installed.

### Available Prompts

HealthAI utilizes various prompts to interact with users and process their input. Below is an overview of the available prompts:

1. **Data Collection Analysis**

   ```python
   data_collection_prompt(health_history, family_history, medical_history, living_style)
   ```
   - Analyzes provided health details and summarizes the patient's current health status.

2. **Health Assessment**

   ```python
   health_assessment_prompt(health_history, family_history, medical_history, living_style)
   ```
   - Assesses health risks, offers improvement suggestions, and recommends follow-ups.

3. **Personalized Health Tips**

   ```python
   health_awareness_prompt(name, age, health_goal)
   ```
   - Provides tailored health advice based on user demographics and goals.

4. **Counseling Advice**

   ```python
   counseling_prompt(question)
   ```
   - Offers supportive and informative advice for user queries.

5. **Advocacy Resources**

   ```python
   advocacy_prompt()
   ```
   - Lists resources supporting health rights, social support, and healthcare access.

6. **Family Planning Advice**

   ```python
   family_planning_prompt(health_history, family_history, medical_history)
   ```
   - Provides detailed family planning recommendations, including risks and suggestions.

7. **Sexual Education**

   ```python
   sexual_education_prompt(sex_question)
   ```
   - Answers sexual health questions with accurate and appropriate information.

8. **Community Health Visit Planning**

   ```python
   community_visits_prompt(location)
   ```
   - Plans community health visits, detailing services, outreach strategies, and impact.

9. **Medical Report Extraction**

   ```python
   report_extraction_prompt()
   ```
   - Extracts and organizes data from uploaded medical reports into a structured format.

10. **Report Analysis**

    ```python
    report_analysis_prompt(extracted_report)
    ```
    - Analyzes extracted medical data, identifies abnormalities, and provides health insights.

11. **Error Handling**

    ```python
    error_handling_prompt()
    ```
    - Manages errors during data extraction or report analysis, guiding users to correct issues.

## Code Structure

Understanding the codebase structure will help in navigating and potentially contributing to the project.

### `prompts.py`

This module contains functions that generate specific prompts used throughout the application. Each function corresponds to a particular feature, such as health assessment or counseling advice.

#### Key Functions:

- `data_collection_prompt(...)`
- `health_assessment_prompt(...)`
- `health_awareness_prompt(...)`
- `counseling_prompt(...)`
- `advocacy_prompt()`
- `family_planning_prompt(...)`
- `sexual_education_prompt(...)`
- `community_visits_prompt(...)`
- `report_extraction_prompt()`
- `report_analysis_prompt(...)`
- `error_handling_prompt()`

Each function formats a prompt string that is sent to the OpenAI API for processing.

### `config.py`

Handles configuration settings, particularly API integration details.

```python
import os

# Set your API key and base URL here
AIML_API_KEY = os.getenv('AIML_API')  # Make sure to set this in your environment
BASE_URL = "https://api.aimlapi.com/"
```

- **AIML_API_KEY:** Fetches the API key from environment variables.
- **BASE_URL:** Base endpoint for API requests.

Ensure that environment variables are correctly set to enable seamless API interactions.

## API Integration

HealthAI integrates with OpenAI's language models to process and generate responses based on user input. The integration is managed through the `openai` library.

### Setting Up OpenAI API Key

1. **Obtain API Key:**

   - Sign up or log in to your [OpenAI account](https://beta.openai.com/).
   - Navigate to the API section and generate a new API key.

2. **Configure API Key:**

   - Create a `.env` file in the root directory.
   - Add the following line, replacing the placeholder with your actual API key:

     ```env
     AIML_API=your_openai_api_key_here
     ```

   - Ensure that `python-dotenv` is installed to load environment variables.

### Making API Requests

The application constructs prompt strings using functions from `prompts.py` and sends them to the OpenAI API using parameters such as model type, temperature, and max tokens. Responses are then processed and displayed to the user.

## Error Handling

HealthAI includes robust error handling to manage issues during data extraction and report analysis. The `error_handling_prompt()` function generates guidance for users when errors occur, ensuring clarity and providing steps to resolve issues.

### Common Error Scenarios:

- **Invalid Input:** User provides incomplete or incorrect data.
- **API Failures:** Issues with the OpenAI API, such as rate limiting or downtime.
- **Data Extraction Errors:** Problems parsing or extracting information from medical reports.

### User Guidance:

When an error is detected, the application:

1. **Displays a Clear Message:** Explains what went wrong in simple terms.
2. **Provides Correction Steps:** Offers actionable steps to fix the issue.
3. **Suggests Improvements:** Recommends ways to enhance input quality for better results.

## Contributing

We welcome contributions to enhance HealthAI! Whether it's reporting bugs, suggesting features, or submitting pull requests, your input is valuable.

### Steps to Contribute:

1. **Fork the Repository:**

   - Click the "Fork" button on the repository page to create a personal copy.

2. **Clone the Forked Repository:**

   ```bash
   git clone https://github.com/yourusername/healthai.git
   cd healthai
   ```

3. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes:**

   - Implement your feature or fix.

5. **Commit Your Changes:**

   ```bash
   git commit -m "Add feature: YourFeatureName"
   ```

6. **Push to Your Fork:**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request:**

   - Navigate to the original repository and create a pull request from your forked branch.

### Code Standards:

- Follow Python's PEP 8 style guidelines.
- Include docstrings and comments for clarity.
- Ensure all tests pass before submitting.


## Acknowledgements

- **OpenAI:** For providing the powerful language models that drive HealthAI.
- **Streamlit:** For enabling the creation of an interactive web interface.
- **Pandas & Pillow:** For data manipulation and image processing capabilities.
- **Python-dotenv:** For managing environment variables effectively.

---

For further assistance or inquiries, please contact [nwasi1930@gmail.com](nwasi1930@gmail.com).