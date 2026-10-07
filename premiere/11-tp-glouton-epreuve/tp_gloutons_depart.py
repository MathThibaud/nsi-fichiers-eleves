"""TP de fin de chapitre "Algorithmes gloutons" -- Le glouton a l'epreuve.

Trois problemes d'optimisation : pour chacun, on programme un algorithme
glouton, on calcule la VRAIE meilleure solution en essayant tout (force
brute, possible seulement sur de petites tailles), et on MESURE l'ecart.

Completer les fonctions dans l'ordre du TP (remplacer les ...), puis lancer
le programme : en bas du fichier, chaque partie est testee et affiche
[OK] ou [A FAIRE]. Au debut, tout est A FAIRE : c'est normal.
"""

import math
import random
import time
import itertools


# ============================================ Partie 1 : rendu de monnaie
def rendu_glouton(systeme, somme):
    """Nombre de pieces rendues par le glouton (systeme trie du plus grand
    au plus petit), ou None si le glouton n'arrive pas a rendre la somme."""
    n = 0
    for p in systeme:
        while somme >= p:
            somme = somme - p
            n = n + 1
    if somme != 0:
        return None
    return n


def optimal3(systeme, somme):
    """VRAI nombre minimal de pieces pour un systeme de 3 pieces [p1, p2, p3]
    (force brute : on essaie tous les nombres a de pieces p1 et b de pieces
    p2), ou None si la somme ne peut pas etre rendue."""
    p1, p2, p3 = systeme
    meilleur = None
    for a in range(somme // p1 + 1):
        for b in range(...):
            ...
    return meilleur


def premier_contre_exemple(systeme, smax):
    """Plus petite somme de 1 a smax pour laquelle le glouton ne donne pas
    le nombre optimal de pieces, ou None s'il n'y en a pas."""
    ...


# ============================================ Partie 2 : sac a dos
# un objet = (nom, poids en kg, interet en points)
OBJETS = [("tente", 4, 75), ("duvet", 2, 60), ("réchaud", 2, 30),
          ("nourriture", 3, 70), ("trousse de secours", 1, 40),
          ("gourde de 2 L", 2, 55), ("appareil photo", 1, 25),
          ("jumelles", 1, 10), ("doudoune", 2, 45), ("livre", 1, 5)]
CAPACITE = 10


def interet(objet):
    return objet[2]


def poids(objet):
    return objet[1]


def rapport(objet):
    ...


def sac_glouton(objets, capacite, critere, decroissant):
    """Remplit le sac en prenant les objets dans l'ordre du critere
    (decroissant ou non), tant qu'ils rentrent. Renvoie (liste des noms
    pris, poids total, interet total)."""
    pris = []
    poids_total = 0
    interet_total = 0
    for objet in sorted(objets, key=critere, reverse=decroissant):
        ...
    return pris, poids_total, interet_total


def sac_optimal(objets, capacite):
    """Force brute : essaie les 2**n sous-ensembles. Le nombre k, ecrit en
    binaire sur n bits, dit quels objets on prend (bit i = 1 : objet i pris).
    Renvoie (liste des noms pris, poids total, interet total)."""
    n = len(objets)
    meilleur = ([], 0, 0)
    for k in range(2 ** n):
        pris = []
        poids_total = 0
        interet_total = 0
        for i in range(n):
            if (k // 2 ** i) % 2 == 1:      # le bit i de k vaut 1
                ...
        ...
    return meilleur


def objets_au_hasard(n):
    """n objets de poids 1 a 6 kg et d'interet 5 a 100 points."""
    return [("objet" + str(i), random.randint(1, 6), 5 * random.randint(1, 20))
            for i in range(n)]


# ============================================ Partie 3 : voyageur de commerce
# coordonnees en km (x vers l'est, y vers le nord), origine : Monaco
VILLES = {"Monaco": (0.0, 0.0), "Menton": (5.9, 4.0), "Sospel": (2.0, 15.4),
          "Eze": (-5.1, -1.1), "Nice": (-13.1, -3.1), "Vence": (-25.2, -1.8),
          "Grasse": (-40.3, -8.8), "Cannes": (-32.8, -20.5),
          "Antibes": (-24.1, -17.4), "Saint-Martin-Vesubie": (-13.6, 36.5)}


def distance(v1, v2):
    """Distance a vol d'oiseau (km) entre deux villes de VILLES."""
    x1, y1 = VILLES[v1]
    x2, y2 = VILLES[v2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def longueur(tournee):
    """Longueur d'une tournee qui REVIENT a son point de depart."""
    ...


def plus_proche_voisin(depart, villes):
    """Tournee gloutonne : depuis depart, aller toujours vers la ville
    non visitee la plus proche."""
    tournee = [depart]
    a_visiter = [v for v in villes if v != depart]
    while len(a_visiter) > 0:
        ...
    return tournee


def tournee_optimale(depart, villes):
    """Force brute : essaie tous les ordres possibles des autres villes."""
    autres = [v for v in villes if v != depart]
    meilleure = None
    for ordre in itertools.permutations(autres):
        tournee = [depart] + [v for v in ordre]
        ...
    return meilleure


# ============================================ Tests (ne pas modifier)
def test_partie1():
    assert rendu_glouton([10, 6, 1], 12) == 3
    assert rendu_glouton([3, 2], 4) is None
    assert optimal3([10, 6, 1], 12) == 2
    assert optimal3([5, 2, 1], 9) == 3
    assert optimal3([6, 4, 2], 7) is None
    assert premier_contre_exemple([10, 6, 1], 100) == 12
    assert premier_contre_exemple([5, 2, 1], 100) is None


def test_partie2():
    assert sac_glouton(OBJETS, CAPACITE, interet, True)[2] == 245
    assert sac_optimal(OBJETS, CAPACITE)[2] == 270
    assert sac_optimal([("a", 3, 10), ("b", 2, 7), ("c", 2, 6)], 4)[2] == 13


def test_partie3():
    assert round(distance("Monaco", "Menton"), 1) == 7.1
    assert round(longueur(["Monaco", "Menton", "Sospel"]), 1) == 34.7
    assert plus_proche_voisin("Monaco", VILLES)[:3] == ["Monaco", "Eze", "Nice"]


# ============================================ Lancement des tests (ne pas modifier)
def lancer(nom, test):
    try:
        test()
        print("[OK]      ", nom)
    except Exception:
        print("[A FAIRE] ", nom)


lancer("Partie 1 : rendu de monnaie", test_partie1)
lancer("Partie 2 : sac a dos", test_partie2)
lancer("Partie 3 : voyageur de commerce", test_partie3)
