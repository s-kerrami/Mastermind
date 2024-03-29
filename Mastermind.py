print("hello")
print("Bienvenu au jeu de Mastermind!")



type_de_jeu = int(input("Quel mode de jeu souhaitez-vous? : \n"
                        "1. Jeu solo \n"
                        "2. Maître de jeu VS joueur \n"))
match type_de_jeu:
    case 1 :
        correct = False
        print("solo")
        pass
    case 2 :
        correct = False
        print("2 joueurs")
        pass
    case _ :
        correct = False
        pass

#couleur = ["Blanc", "Bleu", "Rouge", "Vert", "Jaune", "Orange", "Mauve", "Brun"]

place1 = int(input("Choix de la couleur pour la place : {tab_rempli} : "))

place = 0

choix_couleur = int(input("Veuillez entrer la couleur choisie à la place {place} : \n"
                            "0. Blanc \n"
                            "1. Bleu \n"
                            "2. Rouge \n"
                            "3. Vert \n"
                            "4. Jaune \n"
                            "5. Orange \n"
                            "6. Mauve \n"
                            "7. Brun \n"))
match choix_couleur:
    case 1 :
        pass
    case 2 :
        pass
    case 3 :
        pass
    case 4 :
        pass
    case 5 :
        pass
    case 6 :
        pass
    case 7 :
        pass
    case 8 :
        pass
    case _ :
        pass 




