from Solver import * 
from Generator import *


solver = Solver()
sudoku = [[8, 3, 7, 4, 9, 2, 6, 5, 1],
[6, 5, 2, 3, 8, 1, 4, 9, 7],
[4, 1, 9, 5, 7, 6, 3, 2, 8],
[9, 4, 5, 1, 2, 7, 0, 6, 3],
[2, 6, 8, 9, 4, 3, 1, 7, 5],
[1, 7, 3, 6, 5, 8, 2, 4, 9],
[7, 9, 1, 2, 3, 4, 0, 8, 6],
[3, 8, 4, 7, 6, 5, 9, 1, 2],
[5, 2, 6, 8, 1, 9, 7, 3, 4]]
solver.nb_solu(sudoku)


#generator = Generator()
#print(generator.remplir_grille([[0 for i in range(9)] for i in range(9)], 60, 9, 0))
