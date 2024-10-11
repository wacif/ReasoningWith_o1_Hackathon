import base64
import re

def sanitize_input(input_text):
    """
    Sanitize the input text to prevent XSS and other attacks.
    """
    # Remove any potentially dangerous characters or HTML tags
    return re.sub(r'<[^>]*>', '', input_text)

def encode_image(uploaded_file):
    """
    Encode an image file to base64 format.
    """
    try:
        return base64.b64encode(uploaded_file.read()).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Error encoding image: {e}")

def validate_image(uploaded_file):
    """
    Validate if the uploaded file is an image of the correct format.
    """
    valid_extensions = ['jpg', 'jpeg']
    if uploaded_file.type.split('/')[-1] in valid_extensions:
        return True
    return False
