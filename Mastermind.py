

import random

# Définition des couleurs possibles
couleur = ["rouge", "bleu", "vert", "jaune", "orange", "violet", "blanc", "noir"]

# Choix aléatoire des couleurs du maître du jeu
place1, place2, place3, place4 = random.sample(couleur, 4)

# Compteur de tentatives restantes
tentatives_restantes = 10

print("Le maître du jeu a choisi 4 couleurs parmi", ", ".join(couleur))
print("Vous avez 10 tentatives pour deviner les bonnes couleurs dans le bon ordre.")

while tentatives_restantes > 0:
    # Saisie des couleurs par les joueurs
    proposition = input("Entrez vos couleurs séparées par des espaces : ").strip().split()
    
    if len(proposition) != 4:
        print("Vous devez entrer exactement 4 couleurs.")
        continue

    bien_place = mal_place = 0
    for i in range(4):
        if proposition[i] == place1 or proposition[i] == place2 or proposition[i] == place3 or proposition[i] == place4:
            if proposition[i] == place1 and i == 0:
                bien_place += 1
            elif proposition[i] == place2 and i == 1:
                bien_place += 1
            elif proposition[i] == place3 and i == 2:
                bien_place += 1
            elif proposition[i] == place4 and i == 3:
                bien_place += 1
            else:
                mal_place += 1

    if bien_place == 4:
        print("Félicitations, vous avez trouvé les bonnes couleurs dans le bon ordre !")
        break
    else:
        print("Vous avez", bien_place, "couleur(s) bien placée(s) et", mal_place, "couleur(s) mal placée(s).")
        tentatives_restantes -= 1
        print("Il vous reste", tentatives_restantes, "tentative(s).")

if tentatives_restantes == 0:
    print("Désolé, vous n'avez pas réussi à trouver les bonnes couleurs. Les couleurs étaient :", place1, place2, place3, place4)
