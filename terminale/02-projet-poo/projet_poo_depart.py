# Projet de fin de chapitre -- La Bataille, en objets
# Fichier de depart : completer les parties marquees A COMPLETER,
# puis relancer le fichier : les tests de la fin indiquent ce qui fonctionne.

import random

VALEURS = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]   # de la plus faible a la plus forte
COULEURS = ["pique", "coeur", "carreau", "trefle"]


# ---------------------------------------------------------------------
# Partie 1 -- La classe Carte
# ---------------------------------------------------------------------
class Carte:
    """Une carte a jouer. Attributs prives : _valeur et _couleur."""
    def __init__(self, valeur, couleur):
        ...                      # A COMPLETER (lever ValueError si carte inconnue)

    def valeur(self):
        ...

    def couleur(self):
        ...

    def rang(self):
        """Position de la valeur dans VALEURS : 0 pour un 7, 7 pour un As."""
        ...

    # A COMPLETER : __repr__, puis __eq__ et __lt__


# ---------------------------------------------------------------------
# Partie 2 -- La classe Paquet
# ---------------------------------------------------------------------
class Paquet:
    """Un jeu de 32 cartes. Attribut prive : _cartes (liste de Carte)."""
    def __init__(self):
        ...

    def taille(self):
        ...

    def melanger(self, graine=None):
        """Melange le paquet ; avec une graine, le melange est reproductible."""
        ...

    def distribuer(self, nb_joueurs):
        """Distribue toutes les cartes une par une, a tour de role ;
        renvoie la liste des mains (une liste de Carte par joueur)."""
        ...


# ---------------------------------------------------------------------
# Partie 3 -- La classe Joueur
# ---------------------------------------------------------------------
class Joueur:
    """Un joueur : un nom et une main (attribut prive _main, liste de Carte,
    la carte du dessus etant au debut de la liste)."""
    def __init__(self, nom, cartes):
        ...

    def nb_cartes(self):
        ...

    def a_perdu(self):
        ...

    def nb_cartes_de(self, valeur):
        """Nombre de cartes de cette valeur dans la main (a ecrire avec filter)."""
        ...

    def jouer_carte(self):
        """Retire et renvoie la carte du dessus."""
        ...

    def ramasser(self, cartes):
        """Place les cartes, dans l'ordre, sous la main."""
        ...


# ---------------------------------------------------------------------
# Partie 4 -- La classe Partie
# ---------------------------------------------------------------------
class Partie:
    def __init__(self, nom1, nom2, graine=None, max_plis=2000, tapis_melange=False):
        p = Paquet()
        p.melanger(graine)
        m1, m2 = p.distribuer(2)
        self.j1 = Joueur(nom1, m1)
        self.j2 = Joueur(nom2, m2)
        self.nb_plis = 0
        self.nb_batailles = 0
        self.max_plis = max_plis
        self.tapis_melange = tapis_melange     # utile seulement en partie 6

    def jouer_pli(self):
        """A COMPLETER : joue un pli (avec batailles eventuelles)
        et renvoie le Joueur qui ramasse le tapis."""
        ...

    def jouer(self):
        """A COMPLETER : joue des plis jusqu'a ce qu'un joueur n'ait plus de
        cartes, ou que max_plis soit atteint ; renvoie vainqueur()."""
        ...

    def vainqueur(self):
        """Nom du vainqueur, ou None si la partie n'est pas terminee."""
        if self.j2.a_perdu():
            return self.j1.nom
        if self.j1.a_perdu():
            return self.j2.nom
        return None


# ---------------------------------------------------------------------
# Partie 5 -- Statistiques (style fonctionnel)
# ---------------------------------------------------------------------
def resume(graine, tapis_melange=False):
    """A COMPLETER : joue la partie Ada contre Alan de graine donnee et renvoie
    le dictionnaire {"graine", "vainqueur", "plis", "batailles", "as_ada"}
    (as_ada = nombre d'As d'Ada au depart)."""
    ...


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

    def t_carte():
        c = Carte("Roi", "coeur")
        assert c.valeur() == "Roi" and c.couleur() == "coeur" and c.rang() == 6
        assert repr(c) == "Roi de coeur"
        try:
            Carte("2", "coeur")
            assert False, "Carte('2', 'coeur') doit lever ValueError"
        except ValueError:
            pass

    def t_comparer():
        r1 = Carte("Roi", "coeur")
        r2 = Carte("Roi", "trefle")
        sept = Carte("7", "pique")
        assert r1 == r2 and sept < r1 and not r1 < r2
        main = [r1, sept, Carte("As", "pique"), Carte("9", "coeur")]
        assert repr(sorted(main)) == "[7 de pique, 9 de coeur, Roi de coeur, As de pique]"

    def t_paquet():
        p = Paquet()
        assert p.taille() == 32
        p.melanger(1)
        mains = p.distribuer(2)
        assert len(mains) == 2 and len(mains[0]) == 16 and p.taille() == 0
        a = Paquet()
        b = Paquet()
        a.melanger(7)
        b.melanger(7)
        assert repr(a.distribuer(2)) == repr(b.distribuer(2))

    def t_joueur():
        cartes = [Carte("As", "coeur"), Carte("8", "pique")]
        j = Joueur("Ada", cartes)
        cartes.append(Carte("7", "coeur"))      # ne doit pas modifier la main d'Ada
        assert j.nb_cartes() == 2 and j.nb_cartes_de("As") == 1
        assert repr(j.jouer_carte()) == "As de coeur"
        j.ramasser([Carte("Roi", "pique"), Carte("9", "pique")])
        assert [repr(j.jouer_carte()) for _ in range(3)] == ["8 de pique", "Roi de pique", "9 de pique"]
        assert j.a_perdu()

    def t_pli():
        pa = Partie("x", "y")
        pa.j1 = Joueur("A", [Carte("Roi", "coeur"), Carte("7", "pique"), Carte("8", "pique")])
        pa.j2 = Joueur("B", [Carte("Roi", "pique"), Carte("As", "pique"), Carte("10", "pique")])
        assert pa.jouer_pli() is pa.j2
        assert pa.j2.nb_cartes() == 6 and pa.j1.a_perdu() and pa.nb_batailles == 1
        pa.j1 = Joueur("A", [Carte("Roi", "coeur")])            # bataille impossible a finir
        pa.j2 = Joueur("B", [Carte("Roi", "pique"), Carte("As", "pique")])
        assert pa.jouer_pli() is pa.j2 and pa.j2.nb_cartes() == 3

    def t_partie():
        for g in range(100):
            pt = Partie("Ada", "Alan", g)
            pt.jouer()
            assert pt.j1.nb_cartes() + pt.j2.nb_cartes() == 32, "des cartes ont disparu"
        pt = Partie("Ada", "Alan", 2026)
        assert pt.jouer() == "Alan" and pt.nb_plis == 106

    def t_resume():
        r = resume(2026)
        assert r["vainqueur"] == "Alan" and r["plis"] == 106 and r["batailles"] == 8

    for nom, f in [("Partie 1 : Carte", t_carte), ("Partie 1 : comparer des cartes", t_comparer),
                   ("Partie 2 : Paquet", t_paquet), ("Partie 3 : Joueur", t_joueur),
                   ("Partie 4 : jouer_pli", t_pli), ("Partie 4 : jouer", t_partie),
                   ("Partie 5 : resume", t_resume)]:
        essai(nom, f)


if __name__ == "__main__":
    lancer_tests()
