import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# 1. Exemplo Solucionado Supernó
with schemdraw.Drawing(file=os.path.join(img_dir, "superno_ex.png"), show=False) as d:
    d += elm.SourceI().up().label('4A')
    d += elm.Line().right().length(3)
    d += elm.Dot().label('V1', loc='top')
    d.push()
    d += elm.Resistor().down().label('2Ω')
    d += elm.Line().left().length(3)
    d.pop()
    # Fonte de tensao entre V1 e V2 (Positivo na esquerda)
    d += elm.SourceV().right().label('6V')
    d += elm.Dot().label('V2', loc='top')
    d.push()
    d += elm.Resistor().down().label('4Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Line().right().length(3)
    d += elm.SourceI().down().reverse().label('2A')
    d += elm.Line().left().length(3+3+3)

# 2. Exercicio Proposto Supernó
with schemdraw.Drawing(file=os.path.join(img_dir, "superno_proposto.png"), show=False) as d:
    # 2A para baixo, saindo de V1
    d += elm.SourceI().down().label('2A')
    d += elm.Line().right().length(3)
    d += elm.Dot().label('V1', loc='bot')
    d.push()
    d += elm.Resistor().up().label('4Ω')
    d += elm.Line().left().length(3)
    d.pop()
    # Fonte de tensao entre V1 e V2 (Positivo na direita, entao reverse)
    # SourceV default tem positivo no fim do path. Entao se for pra direita, + fica na direita.
    d += elm.SourceV().right().label('12V')
    d += elm.Dot().label('V2', loc='bot')
    d.push()
    d += elm.Resistor().up().label('2Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Line().right().length(3)
    # 11A entrando em V2 (vindo de cima ou apontando pra baixo reverse)
    d += elm.SourceI().up().reverse().label('11A')
    d += elm.Line().left().length(3+3+3)
    # Ground at the top to make it spicy? No, ground at bottom, nodes at top.
    
# Wait, let's redraw Proposed correctly with ground at bottom:
with schemdraw.Drawing(file=os.path.join(img_dir, "superno_proposto.png"), show=False) as d:
    # Inicia do bottom left e vai pra cima pra criar a fonte
    # Como a fonte de 2A deve sair de V1 e ir pro ground, a seta aponta pra baixo.
    # Da esquerda, partindo do terra:
    d += elm.SourceI().down().label('2A') # Vai pra baixo? Nao, d+=...down() draw a line downward.
    # We want standard layout.
    pass
    
with schemdraw.Drawing(file=os.path.join(img_dir, "superno_proposto.png"), show=False) as d:
    d += elm.SourceI().up().reverse().label('2A') # Desenha de baixo pra cima, seta pra baixo
    d += elm.Line().right().length(3)
    d += elm.Dot().label('V1', loc='top')
    d.push()
    d += elm.Resistor().down().label('4Ω')
    d += elm.Line().left().length(3)
    d.pop()
    # Fonte de 12V com positivo na direita
    d += elm.SourceV().right().label('12V')
    d += elm.Dot().label('V2', loc='top')
    d.push()
    d += elm.Resistor().down().label('2Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Line().right().length(3)
    d += elm.SourceI().down().reverse().label('11A') # Desenha de cima pra baixo, seta pra cima
    d += elm.Line().left().length(3+3+3)
    d += elm.Ground()

# 3. Exercicio Proposto Resolvido
with schemdraw.Drawing(file=os.path.join(img_dir, "superno_proposto_resolvido.png"), show=False) as d:
    d += elm.SourceI().up().reverse().label('2A') 
    d += elm.Line().right().length(3)
    d += elm.Dot().label('V1\n(4V)', loc='top', color='red')
    d.push()
    d += elm.Resistor().down().label('4Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.SourceV().right().label('12V')
    d += elm.Dot().label('V2\n(16V)', loc='top', color='red')
    d.push()
    d += elm.Resistor().down().label('2Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Line().right().length(3)
    d += elm.SourceI().down().reverse().label('11A')
    d += elm.Line().left().length(3+3+3)
    d += elm.Ground()
