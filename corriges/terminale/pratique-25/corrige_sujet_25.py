import random


class Noeud:
    """Un noeud d'arbre binaire : une valeur et deux sous-arbres (None si vide)"""

    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite


def inserer(a, x):
    """Insère la valeur x dans l'arbre binaire de recherche a et renvoie
    l'arbre obtenu. Si x est déjà présente, l'arbre n'est pas modifié."""
    if a is None:
        return Noeud(x)
    if x < a.valeur:
        a.gauche = inserer(a.gauche, x)
    elif x > a.valeur:
        a.droite = inserer(a.droite, x)
    return a


def construire_abr(valeurs):
    """Renvoie l'ABR obtenu en insérant une à une les valeurs de la liste,
    dans l'ordre de la liste, à partir d'un arbre vide"""
    a = None
    for v in valeurs:
        a = inserer(a, v)
    return a


def hauteur(a):
    """Renvoie la hauteur de l'arbre a (0 pour l'arbre vide)"""
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droite))


def recherche(a, x):
    """Question 2 : on descend à gauche ou à droite selon la comparaison"""
    if a is None:
        return False
    if x == a.valeur:
        return True
    if x < a.valeur:
        return recherche(a.gauche, x)
    else:
        return recherche(a.droite, x)


def infixe(a):
    """Question 3 : sous-arbre gauche, puis racine, puis sous-arbre droit"""
    if a is None:
        return []
    return infixe(a.gauche) + [a.valeur] + infixe(a.droite)


def tri_abr(valeurs):
    """Question 3 : le parcours infixe d'un ABR donne ses valeurs triées"""
    return infixe(construire_abr(valeurs))


def experience(n):
    """Construit deux ABR contenant les entiers de 1 à n : l'un en les insérant
    dans l'ordre croissant, l'autre dans un ordre aléatoire, et affiche la
    hauteur de chacun"""
    croissant = construire_abr(list(range(1, n + 1)))
    melange = list(range(1, n + 1))
    random.shuffle(melange)
    aleatoire = construire_abr(melange)
    print("insertion dans l'ordre croissant :", hauteur(croissant))
    print("insertion dans un ordre aléatoire :", hauteur(aleatoire))


def test_recherche():
    a = construire_abr([8, 3, 10, 1, 6, 14, 4, 7])
    assert recherche(a, 6)
    assert recherche(a, 14)
    assert recherche(a, 8)
    assert not recherche(a, 5)
    assert not recherche(a, 20)
    assert not recherche(None, 3)


def test_tri():
    a = construire_abr([8, 3, 10, 1, 6, 14, 4, 7])
    assert infixe(a) == [1, 3, 4, 6, 7, 8, 10, 14]
    assert infixe(None) == []
    assert tri_abr([5, 2, 9, 2, 1]) == [1, 2, 5, 9]
    assert tri_abr([]) == []


if __name__ == "__main__":
    test_recherche()
    test_tri()
    a = construire_abr([8, 3, 10, 1, 6, 14, 4, 7])
    print("hauteur de l'arbre de la question 1 :", hauteur(a))
    experience(200)
