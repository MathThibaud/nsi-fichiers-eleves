"""Projet Sudoku (Premiere NSI) : verifier une grille.

Fichier eleve : completer les fonctions marquees A COMPLETER.
Lancer le fichier a tout moment : les tests en bas indiquent ce qui marche.
Une grille est un tableau de 9 lignes de 9 entiers ; 0 = case vide.
"""
import random

from sudoku_grilles import FACILE, COMPLETE_OK, DOUBLON_LIGNE, DOUBLON_COLONNE


# ---------------------------------------------------------------
# Exercice 1 : lire une ligne, une colonne et un bloc
# ---------------------------------------------------------------

def valeurs_ligne(grille, i):
    """Renvoie le tableau des 9 valeurs de la ligne i."""
    # A COMPLETER
    return None


def valeurs_colonne(grille, j):
    """Renvoie le tableau des 9 valeurs de la colonne j."""
    # A COMPLETER
    return None


def valeurs_bloc(grille, i, j):
    """Renvoie le tableau des 9 valeurs du bloc 3x3 contenant la case (i, j)."""
    debut_i = (i // 3) * 3
    debut_j = (j // 3) * 3
    valeurs = []
    # A COMPLETER : parcourir les 3 lignes (de debut_i a debut_i+2)
    # et les 3 colonnes (de debut_j a debut_j+2), et ajouter chaque valeur
    return valeurs


# ---------------------------------------------------------------
# Exercice 2 : a-t-on le droit d'ecrire v en (i, j) ?
# ---------------------------------------------------------------

def placement_valide(grille, i, j, v):
    """Renvoie True si ecrire v en (i, j) ne cree aucun doublon
    dans la ligne, la colonne ou le bloc de la case."""
    # A COMPLETER
    return None


# ---------------------------------------------------------------
# Exercice 3 : verifier une grille entiere
# ---------------------------------------------------------------

def grille_complete(grille):
    """Renvoie True si aucune case ne vaut 0."""
    # A COMPLETER
    return None


def grille_valide(grille):
    """Renvoie True si la grille respecte les trois regles
    (aucun doublon en ligne, en colonne, dans un bloc)."""
    # A COMPLETER
    return None


# ---------------------------------------------------------------
# Pour aller plus loin
# ---------------------------------------------------------------

def cases_vides(grille):
    """Renvoie le nombre de cases encore a remplir."""
    # A COMPLETER
    return None


def coups_possibles(grille, i, j):
    """Renvoie le tableau des chiffres que l'on pourrait ecrire en (i, j)."""
    # A COMPLETER
    return None


# ---------------------------------------------------------------
# Exercice 4 (bonus) : le generateur de grilles
# grille_patron, transposer et generer_grille_complete sont fournies.
# ---------------------------------------------------------------

def grille_patron():
    """Renvoie la grille patron, deja correcte."""
    grille = []
    for i in range(9):
        ligne = []
        for j in range(9):
            ligne.append((3 * (i % 3) + i // 3 + j) % 9 + 1)
        grille.append(ligne)
    return grille


def renommer_chiffres(grille):
    """Remplace chaque chiffre selon une permutation tiree au hasard."""
    nouveaux = list(range(1, 10))
    random.shuffle(nouveaux)          # une permutation au hasard
    # A COMPLETER : construire le dictionnaire {1:nouveaux[0], ...}
    # puis renvoyer la grille avec chaque valeur remplacee
    return None


def melanger_lignes(grille):
    """Re-agence les lignes, bande par bande."""
    bandes = [0, 1, 2]
    random.shuffle(bandes)
    resultat = []
    for b in bandes:
        lignes = [b * 3, b * 3 + 1, b * 3 + 2]
        random.shuffle(lignes)
        # A COMPLETER : ajouter grille[indice] a resultat pour chaque indice
    return resultat


def transposer(grille):
    """Echange lignes et colonnes."""
    resultat = []
    for j in range(9):
        ligne = []
        for i in range(9):
            ligne.append(grille[i][j])
        resultat.append(ligne)
    return resultat


def generer_grille_complete():
    """Patron, renommage, melange des lignes, transposition,
    melange des lignes (donc des colonnes), transposition."""
    g = grille_patron()
    g = renommer_chiffres(g)
    g = melanger_lignes(g)
    g = transposer(g)
    g = melanger_lignes(g)
    g = transposer(g)
    return g


# ===============================================================
# TESTS : ne pas modifier. Chaque partie affiche OK ou A FAIRE.
# ===============================================================

def tester_exercice_1():
    assert valeurs_ligne(FACILE, 0) == [5, 3, 0, 0, 7, 0, 0, 0, 0]
    assert valeurs_colonne(FACILE, 0) == [5, 6, 0, 8, 4, 7, 0, 0, 0]
    assert valeurs_bloc(FACILE, 0, 0) == [5, 3, 0, 6, 0, 0, 0, 9, 8]


def tester_exercice_2():
    assert placement_valide(FACILE, 0, 2, 4) == True
    assert placement_valide(FACILE, 0, 2, 5) == False
    assert placement_valide(FACILE, 0, 2, 8) == False


def tester_exercice_3():
    assert grille_complete(FACILE) == False
    assert grille_complete(COMPLETE_OK) == True
    assert grille_valide(COMPLETE_OK) == True
    assert grille_valide(DOUBLON_LIGNE) == False
    assert grille_valide(DOUBLON_COLONNE) == False


def tester_plus_loin():
    assert cases_vides(FACILE) == 51
    assert coups_possibles(FACILE, 0, 2) == [1, 2, 4]


def tester_bonus():
    for k in range(50):
        g = generer_grille_complete()
        assert grille_complete(g) == True
        assert grille_valide(g) == True


def lancer(nom, test):
    try:
        test()
        print("[OK]      ", nom)
    except Exception:
        print("[A FAIRE] ", nom)


lancer("Exercice 1 : lire ligne, colonne, bloc", tester_exercice_1)
lancer("Exercice 2 : placement_valide", tester_exercice_2)
lancer("Exercice 3 : grille_complete et grille_valide", tester_exercice_3)
lancer("Pour aller plus loin : cases_vides, coups_possibles", tester_plus_loin)
lancer("Exercice 4 (bonus) : generateur de grilles", tester_bonus)
