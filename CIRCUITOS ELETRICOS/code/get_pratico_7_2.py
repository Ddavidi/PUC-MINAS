import fitz
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
doc = fitz.open(pdf_path)

found_page = -1
for i in range(240, 260):
    page = doc.load_page(i)
    text = page.get_text()
    if "prático 7.2\n" in text.lower() or "prático 7.2 " in text.lower() or "prático 7.2" in text.lower():
        print(f"Found on page {i}!")
        idx = text.lower().find("prático 7.2")
        found_page = i
        break

if found_page != -1:
    page = doc.load_page(found_page)
    pix = page.get_pixmap(dpi=150)
    img_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_7_2.png"
    pix.save(img_path)
    print(f"Saved page image to {img_path}")
