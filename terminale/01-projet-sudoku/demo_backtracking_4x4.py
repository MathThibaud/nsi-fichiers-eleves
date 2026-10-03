# -*- coding: utf-8 -*-
"""
DEMO -- le retour sur trace en direct, sur une mini-grille 4x4.

But : VOIR le backtracking. On resout un Sudoku 4x4 (chiffres 1 a 4,
blocs 2x2) en affichant chaque essai et chaque retour en arriere.
A lancer tel quel :   python3 demo_backtracking_4x4.py

Rien a completer ici : ce fichier sert d'illustration avant d'ecrire
soi-meme le solveur 9x9 (voir terminale_squelette.py).
"""

# Mini-grille de depart (0 = case vide) :
#     1 . | . .
#     . . | . 2
#     ----+----
#     3 . | . .
#     . . | . 4
GRILLE_4x4 = [
    [1, 0, 0, 0],
    [0, 0, 0, 2],
    [3, 0, 0, 0],
    [0, 0, 0, 4],
]

nb_retours = 0     # compteur de retours en arriere (pour le bilan)


def placement_valide(grille, i, j, v):
    """True si ecrire v en (i, j) ne cree pas de doublon (ligne, colonne, bloc 2x2)."""
    for k in range(4):
        if grille[i][k] == v or grille[k][j] == v:
            return False
    di = (i // 2) * 2
    dj = (j // 2) * 2
    for a in range(di, di + 2):
        for b in range(dj, dj + 2):
            if grille[a][b] == v:
                return False
    return True


def trouver_case_vide(grille):
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                return (i, j)
    return None


def resoudre_bavard(grille, profondeur=0):
    """Comme le solveur 9x9, mais il RACONTE ce qu'il fait."""
    global nb_retours
    marge = "    " * profondeur
    case = trouver_case_vide(grille)
    if case is None:
        print(marge + "=> grille complete !")
        return True
    i, j = case
    for v in range(1, 5):
        if placement_valide(grille, i, j, v):
            grille[i][j] = v
            print(marge + f"-> j'ecris {v} en ({i},{j})")
            if resoudre_bavard(grille, profondeur + 1):
                return True
            grille[i][j] = 0
            nb_retours += 1
            print(marge + f"X  j'efface {v} en ({i},{j})   (retour n{nb_retours})")
    # aucun chiffre n'a marche ici : impasse, on rend la main a la case precedente
    return False


if __name__ == "__main__":
    print("Resolution pas a pas d'un Sudoku 4x4 :\n")
    resoudre_bavard([ligne[:] for ligne in GRILLE_4x4])
    print(f"\nNombre total de retours en arriere : {nb_retours}")
