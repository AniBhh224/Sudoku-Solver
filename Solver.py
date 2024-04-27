class Solver:
    def __init__(self):
        self.nb_solutions = 0


    def doublon_ligne(self, l, x, y, v):
        for i in range(len(l[0])):
            if l[y][i] == v and i != x:
                return True
        return False     

    def doublon_colonne(self, l, x, y, v):
        for i in range(len(l)):
            if l[i][x] == v and i != y:
                return True
        return False     

    def doublon_sub(self, l, x, y, v):
        taille_subdivision = 3
        debut_subdivision_ligne = (x // taille_subdivision) * taille_subdivision
        debut_subdivision_colonne = (y // taille_subdivision) * taille_subdivision
        fin_subdivision_ligne = debut_subdivision_ligne + taille_subdivision - 1
        fin_subdivision_colonne = debut_subdivision_colonne + taille_subdivision - 1
        for i in range(debut_subdivision_ligne, fin_subdivision_ligne+1):
            for j in range(debut_subdivision_colonne, fin_subdivision_colonne+1):
                if l[j][i] == v and (i != x or j != y):
                    return True
        return False

    def valeur_possible(self, l, x, y):
        val_poss = []
        for i in range(1, 10):
            if (not self.doublon_colonne(l, x, y, i) and
                not self.doublon_ligne(l, x, y, i) and
                not self.doublon_sub(l, x, y, i)):
                val_poss.append(i)
        return val_poss

    def nb_solu(self, sudoku):
        self.resoudre(sudoku)
        return self.nb_solutions

    def resoudre(self, sudoku):
        for y in range(len(sudoku)):
            for x in range(len(sudoku)):
                if sudoku[y][x] == 0:
                    tab = self.valeur_possible(sudoku, x, y)
                    for n in tab:
                        sudoku[y][x] = n
                        self.resoudre(sudoku)
                        sudoku[y][x] = 0
                    return
                if x == 8 and y == 8:
                    self.nb_solutions += 1
        print(sudoku)