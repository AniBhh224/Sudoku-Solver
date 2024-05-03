from Solver import *
from Generator import *
import random
import copy




def jeu_sans_aide():
    solver = Solver()
    generator = Generator()
    print("Bienvenue dans le Jeu du Sudoku.")
    print("Choisissez le niveau de votre grille ")

    while True:
        try:
            niveau = int(input("Choisissez le niveau de votre grille \n1 : Niveau Facile \n2 : Niveau Moyen \n3 : Niveau Difficile\n"))
            if niveau in [1, 2, 3]:
                break
            else:
                print("Erreur, veuillez entrer 1, 2 ou 3.")
        except ValueError:
            print("Erreur, veuillez entrer un entier.")

    reponse = generator.generer(9)
    grille_jouable = generator.generer_jouable(reponse, 9, niveau)
    grille_init = copy.deepcopy(grille_jouable)
    print("Voici votre grille :")
    generator.affichier(reponse)
    print("-----------------------------")


    termine = False
    tour = 1
    while not termine:
        generator.affichier(grille_jouable)
        print("Tour N° ", tour)
        while True:
            try:
                x = int(input("Entrez la coordonnée x : ")) - 1
                y = int(input("Entrez la coordonnée y : ")) - 1
                
                if (x < 0 or x >= 9) or (y < 0 or y >= 9) or grille_init[y][x] != 0:
                    raise ValueError("La case sélectionnée n'est pas vide ou les coordonnées sont invalides.")
                break
            except ValueError as e:
                print(e)
                print("Erreur, veuillez entrer des entiers valides pour les coordonnées.")



        value = int(input("Entrer la valeur : "))
        grille_jouable[y][x] = value
        if grille_jouable == reponse:
            print("Bravo, vou avez gagné !")
            termine = True
        tour += 1


 
def jeu_avec_aide():
    solver = Solver()
    generator = Generator()
    print("Bienvenue dans le Jeu du Sudoku.")
    print("Choisissez le niveau de votre grille ")
    while True:
        try:
            niveau = int(input("Choisissez le niveau de votre grille \n1 : Niveau Facile \n2 : Niveau Moyen \n3 : Niveau Difficile\n"))
            if niveau in [1, 2, 3]:
                break
            else:
                print("Erreur, veuillez entrer 1, 2 ou 3.")
        except ValueError:
            print("Erreur, veuillez entrer un entier.")

    reponse = generator.generer(9)
    grille_jouable = generator.generer_jouable(reponse, 9, niveau)
    grille_init = copy.deepcopy(grille_jouable)
    print("Voici votre grille :")
    generator.affichier(reponse)
    print("-----------------------------")


    termine = False
    tour = 1
    while not termine:
        generator.affichier(grille_jouable)
        print("Tour N° ", tour)
        while True:
            try:
                x = int(input("Entrez la coordonnée x : ")) - 1
                y = int(input("Entrez la coordonnée y : ")) - 1
                
                if (x < 0 or x >= 9) or (y < 0 or y >= 9) or grille_init[y][x] != 0:
                    raise ValueError("La case sélectionnée n'est pas vide ou les coordonnées sont invalides.")
                break
            except ValueError as e:
                print(e)
                print("Erreur, veuillez entrer des entiers valides pour les coordonnées.")



        value = int(input("Entrer la valeur : "))
        while value not in solver.valeur_possible(grille_jouable, x, y):
            value = int(input("Entrer une valeur possible : "))
        grille_jouable[y][x] = value
        if grille_jouable == reponse:
            print("Bravo, vou avez gagné !")
            termine = True
        tour += 1




