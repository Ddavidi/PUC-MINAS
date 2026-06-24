import fitz
import re

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
doc = fitz.open(pdf_path)

import os
img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

for page_num in [265, 269]:
    page = doc.load_page(page_num)
    pix = page.get_pixmap(dpi=150)
    img_path = os.path.join(img_dir, f"sadiku_page_{page_num}.png")
    pix.save(img_path)
    print(f"Saved {img_path}")
print(f"Saved {img_path}")
