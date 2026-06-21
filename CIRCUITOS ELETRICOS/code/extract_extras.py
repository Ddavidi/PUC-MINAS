import fitz
import os

extras_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\capitulo_07\pdfs_extras"
out_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\capitulo_07\pdfs_extras_texto.txt"

text = ""
for filename in os.listdir(extras_dir):
    if filename.endswith(".pdf"):
        path = os.path.join(extras_dir, filename)
        text += f"\n\n{'='*50}\nCONTEÚDO DO PDF: {filename}\n{'='*50}\n\n"
        try:
            doc = fitz.open(path)
            for page in doc:
                text += page.get_text()
            doc.close()
        except Exception as e:
            text += f"Erro ao ler {filename}: {e}\n"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extras do cap 7 extraídos para {out_path}")
