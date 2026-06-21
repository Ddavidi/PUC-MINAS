import fitz
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"

chapters = {
    "06": (209, 242),
    "07": (243, 295),
    "11": (425, 464)
}

doc = fitz.open(pdf_path)

for cap, (start_page, end_page) in chapters.items():
    print(f"Processando Capítulo {cap} (páginas {start_page} a {end_page})...")
    
    # Text
    text = ""
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        text += f"--- PÁGINA {page_num + 1} ---\n"
        text += page.get_text()
        text += "\n\n"
        
    out_dir = os.path.join(base_dir, f"capitulo_{cap}")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"capitulo{cap}_texto.txt"), "w", encoding="utf-8") as f:
        f.write(text)
        
    # Images
    img_dir = os.path.join(out_dir, "imagens")
    os.makedirs(img_dir, exist_ok=True)
    
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        pix.save(os.path.join(img_dir, f"pagina_{page_num + 1}.png"))
        
print("Extração em lote finalizada!")
doc.close()
