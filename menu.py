import tkinter as tk
from choix_grille import *
from Jeu_graphique import *
import os

def string_to_grid(grid_string):
    parts = grid_string.split(" // ")
    grid = eval(parts[2])
    reponse = eval(parts[3])
    grid_init = eval(parts[4])
    time = float(parts[5])
    return int(parts[0]), int(parts[1]), grid, reponse, grid_init, time

def reprendre_grille(info_dico, i):
    root.destroy()
    open_game(list(info_dico[i][2]), list(info_dico[i][3]), info_dico, i)
    menu(file_in_dico(info_dico))
    

def file_in_dico(info_dico):
    user_file_path = os.path.join("Users", info_dico["User"])
    if os.path.isfile(user_file_path):
        with open(user_file_path, "r") as file:
            verify = file.read().splitlines()
            dico = {}
            dico["User"] = verify[0]
            dico["Pass"] = verify[1]
            dico["Score"] = verify[2]
            if len(verify) > 3:
                for i in range(3, len(verify)):
                    dico[i-2] = string_to_grid(verify[i])
    return dico

def refresh(info_dico):
    info_dico = file_in_dico(info_dico)
    global root
    root.destroy()
    root = None
    menu(info_dico)

def calcul_pourcent_grid(info_dico, i):
    grille = info_dico[i][2]
    grid_init = info_dico[i][4]
    reponse = info_dico[i][3]
    total_cases = 0
    cases_remplies = 0
    for y in range(9):
        for x in range(9):
            if grid_init[y][x] == 0:  
                total_cases += 1
                if grille[y][x] != 0 and (grille[y][x] == reponse[y][x]):
                    cases_remplies += 1
    pourcentage = (cases_remplies / total_cases) * 100 if total_cases != 0 else 0
    return int(pourcentage)

def menu(info_dico):
    global root, error_label  
    root = tk.Tk()
    if len(info_dico)>=7:
        root.geometry("750x600")
    elif len(info_dico) ==4:
        root.geometry("750x400")
    elif len(info_dico) ==5:
        root.geometry("750x450")
    else:
        root.geometry("750x500")
    root.title("Sudoku Menu")

    score_frame = tk.Frame(root)
    score_frame.pack(side=tk.TOP, padx=10, pady=10, anchor='ne')

    # Score du joueur
    score_label = tk.Label(score_frame, text="Score : " + info_dico["Score"], font=("Arial", 16))
    score_label.pack()

    frame_bienvenue = tk.Frame(root, bd=2, relief="solid")
    frame_bienvenue.pack(pady=10)
    label_bienvenue = tk.Label(frame_bienvenue, text="Bonjour {0}".format(info_dico["User"]), font=("Arial", 24), fg="#ffa100")
    label_bienvenue.pack(padx=10, pady=10)

    btn_classement = tk.Button(score_frame, text="Classement", font=("Arial", 16), command=lambda: classement())
    btn_classement.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True, padx=20, pady=20, side=tk.LEFT, anchor='n')

    label_reprendre = tk.Label(button_frame, text="Reprendre une grille", font=("Helvetica", 16), padx=25)
    label_reprendre.pack(pady=10)



    def classement():
        # Créer une nouvelle fenêtre
        classement_window = tk.Toplevel(root)
        classement_window.title("Classement")
        classement_window.geometry("350x400")

        # Lire tous les utilisateurs et leurs scores du dossier Users
        user_scores = []
        users_dir = "Users"
        for filename in os.listdir(users_dir):
            if "." not in filename:
                with open(os.path.join(users_dir, filename), "r") as file:
                    lines = file.read().splitlines()
                    print(lines)
                    if len(lines) >= 3:
                        user_scores.append((lines[0], int(lines[2])))

        # Trier les utilisateurs par score décroissant
        user_scores.sort(key=lambda x: x[1], reverse=True)


        # Afficher les utilisateurs et leurs scores dans la fenêtre de classement
        # Ajouter un cadre avec des bordures autour du texte "Classement des utilisateurs"
        frame_title = tk.Frame(classement_window, bd=2, relief="solid")
        frame_title.pack(pady=10)
        tk.Label(frame_title, text="Classement des utilisateurs", font=("Arial", 16)).pack(pady=10, padx=10)

        # Afficher les utilisateurs et leurs scores dans la fenêtre de classement
        for i, (user, score) in enumerate(user_scores, start=1):
            tk.Label(classement_window, text=f"{i}. {user} - Score: {score}", font=("Arial", 14)).pack(anchor="w", padx=20, pady=5)


            

    def supprimer_grille(info_dico, no):
        new_dico = {}
        new_dico["User"] = info_dico["User"]
        new_dico["Pass"] = info_dico["Pass"]
        new_dico["Score"] = info_dico["Score"]
        for i in range(1, no):
            new_dico[i] = info_dico[i]
        for i in range(no, len(info_dico) - 3):
            new_dico[i] = info_dico[i + 1]
        save_dico_in_file(new_dico)
        refresh(new_dico)
        return new_dico

    def creer_menu_contextuel(bouton, grille, no):
        menu_contextuel = tk.Menu(bouton, tearoff=0)
        menu_contextuel.add_command(label="Supprimer", command=lambda: supprimer_grille(info_dico, no))
        bouton.bind("<Button-3>", lambda event: menu_contextuel.post(event.x_root, event.y_root))

    def mettre_a_jour_boutons(info_dico):
        if len(info_dico) > 3:
            j = 1
            for i in range(1, len(info_dico) - 2):
                if int(info_dico[i][0]) == 1:
                    btn_grille = tk.Button(button_frame, text="Grille niveau facile no " + str(j) + " | " + str(calcul_pourcent_grid(info_dico, i)) + "%", font=("Helvetica", 16), padx=25, bd=5, relief="raised", command=lambda i=i: reprendre_grille(info_dico, i))
                    btn_grille.pack(pady=5)
                    creer_menu_contextuel(btn_grille, info_dico[i][2], i)
                    j += 1
            j = 1
            for i in range(1, len(info_dico) - 2):
                if info_dico[i][0] == 2:
                    btn_grille = tk.Button(button_frame, text="Grille niveau moyen no " + str(j) + " | " + str(calcul_pourcent_grid(info_dico, i)) + "%", font=("Helvetica", 16), padx=25, bd=5, relief="raised", command=lambda i=i: reprendre_grille(info_dico, i))
                    btn_grille.pack(pady=5)
                    creer_menu_contextuel(btn_grille, info_dico[i][2], i)
                    j += 1        
            j = 1
            for i in range(1, len(info_dico) - 2):
                if info_dico[i][0] == 3:
                    btn_grille = tk.Button(button_frame, text="Grille niveau difficile no " + str(j) + " | " + str(calcul_pourcent_grid(info_dico, i)) + "%", font=("Helvetica", 16), padx=25, bd=5, relief="raised", command=lambda i=i: reprendre_grille(info_dico, i))
                    btn_grille.pack(pady=5)
                    creer_menu_contextuel(btn_grille, info_dico[i][2], i)
                    j += 1
        else:
            no_grille_label = tk.Label(button_frame, text="Vous n'avez pas de grilles commencées", font=("Helvetica", 16))
            no_grille_label.pack()

    mettre_a_jour_boutons(info_dico)

    new_game_frame = tk.Frame(root)
    new_game_frame.pack(expand=True, padx=20, pady=20, side=tk.RIGHT, anchor='n')

    btn_nv = tk.Button(new_game_frame, text="Commencer une nouvelle grille", font=("Helvetica", 16), padx=25, bd=5, relief="raised", height=3)
    btn_nv.pack(pady=30)

    error_label = tk.Label(new_game_frame, text="", font=("Helvetica", 12), fg="red")  # Initialisation de error_label
    error_label.pack()

    def grille_facile_r(info_dico, i):
        if len(info_dico) < 8:
            root.destroy()
            grille_facile(info_dico, len(info_dico) - 2)
            menu(info_dico)
        else:
            error_label.config(text="Impossible de créer plus de 5 grilles")
    def grille_moyenne_r(info_dico, i):
        if len(info_dico) < 8:
            root.destroy()
            grille_moyenne(info_dico, len(info_dico) - 2)
            menu(info_dico)
        else:
            error_label.config(text="Impossible de créer plus de 5 grilles")
    def grille_difficile_r(info_dico, i):
        if len(info_dico) < 8:
            root.destroy()
            grille_difficile(info_dico, len(info_dico) - 2)
            menu(info_dico)
        else:
            error_label.config(text="Impossible de créer plus de 5 grilles")

    menu_deroulant = tk.Menu(new_game_frame, tearoff=0)
    menu_deroulant.add_command(label="Facile", command=lambda: grille_facile_r(info_dico, len(info_dico) - 2))
    menu_deroulant.add_command(label="Moyen", command=lambda: grille_moyenne_r(info_dico, len(info_dico) - 2))
    menu_deroulant.add_command(label="Difficile", command=lambda: grille_difficile_r(info_dico, len(info_dico) - 2))

    def show_menu(event):
        menu_deroulant.post(event.x_root, event.y_root)

    btn_nv.bind("<Button-1>", show_menu)

    # Create the main menu with a "Refresh" option
    main_menu = tk.Menu(root)
    root.config(menu=main_menu)

    options_menu = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Refresh", command=lambda: refresh(info_dico))

    root.mainloop()
