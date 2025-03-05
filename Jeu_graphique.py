from tkinter import *
from Solver import *
from choix_grille import *

import os
import time
from menu import *

def grid_to_string(grid, reponse, grid_init):
    #Transforme les 3 grilles en chaine de caractere pour pouvoir les mettre dans le fichier.
    grid_string = str(grid)
    reponse_string = str(reponse)
    grid_initale = str(grid_init)
    final_string = f"{grid_string} // {reponse_string} // {grid_initale}"
    return final_string


def save_dico_in_file(info_dico):
    user_file_path = os.path.join("Users", info_dico["User"])
    with open(user_file_path, "w") as file:
        file.write(info_dico["User"] + "\n")
        file.write(info_dico["Pass"] + "\n")
        file.write(info_dico["Score"] + "\n")
        for i in range(1, len(info_dico)-2):
            file.write(str(info_dico[i][0]) + " // " + str(info_dico[i][1]) + " // ")
            file.write(grid_to_string(info_dico[i][2], info_dico[i][3], info_dico[i][4])+ " // "+ str(info_dico[i][5]) + "\n")



def open_game(grille, reponse, info_dico, i):
    game = Tk()
    game.title("Sudoku Solver")
    game.geometry("700x700")
    game.protocol("WM_DELETE_WINDOW", lambda: on_close(info_dico, i, elapsed_time))
    timer_label = Label(game, text="00:00", font=("Helvetica", 25))
    timer_label.grid(row=0, column=0, columnspan=2, padx=5, pady=15)
    finished = False
    start_time = time.time()

    def navigate_grid(event):
        nonlocal last_clicked
        current_cell = last_clicked[-1]
        row, col = current_cell[1], current_cell[0]
        if event.keysym == "Right":
            col = min(col + 1, 9)
        elif event.keysym == "Left":
            col = max(col - 1, 1)
        elif event.keysym == "Down":
            row = min(row + 1, 9)
        elif event.keysym == "Up":
            row = max(row - 1, 1)
        cell_clicked(cells, col, row, "white")
        cells[(row, col)].focus_set()# Simuler un clic sur la nouvelle cellule sélectionnée

    game.bind("<Right>", navigate_grid)
    game.bind("<Left>", navigate_grid)
    game.bind("<Down>", navigate_grid)
    game.bind("<Up>", navigate_grid)
    
    def on_close(info_dico, i, time):
        #Fonction executée lors de la fermeture de la page, elle enregistre la grille, la supprime si elle est terminée.
        nonlocal finished
        update_grid_in_dico(info_dico[i][3], info_dico, i, time)
        if finished == True:
            info_dico = supprimer_grille(info_dico, i)
        
        save_dico_in_file(info_dico)
        
        game.destroy()
        

    def supprimer_grille(info_dico, no):
        new_dico = {}
        new_dico["User"] = info_dico["User"]
        new_dico["Pass"] = info_dico["Pass"]
        new_dico["Score"] = info_dico["Score"]
        for i in range(1, no):
            new_dico[i] = info_dico[i]
        for i in range(no, len(info_dico)-3):
            new_dico[i] = info_dico[i+1]
        save_dico_in_file(new_dico)
        
        return new_dico

    elapsed_time = 0
    
    def update_timer():
        nonlocal elapsed_time
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        game.after(10, update_timer)

    def resume_timer(start_point):
        nonlocal start_time
        start_time = time.time() - start_point
        update_timer()

    resume_timer(info_dico[i][5])

    game.grid_rowconfigure(0, weight=1)
    game.grid_rowconfigure(17, weight=1)
    game.grid_columnconfigure(0, weight=1)
    game.grid_columnconfigure(11, weight=1)

    menu_bar = Menu(game)
    game.config(menu=menu_bar)

    label = Label(game, text="Remplissez cette grille le plus vite possible", font=("Helvetica", 16))
    label.grid(row=0, column=1, columnspan=9)

    errLabel = Label(game, text="", fg="red")
    errLabel.grid(row=15, column=1, columnspan=10, pady=5)

    solvedLabel = Label(game, text="", fg="green")
    solvedLabel.grid(row=16, column=1, columnspan=10, pady=5)

    cells = {}
    last_clicked = []

    def ValidateNumber(P):
        return (P.isdigit() or P == "") and len(P) < 2
    reg = game.register(ValidateNumber)

    def draw9x9Grid(board):
        color = "white"
        font_size = 12
        text_color = "black"
        for rowNo in range(1, 10, 3):
            for colNo in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        val = board[4][rowNo+i-1][colNo+j]
                        bgcolor = color
                        if val == 0:
                            if board[2][rowNo+i-1][colNo+j] != 0:
                                val = board[2][rowNo+i-1][colNo+j] 
                            else : 
                                val = ""
                        e = Entry(game, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"), font=("Helvetica", font_size), fg=text_color)
                        e.grid(row=rowNo+i+1, column=colNo+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
                        e.insert(0, str(val))
                        e.redcolored = False
                        #Rajoute un attribut "redcolored" pour savoir si cette case a été coloriée en rouge
                        if val != "" and board[4][rowNo+i-1][colNo+j] != 0 :
                            e.config(state='disabled')
                            e.configure({"disabledbackground": 'white'})
                        else:
                            e.config(state='normal')
                            e.bind("<KeyRelease>", lambda event, r=rowNo+i, c=colNo+j+1: color_entry(cells, r, c))
                        e.variable = StringVar()
                        cells[(rowNo+i, colNo+j+1)] = e
                        e.bind("<Button-1>", lambda event, r=rowNo+i, c=colNo+j+1: cell_clicked(cells, c, r, bgcolor))

                    if colNo != 6:
                        frame = Frame(game, width=2, height=30, bg="black")  
                        frame.grid(row=rowNo+i+1, column=colNo+j+1, sticky="nse")
                    if rowNo != 7:
                        frame = Frame(game, width=90, height=2, bg="black")  
                        frame.grid(row=rowNo+3, column=colNo+1, columnspan=3, sticky="swe")

    def fill_color(cells, c, r, color):
        #Remplie la subdivision, ligne, colonne de la case selectionnée.
        for i in range(1, 10):
            entry = cells[r, i]
            if entry.redcolored == False:
                if entry["state"] == "disabled":
                    entry.config(disabledbackground=color)
                else:
                    entry.config(bg=color)
            entry = cells[i, c]
            if entry.redcolored == False:
                if entry["state"] == "disabled":
                    entry.config(disabledbackground=color)
                else:
                    entry.config(bg=color)

        debut_subdivision_ligne = 3 * ((r - 1) // 3) + 1
        debut_subdivision_colonne = 3 * ((c - 1) // 3) + 1

        for i in range(debut_subdivision_ligne, debut_subdivision_ligne + 3):
            for j in range(debut_subdivision_colonne, debut_subdivision_colonne + 3):
                entry = cells[i, j]
                if entry.redcolored == False:
                    if entry["state"] == "disabled":
                        entry.config(disabledbackground=color)
                    else:
                        entry.config(bg=color)

    def cell_clicked(cells, c, r, original_color):
        nonlocal last_clicked
        if len(last_clicked) == 0: #Si la case cliquée est la première, colorier seulement la case sans reinitialiser la couleur de l'ancienne
            fill_color(cells, c, r, "#ffc768")
            entry = cells[r, c]
            if entry["state"] == "disabled":
                entry.config(disabledbackground='#ffa100')
            else:
                entry.config(bg='#ffa100')
            last_clicked.append([c, r])
        else:
            fill_color(cells, last_clicked[-1][0], last_clicked[-1][1], "white")
            fill_color(cells, c, r, "#ffc768")
            entry = cells[r, c]
            if entry["state"] == "disabled":
                entry.config(disabledbackground='#ffa100')
            else:
                entry.config(bg='#ffa100')
            last_clicked.append([c, r])


    def color_entry(cells, r, c):
        grid = constitute_grid()
        entry = cells[(r, c)]
        y, x = int(r-1), int(c-1)
        grid[y][x] = 0
        
        if entry.get() == "":
            if entry.redcolored == True:
                entry.redcolored = False
            entry.config(bg="#ffa100")
            last_clicked.append([c, r])
        else:
            if int(entry.get()) not in Solver().valeur_possible(grid, x, y):
                entry.config(bg="red")
                entry.redcolored = True
            else:
                entry.redcolord = False
                entry.config(bg="#ffa100")

    def constitute_grid():
        #Retourne la grille actuelle en format liste.
        current_solution = []
        for row in range(1, 10):
            rows = []
            for col in range(1, 10):
                val = cells[(row, col)].get()
                rows.append(int(val) if val else 0)
            current_solution.append(rows)
        return current_solution
    
    def grid_finished(info_dico, i):
        #Attribution des points.
        score = 0
        if info_dico[i][0] == 1 :
            if info_dico[i][5] <= 300:
                score += 100
            elif info_dico[i][5] > 300 and info_dico[i][5] <= 600:
                score += 50
            else:
                score += 25

        elif info_dico[i][0] == 2:
            if info_dico[i][5] <= 550:
                score += 100
            elif info_dico[i][5] > 550 and info_dico[i][5] <= 750:
                score += 50
            else:
                score += 25
        else:
            if info_dico[i][5] <= 600:
                score += 100
            elif info_dico[i][5] > 600 and info_dico[i][5] <= 900:
                score += 50
            else:
                score += 25
            
        return score
    
    def verify_solution(info_dico, i, time, verify_button):
        nonlocal finished
        current_solution = constitute_grid()
        if current_solution == info_dico[i][3]:
            update_grid_in_dico(info_dico[i][3], info_dico, i, time)
            score = grid_finished(info_dico, i)
            total_score = int(info_dico["Score"]) + score
            solvedLabel.configure(text="La réponse est correcte ! Vous gagnez "+str(score)+"\n Votre score total est "+str(total_score), font=30)
            info_dico["Score"] = str(total_score)
            update_grid_in_dico(info_dico[i][3], info_dico, i, time)
            verify_button.config(state="disabled")  # Désactiver le bouton "Vérifier"  # Désactiver le bouton "Enregistrer"
            finished = True
            errLabel.configure(text="")
        else:
            solvedLabel.configure(text="La réponse est incorrecte !", font=30, fg="red")
            errLabel.configure(text="")

    def update_grid_in_dico(reponse, info_dico, i, time):
        grille = constitute_grid()
        info_dico[int(i)] = (info_dico[i][0], info_dico[i][1], grille, reponse, info_dico[i][4], time)
        return info_dico

    def enregistrer_grille(reponse,info_dico, i, time):
        update_grid_in_dico(reponse, info_dico, i, time)
        save_dico_in_file(info_dico)


    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Options", menu=file_menu)
    file_menu.add_command(label="Enregistrer et quitter", command=lambda: on_close(info_dico, i, elapsed_time))


    draw9x9Grid(info_dico[i])

    verify_button = Button(game, text="Verifier", font=("Helvetica", 16), command=lambda: verify_solution(info_dico, i, elapsed_time, verify_button))
    verify_button.grid(row=14, column=1, columnspan=10, pady=20)

    game.mainloop()