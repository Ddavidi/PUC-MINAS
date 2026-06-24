import fitz  # PyMuPDF

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"

try:
    doc = fitz.open(pdf_path)
    for i in range(250, 300):
        page = doc[i]
        text = page.get_text()
        if "7.15" in text:
            print(f"--- Page {i+1} ---")
            lines = text.split('\n')
            for j, line in enumerate(lines):
                if "7.15" in line or "Figura 7.95" in line:
                    start = max(0, j-5)
                    end = min(len(lines), j+25)
                    for k in range(start, end):
                        print(lines[k])
                    break
except Exception as e:
    print(f"Error: {e}")
