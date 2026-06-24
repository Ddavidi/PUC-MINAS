import fitz

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
doc = fitz.open(pdf_path)

targets = [
    "Problema prático 7.10",
    "Problema prático 7.12",
    "7.2 ",
    "7.3 ",
    "7.4 "
]

for page_num in range(250, 300):
    page = doc.load_page(page_num)
    text = page.get_text()
    for target in targets:
        if target in text:
            print(f"'{target}' found on page {page_num}")
