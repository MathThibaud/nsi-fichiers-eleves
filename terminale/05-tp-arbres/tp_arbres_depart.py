# TP de fin de chapitre -- Un arbre binaire de recherche, de A a Z
# Fichier de depart : completer les parties marquees A COMPLETER,
# puis relancer le fichier : les tests de la fin indiquent ce qui fonctionne.

import random
import math
import sys

sys.setrecursionlimit(20000)   # hauteur() est recursive : utile pour les arbres tres hauts


# ---------------------------------------------------------------------
# Fourni : le noeud et les deux fonctions du cours
# ---------------------------------------------------------------------
class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche      # un Noeud, ou None
        self.droite = droite      # un Noeud, ou None


def taille(a):
    if a is None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droite)


def hauteur(a):
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droite))


# ---------------------------------------------------------------------
# Parties 1 a 3 -- La classe ABR
# ---------------------------------------------------------------------
class ABR:
    """Un arbre binaire de recherche sans doublon.
    Attributs prives : _racine (un Noeud ou None) et _taille (un entier)."""
    def __init__(self):
        self._racine = None
        self._taille = 0

    def est_vide(self):
        return self._racine is None

    def taille(self):
        return self._taille

    def hauteur(self):
        return hauteur(self._racine)

    def inserer(self, x):
        """A COMPLETER (avec une boucle while, sans recursivite).
        Insere x s'il n'est pas deja present ; renvoie True si x a ete ajoute,
        False sinon."""
        ...

    def contient(self, x):
        """A COMPLETER. Renvoie le couple (x present ?, nombre de noeuds visites)."""
        ...

    def minimum(self):
        """A COMPLETER. Plus petite valeur (ValueError si l'arbre est vide)."""
        ...

    def maximum(self):
        """A COMPLETER. Plus grande valeur (ValueError si l'arbre est vide)."""
        ...

    def infixe(self):
        """A COMPLETER. Liste des valeurs dans l'ordre du parcours infixe."""
        ...

    def entre(self, a, b):
        """A COMPLETER (defi). Valeurs v telles que a <= v <= b, dans l'ordre
        croissant, sans explorer les sous-arbres inutiles.
        Renvoie le couple (liste des valeurs, nombre de noeuds visites)."""
        ...


def tri_abr(tab):
    """A COMPLETER. Renvoie les valeurs de tab triees (sans doublon), a l'aide d'un ABR."""
    ...


# ---------------------------------------------------------------------
# Partie 4 -- Mesurer la hauteur
# ---------------------------------------------------------------------
def hauteur_aleatoire(n, essais=20):
    """A COMPLETER. Hauteur moyenne, sur `essais` essais, d'un ABR obtenu en
    inserant les entiers 0, 1, ..., n-1 dans un ordre aleatoire."""
    ...


def hauteur_triee(n):
    """A COMPLETER. Hauteur de l'ABR obtenu en inserant 0, 1, ..., n-1 dans l'ordre."""
    ...


# ---------------------------------------------------------------------
# Partie 5 -- Un index de mots
# ---------------------------------------------------------------------
class NoeudIndex:
    """Fourni : un noeud de l'index, avec le mot (cle de l'ABR) et la liste
    croissante des numeros de lignes ou il apparait."""
    def __init__(self, mot):
        self.valeur = mot
        self.lignes = []
        self.gauche = None
        self.droite = None


class Index:
    """Un ABR de NoeudIndex, range selon l'ordre des mots."""
    def __init__(self):
        self._racine = None
        self._nb_mots = 0

    def nb_mots(self):
        return self._nb_mots

    def hauteur(self):
        return hauteur(self._racine)

    def ajouter(self, mot, ligne):
        """A COMPLETER. Ajoute le numero de ligne au noeud du mot (en creant
        le noeud s'il n'existe pas) ; un numero n'est pas ajoute deux fois."""
        ...

    def lignes(self, mot):
        """A COMPLETER. Liste des lignes ou apparait le mot ([] s'il est absent)."""
        ...

    def afficher(self):
        """A COMPLETER. Affiche l'index, un mot par ligne, dans l'ordre des mots :
        arbre : 1, 6, 8"""
        ...


def mots_de(ligne):
    """Fournie. Decoupe une ligne en mots en minuscules, sans ponctuation."""
    propre = ""
    for c in ligne.lower():
        if c.isalpha() or c == "-":
            propre = propre + c
        else:
            propre = propre + " "
    return propre.split()


def indexer(texte):
    """Fournie. Construit l'index d'un texte (lignes numerotees a partir de 1)."""
    idx = Index()
    num = 1
    for ligne in texte.split("\n"):
        for mot in mots_de(ligne):
            idx.ajouter(mot, num)
        num = num + 1
    return idx


TEXTE = """Un arbre binaire de recherche range ses valeurs avec ordre :
à gauche les plus petites, à droite les plus grandes.
Pour chercher une valeur, on part de la racine et on descend,
à gauche ou à droite, comme dans une recherche dichotomique.
Chaque comparaison élimine tout un sous-arbre.
Si l'arbre est équilibré, sa hauteur reste petite
et la recherche est très rapide, même parmi un million de valeurs.
Mais si l'on insère des valeurs déjà triées, l'arbre devient un peigne :
chaque nœud n'a qu'un fils, la hauteur égale la taille,
et chercher devient aussi lent que parcourir une liste.
Les bases de données utilisent des arbres équilibrés
pour garder une hauteur petite quoi qu'il arrive."""


# ---------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------
def lancer_tests():
    def essai(nom, f):
        try:
            f()
            print("[OK]     ", nom)
        except Exception as e:
            print("[A FAIRE]", nom, "->", type(e).__name__, e)

    def exemple():
        a = ABR()
        for v in [15, 8, 20, 5, 12, 25, 10, 18, 2]:
            a.inserer(v)
        return a

    def t_inserer():
        a = exemple()
        assert a.taille() == 9 and a.hauteur() == 4
        assert a.inserer(12) is False and a.taille() == 9
        assert taille(a._racine) == 9            # l'attribut _taille est juste

    def t_contient():
        a = exemple()
        assert a.contient(15) == (True, 1)
        assert a.contient(10) == (True, 4)
        assert a.contient(13) == (False, 3)
        assert a.minimum() == 2 and a.maximum() == 25
        try:
            ABR().minimum()
            assert False, "minimum d'un arbre vide : ValueError attendue"
        except ValueError:
            pass

    def t_infixe():
        assert exemple().infixe() == [2, 5, 8, 10, 12, 15, 18, 20, 25]
        assert tri_abr([5, 3, 9, 3, 1, 7]) == [1, 3, 5, 7, 9]
        assert tri_abr([]) == []

    def t_mesures():
        assert hauteur_triee(100) == 100
        h = hauteur_aleatoire(1000)
        assert 15 <= h <= 30, "hauteur moyenne surprenante : " + str(h)

    def t_index():
        idx = indexer(TEXTE)
        assert idx.nb_mots() == 77
        assert idx.lignes("hauteur") == [6, 9, 12]
        assert idx.lignes("arbre") == [1, 6, 8]
        assert idx.lignes("chat") == []

    def t_entre():
        a = exemple()
        assert a.entre(9, 19) == ([10, 12, 15, 18], 6)

    for nom, f in [("Partie 1 : inserer", t_inserer), ("Partie 2 : contient, minimum, maximum", t_contient),
                   ("Partie 3 : infixe et tri", t_infixe), ("Partie 4 : mesures", t_mesures),
                   ("Partie 5 : index", t_index), ("Defi : entre", t_entre)]:
        essai(nom, f)


if __name__ == "__main__":
    lancer_tests()
