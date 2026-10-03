def recherche_sequentielle(tab, x):
    """Renvoie un indice où se trouve x dans le tableau tab, ou -1 si x n'est
    pas dans tab"""
    for i in range(len(tab)):
        if tab[i] == x:
            return i
    return -1


def recherche_dichotomique(tab, x):
    """tab est un tableau trié dans l'ordre croissant. Renvoie un indice où se
    trouve x dans tab, ou -1 si x n'est pas dans tab"""
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1


def comparaisons_sequentielle(tab, x):
    """Renvoie le nombre d'éléments de tab comparés à x par la recherche
    séquentielle"""
    nb = 0
    for i in range(len(tab)):
        nb = nb + 1
        if tab[i] == x:
            return nb
    return nb


def comparaisons_dichotomique(tab, x):
    """Renvoie le nombre d'éléments de tab comparés à x par la recherche
    dichotomique"""
    nb = 0
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        nb = nb + 1
        if tab[milieu] == x:
            return nb
        elif tab[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return nb


def premiere_occurrence(tab, x):
    """tab est un tableau trié dans l'ordre croissant, qui peut contenir des
    doublons. Renvoie le plus petit indice où se trouve x dans tab, ou -1 si x
    n'est pas dans tab"""
    resultat = -1
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] == x:
            resultat = milieu        # on a trouvé x, mais peut-être pas le premier :
            fin = milieu - 1         # on continue à chercher à gauche
        elif tab[milieu] < x:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return resultat


def recherche_rec(tab, x, debut, fin):
    """Question 4 : version récursive, cherche x entre les indices debut et fin"""
    if debut > fin:
        return -1
    milieu = (debut + fin) // 2
    if tab[milieu] == x:
        return milieu
    elif tab[milieu] < x:
        return recherche_rec(tab, x, milieu + 1, fin)
    else:
        return recherche_rec(tab, x, debut, milieu - 1)


#############################################################################
# Fonction nécessaire pour la question 2                                    #
#############################################################################


def comparer(n):
    """Cherche une valeur absente dans le tableau trié des n premiers nombres
    pairs et affiche le nombre de comparaisons de chaque méthode"""
    tab = list(range(0, 2 * n, 2))
    print("n =", n)
    print("  séquentielle :", comparaisons_sequentielle(tab, 2 * n + 1))
    print("  dichotomique :", comparaisons_dichotomique(tab, 2 * n + 1))


def test_recherche():
    tab = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert recherche_dichotomique(tab, 2) == 0
    assert recherche_dichotomique(tab, 13) == 5
    assert recherche_dichotomique(tab, 23) == 8
    assert recherche_dichotomique(tab, 4) == -1
    assert recherche_dichotomique([], 4) == -1


def test_comparaisons():
    assert comparaisons_dichotomique([10, 20, 30], 20) == 1
    assert comparaisons_dichotomique(list(range(1000)), -1) == 9


def test_premiere_occurrence():
    assert premiere_occurrence([1, 2, 2, 2, 3], 2) == 1
    assert premiere_occurrence([5, 5, 5, 5, 5, 5, 5], 5) == 0
    assert premiere_occurrence([1, 2, 3], 4) == -1
    assert premiere_occurrence([], 4) == -1
    assert premiere_occurrence([1, 1, 2, 2, 2, 2, 2, 2, 3], 2) == 2


def test_recherche_rec():
    tab = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert recherche_rec(tab, 13, 0, len(tab) - 1) == 5
    assert recherche_rec(tab, 2, 0, len(tab) - 1) == 0
    assert recherche_rec(tab, 4, 0, len(tab) - 1) == -1
    assert recherche_rec([], 4, 0, -1) == -1


if __name__ == "__main__":
    test_recherche()
    test_comparaisons()
    test_premiere_occurrence()
    test_recherche_rec()
    for n in [1000, 1000000]:
        comparer(n)
