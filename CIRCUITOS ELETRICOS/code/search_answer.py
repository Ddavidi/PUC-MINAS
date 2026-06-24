import fitz  # PyMuPDF
import sys

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"

try:
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    # Search the last 50 pages for the answer section
    print(f"Searching the last 50 pages of {num_pages} pages...")
    with open("respostas.txt", "w", encoding="utf-8") as f:
        for i in range(max(0, num_pages - 50), num_pages):
            page = doc[i]
            text = page.get_text()
            if "7.13" in text or "7.15" in text or "Capítulo 7" in text:
                f.write(f"--- Page {i+1} ---\n")
                lines = text.split('\n')
                for j, line in enumerate(lines):
                    if "7." in line:
                        f.write(line.strip() + "\n")
except Exception as e:
    with open("respostas.txt", "a", encoding="utf-8") as f:
        f.write(f"Error: {e}\n")
