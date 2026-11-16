import numpy as np
from PIL import Image

# 1. On charge l'image sous forme de tableau de chiffres (Hauteur, Largeur, Couleurs)
img = Image.open("gold.png")
tableau = np.array(img)

# 2. On duplique chaque ligne 2 fois, puis chaque colonne 2 fois (aucun calcul, juste du copier-coller)
tableau_double = tableau.repeat(2, axis=0).repeat(2, axis=1)

# 3. On vérifie sur les premiers pixels en haut à gauche
print("Pixel original (0,0) :", tableau[0, 0])
print("Bloc 2x2 généré :\n", tableau_double[0:2, 0:2])

# 4. On sauvegarde en PNG (indispensable pour ne pas perdre la précision des couleurs)
Image.fromarray(tableau_double).save("mon_image_2x_exact.png")
