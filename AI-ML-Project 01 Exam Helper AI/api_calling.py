import os
import io
import json
from dotenv import load_dotenv
import google.generativeai as genai
from gtts import gTTS

# ---------------- LOAD ENV ----------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-3-flash-preview"


# ---------------- NOTE GENERATOR ----------------
def note_generator(images, subject=""):
    prompt = f"""
You are an expert Bangladeshi exam teacher.

Create EXAM READY NOTES in Bangla.

Subject: {subject}

Rules:
- Use clean markdown
- Must be structured:
  1. Topic Summary
  2. Key Points
  3. Important Facts
  4. Exam Tips
- Keep under 150 words
- Easy Bangla
"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content([prompt] + images)

    return response.text


# ---------------- AUDIO GENERATOR ----------------
def audio_generator(text):
    clean_text = text.replace("#", "").replace("*", "").replace("-", "")

    speech = gTTS(text=clean_text, lang="bn", slow=False)

    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return audio_buffer


# ---------------- QUIZ GENERATOR ----------------
def quiz_generator(images, difficulty, subject=""):
    prompt = f"""
Create 3 EXAM MCQs based on images.

Subject: {subject}
Difficulty: {difficulty}

Rules:
- 4 options each
- include correct answer
- output ONLY JSON format like this:

[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "B"
  }}
]

Language: Bangla
"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content([prompt] + images)

    try:
        return json.loads(response.text)
    except:
        return [
            {
                "question": "Error generating quiz",
                "options": ["A", "B", "C", "D"],
                "answer": "A"
            }
        ]