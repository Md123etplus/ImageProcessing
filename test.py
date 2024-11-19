# # import numpy as np
# # from PIL import Image

# # # Créer une image binaire 9x9 avec un seul canal
# # image_binary = np.zeros((9, 9), dtype=np.uint8)

# # # Remplir certains pixels pour former un motif en blanc
# # image_binary[1:8, 1:8] = 255  # Remplit un carré blanc au centre

# # # Sauvegarder l'image en tant qu'image binaire
# # Image.fromarray(image_binary).save("image_binaire_9x9.bmp")
# # im= Image.open("image_binaire_9x9.bmp")
# # im.show()

import numpy as npy
from PIL import Image
import matplotlib.pyplot as plt

#dans tout le programme on aura ces deux fichiers
I2_BMP_FILE='I2_binaire.bmp'
I1_BMP_FILE='I1_binaire.bmp'

#1ere image sous forme binaire
I1 = npy.array([
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,1],
    [1,0,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1]
], dtype=npy.uint8)
I1=I1*255
I1_resized=Image.fromarray(I1).convert('1')

I1_resized = I1_resized.resize((I1_resized.width * 100, I1_resized.height * 100), Image.NEAREST)
#format bmp
I1_resized.save(I1_BMP_FILE)
I1_resized.show()
print("L'I 1 est generee avec succes!")
#2ieme image sous forme binaire
# I2 = npy.array([
#     [1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1]
# ], dtype=npy.uint8)

I2 = npy.full((9, 9), 255, dtype=npy.uint8)  # Remplit toute l'image de 255 (blanc)

# Remplir un carre 2x2 en noir aux positions (3,3) a (4,4)
I2[3:5, 3:5] = 0#couleur noire

# Agrandir l'image 
I2_resized = Image.fromarray(I2).convert('1')
I2_resized = I2_resized.resize((I2_resized.width * 100, I2_resized.height * 100), Image.NEAREST)

#format bmp
I2_resized.save(I2_BMP_FILE)
I2_resized.show()
print("L'I 2 est generee avec succes!")

#question 1.a addition (je suppose que je n'avais pas la representation mtriciell)

I1=npy.array(Image.open(I1_BMP_FILE).convert('1'), dtype=npy.uint8)
I2 = npy.array(Image.open(I2_BMP_FILE).convert('1'), dtype=npy.uint8)
Iad= I1+I2
Iad=npy.clip(Iad,0,1)
Iad*=255
Iad=Image.fromarray(Iad).convert('1')
Iad.save("Iad_somme_result.bmp")
Iad.show()
print("La somme des deux images a ete generee avec succes!!")

#question 1.b soustraction (je suppose que je n'avais pas la representation mtriciell)

I1=npy.array(Image.open(I1_BMP_FILE).convert('1'), dtype=npy.uint8)
I2 = npy.array(Image.open(I2_BMP_FILE).convert('1'), dtype=npy.uint8)
Is=I1-I2
Is=npy.clip(Is,0,1)
Is*=255
Is=Image.fromarray(Is).convert('1')
Is.save("Is_diff_result.bmp")
Is.show()
print("La difference des deux images a ete generee avec succes (I1-I2)!!")

#question 1.c multiplication par 2 de l'img donnee

Img_niveau_gris = npy.array([
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,3,3,4,4,5,5,6,0],
    [0,3,3,4,4,5,5,6,0],
    [0,6,6,5,5,4,4,3,0],
    [0,7,8,9,7,8,9,7,0],
    [0,9,9,8,8,7,7,7,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
], dtype=npy.uint8)

Ip=npy.clip(Img_niveau_gris*2,0,15)
Ip=Ip*(255//15).astype(npy.uint8)
# un clip??
image = Image.fromarray(Ip).convert('L')

# pas la peine de faire ca
# image_resized = image_resized.resize((image_resized.width * 100, image_resized.height * 100), image.NEAREST)

image.save("image_niveau_gris_multipliee_par_2.bmp")
print("L'image en niveau de gris (x2) a ete generee avec succes!!")
image.show()

# question 2.) (je vais utiliser mon portrait)

# Charger l'image couleur
mon_portrait = Image.open('me.jpeg')
image_rgb = mon_portrait.convert('RGB')
image_array = npy.array(image_rgb)

# Calculer l'histogramme pour chaque canal (R, G, B)
r_hist, r_bins = npy.histogram(image_array[:,:,0], bins=256, range=(0, 255))
g_hist, g_bins = npy.histogram(image_array[:,:,1], bins=256, range=(0, 255))
b_hist, b_bins = npy.histogram(image_array[:,:,2], bins=256, range=(0, 255))

# Créer la figure avec trois sous-graphiques
plt.figure(figsize=(15, 6))

# Histogramme du canal rouge
plt.subplot(131)  # 1ère position sur 3
plt.bar(r_bins[:-1], r_hist, color='red', alpha=0.6, width=1.0)
plt.title("Histogramme - Canal Rouge")
plt.xlabel("Valeur d'intensité des pixels(n)")
plt.ylabel("Fréquence")
plt.grid(True)

# Histogramme du canal vert
plt.subplot(132)  # 2ème position sur 3
plt.bar(g_bins[:-1], g_hist, color='green', alpha=0.6, width=1.0)
plt.title("Histogramme - Canal Vert")
plt.xlabel("Valeur d'intensité des pixels")
plt.ylabel("Fréquence")
plt.grid(True)

# Histogramme du canal bleu
plt.subplot(133)  # 3ème position sur 3
plt.bar(b_bins[:-1], b_hist, color='blue', alpha=0.6, width=1.0)
plt.title("Histogramme - Canal Bleu")
plt.xlabel("Valeur d'intensité des pixels")
plt.ylabel("Fréquence")
plt.grid(True)

# Afficher tous les sous-graphiques
plt.tight_layout()  # Ajuste les espaces entre les sous-graphiques
plt.show()

#question 3 (choix donne a l'utilisateur)
mon_portrait=Image.open('me.jpeg')

choix = -1 

while choix != 0:
    print("Bonjour Bienvenu! Veuillez choisir:")
    print("1 - Image Binaire")
    print("2 - Image en niveau de gris")
    print("0 - Quitter le programme")
    choix = int(input("Entrez votre choix: "))

    if choix == 1:
        print("Vous avez choisi l'image binaire.")
        mon_portrait_binaire=mon_portrait.convert('1')
        mon_portrait_binaire.save()
        mon_portrait_binaire.show()

    elif choix == 2:
        # print("Veuillez entrer le nombre de bit souhaite")
        nbre_bit=int(input("Veuillez entrer le nombre de bit souhaite:"))
        print("Vous avez entre "+ nbre_bit+" donc une plage de 0-"+2**nbre_bit-1)
        mon_portrait_array= npy.array(mon_portrait)
        mon_portrait_array=mon_portrait_array*(255//(2**nbre_bit-1)).astype(npy.uint8)
        mon_portrait_array.save()
        mon_portrait_array.show()
    elif choix == 0:
        print("Au revoir!")
    else:
        print("Choix invalide, veuillez entrer une option valide.")

# mon_portrait=npy.array(Image.open('me.jpeg').convert('1'), dtype=npy.uint8)
# npy.set_printoptions(threshold=npy.inf)  # Désactive la troncature
# print(mon_portrait)

# from PIL import I

# # Créer une I binaire 9x9 avec tous les pixels en blanc
# I_binary = np.full((9, 9), 255, dtype=np.uint8)  # Remplit toute l'I de 255 (blanc)

# # Remplir un carré 2x2 en noir aux positions (3,3) à (4,4)
# I_binary[3:5, 3:5] = 0  # Remplit le carré 2x2 au centre avec 0 (noir)

# # Sauvegarder l'I
# I.fromarray(I_binary).save("I_binaire_9x9_carre_noir_centre.bmp")

# import numpy as np
# from PIL import I

# # Créer une I binaire 9x9 avec tous les pixels en blanc
# I_binary = np.full((9, 9), 255, dtype=np.uint8)  # Remplit toute l'I de 255 (blanc)

# # Remplir un carré 2x2 en noir aux positions (3,3) à (4,4)
# I_binary[3:5, 3:5] = 0  # Remplit le carré 2x2 au centre avec 0 (noir)

# # Agrandir l'I à une résolution plus haute pour une meilleure qualité d'affichage
# I_resized = I.fromarray(I_binary)
# I_resized = I_resized.resize((I_resized.width * 100, I_resized.height * 100), I.NEAREST)

# # Sauvegarder l'I en PNG (format sans perte)
# I_resized.save("I_binaire_9x9_carre_noir_centre.bmp")
# I_resized.show()
# print("L'I a été générée avec succès.")
# print(255/15)
# print(255//15)