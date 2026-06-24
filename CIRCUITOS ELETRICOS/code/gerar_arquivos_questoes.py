import os

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\capitulo_07\atividades"

md_templates = {
    "questao_revisao_7_4.md": """# Questão de Revisão 7.4
*(Página 265 do PDF)*

> **Objetivo:** Calcular o tempo necessário para um indutor atingir uma porcentagem do seu valor estacionário.
> **Instrução:** Encontre o $\tau$ e use a fórmula universal de carga/descarga!

![Enunciado](../../_base_dados_ia/imagens_geradas/revisao_7_4.png)

---

## ✍️ Sua Vez!
*(Mostre os cálculos que você fez para chegar na resposta!)*
""",
    "questao_revisao_7_5.md": """# Questão de Revisão 7.5
*(Página 265 do PDF)*

> **Objetivo:** Encontrar a tensão inicial $v(0)$ no capacitor, que dita de onde a curva exponencial vai partir.
> **Instrução:** Analise o circuito DC em regime estacionário *antes* da chave abrir/fechar. Lembre-se: o que o capacitor vira em CC?

![Enunciado](../../_base_dados_ia/imagens_geradas/revisao_7_5_7_6.png)

---

## ✍️ Sua Vez!
*(Escreva como você deduziu o valor de tensão inicial!)*
""",
    "questao_revisao_7_6.md": """# Questão de Revisão 7.6
*(Página 265 do PDF)*

> **Objetivo:** Encontrar a tensão final $v(\infty)$ no capacitor.
> **Instrução:** Analise o circuito *muito tempo depois* da chave abrir/fechar. 

![Enunciado](../../_base_dados_ia/imagens_geradas/revisao_7_5_7_6.png)

---

## ✍️ Sua Vez!
*(Escreva como você deduziu o valor de tensão final!)*
""",
    "questao_revisao_7_7.md": """# Questão de Revisão 7.7
*(Página 265 do PDF)*

> **Objetivo:** Encontrar a corrente inicial $i(0)$ no indutor.
> **Instrução:** Analise o circuito em regime estacionário (CC) *antes* da chave agir. O que o indutor vira em CC?

![Enunciado](../../_base_dados_ia/imagens_geradas/revisao_7_7.png)

---

## ✍️ Sua Vez!
*(Qual o caminho que a corrente vai preferir fazer em regime estacionário?)*
"""
}

for name, content in md_templates.items():
    path = os.path.join(base_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")
