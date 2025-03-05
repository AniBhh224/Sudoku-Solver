from tkinter import *
import os
from menu import *


if not os.path.exists("Users"):
    os.makedirs("Users")

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Veuillez entrer vos informations").pack(pady=20)
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Nom d'utilisateur * ")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Mot de passe * ")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="S'inscire", width=10, height=1, bg="#fd7258", command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Entrez vos informations de connexion").pack(pady=20)
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Nom d'utilisateur * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Mot de passe * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    password_login_entry.bind('<Return>', lambda event=None: login_verify())
    Button(login_screen, text="Se connecter", width=10, height=1, bg="#fd7258", command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    
    # Chemin du fichier utilisateur
    user_file_path = os.path.join("Users", username_info)
    
    # Vérifier si l'utilisateur existe déjà
    if os.path.isfile(user_file_path):
        Label(register_screen, text="Ce nom d'utilisateur est déja pris", fg="red", font=("calibri", 11)).pack()
    else:
        with open(user_file_path, "w") as file:
            file.write(username_info + "\n")
            file.write(password_info + "\n")
            file.write(str(0) + "\n")
        
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        
        Label(register_screen, text="Compte crée avec succés", fg="green", font=("calibri", 11)).pack()

def make_dico(verify):
    dico = {}
    dico["User"] = verify[0]
    dico["Pass"] = verify[1]
    dico["Score"] = verify[2]
    if len(verify) > 3:
        for i in range(3, len(verify)):
            dico[i-2] = string_to_grid(verify[i])
    return dico

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    user_file_path = os.path.join("Users", username1)
    if os.path.isfile(user_file_path):
        with open(user_file_path, "r") as file:
            verify = file.read().splitlines()
            if password1 == verify[1]:
                
                info_dico = make_dico(verify)
                login_sucess(info_dico)
            else:
                password_not_recognised()
    else:
        user_not_found()




def login_sucess(info_dico):
    # Fermer les autres fenêtres
    if 'login_screen' in globals() and login_screen.winfo_exists():
        login_screen.destroy()

    main_screen.destroy()


    menu(info_dico)


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Erreur")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Mot de passe invalide").pack(pady=15)
    Button(password_not_recog_screen, text="OK" , bg="#fd7258", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Erreur")
    user_not_found_screen.geometry("200x100")
    Label(user_not_found_screen, text="Nom d'utilisateur introuvable").pack(pady=15)
    Button(user_not_found_screen, text="OK", bg="#fd7258", command=delete_user_not_found_screen).pack()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("700x450")
    main_screen.title("Account Login")


    Label(main_screen, text="Bienvenue sur le jeu du SUDOKU", bg="#fd7258", width="300", height="2", font=("Calibri", 13)).pack()

    img = PhotoImage(file='login.png')
    img = img.subsample(2) 

 
    frame = Frame(main_screen)
    frame.pack(pady=20)  


    Label(frame, image=img, bg='white').grid(row=0, column=0, rowspan=2, padx=10)


    Button(frame, text="Se connecter", height="5", width="30", bd=5, relief="raised", command=login).grid(row=0, column=1, padx=10, pady=(2, 1))
    Button(frame, text="Créer un compte", height="5", width="30", bd=5, relief="raised", command=register).grid(row=1, column=1, padx=10, pady=(1, 2))

    main_screen.mainloop()


