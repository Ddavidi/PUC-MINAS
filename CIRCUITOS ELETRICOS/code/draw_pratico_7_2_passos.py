import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# Imagem 1: t < 0 (Chave Fechada, Cap = Aberto)
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_2_t_menor_0.png"), show=False) as d:
    d.config(unit=4, fontsize=14)
    start_point = d.here
    d += elm.SourceV().up().label('24V', loc='left')
    
    # Fio superior com resistor 6 e chave FECHADA (linha)
    d += elm.Resistor().right().label('6Ω', loc='bot')
    d += elm.Line().right().label('Chave\nFechada', loc='top', color='green')
    top_mid = d.here
    
    # Ramo do Capacitor (ABERTO)
    d.push()
    d += elm.Gap().down().label('Capacitor\nAberto', color='blue').label(('+', '$v(0)$', '-'), loc='top')
    d.pop()
    
    # Ramo 12 ohm
    d += elm.Line().right().length(2)
    d.push()
    d += elm.Resistor().down().label('12Ω', loc='bot')
    d.pop()
    
    # Ramo 4 ohm
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('4Ω', loc='bot')
    
    # Fechando o circuito embaixo
    d += elm.Line().left().tox(top_mid)
    d += elm.Line().left().tox(start_point)

# Imagem 2: t > 0 (Chave Aberta, Esquerda Desconectada)
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_2_t_maior_0.png"), show=False) as d:
    d.config(unit=4, fontsize=14)
    
    start_point = d.here
    # Apenas do capacitor para a direita
    d.push()
    d += elm.Capacitor().down().label('1/6 F', loc='bot').label(('+', '$v$', '-'), loc='top', color='blue')
    d.pop()
    
    d += elm.Line().right().length(2)
    d.push()
    d += elm.Resistor().down().label('12Ω', loc='bot')
    d.pop()
    
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('4Ω', loc='bot')
    
    d += elm.Line().left().tox(start_point)

# Imagem 3: Req visto pelo Capacitor
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_2_req.png"), show=False) as d:
    d.config(unit=4, fontsize=14)
    
    start_point = d.here
    # Terminais onde estava o Capacitor
    d.push()
    d += elm.Dot().label('Terminal Sup.', loc='top')
    d += elm.Gap().down().label('Req visto\npelo Cap.', color='blue')
    d += elm.Dot().label('Terminal Inf.', loc='bot')
    d.pop()
    
    d += elm.Line().right().length(2)
    d.push()
    d += elm.Resistor().down().label('12Ω', loc='bot')
    d.pop()
    
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('4Ω', loc='bot')
    
    d += elm.Line().left().tox(start_point)
