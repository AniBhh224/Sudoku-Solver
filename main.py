from Solver import * 
from Generator import *

generator = Generator()
solver = Solver()
sudoku = generator.generer(9)



#generator = Generator()
#print(generator.remplir_grille([[0 for i in range(9)] for i in range(9)], 60, 9, 0))
