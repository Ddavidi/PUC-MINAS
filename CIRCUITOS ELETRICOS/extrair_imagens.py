import fitz  # PyMuPDF
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
output_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\CIRCUITOS ELETRICOS\capitulo9_imagens"

# Create output directory
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Chapter 9: pages 349-388 (1-indexed), so 0-indexed: 348-387
start_page = 349 - 1
end_page = 389 - 1

print(f"Extraindo páginas {start_page+1} a {end_page} como imagens...")

for page_num in range(start_page, end_page):
    page = doc[page_num]
    # Render at 2x resolution for clarity (default is 72 DPI, so 144 DPI)
    mat = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=mat)
    output_path = os.path.join(output_dir, f"pagina_{page_num + 1}.png")
    pix.save(output_path)
    print(f"  [OK] Pagina {page_num + 1} salva")

doc.close()
print(f"\nTotal: {end_page - start_page} páginas extraídas em: {output_dir}")
