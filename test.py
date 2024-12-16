import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#c'est avec ca que je genere l'image de l'histo

# data = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255]],
#                 [[255, 255, 255], [0, 0, 0], [255, 0, 255], [0, 255, 0], [0, 0, 0]],
#                 [[255, 0, 0], [255, 255, 0], [0, 0, 255], [0, 0, 0], [255, 0, 255]],
#                 [[0, 255, 255], [255, 0, 255], [255, 255, 255], [0, 0, 0], [0, 255, 0]],
#                 [[0, 0, 255], [255, 0, 0], [255, 255, 0], [0, 255, 0], [255, 255, 255]]], dtype=np.uint8)

# # Créer une image à partir de la matrice
# image = Image.fromarray(data)
# large_image = image.resize((image.width * 100, image.height * 100), Image.NEAREST)
# large_image.show()
# large_image.save("bon_choix.png")

# # Sauvegarder l'image générée
# image.save("image_generée.png")
# Fichiers pour les images binaires
I2_BMP_FILE = 'I2_binaire.bmp'
I1_BMP_FILE = 'I1_binaire.bmp'

# Fonction principale
def menu():
    while True:
        print("\nMenu principal:")
        print("1 - Manipuler les images binaires")
        print("2 - Histogramme de l'image couleur")
        print("3 - Conversion vers image binaire ou niveau de gris(le niveau de gris vous sera demander)")
        print("4 - L'hitogramme de l'image utilisee dans la question 2")
        print("5 - Filtre de Nagao appliquee a une image en niveau de gris")
        print("0 - Quitter")
        
        choix = int(input("Entrez votre choix: "))
        
        if choix == 1:
            menu_images_binaires()
        elif choix == 2:
            histogramme_image_couleur()
        elif choix == 3:
            convert_image()
        elif choix == 4:

            # Recharger l'image sauvegardée

            mon_portrait = Image.open("me.jpeg")
            mon_portrait = mon_portrait.resize((5, 5))
            image_array = np.array(mon_portrait)

            # Séparer les canaux R, G et B
            R = image_array[:, :, 0]  # Canal Rouge
            G = image_array[:, :, 1]  # Canal Vert
            B = image_array[:, :, 2]  # Canal Bleu

            # Affichage des matrices dans la console
            print("Matrice du canal Rouge (après rechargement) :")
            print(R)

            print("\nMatrice du canal Vert (après rechargement) :")
            print(G)

            print("\nMatrice du canal Bleu (après rechargement) :")
            print(B)

        elif choix == 5:
            print('Processing...')
            appliquer_filtre_nagao('me.jpeg')
            print('Done')
        elif choix == 0:
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Sous-menu pour manipuler les images binaires
def menu_images_binaires():
    while True:
        print("\nSous-menu Images Binaires:")
        print("1.a - Générer les images binaires")
        print("1.b - Additionner les images binaires")
        print("1.c - Soustraire les images binaires")
        print("1.d - Multiplication par 2 de l'image en niveaux de gris")
        print("0 - Retour au menu principal")
        
        choix = input("Entrez votre choix: ").strip()
        
        if choix == '1.a':
            generer_images_binaires()
        elif choix == '1.b':
            addition_images()
        elif choix == '1.c':
            soustraction_images()
        elif choix == '1.d':
            multiplication_image_gris()
        elif choix == '0':
            break  # Retour au menu principal
        else:
            print("Choix invalide, veuillez réessayer.")

# Fonction pour générer les images binaires
def generer_images_binaires():
    I1 = np.array([
        [1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1,1],
        [1,0,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1]
    ], dtype=np.uint8)
    I1 = I1 * 255
    I1_resized = Image.fromarray(I1).convert('1')
    I1_resized = I1_resized.resize((I1_resized.width * 100, I1_resized.height * 100), Image.NEAREST)
    I1_resized.save(I1_BMP_FILE)
    I1_resized.show()
    print("L'I 1 est générée avec succès!")
    
    I2 = np.full((9, 9), 255, dtype=np.uint8)
    I2[3:5, 3:5] = 0  # Remplir un carré 2x2 en noir aux positions (3,3) à (4,4)
    I2_resized = Image.fromarray(I2).convert('1')
    I2_resized = I2_resized.resize((I2_resized.width * 100, I2_resized.height * 100), Image.NEAREST)
    I2_resized.save(I2_BMP_FILE)
    I2_resized.show()
    print("L'I 2 est générée avec succès!")

# Fonction pour additionner les images binaires
def addition_images():
    I1 = np.array(Image.open(I1_BMP_FILE).convert('1'), dtype=np.uint8)
    I2 = np.array(Image.open(I2_BMP_FILE).convert('1'), dtype=np.uint8)
    Iad = I1 + I2
    Iad = np.clip(Iad, 0, 1)  # Assurez-vous que les valeurs sont dans l'intervalle [0, 1]
    Iad *= 255
    Iad = Image.fromarray(Iad).convert('1')
    Iad.save("Iad_somme_result.bmp")
    Iad.show()
    print("La somme des deux images a été générée avec succès!")

# Fonction pour soustraire les images binaires
def soustraction_images():
    I1 = np.array(Image.open(I1_BMP_FILE).convert('1'), dtype=np.uint8)
    I2 = np.array(Image.open(I2_BMP_FILE).convert('1'), dtype=np.uint8)
    Is = I1 - I2
    Is = np.clip(Is, 0, 1)
    Is *= 255
    Is = Image.fromarray(Is).convert('1')
    Is.save("Is_diff_result.bmp")
    Is.show()
    print("La différence des deux images a été générée avec succès (I1 - I2)!")

# Fonction pour multiplier par 2 l'image en niveaux de gris
def multiplication_image_gris():
    Img_niveau_gris = np.array([
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,3,3,4,4,5,5,6,0],
        [0,3,3,4,4,5,5,6,0],
        [0,6,6,5,5,4,4,3,0],
        [0,7,8,9,7,8,9,7,0],
        [0,9,9,8,8,7,7,7,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ], dtype=np.uint8)
    Ip = np.clip(Img_niveau_gris * 2, 0, 15)
    Ip = (Ip * (255 // 15)).astype(np.uint8)
    image = Image.fromarray(Ip).convert('L')
    image = image.resize((image.width * 100, image.height * 100), Image.NEAREST)

    image.save("image_niveau_gris_multipliee_par_2.bmp")
    image.show()
    print("L'image en niveau de gris (multipliée par 2) a été générée avec succès!")
#question 3
def convert_image():
    mon_portrait = Image.open('me.jpeg')
    choix = -1

    while choix != 0:
        print("Bonjour Bienvenue! Veuillez choisir:")
        print("1 - Image Binaire")
        print("2 - Image en niveau de gris")
        print("0 - Revenir au menu principal")
        choix = int(input("Entrez votre choix: "))

        if choix == 1:
            print("Vous avez choisi l'image binaire.")
            mon_portrait_binaire = mon_portrait.convert('1')
            mon_portrait_binaire.save('portrait_binaire.bmp')
            mon_portrait_binaire.show()

        elif choix == 2:
            print("Veuillez entrer le nombre de bits souhaité.")
            nbre_bit = int(input("Veuillez entrer le nombre de bits souhaité: "))
            print(f"Vous avez choisi {nbre_bit} bits, donc une plage de 0 à {2**nbre_bit - 1}.")
            mon_portrait_array = np.array(mon_portrait)
            mon_portrait_array = mon_portrait_array * (255 // (2**nbre_bit - 1))
            mon_portrait_array = mon_portrait_array.astype(np.uint8)
            image = Image.fromarray(mon_portrait_array)
            image.save('portrait_niveau_gris.bmp')
            image.show()

        elif choix == 0:
            print("See ya!")

        else:
            print("Choix invalide, veuillez entrer une option valide.")

# Fonction pour afficher l'histogramme d'une image couleur
def histogramme_image_couleur():
    # Charger l'image couleur (remplacez 'me.jpeg' par le chemin de votre image)
    mon_portrait = Image.open('me.jpeg')
    image_rgb = mon_portrait.convert('RGB')
    image_array = np.array(image_rgb)

    # Calculer l'histogramme pour chaque canal (R, G, B)
    r_hist, r_bins = np.histogram(image_array[:, :, 0], bins=256, range=(0, 255))
    g_hist, g_bins = np.histogram(image_array[:, :, 1], bins=256, range=(0, 255))
    b_hist, b_bins = np.histogram(image_array[:, :, 2], bins=256, range=(0, 255))

    # Créer la figure avec trois sous-graphiques
    plt.figure(figsize=(15, 6))

    # Histogramme du canal rouge
    plt.subplot(131)  # 1ère position sur 3
    plt.bar(r_bins[:-1], r_hist, color='red', alpha=0.6, width=1.0)
    plt.title("Histogramme - Canal Rouge")
    plt.xlabel("Valeur d'intensité des pixels")
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
    plt.tight_layout()
    plt.show()
# Fonction pour appliquer le filtre de Nagao
def appliquer_filtre_nagao(image_path):    
    # Charger l'image couleur avec Pillow
    image = Image.open(image_path)
    
    # Convertir l'image couleur en niveaux de gris avec Pillow
    image_gray = image.convert('L')
    print('Voici l''image qu''on va utiliser')
    image_gray.show()
    # Convertir l'image PIL en un tableau NumPy
    image_array = np.array(image_gray)
    
    # On récupère les dimensions de l'image
    hauteur, largeur = image_array.shape
    
    # Créer une nouvelle image pour stocker l'image filtrée
    image_filtrée = np.zeros((hauteur, largeur), dtype=np.uint8)
    
    # Appliquer le filtre de Nagao sur chaque pixel de l'image
    for i in range(1, hauteur - 1):  # Ne pas traiter les bords
        for j in range(1, largeur - 1):
            # Extraire la fenêtre 3x3 autour du pixel (i, j)
            fenêtre = image_array[i-1:i+2, j-1:j+2]
            
            # Calculer la médiane des pixels de la fenêtre
            médiane = np.median(fenêtre)
            
            # Remplacer le pixel par la médiane
            image_filtrée[i, j] = médiane
    
    # Convertir l'image filtrée (NumPy array) en image PIL
    image_filtrée_pil = Image.fromarray(image_filtrée)
    print("Voici l'image resultante apres le filtre de Nagao")
    # Afficher l'image filtrée
    image_filtrée_pil.show()

    # Sauvegarder l'image filtrée
    image_filtrée_pil.save('portrait_filtré_nagao.jpg')


menu()
