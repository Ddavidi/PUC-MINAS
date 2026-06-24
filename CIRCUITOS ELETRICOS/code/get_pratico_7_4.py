import fitz
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
doc = fitz.open(pdf_path)

page = doc.load_page(251) # Same page as 7.3
pix = page.get_pixmap(dpi=150)
img_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_7_4.png"
pix.save(img_path)
print(f"Saved page image to {img_path}")
