class Noeud:
    """Un noeud d'arbre binaire : une valeur et deux sous-arbres (None si vide)"""

    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite


def est_feuille(a):
    """Renvoie True si le noeud a n'a aucun fils"""
    return a.gauche is None and a.droite is None


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
    """Question 2 : chaque opération est entourée de parenthèses"""
    if est_feuille(a):
        return str(a.valeur)
    return "(" + en_chaine(a.gauche) + " " + a.valeur + " " + en_chaine(a.droite) + ")"


def evaluer(a):
    """Question 3"""
    if est_feuille(a):
        return a.valeur
    valeur_gauche = evaluer(a.gauche)
    valeur_droite = evaluer(a.droite)
    if a.valeur == '+':
        return valeur_gauche + valeur_droite
    elif a.valeur == '-':
        return valeur_gauche - valeur_droite
    else:
        return valeur_gauche * valeur_droite


def nb_operateurs(a):
    """Question 4"""
    if est_feuille(a):
        return 0
    return 1 + nb_operateurs(a.gauche) + nb_operateurs(a.droite)


def test_en_chaine():
    assert en_chaine(e3) == "12"
    assert en_chaine(e1) == "((3 + 5) * (7 - 2))"
    assert en_chaine(e2) == "((2 * (1 + 9)) - 4)"
    assert en_chaine(e4) == "((8 - 3) - 1)"
    assert en_chaine(e5) == "(8 - (3 - 1))"


def test_evaluer():
    assert evaluer(e3) == 12
    assert evaluer(e1) == 40
    assert evaluer(e2) == 16
    assert evaluer(e4) == 4
    assert evaluer(e5) == 6


def test_nb_operateurs():
    assert nb_operateurs(e3) == 0
    assert nb_operateurs(e1) == 3
    assert nb_operateurs(e2) == 3
    assert nb_operateurs(Noeud('+', Noeud(1), Noeud(2))) == 1


if __name__ == "__main__":
    test_en_chaine()
    test_evaluer()
    test_nb_operateurs()
    print(en_chaine(e2), "=", evaluer(e2))
