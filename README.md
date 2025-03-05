# 🧩 Sudoku Solver

## 📌 Description
Ce projet est une application complète de **jeu de Sudoku** développée en **Python**, avec une interface graphique réalisée en **Tkinter**.

### 🎯 Fonctionnalités :
- ✅ Système d'authentification (création et connexion d’utilisateurs).
- ✅ Génération de grilles de Sudoku avec différents niveaux de difficulté.
- ✅ Sauvegarde automatique et reprise des parties.
- ✅ Classement des utilisateurs basé sur leurs performances.
- ✅ Jeu disponible en version console et graphique.
- ✅ Vérification de la validité des grilles et correction automatique.

---

## 🚀 Lancement du projet

### 1️⃣ Cloner le dépôt :
```bash
git clone https://github.com/AniBhh224/Sudoku-Solver.git
```

### 2️⃣ Installer les dépendances :
Le projet utilise uniquement des bibliothèques standard de Python (comme `tkinter`), mais assure-toi que **Python 3** est installé sur ta machine.

### 3️⃣ Lancer l’application :
```bash
python3 main.py
```

---

## 🏷️ Utilisation

- Lance l’application avec :
  ```bash
  python3 main.py
  ```

- Depuis le menu principal :
  - Connecte-toi ou crée un compte.
  - Choisis de reprendre une grille existante ou d'en générer une nouvelle (facile, moyen, difficile).
  - Joue via l'interface graphique et sauvegarde automatiquement ta progression.
  - Consulte le classement global des joueurs.

---

## 🛠️ Structure du projet

| Fichier              | Rôle                                               |
|----------------------|----------------------------------------------------|
| `main.py`           | Point d'entrée de l'application                    |
| `connexion_page.py` | Gestion de l'inscription et de la connexion        |
| `menu.py`           | Menu principal et gestion des grilles sauvegardées |
| `Generator.py`      | Générateur de grilles de Sudoku                    |
| `Solver.py`         | Algorithme de résolution du Sudoku                 |
| `Jeu_graphique.py`  | Interface de jeu en mode graphique                 |
| `Jeu_Console.py`    | Mode console du jeu                                |
| `choix_grille.py`   | Gestion de la création de nouvelles grilles        |

---

## 🏆 Classement et scores

- Système de points selon la difficulté et le temps de résolution :
  - **Facile** : jusqu’à 100 points.
  - **Moyen** : jusqu’à 100 points.
  - **Difficile** : jusqu’à 100 points.

Le classement est consultable directement dans l’application.

---

## 📂 Sauvegardes
Chaque utilisateur a un fichier dans le dossier `Users/` contenant :
- Identifiants.
- Score global.
- Grilles sauvegardées avec progression et temps écoulé.


