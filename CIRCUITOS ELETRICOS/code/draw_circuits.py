import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# 1. Exemplo Nodal
with schemdraw.Drawing(file=os.path.join(img_dir, "nodal_ex.png"), show=False) as d:
    d += elm.SourceI().up().label('3A')
    d += elm.Line().right().length(3)
    d += elm.Dot().label('V1', loc='top')
    d.push()
    d += elm.Resistor().down().label('2Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Resistor().right().label('4Ω')
    d += elm.Dot().label('V2', loc='top')
    d.push()
    d += elm.Resistor().down().label('6Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Line().right().length(3)
    d += elm.SourceI().down().label('1A')
    d += elm.Line().left().length(3)
    d += elm.Ground()

# 2. Exemplo Malhas
with schemdraw.Drawing(file=os.path.join(img_dir, "malhas_ex.png"), show=False) as d:
    d += elm.SourceV().up().label('12V')
    d += elm.Resistor().right().label('R1\n2Ω')
    d.push()
    d += elm.Resistor().down().label('R2\n4Ω')
    d += elm.Line().left()
    d.pop()
    d += elm.Resistor().right().label('R3\n3Ω')
    d += elm.SourceV().down().reverse().label('6V', loc='bot')
    d += elm.Line().left()

# 3. Exemplo Thevenin Original
with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_ex.png"), show=False) as d:
    d += elm.SourceV().up().label('32V')
    d += elm.Resistor().right().label('4Ω')
    d += elm.Dot().label('Nó C', loc='top')
    d.push()
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left()
    d += elm.Ground()
    d.pop()
    d += elm.Line().right().length(2)
    d.push()
    # SourceI default direction is right, if up() is used it goes up.
    # To draw down but point up: start at top, go down, but make current point UP
    # In schemdraw, SourceI().down().reverse() draws a downward line with arrow pointing up.
    d += elm.SourceI().down().reverse().label('2A')
    d += elm.Line().left().length(2)
    d.pop()
    d += elm.Resistor().right().label('1Ω')
    d += elm.Dot().label('A', loc='right')
    d += elm.Line().down().length(3).color('white') # invisible line to go down
    d += elm.Dot().label('B', loc='right')
    d += elm.Line().left().length(3 + 2 + 3) # Complete ground loop

# 4. Thevenin Rth
with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_rth.png"), show=False) as d:
    d += elm.Line().up().length(3) # Curto circuito da fonte
    d += elm.Resistor().right().label('4Ω')
    d += elm.Dot().label('Nó C', loc='top')
    d.push()
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left()
    d += elm.Ground()
    d.pop()
    d += elm.Line().right().length(2)
    d.push()
    d += elm.Line().down().length(3).color('white').label('Fonte\nAberta') # Circuito aberto
    d += elm.Line().left().length(2)
    d.pop()
    d += elm.Resistor().right().label('1Ω')
    d += elm.Dot().label('A', loc='right')
    d += elm.Line().down().length(3).color('white')
    d += elm.Dot().label('B', loc='right')
    d += elm.Line().left().length(3 + 2 + 3)

# 5. Thevenin Vth
with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_vth.png"), show=False) as d:
    d += elm.SourceV().up().label('32V')
    d += elm.Resistor().right().label('4Ω')
    d += elm.Dot().label('Nó C', loc='top')
    d.push()
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left()
    d += elm.Ground()
    d.pop()
    d += elm.Line().right().length(2)
    d.push()
    d += elm.SourceI().down().reverse().label('2A')
    d += elm.Line().left().length(2)
    d.pop()
    d += elm.Resistor().right().label('1Ω\n(i=0A)')
    d += elm.Dot().label('A (+Vth)', loc='right')
    d += elm.Line().down().length(3).color('white')
    d += elm.Dot().label('B (-Vth)', loc='right')
    d += elm.Line().left().length(3 + 2 + 3)

print("Todas as 5 imagens de circuitos foram geradas com sucesso.")
