import os
from flask import Flask, render_template, request, jsonify
import PyPDF2
import docx
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini 2.5 Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def extract_pdf(file):
    reader = PyPDF2.PdfReader(file)
    return "".join([page.extract_text() or "" for page in reader.pages])

def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    jd = request.form.get('job_description')
    file = request.files.get('resume')

    if not jd or not file:
        return jsonify({"error": "JD or Resume missing"}), 400

    try:
        # File Extraction
        text = extract_pdf(file) if file.filename.endswith('.pdf') else extract_docx(file)
        
        # Cleaning to avoid Python 3.10 f-string backslash error
        clean_text = text.replace('"', "'").replace('\n', ' ')
        clean_jd = jd.replace('"', "'").replace('\n', ' ')

        # Gemini 2.5 Analysis
        prompt = f"Act as an ATS. Compare JD: {clean_jd} with Resume: {clean_text}. Return: Match Score, Missing Keywords, and Advice."
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({"analysis": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)