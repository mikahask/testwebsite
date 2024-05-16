from flask import Flask, request, jsonify
from input import extract_text_from_pdf, select_pdf_file

app = Flask(__name__)

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'pdfFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    pdf_file = request.files['pdfFile']
    if pdf_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    pdf_text = extract_text_from_pdf(pdf_file)
    return jsonify({'text': pdf_text})

if __name__ == '__main__':
    app.run(debug=True)
