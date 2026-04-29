# 🤖 AI LeetCode Solver

A mobile-friendly AI-powered coding assistant that helps you **understand and solve LeetCode-style problems** using natural language.

This project focuses on **learning + problem solving**, not just giving answers.

---

## 🚀 Features

- 💡 **Hints Mode (Learning First)**
  - Step-by-step guidance
  - Helps you think, not just copy

- 🛠️ **Full Solution Mode**
  - Complete explanation
  - Clean C++ & Python code
  - Time & Space complexity

- 📱 **Mobile-Friendly UI**
  - Clean and responsive design
  - Works smoothly on phones

- ⚡ **Fast AI Responses**
  - Powered by Google Gemini API

- 🧠 **Beginner-Friendly Explanations**
  - Easy-to-understand logic
  - Structured output

---

## 🎥 Demo & Explanation Video

Watch the full demo and explanation of the project:

👉 [https://youtube.com/shorts/cDdLSeD4f5w](https://youtube.com/shorts/cDdLSeD4f5w)


### 📌 What the video covers:

- 🔍 Project overview
- 🧠 How the AI solves problems (Hints vs Full Solution)
- 📱 Mobile-friendly UI walkthrough
- 💻 Live demo (input → solution)
- ⚙️ Code structure explanation

---

## 🎯 Use Cases

- 📖 Practice coding problems
- 🧠 Understand algorithms easily
- 🎯 Prepare for interviews
- 💻 Learn problem-solving approaches
- ⚡ Get unstuck quickly

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** (UI)
- **Google Gemini API** (LLM)
- **python-dotenv**

---

## 🏗️ How It Works

```
User Inputs Problem (Text)
        ↓
   Streamlit UI
        ↓
   Gemini API (LLM)
        ↓
 ┌───────────────┬───────────────┐
 │ Hints Mode    │ Full Solution │
 ↓               ↓
Guidance         Code + Explanation
```

---

## 📁 Project Structure

```
AI-ML-Project 04 AI LeetCode Solver/
├── app.py          # Streamlit UI
├── solver.py       # AI logic (Gemini integration)
├── requirements.txt
├── .env.example
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/monjurmbm404/AI-ML-Projects.git
cd "AI-ML-Projects/AI-ML-Project 04 AI LeetCode Solver"
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 How to Use

1. Paste a coding problem (e.g. from LeetCode)
2. Select mode:
   - 💡 Hints → for learning
   - 🛠️ Full Solution → for complete answer

3. Click **Solve Problem**
4. Get:
   - 🧠 Explanation
   - ⚙️ Code
   - ⏱️ Complexity analysis

---

## 📌 Example

**Input:**

```
Given an array nums, find the maximum subarray sum.
```

**Output:**

- Algorithm: Kadane’s Algorithm
- Explanation
- C++ / Python code
- Time Complexity: O(n)

---

## ⚠️ Limitations

- Requires internet connection
- AI responses may vary slightly
- Not a replacement for real practice
- Depends on API performance

---

## 🔮 Future Improvements

- 🔍 Similar problem suggestions (RAG)
- 🧠 Chat history / memory
- 📋 Copy code button
- 🌐 Multi-language support
- 📊 Difficulty detection (Easy/Medium/Hard)
- 🚀 Deployment (Streamlit Cloud)

---

## 💡 Why This Project?

Most beginners struggle with:

- Understanding problem statements
- Finding the right approach
- Writing optimized code

This tool helps by:

- Explaining problems clearly
- Guiding step-by-step
- Providing structured solutions

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
