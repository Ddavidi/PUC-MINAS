import fitz
import os

pdf_path = [f for f in os.listdir('.') if 'Sadiku' in f and f.endswith('.pdf')][0]
doc = fitz.open(pdf_path)

text = '\n'.join([page.get_text() for page in doc.pages(260, 295)])
i = text.find('7.15')
if i != -1:
    print(text[i-50:i+1500])
else:
    print("Not found")
