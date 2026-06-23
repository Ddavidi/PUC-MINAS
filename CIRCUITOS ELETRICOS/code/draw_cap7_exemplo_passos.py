import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# Desenho para t < 0 (Capacitor como Circuito Aberto)
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_exemplo_rc_t_menor_0.png"), show=False) as d:
    d.config(unit=3)
    d += elm.SourceV().up().label('24V')
    d += elm.Line().right().length(1)
    d += elm.Line().right().length(1.5).label('Chave Fechada', loc='top', color='gray')
    d += elm.Resistor().right().label('4Ω')
    top_node = d.here
    d.push()
    d += elm.Dot().label('+ v(0)', loc='right', color='red')
    d += elm.Gap().down().label('Capacitor\nAberto', color='red')
    d += elm.Dot().label('- v(0)', loc='right', color='red')
    bot_node = d.here
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left().tox(bot_node)
    d += elm.Line().left().to((0,0))

# Desenho para t > 0 achando Req (Capacitor arrancado)
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_exemplo_rc_req.png"), show=False) as d:
    d.config(unit=3)
    # Apenas o resistor de 12 ohms
    d += elm.Line().right().length(1).color('white') # Espaçamento
    top_node = d.here
    d.push()
    d += elm.Dot().label('Terminal Sup.', loc='left')
    d += elm.Gap().down().label('Enxergando\no Req', color='blue')
    d += elm.Dot().label('Terminal Inf.', loc='left')
    bot_node = d.here
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left().tox(bot_node)

# Desenho para o caso extra (Se a chave fechasse em t=0) - Para achar o Req extra
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_exemplo_rc_extra_req.png"), show=False) as d:
    d.config(unit=3)
    # Fonte 24V zerada vira fio liso
    d += elm.Line().up().label('Fonte 24V\nZerada (Fio)', color='gray')
    d += elm.Line().right().length(2.5)
    d += elm.Resistor().right().label('4Ω')
    top_node = d.here
    d.push()
    d += elm.Dot().label('Terminal Sup.', loc='right')
    d += elm.Gap().down().label('Req visto\npelo Cap.', color='blue')
    d += elm.Dot().label('Terminal Inf.', loc='right')
    bot_node = d.here
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left().tox(bot_node)
    d += elm.Line().left().to((0,0))
