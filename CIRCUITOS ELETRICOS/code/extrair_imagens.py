import fitz  # PyMuPDF
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"

print("--- Extrator de Imagens de Circuitos ---")
capitulo = input("Digite o número do capítulo (ex: 06, 07, 09, 11): ").strip()

start_page = int(input("Digite a página inicial do capítulo no PDF (número impresso no rodapé): "))
end_page = int(input("Digite a página final do capítulo no PDF (número impresso no rodapé): "))

# 0-indexed
start_index = start_page - 1
end_index = end_page - 1

output_dir = os.path.join(r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS", f"capitulo_{capitulo}", "imagens")
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)

print(f"Extraindo páginas {start_page} a {end_page} como imagens...")

for page_num in range(start_index, end_index + 1):
    page = doc[page_num]
    # Render at 2x resolution
    mat = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=mat)
    output_path = os.path.join(output_dir, f"pagina_{page_num + 1}.png")
    pix.save(output_path)
    print(f"  [OK] Pagina {page_num + 1} salva")

doc.close()
print(f"\nTotal: {(end_index + 1) - start_index} páginas extraídas em: {output_dir}")
