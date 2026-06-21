import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "usuario_nodal_2.png"), show=False) as d:
    # Nó superior esquerdo V1, superior direito V2, inferior Terra
    d += elm.Resistor().down().label('2Ω')
    d += elm.Line().right().length(4)
    d.push()
    d += elm.Resistor().up().label('6Ω')
    d += elm.Dot().label('V2', loc='bot')
    d.pop()
    d += elm.Line().right().length(3)
    d += elm.SourceI().up().label('10A')
    d += elm.Line().left().length(3) # volta pro V2
    # Resistor 4 ohms entre V1 e V2
    d += elm.Resistor().left().length(4).label('4Ω')
    d += elm.Dot().label('V1', loc='bot')
    # Fonte de 5A entre V1 e V2 no topo
    d.push()
    d += elm.Line().up().length(2)
    d += elm.SourceI().right().reverse().label('5A')
    d += elm.Line().down().length(2)
    d.pop()
    # Adicionar o terra
    d += elm.Ground().at((4, 0)) # no meio do fio inferior
