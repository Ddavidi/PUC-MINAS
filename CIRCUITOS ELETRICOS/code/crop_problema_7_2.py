from PIL import Image
import os

img_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\sadiku_page_cap7_prob_285.png"
out_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas\problema_7_2.png"

img = Image.open(img_path)
# Crop coordinates: Left, Top, Right, Bottom
# Look at the image, problem 7.2 is below 7.1, on the left column.
# Let's crop a lower area where 7.2 is located
crop_img = img.crop((60, 950, 600, 1300))
crop_img.save(out_path)
print(f"Saved {out_path}")
