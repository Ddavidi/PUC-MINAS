import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# 1. CIRCUITO ORIGINAL
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_4_orig.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    # Inicia no canto inferior esquerdo
    d += elm.Resistor().up().length(4).label('24Ω', loc='bot')
    top_24 = d.here
    
    d += elm.Line().right().length(2.5)
    top_src = d.here
    d += elm.SourceI().down().length(4).label('15 A', loc='bot').reverse() # reverse to make arrow UP
    bot_src = d.here
    
    d += elm.Line().left().tox(top_24) # fecha o retangulo da esquerda
    
    # Chave
    d += elm.Switch().right().at(top_src).length(3).label('$t=0$', loc='top')
    node_A = d.here
    
    # Ramo do meio (12 ohm e Indutor)
    d += elm.Resistor().down().length(2).label('12Ω', loc='bot')
    node_B = d.here
    d += elm.Inductor().down().length(2).label('2 H', loc='bot').label('$i(t)$ ↓', loc='top', color='red')
    bot_mid = d.here
    
    # Top wire para a direita
    d += elm.Line().right().at(node_A).length(3)
    node_D = d.here
    
    # Ramo da direita (8 ohm)
    d += elm.Resistor().down().length(2).label('8Ω', loc='bot')
    node_C = d.here
    d += elm.Line().down().length(2)
    bot_right = d.here
    
    # Resistor de 5 ohm horizontal
    d += elm.Resistor().right().at(node_B).tox(node_C).label('5Ω', loc='bot')
    
    # Fio de baixo fechando tudo
    d += elm.Line().left().at(bot_right).tox(bot_src)

# 2. CIRCUITO t < 0 (Achar i(0))
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_4_t0.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    d += elm.Resistor().up().length(4).label('24Ω', loc='bot')
    top_24 = d.here
    d += elm.Line().right().length(2.5)
    top_src = d.here
    d += elm.SourceI().down().length(4).label('15 A', loc='bot').reverse()
    bot_src = d.here
    d += elm.Line().left().tox(top_24)
    
    d += elm.Line().right().at(top_src).length(3).label('Chave\nFechada', loc='top', color='blue')
    node_A = d.here
    
    d += elm.Resistor().down().length(2).label('12Ω', loc='bot')
    node_B = d.here
    d += elm.Line().down().length(2).label('Curto\n(Indutor)', loc='bot', color='blue').label('$i(0)$ ↓', loc='top', color='red')
    bot_mid = d.here
    
    d += elm.Line().right().at(node_A).length(3)
    node_D = d.here
    
    d += elm.Resistor().down().length(2).label('8Ω', loc='bot')
    node_C = d.here
    d += elm.Line().down().length(2)
    bot_right = d.here
    
    d += elm.Resistor().right().at(node_B).tox(node_C).label('5Ω (Curto-circuitado)', loc='bot', color='gray')
    
    d += elm.Line().left().at(bot_right).tox(bot_src)

# 3. CIRCUITO t > 0 (Achar Req)
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_4_req.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    # Chave abriu, lado esquerdo some. Fica só a parte direita.
    # Começamos do Node A
    d += elm.Dot().label('A')
    node_A = d.here
    
    d += elm.Resistor().down().length(2).label('12Ω', loc='bot')
    node_B = d.here
    d += elm.Gap().down().length(2).label('Req', loc='bot', color='blue')
    bot_mid = d.here
    
    d += elm.Line().right().at(node_A).length(3)
    node_D = d.here
    
    d += elm.Resistor().down().length(2).label('8Ω', loc='bot')
    node_C = d.here
    d += elm.Line().down().length(2)
    bot_right = d.here
    
    d += elm.Resistor().right().at(node_B).tox(node_C).label('5Ω', loc='bot')
    
    d += elm.Line().left().at(bot_right).tox(bot_mid)

# 4. CIRCUITO DIDATICO (Curto-circuito anulando o 5 ohm)
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_4_curto.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    d += elm.Line().down().length(2).label('Corrente Total\nDescendo', loc='left')
    node_B = d.here
    
    d += elm.Line().down().length(4).color('blue').label('Fio Liso (0Ω)\n100% da Água', loc='left', color='blue')
    bot_mid = d.here
    
    d += elm.Resistor().right().at(node_B).length(5).color('gray').label('Resistor de 5Ω\nCaminho Difícil\n0% da Água', loc='bot', color='gray')
    node_C = d.here
    
    d += elm.Line().down().length(3).color('gray')
    bot_right = d.here
    
    d += elm.Line().left().at(bot_right).tox(bot_mid)
