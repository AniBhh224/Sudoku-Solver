from Solver import *
import random

class Generator:
    def __init__(self):
        self.solver = Solver()

    def remplir_grille(self, nb, N):
            grille = [[0 for i in range(N)] for i in range(N)]
            cases_libres = [(i, j) for i in range(N) for j in range(N) if (i, j) ]
            for i in range(nb):
                p = 0
                if cases_libres:
                    x, y = random.choice(cases_libres)
                    nb_a_placer = random.randint(1, 9)
                    while nb_a_placer not in self.solver.valeur_possible(grille, x, y):
                        if nb_a_placer not in self.solver.valeur_possible(grille, x, y):
                            nb_a_placer = random.randint(1, 9)
                            p += 1
                        if  p > 1000:
                            return (grille, "Case",x,y, grille[y][x])
                            x, y = random.choice(cases_libres)
                    grille[y][x] = nb_a_placer
                    cases_libres.remove((x, y))
            return grille

    def generateur(self, N, niveau):
            if niveau == 1:
                nb = 81
                grille = self.remplir_grille(nb, N)
                print(self.solver.nb_solu(grille))
                while self.solver.nb_solu(grille) <= 1:
                    grille = [[0 for i in range(N)] for i in range(N)]
                    grille = self.remplir_grille(grille, nb, N)
                    print(self.solver.nb_solu(grille))
            return grille


# Exemple d'utilisation
generator = Generator()
print(generator.remplir_grille(70, 9,))
