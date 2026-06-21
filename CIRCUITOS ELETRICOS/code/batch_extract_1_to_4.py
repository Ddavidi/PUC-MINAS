import fitz
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"

chapters = {
    "01": (23, 45),
    "02": (46, 89),
    "03": (90, 131),
    "04": (132, 173)
}

doc = fitz.open(pdf_path)

for cap, (start_page, end_page) in chapters.items():
    print(f"Processando Capítulo {cap} (páginas {start_page} a {end_page})...")
    out_dir = os.path.join(base_dir, f"capitulo_{cap}")
    os.makedirs(out_dir, exist_ok=True)
    
    # Text
    text = ""
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        text += f"--- PÁGINA {page_num + 1} ---\n"
        text += page.get_text()
        text += "\n\n"
        
    ai_dir = os.path.join(out_dir, "_base_dados_ia")
    os.makedirs(ai_dir, exist_ok=True)
    
    with open(os.path.join(ai_dir, f"capitulo{cap}_texto.txt"), "w", encoding="utf-8") as f:
        f.write(text)
        
    # Images
    for page_num in range(start_page - 1, end_page):
        page = doc[page_num]
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        pix.save(os.path.join(ai_dir, f"pagina_{page_num + 1}.png"))
        
    # Cria diretórios extras p/ organização padrão
    os.makedirs(os.path.join(out_dir, "atividades"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "pdfs_extras"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "exercicios_propostos"), exist_ok=True)
        
print("Extração em lote finalizada para os capítulos 1 ao 4!")
doc.close()
