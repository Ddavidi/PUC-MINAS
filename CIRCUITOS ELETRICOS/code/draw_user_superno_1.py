import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "usuario_superno_1.png"), show=False) as d:
    # V1 (esq), V2 (meio), V3 (dir)
    d += elm.SourceV().up().label('10V').reverse()
    d += elm.Dot().label('V1', loc='bot')
    d.push()
    d += elm.Resistor().right().label('2Ω')
    d += elm.Dot().label('V2', loc='bot')
    d.push()
    d += elm.Resistor().down().label('8Ω')
    d += elm.Line().left().length(3)
    d += elm.Ground()
    d.pop()
    # Fonte de tensao entre V2 e V3 (+ na esquerda)
    d += elm.SourceV().right().label('5V')
    d += elm.Dot().label('V3', loc='bot')
    d.push()
    d += elm.Resistor().down().label('6Ω')
    d += elm.Line().left().length(6) # conecta com o terra
    d.pop()
    d.pop() # volta pro V1
    # Fio de cima entre V1 e V3
    d.push()
    d += elm.Line().up().length(2)
    d += elm.Resistor().right().length(6).label('4Ω')
    d += elm.Line().down().length(2)
    d.pop()
