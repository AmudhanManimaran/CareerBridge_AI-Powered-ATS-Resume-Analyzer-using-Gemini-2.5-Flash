# CareerBridge — AI-Powered ATS Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?style=flat-square&logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> A Flask web application that uses **Gemini 2.5 Flash** to compare a resume against a job description — returning an ATS match score, missing keywords, and targeted improvement advice in real time.

---

## 🎯 What It Does

- Accepts a **resume** (PDF or DOCX) and a **job description** (text input)
- Extracts and normalizes raw text from the uploaded file
- Sends both to **Gemini 2.5 Flash** with an ATS-persona prompt
- Returns: **Match Score**, **Missing Keywords**, and **Actionable Advice**
- Displays results instantly in the browser via a Flask web interface

---

## 🏗️ System Architecture

```
User Uploads Resume (PDF / DOCX) + Job Description (Text)
                    │
                    ▼
     ┌──────────────────────────────┐
     │    Text Extraction Layer     │
     │  PyPDF2 (PDF) / python-docx  │  ← Parses raw resume text
     └──────────────────────────────┘
                    │
                    ▼
     ┌──────────────────────────────┐
     │     Prompt Construction      │  ← Injects JD + Resume into
     │    (ATS Evaluator Persona)   │    a structured ATS prompt
     └──────────────────────────────┘
                    │
                    ▼
     ┌──────────────────────────────┐
     │     Gemini 2.5 Flash         │  ← Compares JD vs Resume
     │     (LLM Analysis Engine)    │    Returns structured analysis
     └──────────────────────────────┘
                    │
                    ▼
          Match Score + Missing Keywords
              + Improvement Advice
                    │
                    ▼
          Flask Web Dashboard
```

---

## 📁 Project Structure

```
CareerBridge/
│
├── ats-resume-checker/
│   ├── app.py                   # Flask backend + Gemini API call
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # API key template
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Frontend styling
│   │   └── js/
│   │       └── script.js        # Async fetch + UI logic
│   └── templates/
│       └── index.html           # Upload + results interface
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AmudhanManimaran/CareerBridge.git
cd CareerBridge/ats-resume-checker
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
```bash
cp .env.example .env
# Open .env and add your Gemini API key:
# GEMINI_API_KEY=your_api_key_here
```
Get your free Gemini API key at: [aistudio.google.com](https://aistudio.google.com)

### 5. Run the Application
```bash
python app.py
```
Visit `http://localhost:5001` in your browser.

---

## 🚀 Usage

1. Open `http://localhost:5001`
2. Paste the **Job Description** into the text box
3. Upload your **Resume** as PDF or DOCX
4. Click **"Analyze"**
5. Review your ATS match score, missing keywords, and advice

---

## 🧠 Technical Details

### Text Extraction
- **PDF** — parsed using `PyPDF2.PdfReader`, concatenating text from all pages
- **DOCX** — parsed using `python-docx`, joining all paragraph text
- Text is cleaned before prompt injection to prevent f-string parsing errors

### LLM Prompt Strategy
A single structured prompt with an **ATS evaluator persona**:
```
Act as an ATS. Compare JD: {job_description} with Resume: {resume_text}.
Return: Match Score, Missing Keywords, and Advice.
```
Gemini 2.5 Flash processes both documents in a single inference call and returns a structured natural language report.

### Why Gemini 2.5 Flash
- Long-context window handles full resumes + job descriptions
- Fast inference suitable for real-time web response
- Strong instruction-following for structured output

---

## 📦 Requirements

```
flask>=2.0.0
PyPDF2>=3.0.0
python-docx>=0.8.11
google-genai>=0.3.0
python-dotenv>=1.0.0
```

---

## ⚠️ Environment Variables

Create a `.env` file inside `ats-resume-checker/`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Never commit your API key to GitHub.** The `.gitignore` excludes `.env` automatically.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Amudhan Manimaran**
- 🌐 Portfolio: [amudhanmanimaran.github.io/Portfolio](https://amudhanmanimaran.github.io/Portfolio/)
- 💼 LinkedIn: [linkedin.com/in/amudhan-manimaran-3621bb32a](https://www.linkedin.com/in/amudhan-manimaran-3621bb32a)
- 🐙 GitHub: [github.com/AmudhanManimaran](https://github.com/AmudhanManimaran)
