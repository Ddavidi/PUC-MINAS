import os
from PIL import Image

img284_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_cap7_questoes_284.png"
img285_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_cap7_prob_285.png"
img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"

img284 = Image.open(img284_path)
img285 = Image.open(img285_path)

# Approximate crops
crops = {
    "7_1": (img284, (60, 560, 520, 630)),
    "7_4": (img284, (60, 780, 520, 855)),
    "7_5_7_6": (img284, (530, 560, 950, 740)), # right column top
    "7_7": (img284, (530, 740, 950, 950)), # right column bottom
    "7_8_7_9": (img285, (60, 100, 500, 260)), # pg 285 top left
    "7_10": (img285, (500, 100, 950, 260)) # pg 285 top right
}

for name, (img, box) in crops.items():
    out = os.path.join(img_dir, f"revisao_{name}.png")
    img.crop(box).save(out)
    print(f"Saved {out}")
