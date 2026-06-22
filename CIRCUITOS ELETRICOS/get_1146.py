import fitz
import os

pdf_path = [f for f in os.listdir('.') if 'Sadiku' in f and f.endswith('.pdf')][0]
doc = fitz.open(pdf_path)

for i, page in enumerate(doc):
    text = page.get_text()
    if '11.46' in text:
        print(f"--- Page {i+1} ---")
        print(text)
        print("-----------------")
