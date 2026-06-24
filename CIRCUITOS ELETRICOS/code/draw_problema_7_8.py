import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_8.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Start at top left (0,3)
    
    # Resistor R on the left branch
    d += elm.Resistor().down().at((0,3)).label('R', loc='left').toy(0)
    
    # Top wire with arrow pointing LEFT (so we use arrow='<-' while drawing to the right)
    d += elm.Line(arrow='<-').right().at((0,3)).tox(3).label('i', loc='top')
    
    # Capacitor C on the right branch
    d += elm.Capacitor().down().at((3,3)).label('C', loc='right').label(('+', 'v', '-'), loc='left').toy(0)
    
    # Bottom wire
    d += elm.Line().left().at((3,0)).tox(0)

print("Gerado problema_7_8.png")
