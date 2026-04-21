import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)


def analyze_code(image, mode):
    """
    image: PIL image
    mode: 'Hints' or 'Solution'
    """

    model = genai.GenerativeModel("gemini-3-flash-preview")

    if mode == "Hints":
        prompt = """
        The user uploaded a screenshot of code with an error.

        Your job:
        - Identify the error
        - Give hints ONLY (no full solution)
        - Keep it beginner-friendly
        """

    else:
        prompt = """
        The user uploaded a screenshot of code with an error.

        Your job:
        - Identify the bug
        - Explain clearly
        - Provide the FIXED CODE
        - Format nicely using markdown
        """

    response = model.generate_content([prompt, image])

    return response.text