import PyPDF2
import tkinter as tk
from tkinter import filedialog
import io

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    pdf_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return pdf_path

# Example usage:
if __name__ == "__main__":
    pdf_path = select_pdf_file()
    if pdf_path:
        pdf_text = extract_text_from_pdf(pdf_path)
        print(pdf_text)
    else:
        print("No file selected.")
