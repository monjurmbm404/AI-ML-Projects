import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-3-flash-preview"


def build_prompt(problem_text, mode):
    if mode == "Hints":
        return f"""
You are an expert competitive programmer.

Problem:
{problem_text}

Your task:
- Understand the problem
- Give step-by-step hints ONLY
- Do NOT give full code
- Help user think

Keep it beginner-friendly.
"""

    else:
        return f"""
You are an expert competitive programmer.

Problem:
{problem_text}

Your task:
1. Explain the problem
2. Give optimal approach
3. Provide clean code (C++ and Python)
4. Add time & space complexity

Format nicely using markdown.
"""


def solve_text(problem_text, mode):
    model = genai.GenerativeModel(MODEL)

    prompt = build_prompt(problem_text, mode)

    response = model.generate_content(prompt)

    return response.text


def solve_image(image, mode):
    model = genai.GenerativeModel(MODEL)

    if mode == "Hints":
        prompt = """
You are an expert competitive programmer.

The user uploaded a screenshot of a coding problem.

Your job:
- Understand the problem from image
- Give hints ONLY
- Do NOT give full solution
"""
    else:
        prompt = """
You are an expert competitive programmer.

The user uploaded a screenshot of a coding problem.

Your job:
- Extract problem
- Explain clearly
- Give optimal solution
- Provide code (C++ + Python)
- Include complexity
"""

    response = model.generate_content([prompt, image])

    return response.text