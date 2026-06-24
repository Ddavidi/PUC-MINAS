import os
import re
import fitz

pdf_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\Fundamentos de Circuitos Elétricos Sadiku - 5 Edição - Completo.pdf"
output_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\capitulo_07\atividades"

problemas_praticos = ["7.10", "7.12"]
problemas = ["7.2", "7.3", "7.4", "7.6", "7.8", "7.9", "7.11", "7.14", "7.15", "7.17", "7.18", "7.23", "7.39", "7.40", "7.41", "7.53", "7.54", "7.59", "7.60"]

# We will just generate the markdown templates for now, because extracting exact text across columns
# in the Sadiku PDF is highly unreliable without manual review.
# We will insert the "Receita de Bolo" template in all of them.

template_pratico = """# Problema Prático {num}

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
{text}
*(As imagens dos circuitos originais serão geradas no formato padrão via código assim que iniciarmos a resolução!)*

---

> [!TIP]
> **Receita de Bolo: Análise de Circuitos de Primeira Ordem**
> 1. **Análise em t < 0:** Identifique o estado da chave. Calcule $v(0)$ para capacitores ou $i(0)$ para indutores (eles se comportam como circuito aberto e curto-circuito, respectivamente, em CC).
> 2. **Análise em t > 0:** Redesenhe o circuito com a chave na nova posição. Encontre a resistência equivalente $R_{{eq}}$ vista pelo capacitor/indutor.
> 3. **Constante de Tempo ($\\tau$):** Calcule $\\tau = R_{{eq}}C$ (para RC) ou $\\tau = L/R_{{eq}}$ (para RL).
> 4. **Equação Final:** Use a fórmula da resposta $x(t) = x(\\infty) + [x(0) - x(\\infty)]e^{{-t/\\tau}}$.

## ✍️ Sua Vez!
*(Resolva o problema aqui passo a passo)*
"""

template_problema = """# Problema {num}

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
{text}
*(As imagens dos circuitos originais serão geradas no formato padrão via código assim que iniciarmos a resolução!)*

---

> [!TIP]
> **Receita de Bolo: Análise de Circuitos de Primeira Ordem**
> 1. **Análise em t < 0:** Identifique o estado da chave. Calcule $v(0)$ para capacitores ou $i(0)$ para indutores (eles se comportam como circuito aberto e curto-circuito, respectivamente, em CC).
> 2. **Análise em t > 0:** Redesenhe o circuito com a chave na nova posição. Encontre a resistência equivalente $R_{{eq}}$ vista pelo capacitor/indutor.
> 3. **Constante de Tempo ($\\tau$):** Calcule $\\tau = R_{{eq}}C$ (para RC) ou $\\tau = L/R_{{eq}}$ (para RL).
> 4. **Equação Final:** Use a fórmula da resposta $x(t) = x(\\infty) + [x(0) - x(\\infty)]e^{{-t/\\tau}}$.

## ✍️ Sua Vez!
*(Deixe sua resolução passo a passo aqui)*
"""

# This script extracts the text for the specified problems from the Sadiku PDF.
import fitz

def extract_problems():
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    # We will search from page 286 to 295
    text_content = ""
    for page_num in range(285, 300):
        page = doc.load_page(page_num)
        text_content += page.get_text()
    
    # Clean up text
    text_content = text_content.replace('-\n', '')
    
    # Extract Práticos
    for p in problemas_praticos:
        # Regex to find "Problema prático X.Y"
        match = re.search(r'(Problema prático ' + re.escape(p) + r'.*?)(?=Problema prático|7\.\d)', text_content, re.DOTALL | re.IGNORECASE)
        enunciado = match.group(1).strip() if match else f"Enunciado não encontrado automaticamente para {p}. Consulte o PDF."
        
        filename = f"problema_pratico_{p.replace('.', '_')}.md"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template_pratico.format(num=p, text=enunciado))
        print(f"Created {filename}")
        
    # Extract Finais
    for p in problemas:
        # Regex to find "X.Y" followed by text
        match = re.search(r'(' + re.escape(p) + r'\s+[A-Z].*?)(?=\n\d+\.\d+\s+[A-Z])', text_content, re.DOTALL)
        enunciado = match.group(1).strip() if match else f"Enunciado não encontrado automaticamente para {p}. Consulte o PDF."
        
        filename = f"problema_{p.replace('.', '_')}.md"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template_problema.format(num=p, text=enunciado))
        print(f"Created {filename}")

if __name__ == "__main__":
    extract_problems()
