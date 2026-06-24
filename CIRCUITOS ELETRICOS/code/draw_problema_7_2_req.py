import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_2_req.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Short circuit (killed 50V source)
    d += elm.Line().up().label('Curto-circuito\n(0 V)', loc='left', color='blue').color('blue')
    top_left = d.here
    
    # 120 ohm resistor
    d += elm.Resistor().right().label('120 Ω')
    top_mid = d.here
    
    # 80 ohm resistor
    d += elm.Resistor().down().label('80 Ω', loc='bot')
    bot_mid = d.here
    
    # Bottom wire
    d += elm.Line().left().tox(top_left)
    
    # 12 ohm resistor
    d += elm.Resistor().right().at(top_mid).label('12 Ω')
    top_right = d.here
    
    # Open terminals for Capacitor
    d += elm.Line().down().at(top_right).length(0.75)
    top_term = d.here
    d += elm.Dot(open=True)
    
    d += elm.Gap().down().label('R_eq', loc='right').length(1.5)
    
    d += elm.Dot(open=True)
    d += elm.Line().down().toy(bot_mid)
    bot_term = d.here
    
    # Connect bottom
    d += elm.Line().left().at(bot_term).tox(bot_mid)
    
    # Arrow for Req looking in
    import schemdraw.util as util
    d += elm.Arc2(arrow='<-').at((top_term[0]+0.8, top_term[1]-0.75)).to((top_term[0]+0.1, top_term[1]-0.75))

print("Gerado problema_7_2_req.png")
