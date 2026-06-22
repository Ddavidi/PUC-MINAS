import os
import schemdraw
import schemdraw.elements as elm

schemdraw.use('matplotlib')

base_dir = r"c:\Users\Levty\Documents\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
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

# 6. Thevenin Final Equivalente
with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_final.png"), show=False) as d:
    d += elm.Dot().label('A (+)', loc='left')
    d += elm.Resistor().right().label('Rth = 4Ω')
    d += elm.SourceV().down().reverse().label('Vth = 30V')
    d += elm.Line().left()
    d += elm.Dot().label('B (-)', loc='left')

print("Imagem do Thevenin final gerada com sucesso.")

# 7. Problema 7.15 - Circuito (a) Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob715_a.png"), show=False) as d:
    d.push()
    d += elm.Resistor().down().label('10Ω')
    d.pop()
    d += elm.Line().right()
    d.push()
    d += elm.Resistor().down().label('40Ω')
    d += elm.Line().left()
    d.pop()
    d += elm.Resistor().right().label('2Ω')
    d += elm.Inductor().down().label('5H')
    d += elm.Line().left().length(2)

# 8. Problema 7.15 - Circuito (a) Equivalente
with schemdraw.Drawing(file=os.path.join(img_dir, "prob715_a_eq.png"), show=False) as d:
    d += elm.Resistor().right().label('Req = 10Ω')
    d += elm.Inductor().down().label('5H')
    d += elm.Line().left()
    d += elm.Line().up()

# 9. Problema 7.15 - Circuito (b) Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob715_b.png"), show=False) as d:
    d.push()
    R_left = elm.Resistor().down().length(6).label('40Ω')
    d += R_left
    d.pop()
    d += elm.Line().right().length(2)
    top_mid = d.here
    d.push()
    d += elm.Resistor().down().label('48Ω')
    d += elm.Inductor().down().label('20mH')
    bot_mid = d.here
    d += elm.Line().left().length(2).to(R_left.end)
    d.pop()
    d += elm.Line().right().length(2)
    R_right = elm.Resistor().down().length(6).label('160Ω')
    d += R_right
    d += elm.Line().left().length(2).to(bot_mid)

# 10. Problema 7.15 - Circuito (b) Equivalente
with schemdraw.Drawing(file=os.path.join(img_dir, "prob715_b_eq.png"), show=False) as d:
    d += elm.Resistor().right().label('Req = 80Ω')
    d += elm.Inductor().down().label('20mH')
    d += elm.Line().left()
    d += elm.Line().up()

print("Imagens do Problema 7.15 geradas com sucesso.")

# 11. Problema 7.18 - Circuito Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob718.png"), show=False) as d:
    V_src = elm.SourceV().up().label('v(t)')
    d += V_src
    d += elm.Line().right().length(1)
    d.push()
    d += elm.Line().up().length(1.5)
    d += elm.Resistor().right().length(3).label('2Ω')
    d += elm.Line().down().length(1.5)
    top_right = d.here
    d.pop()
    d += elm.Line().down().length(1.5)
    d += elm.Inductor().right().length(3).label('0,4H').label('i(t) ⟶', loc='bot')
    d += elm.Line().up().length(1.5).to(top_right)
    d += elm.Line().right().length(1)
    d += elm.Resistor().down().toy(V_src.start).label(('+', '$v_o(t)$', '-'), loc='bot').label('3Ω', loc='top')
    d += elm.Line().left().tox(V_src.start)

# 12. Problema 7.18 - Equivalente (t > 0)
with schemdraw.Drawing(file=os.path.join(img_dir, "prob718_eq.png"), show=False) as d:
    d += elm.Inductor().up().label('L = 0,4H').label('i(0)=5A ⟶', loc='bot')
    d += elm.Line().right().length(3)
    d += elm.Resistor().down().label('Req = 1,2Ω')
    d += elm.Line().left().length(3)

print("Imagens do Problema 7.18 geradas com sucesso.")

# 13. Problema 7.17 - Circuito Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob717.png"), show=False) as d:
    d += elm.Line().up().length(3).label('v(t)=0\n(Curto)', loc='left')
    d += elm.Resistor().right().length(3).label('1Ω')
    top_mid = d.here
    d.push()
    d += elm.Resistor().down().length(1.5).label('3Ω', loc='left')
    d += elm.Inductor().down().length(1.5).label('1/4H', loc='left').label('i(t) ↓', loc='right')
    bot_mid = d.here
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Line().down().length(3).color('white').label(('+', '$v_o(t)$', '-'), loc='right')
    d += elm.Line().left().length(2).to(bot_mid)
    d += elm.Line().left().length(3)

# 14. Problema 7.17 - Equivalente
with schemdraw.Drawing(file=os.path.join(img_dir, "prob717_eq.png"), show=False) as d:
    d += elm.Inductor().up().label('L = 1/4H').label('i(0)=6A', loc='bot')
    d += elm.Resistor().right().label('Req = 4Ω')
    d += elm.Line().down()
    d += elm.Line().left()

# 15. Problema 7.23 - Circuito Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob723.png"), show=False) as d:
    d += elm.Line().up().length(0)
    d.push()
    R1 = elm.Resistor().down().length(3).label('1Ω', loc='left').label(('+', '$v_x$', '-'), loc='right')
    d += R1
    d.pop()
    d += elm.Resistor().right().length(3).label('3Ω')
    top_right = d.here
    d.push()
    L1 = elm.Inductor().down().length(3).label('1/3H', loc='left')
    d += L1
    d.pop()
    d += elm.Line().right().length(2)
    R2 = elm.Resistor().down().length(3).label('2Ω', loc='left').label(('+', '$v_o$', '-'), loc='right')
    d += R2
    d += elm.Line().left().length(2).to(L1.end)
    d += elm.Line().left().length(3).to(R1.end)

# 16. Problema 7.23 - Equivalente
with schemdraw.Drawing(file=os.path.join(img_dir, "prob723_eq.png"), show=False) as d:
    d += elm.Inductor().up().label('L = 1/3H')
    d += elm.Resistor().right().label('Req = 4/3Ω')
    d += elm.Line().down()
    d += elm.Line().left()

print("Imagens dos Problemas 7.17 e 7.23 geradas com sucesso.")

# 17. Problema 7.54 - Circuito (a) Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob754_a.png"), show=False) as d:
    start_node = d.here
    d += elm.SourceI().up().length(3).label('2A')
    d += elm.Line().right().length(2)
    top1 = d.here
    d.push()
    d += elm.Resistor().down().length(3).label('4Ω')
    bot1 = d.here
    d.pop()
    d += elm.Line().right().length(2)
    top2 = d.here
    d.push()
    d += elm.Resistor().down().length(1.5).label('12Ω')
    d += elm.Switch().down().length(1.5).label('t=0 (Abre)', loc='right')
    bot2 = d.here
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().length(1.5).label('4Ω')
    d += elm.Inductor().down().length(1.5).label('3,5H').label('i(t) ↓', loc='bot')
    bot3 = d.here
    d += elm.Line().left().length(2)
    d += elm.Line().left().length(2)
    d += elm.Line().left().length(2)

# 18. Problema 7.54 - Circuito (a) t > 0
with schemdraw.Drawing(file=os.path.join(img_dir, "prob754_a_eq.png"), show=False) as d:
    d += elm.SourceI().up().length(3).label('2A')
    d += elm.Line().right().length(2)
    d.push()
    d += elm.Resistor().down().length(3).label('4Ω')
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().length(1.5).label('4Ω')
    d += elm.Inductor().down().length(1.5).label('3,5H').label('i(t) ↓', loc='bot')
    d += elm.Line().left().length(2)
    d += elm.Line().left().length(2)

# 19. Problema 7.54 - Circuito (b) Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob754_b.png"), show=False) as d:
    d += elm.SourceV().up().length(1.5).label('10V')
    d += elm.Resistor().up().length(1.5).label('2Ω', loc='left')
    top_left = d.here
    d += elm.Line().right().length(2.5)
    d.push()
    d += elm.Switch().down().length(1).label('t=0 (Fecha)', loc='right')
    d += elm.SourceV().down().length(1).reverse().label('24V', loc='right')
    d += elm.Resistor().down().length(1).label('6Ω', loc='right')
    bot_mid = d.here
    d.pop()
    d += elm.Line().right().length(2.5)
    d += elm.Resistor().down().length(1.5).label('3Ω', loc='right')
    d += elm.Inductor().down().length(1.5).label('2H', loc='right').label('i(t) ↓', loc='bot')
    d += elm.Line().left().length(2.5)
    d += elm.Line().left().length(2.5)

# 20. Problema 7.54 - Circuito (b) t > 0 (Thevenin Equivalente)
with schemdraw.Drawing(file=os.path.join(img_dir, "prob754_b_eq.png"), show=False) as d:
    d += elm.SourceV().up().length(3).label('13,5V')
    d += elm.Resistor().right().length(3).label('Rth = 1,5Ω')
    d += elm.Resistor().down().length(1.5).label('3Ω', loc='right')
    d += elm.Inductor().down().length(1.5).label('2H', loc='right').label('i(t) ↓', loc='bot')
    d += elm.Line().left().length(3)

print("Imagens do Problema 7.54 geradas com sucesso.")

# 21. Problema 9.39 - Circuito Original
with schemdraw.Drawing(file=os.path.join(img_dir, "prob939.png"), show=False) as d:
    d += elm.SourceV().up().label('12∠0° V')
    d += elm.Line().right().length(1).label('I →', loc='top')
    d += elm.Resistor().right().label('4Ω')
    d += elm.Inductor().right().label('j20Ω')
    top_mid = d.here
    d.push()
    d += elm.Resistor().down().length(3).label('16Ω', loc='right')
    bot_mid = d.here
    d.pop()
    d += elm.Capacitor().right().label('-j14Ω')
    d += elm.Inductor().down().length(3).label('j25Ω', loc='right')
    bot_right = d.here
    d += elm.Line().left().to(bot_mid)
    d += elm.Line().left().to((0,0))

# 22. Problema 9.39 - Equivalente
with schemdraw.Drawing(file=os.path.join(img_dir, "prob939_eq.png"), show=False) as d:
    d += elm.SourceV().up().label('12∠0° V')
    d += elm.Line().right().length(1).label('I →', loc='top')
    d += elm.Resistor().right().label('Zeq')
    d += elm.Line().down()
    d += elm.Line().left().to((0,0))

print("Imagens do Problema 9.39 geradas com sucesso.")
