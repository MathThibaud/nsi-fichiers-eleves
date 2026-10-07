# -*- coding: utf-8 -*-
"""
SQUELETTE ELEVE -- Creer des grilles de Sudoku (Terminale NSI, recursivite).

Prerequis : ton solveur de terminale_squelette.py doit etre TERMINE
(tous ses tests passent) : ce fichier reutilise tes fonctions.

Complete les fonctions marquees  # A COMPLETER , dans l'ordre des etapes
de la fiche, puis lance :   python3 generateur_squelette.py
Les tests s'executent etape par etape : une etape pas encore ecrite est
simplement signalee, les suivantes attendent.
"""

import random

from grilles_test import FACILE, COMPLETE_OK, IMPOSSIBLE, afficher
from terminale_squelette import (placement_valide, trouver_case_vide,
                                 grille_complete, grille_valide, resoudre,
                                 copie)


# Une grille a DEUX solutions : COMPLETE_OK dont on a vide 4 cases.
# (Etape 2 : compter_solutions doit y trouver 2 solutions.)
DEUX_SOLUTIONS = copie(COMPLETE_OK)
for (i, j) in [(0, 3), (0, 4), (3, 3), (3, 4)]:
    DEUX_SOLUTIONS[i][j] = 0


def grille_vide():
    """Une grille 9x9 entierement vide (81 zeros)."""
    return [[0] * 9 for _ in range(9)]


def nb_indices(grille):
    """Nombre de cases remplies (les 'indices' donnes au joueur)."""
    nb = 0
    for i in range(9):
        for j in range(9):
            if grille[i][j] != 0:
                nb = nb + 1
    return nb


# ===========================================================================
# ETAPE 1 -- Une grille complete, differente a chaque fois
# ===========================================================================
def resoudre_aleatoire(grille):
    """Comme resoudre, mais essaie les chiffres dans un ordre ALEATOIRE.
    Remplit la grille sur place ; renvoie True si une solution existe."""
    case = trouver_case_vide(grille)
    if case is None:
        return True
    i, j = case
    valeurs = [i for i in range(1, 10)]
    random.shuffle(valeurs)          # on melange l'ordre des essais
    pass  # A COMPLETER : le meme retour sur trace que resoudre,
          #               mais en parcourant la liste 'valeurs'


# ===========================================================================
# ETAPE 2 -- Compter les solutions (au plus 'limite')
# ===========================================================================
def compter_solutions(grille, limite=2):
    """Renvoie le nombre de solutions de la grille, plafonne a 'limite'.
    La grille doit etre rendue INTACTE (chaque case essayee est remise a 0).

      - cas de base : plus de case vide  ->  1 solution
      - sinon, pour chaque chiffre valide : on l'ecrit, on AJOUTE au total
        le nombre de solutions du reste (en ne cherchant que celles qui
        manquent : limite - total), puis on efface TOUJOURS la case
      - des que total == limite : inutile de continuer, on renvoie total
    """
    pass  # A COMPLETER


# ===========================================================================
# ETAPE 3 -- Creuser des trous en gardant une solution unique
# ===========================================================================
def creuser(grille_pleine, indices):
    """Renvoie une NOUVELLE grille obtenue en vidant des cases de grille_pleine
    (qui n'est pas modifiee), tant que la solution reste unique, jusqu'a
    ce qu'il ne reste que 'indices' cases remplies (ou qu'on ne puisse plus)."""
    pass  # A COMPLETER (algorithme de la fiche)


# ===========================================================================
# ETAPE 4 -- Assembler : generer une grille d'un niveau donne
# ===========================================================================
NIVEAUX = {"facile": 40, "moyen": 32, "difficile": 26}   # indices gardes


def generer(niveau):
    """Renvoie le couple (enonce, solution) pour le niveau demande."""
    pass  # A COMPLETER


# ===========================================================================
# Tests, etape par etape -- ne pas modifier
# ===========================================================================
def _pas_ecrite(nom, resultat):
    if resultat is None:
        print(f"  -> {nom} n'est pas encore ecrite (elle renvoie None).")
        return True
    return False


def _lancer(etape):
    """Lance une etape de test : affiche ECHEC (sans planter) si un test echoue."""
    try:
        return etape()
    except AssertionError as erreur:
        print("  ECHEC", erreur)
    except Exception as erreur:
        print("  ECHEC : erreur", repr(erreur))
    return False


def _etape1():
    print("Etape 1 : resoudre_aleatoire")
    g1 = grille_vide()
    r = resoudre_aleatoire(g1)
    if _pas_ecrite("resoudre_aleatoire", r):
        return False
    assert r == True
    assert grille_complete(g1) and grille_valide(g1)
    g2 = grille_vide()
    resoudre_aleatoire(g2)
    assert g1 != g2, "deux appels devraient (presque toujours) differer"
    print("  OK : grilles completes, valides et differentes.")
    return True


def _etape2():
    print("Etape 2 : compter_solutions")
    n = compter_solutions(copie(COMPLETE_OK))
    if _pas_ecrite("compter_solutions", n):
        return False
    assert n == 1                                    # deja pleine : 1 solution
    assert compter_solutions(copie(IMPOSSIBLE)) == 0
    assert compter_solutions(copie(FACILE)) == 1     # un "vrai" Sudoku
    assert compter_solutions(copie(DEUX_SOLUTIONS)) == 2
    assert compter_solutions(grille_vide(), 2) == 2  # s'arrete des 2 trouvees
    assert compter_solutions(grille_vide(), 5) == 5
    g = copie(FACILE)
    compter_solutions(g)
    assert g == FACILE, "compter_solutions doit rendre la grille intacte"
    print("  OK : 0, 1, 2 solutions reconnues, et la grille est rendue intacte.")
    return True


def _etape3():
    print("Etape 3 : creuser")
    pleine = grille_vide()
    resoudre_aleatoire(pleine)
    sauvegarde = copie(pleine)
    enonce = creuser(pleine, 32)
    if _pas_ecrite("creuser", enonce):
        return False
    assert pleine == sauvegarde, "creuser ne doit pas modifier grille_pleine"
    assert nb_indices(enonce) >= 32
    assert compter_solutions(copie(enonce)) == 1     # solution UNIQUE
    for i in range(9):
        for j in range(9):
            assert enonce[i][j] in (0, pleine[i][j])  # indices = ceux de la solution
    print(f"  OK : {nb_indices(enonce)} indices, solution unique.")
    return True


def _etape4():
    print("Etape 4 : generer")
    res = generer("moyen")
    if _pas_ecrite("generer", res):
        return False
    enonce, solution = res
    assert grille_valide(solution) and grille_complete(solution)
    assert compter_solutions(copie(enonce)) == 1
    print("  OK.\n")
    return True


def _afficher_niveaux():
    print("(Patience : le niveau difficile peut prendre jusqu'a une minute.)\n")
    for niveau in NIVEAUX:
        enonce, solution = generer(niveau)
        print(f"Niveau {niveau} ({nb_indices(enonce)} indices) :")
        afficher(enonce)
        print()
    print("Bravo : ton generateur fonctionne !")


if __name__ == "__main__":
    if resoudre(copie(FACILE)) is None:
        print("Termine d'abord ton solveur dans terminale_squelette.py !")
    elif _lancer(_etape1) and _lancer(_etape2) and _lancer(_etape3) and _lancer(_etape4):
        _afficher_niveaux()
