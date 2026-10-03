# -*- coding: utf-8 -*-
"""
TP de fin de chapitre "Calculabilite et decidabilite" (Terminale NSI).

Fichier de depart. Completer les parties marquees  A COMPLETER,
puis lancer le fichier : les tests indiquent ce qui fonctionne.

  Partie 1-2 : un simulateur de machine de Turing, et des machines a ecrire ;
  Partie 3   : trouver ou verifier ? (le probleme du sous-ensemble de somme) ;
  Partie 4   : une experience sur l'arret (la suite de Syracuse).
"""

import itertools
import random
import time

# =====================================================================
#  PARTIE 1 -- LE SIMULATEUR
# =====================================================================
# Le ruban est un dictionnaire  position -> symbole  (une case absente
# contient le symbole blanc). Une machine est un dictionnaire de regles :
#     (etat, symbole_lu) -> (symbole_ecrit, deplacement, nouvel_etat)
# avec deplacement = "G" (gauche) ou "D" (droite).
# La machine demarre dans l'etat "q0", la tete sur la case 0 (premier
# symbole du mot), et s'arrete des qu'elle entre dans un etat final.

BLANC = "_"
ETATS_FINAUX = ("fin", "oui", "non")


def ruban_initial(mot):
    """Ruban contenant le mot a partir de la case 0."""
    ruban = {}
    for i in range(len(mot)):
        ruban[i] = mot[i]
    return ruban


def lire_ruban(ruban):
    """Le contenu du ruban, sans les blancs du debut et de la fin."""
    cases = [i for i in ruban if ruban[i] != BLANC]
    if cases == []:
        return ""
    contenu = ""
    for i in range(min(cases), max(cases) + 1):
        contenu = contenu + ruban.get(i, BLANC)
    return contenu


def afficher_config(ruban, tete, etat):
    """Affiche l'etat, le ruban, et un ^ sous la case lue."""
    debut = min(min(ruban), tete)
    fin = max(max(ruban), tete)
    ligne = ""
    for i in range(debut, fin + 1):
        ligne = ligne + ruban.get(i, BLANC)
    print(f"{etat:>9} | {ligne}")
    print(" " * 12 + " " * (tete - debut) + "^")


def une_etape(regles, ruban, tete, etat):
    """A COMPLETER.
    Applique UNE regle : lit le symbole sous la tete, ecrit, deplace la tete.
    Modifie ruban et renvoie le couple (nouvelle_position, nouvel_etat)."""
    lu = ruban.get(tete, BLANC)
    ...


def executer(regles, mot, limite=10000, trace=False):
    """Fait tourner la machine sur le mot. Renvoie :
       - (etat_final, contenu_du_ruban, nombre_d_etapes) si elle s'arrete ;
       - ("bloquee", contenu, etapes) si aucune regle ne s'applique ;
       - None si elle n'est pas arretee apres limite etapes."""
    ruban = ruban_initial(mot)
    tete = 0
    etat = "q0"
    etapes = 0
    while etat not in ETATS_FINAUX:
        if etapes == limite:
            return None
        if (etat, ruban.get(tete, BLANC)) not in regles:
            return ("bloquee", lire_ruban(ruban), etapes)
        if trace:
            afficher_config(ruban, tete, etat)
        tete, etat = une_etape(regles, ruban, tete, etat)
        etapes = etapes + 1
    if trace:
        afficher_config(ruban, tete, etat)
    return (etat, lire_ruban(ruban), etapes)


# --- Machine fournie : inverser les bits d'un mot binaire
INVERSER = {
    ("q0", "0"): ("1", "D", "q0"),
    ("q0", "1"): ("0", "D", "q0"),
    ("q0", BLANC): (BLANC, "G", "fin"),
}

# --- Une machine qui ne s'arrete jamais
FUITE = {
    ("q0", "1"): ("1", "D", "q0"),
    ("q0", BLANC): (BLANC, "D", "q0"),
}

# =====================================================================
#  PARTIE 2 -- PROGRAMMER DES MACHINES   (A COMPLETER)
# =====================================================================

# Ajouter 1 a un nombre ecrit en binaire : "1011" -> "1100"
INCREMENT = {
}

# Le mot binaire contient-il un nombre PAIR de 1 ? (etat final "oui" / "non")
PARITE = {
}

# Le mot (lettres a et b) est-il un palindrome ? (etat final "oui" / "non")
PALINDROME = {
    # q0 : effacer le premier symbole, et partir a droite en s'en souvenant
    ("q0", "a"): (BLANC, "D", "cherche_a"),
    ("q0", "b"): (BLANC, "D", "cherche_b"),
    ("q0", BLANC): (BLANC, "D", "oui"),        # plus rien a comparer
    # aller au bout du mot sans rien modifier
    ("cherche_a", "a"): ("a", "D", "cherche_a"),
    ("cherche_a", "b"): ("b", "D", "cherche_a"),
    ("cherche_a", BLANC): (BLANC, "G", "compare_a"),
    ("cherche_b", "a"): ("a", "D", "cherche_b"),
    ("cherche_b", "b"): ("b", "D", "cherche_b"),
    ("cherche_b", BLANC): (BLANC, "G", "compare_b"),
    # A COMPLETER : etats compare_a, compare_b, retour
}


# =====================================================================
#  PARTIE 3 -- TROUVER OU VERIFIER ?
# =====================================================================

def verifier(nombres, cible, choix):
    """A COMPLETER. choix est une liste d'indices de nombres.
    Renvoie True si ces indices sont tous differents et si les nombres
    correspondants ont pour somme cible."""
    ...


def sous_ensemble(k, n):
    """Le k-ieme sous-ensemble des indices 0..n-1 : l'indice i est choisi
    si le bit numero i de k vaut 1. Ex. : sous_ensemble(13, 4) -> [0, 2, 3]
    car 13 s'ecrit 1101 en binaire."""
    return [i for i in range(n) if (k // 2 ** i) % 2 == 1]


def chercher(nombres, cible):
    """A COMPLETER. Force brute : essaie TOUS les sous-ensembles.
    Renvoie le couple (choix, nombre_d_essais), avec choix = None
    si aucun sous-ensemble ne convient."""
    ...


def chronometrer(fonction, *arguments):
    """Duree (en secondes) de l'appel fonction(*arguments)."""
    debut = time.perf_counter()
    fonction(*arguments)
    return time.perf_counter() - debut


def mesures(tailles):
    """Pour chaque taille n : n nombres PAIRS au hasard et une cible
    IMPAIRE (donc aucune solution : la recherche essaie tout)."""
    random.seed(1)
    for n in tailles:
        nombres = [2 * random.randint(1, 50) for _ in range(n)]
        duree = chronometrer(chercher, nombres, 101)
        print(f"n = {n:2}   essais = {2 ** n:>9}   duree = {duree:.3f} s")


# =====================================================================
#  PARTIE 4 -- UNE EXPERIENCE SUR L'ARRET
# =====================================================================

def syracuse_etapes(n, limite):
    """A COMPLETER. Nombre d'etapes pour que la suite de Syracuse partant
    de n atteigne 1 (n pair -> n // 2, n impair -> 3 * n + 1),
    ou None si 1 n'est pas atteint en limite etapes."""
    ...


# =====================================================================
#  TESTS
# =====================================================================

def test_une_etape():
    assert executer(INVERSER, "1011")[1] == "0100"


def test_increment():
    for n in range(300):
        assert executer(INCREMENT, bin(n)[2:])[:2] == ("fin", bin(n + 1)[2:])


def test_parite():
    for n in range(300):
        mot = bin(n)[2:]
        if mot.count("1") % 2 == 0:
            attendu = "oui"
        else:
            attendu = "non"
        assert executer(PARITE, mot)[0] == attendu


def test_palindrome():
    for longueur in range(9):
        for lettres in itertools.product("ab", repeat=longueur):
            mot = "".join(lettres)
            if mot == mot[::-1]:
                attendu = "oui"
            else:
                attendu = "non"
            assert executer(PALINDROME, mot)[0] == attendu, mot


def test_sous_ensemble_somme():
    nombres = [8, 3, 12, 5, 7]
    assert verifier(nombres, 20, [0, 2]) is True
    assert verifier(nombres, 20, [1, 4]) is False
    assert verifier(nombres, 16, [0, 0]) is False      # indice repete
    choix, essais = chercher(nombres, 15)
    assert verifier(nombres, 15, choix)
    assert chercher(nombres, 100) == (None, 32)


def test_syracuse():
    assert syracuse_etapes(1, 10) == 0
    assert syracuse_etapes(6, 100) == 8
    assert syracuse_etapes(27, 100) is None


def tester():
    for test in (test_une_etape, test_increment, test_parite, test_palindrome,
                 test_sous_ensemble_somme, test_syracuse):
        try:
            test()
            print(test.__name__, ": OK")
        except Exception as erreur:
            print(test.__name__, ": ECHEC (", type(erreur).__name__, erreur, ")")


if __name__ == "__main__":
    tester()
