class Noeud:
    """Un noeud d'arbre binaire : une valeur et deux sous-arbres (None si vide)"""

    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite


def est_feuille(a):
    """Renvoie True si le noeud a n'a aucun fils"""
    return a.gauche is None and a.droite is None


# Les feuilles portent des nombres entiers, les autres noeuds un opérateur
# parmi '+', '-' et '*'.

# e1 : l'arbre de la figure 1
e1 = Noeud('*',
           Noeud('+', Noeud(3), Noeud(5)),
           Noeud('-', Noeud(7), Noeud(2)))

e2 = Noeud('-',
           Noeud('*', Noeud(2), Noeud('+', Noeud(1), Noeud(9))),
           Noeud(4))

e3 = Noeud(12)

e4 = Noeud('-', Noeud('-', Noeud(8), Noeud(3)), Noeud(1))

e5 = Noeud('-', Noeud(8), Noeud('-', Noeud(3), Noeud(1)))


def en_chaine(a):
    """Renvoie l'écriture de l'expression représentée par l'arbre a,
    chaque opération étant entourée de parenthèses"""
    if est_feuille(a):
        return str(a.valeur)
    return en_chaine(a.gauche) + " " + a.valeur + " " + en_chaine(a.droite)


def evaluer(a):
    """Renvoie la valeur de l'expression représentée par l'arbre a"""
    pass  # A COMPLETER


def nb_operateurs(a):
    """Renvoie le nombre d'opérateurs de l'expression représentée par a"""
    pass  # A COMPLETER


def test_en_chaine():
    assert en_chaine(e3) == "12"
    assert en_chaine(e1) == "((3 + 5) * (7 - 2))"


def test_evaluer():
    assert evaluer(e3) == 12
    assert evaluer(e1) == 40


def test_nb_operateurs():
    assert nb_operateurs(e3) == 0
    assert nb_operateurs(e1) == 3
