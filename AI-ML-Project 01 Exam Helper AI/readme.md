# 📚 AIML Project 01 — Exam Helper AI

An AI-powered study assistant that converts uploaded notes/images into **exam-ready Bangla notes, MCQ quizzes, and audio summaries** using Google Gemini API and Streamlit.

---

## 🚀 Features

- 📝 **AI Note Generator**
  Converts images into structured, exam-ready Bangla notes (concise & easy to revise)

- ❓ **MCQ Quiz Generator**
  Generates exam-style multiple-choice questions with adjustable difficulty

- 🔊 **Audio Notes (Bangla)**
  Converts generated notes into speech for listening-based learning

- 📸 **Image Input Support**
  Works with handwritten or printed notes (max 3 images)

- ⚡ **Fast & Interactive UI**
  Built with Streamlit for a smooth and simple experience

---

## 🎥 Demo & Explanation Video

Watch the full explanation and live demo of the project:

👉 https://www.youtube.com/watch?v=YOUR_VIDEO_ID

**What the video covers:**

- Project overview
- How the system works (Gemini + Streamlit + gTTS)
- Live demo (upload → notes → quiz → audio)
- Code structure explanation

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API** (`google-generativeai`)
- **Pillow (PIL)**
- **gTTS (Text-to-Speech)**
- **python-dotenv**

---

## 🏗️ How It Works

```
User Uploads Images
        ↓
   Streamlit UI
        ↓
 Gemini API (Vision + Text Processing)
        ↓
 ┌───────────────┬───────────────┐
 │ Notes         │ Quiz          │
 │ Generation    │ Generation    │
 ↓               ↓
Structured Text  JSON MCQs
        ↓
     gTTS
        ↓
   Audio Output
```

---

## 📁 Project Structure

```
AI-ML-Projects/
└── AI-ML-Project 01 Exam Helper AI/
    ├── app.py
    ├── api_calling.py
    ├── requirements.txt
    ├── .env.example
```

---

## ⚙️ Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/monjurBakthMazumder/AI-ML-Projects.git
cd "AI-ML-Projects/AI-ML-Project 01 Exam Helper AI"
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Upload up to **3 images of notes**
2. Enter subject (optional)
3. Select quiz difficulty
4. Click **Generate Exam Content**
5. Get instantly:
   - 📘 Exam-ready structured notes
   - 🔊 Audio version (Bangla)
   - ❓ MCQ quiz with answers

---

## 📌 Use Cases

- 📖 Exam revision from handwritten notes
- 🧠 Quick Bangla study summaries
- 🎯 Self-assessment using MCQs
- 🎧 Learning through audio

---

## ⚠️ Limitations

- Maximum **3 images per session**
- Requires **internet connection**
- Gemini responses may vary slightly
- JSON quiz output may occasionally need fallback handling

---

## 🔮 Future Improvements

- User authentication system
- Save notes & quiz history
- Performance tracking dashboard
- Better image-to-text accuracy
- Mobile-friendly UI

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
