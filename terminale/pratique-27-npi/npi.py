class Pile:
    """Une pile, implémentée à l'aide d'une liste Python"""

    def __init__(self):
        self._contenu = []

    def est_vide(self):
        return self._contenu == []

    def empiler(self, x):
        self._contenu.append(x)

    def depiler(self):
        return self._contenu.pop()

    def sommet(self):
        return self._contenu[-1]

    def taille(self):
        return len(self._contenu)


OPERATEURS = ["+", "-", "*"]


def evaluer_npi(expression):
    """expression est une chaîne de caractères en notation polonaise inverse
    dont les éléments (nombres entiers positifs et opérateurs) sont séparés par
    des espaces. Renvoie la valeur de l'expression."""
    pass  # A COMPLETER


def test_evaluer():
    assert evaluer_npi("42") == 42
    assert evaluer_npi("3 4 +") == 7
    assert evaluer_npi("7 2 -") == 5
    assert evaluer_npi("3 4 + 2 *") == 14


def test_erreurs():
    assert evaluer_npi("2 3 *") == 6
    assert evaluer_npi("3 +") is None
    assert evaluer_npi("3 4") is None
