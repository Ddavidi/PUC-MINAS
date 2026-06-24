from PIL import Image
import os

img_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_cap7_prob_286.png"
img = Image.open(img_path)

# Crop the bottom right area containing 7.14 and 7.15
box = (450, 500, 950, 950) 
crop_img = img.crop(box)
crop_img.save("crop_7_14_15.png")
print("Cropped image saved to crop_7_14_15.png")
