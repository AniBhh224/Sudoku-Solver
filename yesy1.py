def doublon_ligne(l, x, y, v):
    for i in range(len(l[0])):
        if l[y][i] == v and i != x:
            return True
    return False     

def doublon_colonne(l, x, y, v):
    for i in range(len(l)):
        if l[i][x] == v and i != y:
            return True
    return False     

def doublon_sub(l, x, y, v):
    taille_subdivision = len(l) // 3  
    debut_subdivision_ligne = (x // taille_subdivision) * taille_subdivision
    debut_subdivision_colonne = (y // taille_subdivision) * taille_subdivision
    fin_subdivision_ligne = debut_subdivision_ligne + taille_subdivision - 1
    fin_subdivision_colonne = debut_subdivision_colonne + taille_subdivision - 1
    for i in range(debut_subdivision_ligne, fin_subdivision_ligne+1):
        for j in range(debut_subdivision_colonne, fin_subdivision_colonne+1):
            if l[j][i] == v and (i != x or j != y):
                return True
    return False


def valeur_possible(l,x,y):
    val_poss = []
    for i in range(1,10):
        if (doublon_colonne(l, x, y, i) == False and doublon_ligne(l, x, y, i) == False and doublon_sub(l, x, y, i) == False):
            val_poss.append(i)
    return val_poss
def resoudre(sudoku):
    global nb_solutions
    for y in range(len(sudoku)):
        for x in range(len(sudoku)):
            if sudoku[y][x] == 0:
                tab = valeur_possible(sudoku, x, y)
                for n in tab:
                    sudoku[y][x] = n
                    resoudre(sudoku)
                    sudoku[y][x] = 0
                return
            if x == 8 and y == 8:
                nb_solutions += 1

# Exemple d'utilisation
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 0, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 9]
]

nb_solutions = 0
resoudre(sudoku)
print(f"Nombre de solutions possibles : {nb_solutions}")
