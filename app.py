from flask import Flask, request, jsonify
import PyPDF2
import io

app = Flask(__name__)

def extract_text_from_pdf(pdf_bytes):
    text = ""
    with io.BytesIO(pdf_bytes) as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    pdf_file = request.files['pdfFile']
    if pdf_file:
        pdf_bytes = pdf_file.read()
        pdf_text = extract_text_from_pdf(pdf_bytes)
        return jsonify({'text': pdf_text})
    else:
        return jsonify({'error': 'No file uploaded'})

if __name__ == "__main__":
    app.run(debug=True)
