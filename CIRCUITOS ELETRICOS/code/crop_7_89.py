from PIL import Image
import os

img_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_cap7_prob_286.png"
img = Image.open(img_path)

# Approximate coordinates for Figura 7.89
# Page is probably around 800x1100 or something. Let's crop a box.
# Figura 7.89 is right below 7.88.
box = (50, 300, 500, 600) 
crop_img = img.crop(box)
crop_img.save("crop_7_89.png")
print("Cropped image saved to crop_7_89.png")
