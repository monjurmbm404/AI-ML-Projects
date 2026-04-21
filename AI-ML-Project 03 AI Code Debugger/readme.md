# 🐞 AI-ML Project 03 — AI Code Debugger

An AI-powered debugging assistant that analyzes **code error screenshots** and provides **hints or full solutions** using Google Gemini Vision API.

---

## 🚀 Features

- 📸 **Screenshot-Based Debugging**
  Upload images of code errors (IDE, terminal, browser)

- 🧠 **AI Error Analysis**
  Automatically detects bugs and explains issues clearly

- 💡 **Hints Mode**
  Beginner-friendly guidance without revealing full answers

- 🛠️ **Solution Mode**
  Provides complete fixed code with explanation

- ⚡ **Fast Streamlit UI**
  Simple and interactive interface for instant results

---
Here’s the updated section with a demo link added 👇

---

## 🎥 Demo & Explanation Video

Watch the full demo and explanation of the project:

👉 [https://youtube.com/shorts/mlR4ujXphpU](https://youtube.com/shorts/mlR4ujXphpU)

**What the video covers:**

* Upload error screenshot
* Select mode (Hints / Solution)
* AI analyzes and detects the bug
* Get instant debugging help (hints or full solution)


---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API (Vision + LLM)** (`google-generativeai`)
- **Pillow (PIL)**
- **python-dotenv**

---

## 🏗️ How It Works

```
User Uploads Screenshot
        ↓
   Streamlit UI
        ↓
 Gemini Vision Model
        ↓
 Error Understanding
        ↓
 ┌───────────────┬───────────────┐
 │ Hints Mode    │ Solution Mode │
 ↓               ↓
Guidance         Fixed Code
```

---

## 📁 Project Structure

```
AI-ML-Projects/
└── AI-ML-Project 03 AI Code Debugger/
    ├── app.py           # Streamlit UI
    ├── api_utils.py     # Gemini API integration
    ├── requirements.txt
    ├── .env.example
```

---

## ⚙️ Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/monjurBakthMazumder/AI-ML-Projects.git
cd "AI-ML-Projects/AI-ML-Project 03 AI Code Debugger"
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

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

1. Upload a **code error screenshot**
2. Select output type:
   - 💡 Hints (guided help)
   - 🛠️ Solution (full fix)

3. Click **Debug Code**
4. Get:
   - 🧠 Error explanation
   - ✅ Fix or hints

---

## 📌 Use Cases

- 🧑‍💻 Debugging Python / C++ / Java errors
- 📚 Learning programming with guidance
- 🧠 Understanding compiler/runtime errors
- ⚡ Quick help during coding practice

---

## ⚠️ Limitations

- Depends on **image quality**
- May struggle with **blurry or complex screenshots**
- Requires **internet connection**
- Output accuracy depends on Gemini response

---

## 🔮 Future Improvements

- OCR fallback for better text extraction
- Code copy/download button
- Multi-image debugging support
- Chat-based follow-up questions
- Error history tracking
- Deployment (Streamlit Cloud)

---

## 💡 Why This Project?

Many beginners struggle to understand error messages from IDEs or terminals.
This tool simplifies debugging by converting screenshots into **clear explanations and actionable fixes**.

---

## 🧾 Example Scenario

**Input:**
Screenshot of Python error (`ZeroDivisionError`)

**Output (Hints Mode):**

```
You're trying to divide a number by zero.
Check the value of the denominator before division.
```

**Output (Solution Mode):**

```python
a = 10
b = 1  # Avoid zero
result = a / b
print(result)
```

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
