import fitz  # PyMuPDF

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
output_path = r"c:\Users\DD\Documents\DD\PUC MINAS\CIRCUITOS ELETRICOS\capitulo9_senoides_fasores.txt"

doc = fitz.open(pdf_path)

# Chapter 9 goes from page 349 to 388 (1-indexed)
# In PyMuPDF, pages are 0-indexed
start_page = 349 - 1  # 0-indexed: 348
end_page = 389 - 1    # 0-indexed: 388 (exclusive, so up to 387 which is page 388)

full_text = []
for page_num in range(start_page, end_page):
    page = doc[page_num]
    text = page.get_text()
    full_text.append(f"\n{'='*80}\n--- PÁGINA {page_num + 1} ---\n{'='*80}\n")
    full_text.append(text)

doc.close()

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(full_text))

print(f"Capítulo 9 extraído com sucesso!")
print(f"Páginas: {start_page + 1} a {end_page}")
print(f"Salvo em: {output_path}")
