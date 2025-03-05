import tkinter as tk
from tkinter import *
from Jeu_graphique import *
from Generator import *
from menu import *
import os



def save_grid(grid, reponse,info_dico, difficulté, taille):
   
        user_file_path = os.path.join("Users", str(info_dico["User"]))
        if os.path.isfile(user_file_path):
            with open(user_file_path, "a") as file:
                file.write(str(difficulté)+ " // " +str(taille)+ " // ")
                file.write(grid_to_string(grid, reponse, grid))
                file.write(" // " +str(0)+"\n")


def grille_facile(info_dico, i):
    generator = Generator()
    reponse = generator.generer(9)
    grille = generator.generer_jouable(reponse, 9, 1)
    save_grid(grille, reponse, info_dico, 1, 9)
    info_dico[len(info_dico)-2] = (1, 9, grille, reponse, grille, 0)
    open_game(grille, reponse, info_dico, i)

def grille_moyenne(info_dico, i):
    generator = Generator()
    reponse = generator.generer(9)
    grille = generator.generer_jouable(reponse, 9, 2)
    save_grid(grille, reponse, info_dico, 2, 9)
    info_dico[len(info_dico)-2] = (2, 9, grille, reponse, grille, 0)
    open_game(grille, reponse, info_dico, i)

def grille_difficile(info_dico, i):
    generator = Generator()
    reponse = generator.generer(9)
    grille = generator.generer_jouable(reponse, 9, 3)
    save_grid(grille, reponse, info_dico, 3, 9)
    info_dico[len(info_dico)-2] = (3, 9, grille, reponse, grille, 0)
    open_game(grille, reponse, info_dico, i,)

# Créer la fenêtre principale