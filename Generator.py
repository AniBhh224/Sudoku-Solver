from Solver import *
import random
import copy

class Generator:
    def __init__(self):
        self.solver = Solver()

    def genereateur_grille_unsorted(self, N):
        grille = [[0 for i in range(N)] for i in range(N)]
        taille_subdivision = 3
        for i in range(0,N,3):
            for j in range(0,N,3):
                debut_subdivision_ligne = j
                debut_subdivision_colonne = i
                fin_subdivision_ligne = debut_subdivision_ligne + taille_subdivision - 1
                fin_subdivision_colonne = debut_subdivision_colonne + taille_subdivision - 1
                tab = []          
                for p in range(debut_subdivision_colonne, fin_subdivision_colonne+1):
                    for n in range(debut_subdivision_ligne, fin_subdivision_ligne+1):
                        nb_a_placer = random.randint(1, 9)
                        while nb_a_placer in tab :
                            nb_a_placer = random.randint(1, 9)
                        grille[p][n] = nb_a_placer
                        tab.append(nb_a_placer)
        return grille

    
        
    def tri_ligne(self, grille, y, col_trie):
        taille_subdivision = 3
        croise = []
        debut_subdivision_colonne = (y // taille_subdivision) * taille_subdivision
        fin_subdivision_colonne = debut_subdivision_colonne + taille_subdivision - 1
        for i in range(len(grille[0])):
            debut_subdivision_ligne = (i // taille_subdivision) * taille_subdivision
            fin_subdivision_ligne = debut_subdivision_ligne + taille_subdivision - 1
            if grille[y][i]  in croise:
                trouve = False
                j = y+1
                if i not in col_trie:
                    while trouve == False and j <= fin_subdivision_colonne:
                        p = debut_subdivision_ligne
                        while trouve == False and p <= fin_subdivision_ligne:
                            if (grille[j][p] not in croise) and (p not in col_trie) :
                                var = grille[j][p]
                                grille[j][p] = grille[y][i]
                                grille[y][i] = var
                                trouve = True
                                croise.append(grille[y][i])
                            p+=1
                        j+=1
                else:
                    while trouve == False and j <= fin_subdivision_colonne:
                            if (grille[j][i] not in croise):
                                var = grille[j][i]
                                grille[j][i] = grille[y][i]
                                grille[y][i] = var
                                trouve = True
                                croise.append(grille[y][i])
                            j+=1
                        
                    
                if trouve == False:
                    n = 0
                    trouve2 = False
                    while grille[y][n] != grille[y][i]:
                        n+=1
                    debut_subdivision_ligne = (n // taille_subdivision) * taille_subdivision
                    fin_subdivision_ligne = debut_subdivision_ligne + taille_subdivision - 1
                    j = y+1
                    if n not in col_trie:
                        while trouve2 == False and j <= fin_subdivision_colonne:
                            p = debut_subdivision_ligne
                            while trouve2 == False and p <= fin_subdivision_ligne:
                                if (grille[j][p] not in croise) and (p not in col_trie) :
                                    croise.append(grille[j][p])
                                    var = grille[j][p]
                                    grille[j][p] = grille[y][n]
                                    grille[y][n] = var
                                    trouve2 = True
                                    
                                p+=1
                            j+=1
                    else:
                        while trouve2 == False and j <= fin_subdivision_colonne:
                                if (grille[j][n] not in croise):
                                    var = grille[j][n]
                                    grille[j][n] = grille[y][n]
                                    grille[y][n] = var
                                    trouve2 = True
                                    croise.append(grille[y][n])
                                j+=1
                        

                    if trouve2 == False:
                        trouve3 = False
                        c = 0
                        n = 0
                        while grille[y][n] != grille[y][i]:
                            n+=1
                        while trouve3 == False:
                            c+=1
                            if grille[y+1][n] in croise:
                                var = grille[y+1][n]
                                f = 0
                                while grille[y][f] != var :
                                    f+=1 
                                
                                grille[y+1][n] = grille[y][n]
                                grille[y][n] = var
                                n = f
                            else: 
                                var = grille[y+1][n]
                                grille[y+1][n] = grille[y][n]
                                grille[y][n] = var
                                trouve3 = True  
                                croise.append(grille[y][n])
                            if c >= 50:
                                return grille
                            

            else:
                croise.append(grille[y][i])
        return grille 
    


    def tri_colonne(self, grille, x, ligne_trie):
        taille_subdivision = 3
        croise = []
        debut_subdivision_ligne = (x // taille_subdivision) * taille_subdivision
        fin_subdivision_ligne = debut_subdivision_ligne + taille_subdivision - 1
        for i in range(len(grille)):
            debut_subdivision_colonne = (i // taille_subdivision) * taille_subdivision
            fin_subdivision_colonne = debut_subdivision_colonne + taille_subdivision - 1
            if grille[i][x]  in croise:
                trouve = False
                j = x+1
                if i not in ligne_trie:
                    while trouve == False and j <= fin_subdivision_ligne:
                        p = debut_subdivision_colonne
                        while (trouve == False) and (p <= fin_subdivision_colonne):
                            if (p not in ligne_trie) :
                                if grille[p][j] not in croise:
                                    var = grille[p][j]
                                    grille[p][j] = grille[i][x]
                                    grille[i][x] = var
                                    trouve = True
                                    croise.append(grille[i][x])
                                
                            p+=1
                        j+=1
                else:
                    
                    trouve = False
                    while trouve == False and j <= fin_subdivision_ligne:
                            if (grille[i][j] not in croise):
                                var = grille[i][j]
                                grille[i][j] = grille[i][x]
                                grille[i][x] = var
                                trouve = True
                                croise.append(grille[i][x])
                            j+=1
                    
                        
                    
                if trouve == False:
                    n = 0
                    trouve2 = False
                    while grille[n][x] != grille[i][x]:
                        n+=1
                    debut_subdivision_colonne = (n // taille_subdivision) * taille_subdivision
                    fin_subdivision_colonne = debut_subdivision_colonne + taille_subdivision - 1
                    j = x+1
                    if n not in ligne_trie:
                        while trouve2 == False and j <= fin_subdivision_ligne:
                            p = debut_subdivision_colonne
                            while (trouve2 == False) and (p <= fin_subdivision_colonne) :
                                if (p not in ligne_trie) :
                                    if grille[p][j] not in croise:
                                        croise.append(grille[p][j])
                                        var = grille[p][j]
                                        grille[p][j] = grille[n][x]
                                        grille[n][x] = var
                                        trouve2 = True
                                p+=1
                            j+=1
                    else:
                        while trouve2 == False and j <= fin_subdivision_ligne:
                                if (grille[n][j] not in croise):
                                    var = grille[n][j]
                                    grille[n][j] = grille[n][x]
                                    grille[n][x] = var
                                    trouve2 = True
                                    croise.append(grille[n][x])
                                j+=1
                                
                    


                    if trouve2 == False:
                        trouve3 = False
                        c=0
                        n = 0
                        while grille[n][x] != grille[i][x] :
                            n+=1
                        
                        
                        while trouve3 == False:                           
                            if grille[n][x+1] in croise:
                                if c <= 81:
                                    var = grille[n][x+1]
                                    f = 0
                                    while grille[f][x] != var:
                                        f+=1 
                                    
                                    grille[n][x+1] = grille[n][x]
                                    grille[n][x] = var
                                    n = f
                                    c+=1
                                elif x <=6:
                                    grille = self.tri_colonne(grille, x+1, ligne_trie)
                                    grille = self.tri_colonne(grille, x, ligne_trie)
                                    croise = []
                                    for b in range(0, i+1):
                                        croise.append(grille[b][x])
                                    trouve3 = True
                                else: 
                                    trouve3 = True
                                
                                    
                                
                               
                                
                                
                            else: 
                                var = grille[n][x+1]
                                grille[n][x+1] = grille[n][x]
                                grille[n][x] = var
                                trouve3 = True  
                                croise.append(grille[n][x])

                            
                        
            
            else:
                croise.append(grille[i][x])
        return grille 
    


    def is_perfect(self, grille):
        def check_lignes(grille):
            for ligne in grille:
                if sorted(ligne) != list(range(1, 10)):
                    return False
            return True

        def check_colonnes(grille):
            for j in range(9):
                colonne = [grille[i][j] for i in range(9)]
                if sorted(colonne) != list(range(1, 10)):
                    return False
            return True

        def check_subdivisions(grille):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    subdivision = [grille[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if sorted(subdivision) != list(range(1, 10)):
                        return False
            return True

        return check_lignes(grille) and check_colonnes(grille) and check_subdivisions(grille)


    
    def generer(self, N):
        generator = Generator()
        grille = generator.genereateur_grille_unsorted(N)
        ligne_trie = []
        colonne_trie = []
        for i in range(len(grille)):
            grille = generator.tri_ligne(grille, i, colonne_trie)
            ligne_trie.append(i)
            grille = generator.tri_colonne(grille, i, ligne_trie)
            colonne_trie.append(i)
        return grille

    def enlever(self, grille, N, nb):
        grille2 = copy.deepcopy(grille)  # Créer une copie profonde de la grille
        for i in range(nb):
            x, y = random.randint(0, 8), random.randint(0, 8)
            while grille2[y][x] == 0:
                x, y = random.randint(0, 8), random.randint(0, 8)
            grille2[y][x] = 0
        return grille2
    
    def generer_jouable(self, grille, N, niveau):
        solver = Solver()
        reponse_grille = grille
        if niveau == 1:
            a_enlever = random.randint(36, 41)
            grille = self.enlever(reponse_grille, N, a_enlever)
            while Solver().nb_solu(grille) != 1:
                grille = self.enlever(reponse_grille, N, a_enlever)
                

        elif niveau == 2:
            a_enlever = random.randint(41, 45)
            grille = self.enlever(reponse_grille, N, a_enlever)
            while Solver().nb_solu(grille) != 1:
                grille = self.enlever(reponse_grille, N, a_enlever)
        
        elif niveau == 3:
            a_enlever = random.randint(45, 49)
            grille = self.enlever(reponse_grille, N, a_enlever)
            while Solver().nb_solu(grille) != 1:
                grille = self.enlever(reponse_grille, N, a_enlever)
        return grille
    
    def affichier(self, grille):
        for i in range(len(grille)):
            print(grille[i])

generator = Generator()
grille = generator.generer(9)
print(grille)
print(generator.generer_jouable(grille, 9, 1))
