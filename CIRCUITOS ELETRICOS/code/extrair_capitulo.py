import fitz  # PyMuPDF
import os

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"

print("--- Extrator de Capítulos ---")
capitulo = input("Digite o número do capítulo (ex: 06, 07, 09, 11): ").strip()

start_page = int(input("Digite a página inicial do capítulo no PDF (número impresso no rodapé): "))
end_page = int(input("Digite a página final do capítulo no PDF (número impresso no rodapé): "))

# Adjusting to 0-indexed pages (assuming the printed number aligns with PDF page if we account for preface, but usually they don't. 
# We'll assume the user enters the actual PDF page number displayed in their viewer).
start_index = start_page - 1
end_index = end_page - 1

output_dir = os.path.join(r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS", f"capitulo_{capitulo}")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"capitulo{capitulo}_texto.txt")

doc = fitz.open(pdf_path)
text = ""

print(f"Extraindo páginas {start_page} a {end_page}...")

for page_num in range(start_index, end_index + 1):
    page = doc[page_num]
    text += f"--- PÁGINA {page_num + 1} ---\n"
    text += page.get_text()
    text += "\n\n"

doc.close()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Texto extraído e salvo em: {output_path}")
