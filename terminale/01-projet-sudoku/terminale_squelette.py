# -*- coding: utf-8 -*-
"""
SQUELETTE ELEVE -- activite Sudoku (Terminale NSI, recursivite).

Complete les fonctions marquees  # A COMPLETER , puis lance ce fichier :
    python3 terminale_squelette.py
Les tests en bas affichent OK, ou A FAIRE ou ECHEC : ils doivent tous finir en OK.

Ordre de travail (guide dans la fiche) :
* PARTIES 1 et 2 : lire dans la grille, puis placement_valide et la
  verification (tu peux t'inspirer de ce que tu as fait en Premiere) ;
* PARTIE 3 : le solveur recursif (le coeur de l'activite).
"""

from grilles_test import (FACILE, MINI, SOLUTION_MINI, COMPLETE_OK,
                          DOUBLON_LIGNE, DOUBLON_COLONNE, DIFFICILE, IMPOSSIBLE)


# ===========================================================================
# 1. Lire dans la grille  (rappel de Premiere -- a reecrire)
# ===========================================================================
def valeurs_ligne(grille, i):
    """Renvoie la liste des 9 valeurs de la ligne i."""
    pass  # A COMPLETER


def valeurs_colonne(grille, j):
    """Renvoie la liste des 9 valeurs de la colonne j.
    A ecrire par comprehension (collecter grille[i][j] pour i de 0 a 8)."""
    pass  # A COMPLETER


def valeurs_bloc(grille, i, j):
    """Renvoie les 9 valeurs du bloc 3x3 contenant la case (i, j).
    Astuce : le coin haut-gauche du bloc est ((i//3)*3, (j//3)*3)."""
    pass  # A COMPLETER


# ===========================================================================
# 2. Verifier  (rappel de Premiere -- a reecrire)
# ===========================================================================
def placement_valide(grille, i, j, v):
    """True si ecrire v en (i, j) ne cree aucun doublon (ligne, colonne, bloc)."""
    pass  # A COMPLETER


def grille_complete(grille):
    """True s'il ne reste aucune case vide (aucun 0)."""
    pass  # A COMPLETER


def grille_valide(grille):
    """True si une grille REMPLIE respecte les trois regles.
    Astuce : pour tester une case, retire sa valeur, teste, puis remets-la."""
    pass  # A COMPLETER


# ===========================================================================
# 3. Resoudre : le retour sur trace (backtracking)  <-- le coeur de l'activite
# ===========================================================================
def trouver_case_vide(grille):
    """Renvoie (i, j) de la premiere case vide, ou None s'il n'y en a plus."""
    pass  # A COMPLETER


def resoudre(grille):
    """Remplit la grille SUR PLACE. Renvoie True si une solution existe.

    Les trois idees a coder :
      - cas de base : plus de case vide  ->  return True
      - pour chaque chiffre v de 1 a 9 valide : on l'ecrit, puis appel recursif
      - si l'appel recursif echoue : on efface (grille[i][j] = 0)  <- LE RETOUR
    """
    pass  # A COMPLETER


# ---------------------------------------------------------------------------
def copie(grille):
    """Copie independante d'une grille (utile pour ne pas abimer les grilles de test)."""
    return [[v for v in ligne] for ligne in grille]


# ===========================================================================
# Jeux de tests -- chaque test affiche OK, ou A FAIRE ou ECHEC (ne pas modifier)
# ===========================================================================
def test_lire():
    return (valeurs_ligne(FACILE, 0) == [5, 3, 0, 0, 7, 0, 0, 0, 0]
            and valeurs_colonne(FACILE, 0) == [5, 6, 0, 8, 4, 7, 0, 0, 0]
            and valeurs_bloc(FACILE, 0, 0) == [5, 3, 0, 6, 0, 0, 0, 9, 8])


def test_placement_valide():
    return (placement_valide(FACILE, 0, 2, 4) == True
            and placement_valide(FACILE, 0, 2, 5) == False    # 5 deja dans la ligne
            and placement_valide(FACILE, 0, 2, 8) == False)   # 8 deja dans le bloc


def test_grille_complete():
    return grille_complete(COMPLETE_OK) == True and grille_complete(FACILE) == False


def test_grille_valide():
    return (grille_valide(COMPLETE_OK) == True
            and grille_valide(DOUBLON_LIGNE) == False
            and grille_valide(DOUBLON_COLONNE) == False)


def test_trouver_case_vide():
    return trouver_case_vide(FACILE) == (0, 2) and trouver_case_vide(COMPLETE_OK) is None


def test_resoudre():
    g = copie(MINI)
    if not (resoudre(g) == True and g == SOLUTION_MINI):
        return False
    if resoudre(copie(FACILE)) != True or resoudre(copie(DIFFICILE)) != True:
        return False
    return resoudre(copie(IMPOSSIBLE)) == False      # pas de solution, et ca s'arrete


def lancer(nom, test):
    """Lance un test sans planter si la fonction n'est pas encore ecrite."""
    try:
        ok = test()
    except Exception:
        ok = False
    if ok:
        print(nom, ": OK")
    else:
        print(nom, ": A FAIRE ou ECHEC")
    return ok


def tous_les_tests():
    """Lance tous les tests ; renvoie True s'ils passent tous."""
    resultats = [lancer("1. valeurs_ligne / colonne / bloc", test_lire),
                 lancer("2. placement_valide", test_placement_valide),
                 lancer("2. grille_complete", test_grille_complete),
                 lancer("2. grille_valide", test_grille_valide),
                 lancer("3. trouver_case_vide", test_trouver_case_vide),
                 lancer("3. resoudre", test_resoudre)]
    return False not in resultats


if __name__ == "__main__":
    if tous_les_tests():
        print("Bravo : tous les tests passent !")
