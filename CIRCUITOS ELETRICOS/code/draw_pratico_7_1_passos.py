import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# Passo de Req
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_1_req.png"), show=False) as d:
    d.config(unit=3)
    
    # Ramo esquerdo (12 ohm)
    d.push()
    d += elm.Resistor().down().label('12Ω', loc='left')
    bot_left = d.here
    d.pop()
    
    # Fio superior ate o meio
    d += elm.Line().right().length(2.5)
    top_mid = d.here
    
    # Ramo do meio (6 ohm)
    d.push()
    d += elm.Resistor().down().label('6Ω', loc='left')
    bot_mid = d.here
    d.pop()
    
    # Fio com a seta da corrente (em branco) + Resistor de 8 ohm
    d += elm.Line().right().length(1.5)
    d += elm.Resistor().right().label('8Ω', loc='top')
    top_right = d.here
    
    # Ramo direito (Buracos do Capacitor para olhar o Req)
    d.push()
    d += elm.Dot().label('Terminal Sup.', loc='right')
    d += elm.Gap().down().label('Req visto\npelo Cap.', color='blue')
    d += elm.Dot().label('Terminal Inf.', loc='right')
    bot_right = d.here
    d.pop()
    
    # Fechando o circuito embaixo
    d += elm.Line().left().tox(bot_mid)
    d += elm.Line().left().tox(bot_left)
