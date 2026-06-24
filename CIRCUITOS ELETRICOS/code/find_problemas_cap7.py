import fitz
import re

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
doc = fitz.open(pdf_path)

import os
# Let's just save pages 285 to 288 as images
img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

for i in range(285, 289):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    img_path = os.path.join(img_dir, f"sadiku_page_cap7_prob_{i}.png")
    pix.save(img_path)
    print(f"Saved {img_path}")
