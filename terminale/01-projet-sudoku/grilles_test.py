# -*- coding: utf-8 -*-
"""
Grilles de test pour l'activite Sudoku (Terminale NSI -- recursivite).

Convention : un Sudoku 9x9 = une liste de 9 listes de 9 entiers.
             une case vide vaut 0 ; les valeurs vont de 1 a 9.
             acces : grille[i][j]  (i = ligne, j = colonne, indices 0 a 8).

Ce fichier ne contient QUE des donnees : on l'importe depuis les autres
fichiers avec, par exemple :   from grilles_test import FACILE
"""

# ---------------------------------------------------------------------------
# Grille facile classique (fil rouge de l'activite)
# ---------------------------------------------------------------------------
FACILE = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],
    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],
    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9],
]

# ---------------------------------------------------------------------------
# Grille tres facile (peu de trous) : sert de premier test au solveur.
# Sa solution unique est SOLUTION_MINI (ci-dessous).
# ---------------------------------------------------------------------------
MINI = [
    [0,3,4, 6,0,8, 9,1,2],
    [6,7,2, 0,9,5, 3,4,8],
    [1,9,8, 3,4,2, 5,0,7],
    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,0,3, 7,9,1],
    [7,1,3, 9,2,0, 8,5,6],
    [9,6,1, 5,3,7, 2,8,4],
    [2,0,7, 4,1,9, 6,3,5],
    [3,4,5, 2,8,6, 1,7,0],
]

# ---------------------------------------------------------------------------
# Une grille COMPLETE et correcte (aucune regle violee).
# C'est aussi la solution de MINI et de FACILE.
# ---------------------------------------------------------------------------
COMPLETE_OK = [
    [5,3,4, 6,7,8, 9,1,2],
    [6,7,2, 1,9,5, 3,4,8],
    [1,9,8, 3,4,2, 5,6,7],
    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,5,3, 7,9,1],
    [7,1,3, 9,2,4, 8,5,6],
    [9,6,1, 5,3,7, 2,8,4],
    [2,8,7, 4,1,9, 6,3,5],
    [3,4,5, 2,8,6, 1,7,9],
]

SOLUTION_MINI = COMPLETE_OK          # meme grille resolue

# ---------------------------------------------------------------------------
# Grilles COMPLETES mais FAUSSES (pour tester grille_valide).
# ---------------------------------------------------------------------------
# Un 5 en trop sur la premiere ligne (cases (0,0) et (0,8)).
DOUBLON_LIGNE = [
    [5,3,4, 6,7,8, 9,1,5],
    [6,7,2, 1,9,5, 3,4,8],
    [1,9,8, 3,4,2, 5,6,7],
    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,5,3, 7,9,1],
    [7,1,3, 9,2,4, 8,5,6],
    [9,6,1, 5,3,7, 2,8,4],
    [2,8,7, 4,1,9, 6,3,5],
    [3,4,5, 2,8,6, 1,7,9],
]

# Un 5 en trop sur la premiere colonne (cases (0,0) et (8,0)).
DOUBLON_COLONNE = [
    [5,3,4, 6,7,8, 9,1,2],
    [6,7,2, 1,9,5, 3,4,8],
    [1,9,8, 3,4,2, 5,6,7],
    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,5,3, 7,9,1],
    [7,1,3, 9,2,4, 8,5,6],
    [9,6,1, 5,3,7, 2,8,4],
    [2,8,7, 4,1,9, 6,3,5],
    [5,4,5, 2,8,6, 1,7,9],
]

# ---------------------------------------------------------------------------
# Grille difficile (peu d'indices, mais solution unique).
# ---------------------------------------------------------------------------
DIFFICILE = [
    [8,0,0, 0,0,0, 0,0,0],
    [0,0,3, 6,0,0, 0,0,0],
    [0,7,0, 0,9,0, 2,0,0],
    [0,5,0, 0,0,7, 0,0,0],
    [0,0,0, 0,4,5, 7,0,0],
    [0,0,0, 1,0,0, 0,3,0],
    [0,0,1, 0,0,0, 0,6,8],
    [0,0,8, 5,0,0, 0,1,0],
    [0,9,0, 0,0,0, 4,0,0],
]

# ---------------------------------------------------------------------------
# Grille SANS solution : la seule case vide (0,0) ne peut recevoir aucun
# chiffre (le 5 dont elle a besoin est deja present dans sa colonne).
# resoudre doit renvoyer False -- et s'arreter tout de suite.
# ---------------------------------------------------------------------------
IMPOSSIBLE = [
    [0,3,4, 6,7,8, 9,1,2],
    [5,7,2, 1,9,5, 3,4,8],
    [1,9,8, 3,4,2, 5,6,7],
    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,5,3, 7,9,1],
    [7,1,3, 9,2,4, 8,5,6],
    [9,6,1, 5,3,7, 2,8,4],
    [2,8,7, 4,1,9, 6,3,5],
    [3,4,5, 2,8,6, 1,7,9],
]


def afficher(grille):
    """Affiche une grille 9x9 lisiblement (le 0 devient un point)."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        ligne = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                ligne += "| "
            c = grille[i][j]
            if c == 0:
                ligne += ". "
            else:
                ligne += str(c) + " "
        print(ligne)


if __name__ == "__main__":
    print("Grille FACILE :")
    afficher(FACILE)
