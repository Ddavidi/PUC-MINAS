import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# Desenho para t < 0
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_proposto_rl_t_menor_0.png"), show=False) as d:
    d.config(unit=3)
    d += elm.SourceV().up().label('10V')
    d += elm.Switch().right().label('Aberta', loc='top')
    d += elm.Resistor().right().label('2Ω')
    d += elm.Inductor().down().label('4H').label('i(0) = 0A ↓', loc='bot', color='red')
    d += elm.Resistor().left().label('3Ω')
    d += elm.Line().left().to((0,0))

# Desenho para t -> infinito
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_proposto_rl_t_infinito.png"), show=False) as d:
    d.config(unit=3)
    d += elm.SourceV().up().label('10V')
    d += elm.Line().right().length(1.5).label('Fechada', loc='top', color='gray')
    d += elm.Resistor().right().label('2Ω')
    d += elm.Line().down().length(3).color('red').label('Fio Liso\ni(∞) = 2A ↓', loc='right')
    d += elm.Resistor().left().label('3Ω')
    d += elm.Line().left().to((0,0))

# Desenho para achar Req
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_proposto_rl_req.png"), show=False) as d:
    d.config(unit=3)
    d += elm.Line().up().label('Fonte 10V\nZerada', color='gray')
    d += elm.Line().right().length(1.5).label('Fechada', loc='top', color='gray')
    d += elm.Resistor().right().label('2Ω')
    d.push()
    d += elm.Dot().label('Terminal A', loc='left')
    d += elm.Gap().down().label('Req visto\npelo Indutor', color='blue')
    d += elm.Dot().label('Terminal B', loc='left')
    d.pop()
    d += elm.Line().right().length(0).color('white') # dummy
    # Para fechar o circuito a partir do buraco, desenhamos a parte de baixo
    # Mas no schemdraw, o indutor era a linha de descida.
    # Vamos desenhar o resistor de 3 ohms voltando
    d += elm.Line().down().length(3).color('white') # invisível até o chão
    d += elm.Resistor().left().label('3Ω')
    d += elm.Line().left().to((0,0))
