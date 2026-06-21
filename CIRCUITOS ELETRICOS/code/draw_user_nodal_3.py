import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")

with schemdraw.Drawing(file=os.path.join(img_dir, "usuario_nodal_3.png"), show=False) as d:
    # Nó V1 (esq), V2 (meio), V3 (dir), Terra (baixo)
    d += elm.SourceI().up().reverse().label('8A') # Seta pra baixo
    d += elm.Dot().label('V1', loc='bot')
    d.push()
    d += elm.Resistor().right().label('3S')
    d += elm.Dot().label('V2', loc='bot')
    d.push()
    d += elm.Resistor().down().label('1S')
    d += elm.Line().left().length(3) # fio terra
    d.pop()
    d += elm.Resistor().right().label('2S')
    d += elm.Dot().label('V3', loc='bot')
    d += elm.SourceI().down().label('-25A') # Seta pra baixo
    d += elm.Line().left().length(6) # fio terra junta com o outro
    d += elm.Ground()
    d.pop() # volta pro V1
    # Arco superior (4S)
    d.push()
    d += elm.Line().up().length(2)
    d += elm.Resistor().right().length(6).label('4S')
    d += elm.Line().down().length(2)
    d.pop()
    # Arco do meio (Fonte 3A entre V1 e V2)
    d += elm.Line().up().length(1)
    d += elm.SourceI().right().label('3A')
    d += elm.Line().down().length(1)
