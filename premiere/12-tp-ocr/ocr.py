"""
Reconnaissance de chiffres et de lettres manuscrits par les k plus proches voisins.
1re NSI - activite guidee OCR.  TRAME a completer au fil de la fiche.

Ce fichier contient :
  - les fonctions FOURNIES (charger, afficher, grille_vers_vecteur) : ne pas les modifier ;
  - les fonctions A COMPLETER : remplacer chaque ... par votre code,
    en suivant les trous (a), (b), (c), (d), (e) de la fiche ;
  - des TESTS, en bas du fichier : chaque etape affiche [OK] ou [A FAIRE].
    Au debut, tout est A FAIRE : c'est normal.

Donnees (a placer dans le meme dossier) :
    chiffres_train.csv / chiffres_test.csv   -> vrais chiffres manuscrits (MNIST)
    lettres_train.csv  / lettres_test.csv    -> vraies lettres manuscrites (EMNIST)

    python3 ocr.py
"""

import csv

TAILLE = 14   # les images font 14 x 14 pixels


# =====================================================================
#  Charger les donnees (fourni)
# =====================================================================

def charger(fichier):
    """Renvoie une liste de couples (pixels, etiquette).
    pixels est une liste de 196 entiers (0 ou 1) ; etiquette une chaine."""
    donnees = []
    with open(fichier, encoding="utf-8", newline="") as f:
        lecteur = csv.reader(f)
        next(lecteur)                        # sauter la ligne d'en-tete
        for ligne in lecteur:
            etiquette = ligne[0]
            pixels = [int(v) for v in ligne[1:]]
            donnees.append((pixels, etiquette))
    return donnees


# =====================================================================
#  Le coeur du k-NN (partie 1) : A COMPLETER
# =====================================================================

def distance(a, b):
    """somme des ecarts au carre, coordonnee par coordonnee"""
    s = 0
    for i in range(len(a)):
        s = s + ...          # (a) A COMPLETER : l'ecart au carre sur la coordonnee i
    return s


def k_plus_proches(exemples, x, k):
    """Classes des k exemples les plus proches de x."""
    dists = []
    for descripteurs, classe in exemples:
        dists.append((..., classe))           # (b) A COMPLETER : distance de x a cet exemple
    dists.sort(key=lambda couple: ...)        # (c) A COMPLETER : trier par la distance
    return [classe for (d, classe) in dists[:k]]


def vote(classes):
    """Classe la plus frequente dans la liste."""
    compte = {}
    for c in classes:
        compte[c] = ...      # (d) A COMPLETER : ajouter 1 au compteur de c
    meilleure = None
    for c in compte:
        if meilleure is None or compte[c] > compte[meilleure]:
            meilleure = c
    return meilleure


def classer(exemples, x, k):
    """Classe de x par vote de ses k plus proches voisins (voir 1.6)."""
    # A COMPLETER
    return None


def taux_reussite(exemples, tests, k, limite=100):
    """Proportion des limite premieres images de test bien classees."""
    tests = tests[:limite]
    bons = 0
    for pixels, vraie in tests:
        if ...:              # (e) A COMPLETER : la prediction est-elle correcte ?
            bons = bons + 1
    return bons / len(tests)


# =====================================================================
#  Outils fournis : voir ce que la machine voit
# =====================================================================

def afficher(pixels):
    """Affiche une image en art ASCII (# = encre, . = blanc)."""
    for l in range(TAILLE):
        ligne = ""
        for c in range(TAILLE):
            if pixels[l * TAILLE + c] == 1:
                ligne = ligne + "#"     # encre
            else:
                ligne = ligne + "."     # blanc
        print(ligne)


def grille_vers_vecteur(grille):
    """Transforme une grille dessinee a la main (14 chaines de 14 caracteres,
    '#' = encre) en une liste de 196 pixels."""
    pixels = []
    for ligne in grille:
        for c in ligne:
            if c in "#1X*":
                pixels.append(1)     # encre
            else:
                pixels.append(0)     # blanc
    return pixels


# =====================================================================
#  Tests (ne pas modifier)
# =====================================================================

EXEMPLES = [([1, 1], "A"), ([2, 1], "A"), ([5, 4], "B"), ([6, 5], "B")]


def test_distance():
    assert distance([1, 1], [2, 2]) == 2
    assert distance([0, 0, 0], [1, 2, 3]) == 14


def test_k_plus_proches():
    assert k_plus_proches(EXEMPLES, [2, 2], 3) == ["A", "A", "B"]
    assert k_plus_proches(EXEMPLES, [6, 6], 1) == ["B"]


def test_vote():
    assert vote(["A", "B", "A"]) == "A"
    assert vote(["B", "B", "A"]) == "B"


def test_classer():
    assert classer(EXEMPLES, [2, 2], 3) == "A"
    assert classer(EXEMPLES, [5, 5], 3) == "B"


def test_taux_reussite():
    petits_tests = [([2, 2], "A"), ([6, 6], "A")]       # le 2e est mal classe
    assert taux_reussite(EXEMPLES, petits_tests, 1) == 0.5
    train = charger("chiffres_train.csv")
    test = charger("chiffres_test.csv")
    assert taux_reussite(train, test, 3, 10) == 1.0     # 10 bonnes reponses sur 10


def lancer(nom, test):
    try:
        test()
        print("[OK]      ", nom)
    except Exception:
        print("[A FAIRE] ", nom)


# Les tests ne sont lances que si l'on execute ce fichier
# (pas lors d'un import depuis plaque.py).
if __name__ == "__main__":
    lancer("1.3 distance", test_distance)
    lancer("1.4 k_plus_proches", test_k_plus_proches)
    lancer("1.5 vote", test_vote)
    lancer("1.6 classer", test_classer)
    lancer("3.3 taux_reussite (10 images de test)", test_taux_reussite)
    # Vos essais (parties 2 a 5) peuvent s'ecrire ci-dessous, dans ce bloc.
