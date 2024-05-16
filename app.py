from flask import Flask, render_template, request, jsonify
import PyPDF2
import os

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'pdfFile' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['pdfFile']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        text = extract_text_from_pdf(file_path)
        os.remove(file_path)
        return jsonify({'text': text})

    return jsonify({'error': 'Invalid file format'})

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
