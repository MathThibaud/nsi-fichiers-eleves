"""Tim sort --- le tri de Python (insertion sur petits blocs + fusion).
Trame du TP « Tim sort » : remplacer chaque ... (A COMPLETER) comme dans la fiche.
Lancer :  python3 tim_sort.py    (chaque test affiche OK, ou A FAIRE ou ECHEC)
"""
import random


# ---------------------------------------------------------------------------
# Exercice 1 : le tri par insertion sur un sous-tableau
# ---------------------------------------------------------------------------
def tri_insertion(tab, debut, fin):
    """Trie tab entre les indices debut et fin (inclus) par insertion, en place."""
    for i in range(debut + 1, fin + 1):
        cle = tab[i]                    # element a inserer
        j = i - 1
        while j >= debut and tab[j] > ...:     # A COMPLETER (condition)
            tab[j + 1] = ...                    # A COMPLETER
            j = j - 1
        tab[j + 1] = ...                        # A COMPLETER


# ---------------------------------------------------------------------------
# Exercice 2 : fusionner deux sous-tableaux tries
# ---------------------------------------------------------------------------
def fusion_en_place(tab, debut, milieu, fin):
    """Fusionne les sous-tableaux tries tab[debut..milieu] et tab[milieu+1..fin]."""
    nb_gauche = milieu - debut + 1
    nb_droite = fin - milieu
    gauche = tab[debut:milieu + 1]
    droite = tab[milieu + 1:fin + 1]
    i = 0
    j = 0
    k = debut
    while i < nb_gauche and j < nb_droite:
        if gauche[i] <= droite[j]:
            tab[k] = ...                # A COMPLETER
            i = i + 1
        else:
            tab[k] = ...                # A COMPLETER
            j = j + 1
        k = k + 1
    while i < nb_gauche:
        tab[k] = ...                    # A COMPLETER
        i = i + 1
        k = k + 1
    while j < nb_droite:
        tab[k] = ...                    # A COMPLETER
        j = j + 1
        k = k + 1


# ---------------------------------------------------------------------------
# Exercice 3 : assembler le Tim sort
# ---------------------------------------------------------------------------
def tim_sort(tab, taille_bloc=64):
    """Trie tab en place (blocs tries par insertion, puis fusionnes) et le renvoie."""
    n = len(tab)
    for debut_bloc in range(0, n, taille_bloc):     # 1. trier chaque bloc
        fin_bloc = min(debut_bloc + taille_bloc - 1, n - 1)
        tri_insertion(tab, ..., ...)                # A COMPLETER (arguments)
    taille = taille_bloc                            # 2. fusionner deux a deux
    while taille < n:
        for debut in range(0, n, 2 * taille):
            milieu = min(debut + taille - 1, n - 1)
            fin = min(debut + 2 * taille - 1, n - 1)
            if milieu < fin:
                fusion_en_place(tab, ..., ..., ...)     # A COMPLETER (arguments)
        taille = 2 * taille
    return tab


# ---------------------------------------------------------------------------
# Tests (ne pas modifier) : chaque test affiche OK, ou A FAIRE ou ECHEC
# ---------------------------------------------------------------------------
def tableau_hasard(taille_max):
    """Renvoie un tableau d'entiers aleatoires (pour les tests)."""
    t = []
    for k in range(random.randint(0, taille_max)):
        t.append(random.randint(-50, 50))
    return t


def test_tri_insertion():
    t = [12, 11, 13, 5, 6]
    tri_insertion(t, 0, len(t) - 1)
    if t != [5, 6, 11, 12, 13]:
        return False
    t = [5, 2, 9, 1, 3]
    tri_insertion(t, 0, len(t) - 1)
    if t != [1, 2, 3, 5, 9]:
        return False
    t = [9, 8, 5, 2, 7, 1, 0]           # on ne trie que t[2..5]
    tri_insertion(t, 2, 5)
    return t == [9, 8, 1, 2, 5, 7, 0]


def test_fusion_en_place():
    t = [11, 12, 13, 5, 6, 7]
    fusion_en_place(t, 0, 2, 5)
    if t != [5, 6, 7, 11, 12, 13]:
        return False
    t = [1, 4, 7, 2, 3, 9]              # deux moities triees
    fusion_en_place(t, 0, 2, 5)
    return t == [1, 2, 3, 4, 7, 9]


def test_tim_sort():
    if tim_sort([5, 21, 7, 23, 19, 100, 8, 12, 22, 15]) != [5, 7, 8, 12, 15, 19, 21, 22, 23, 100]:
        return False
    if tim_sort([]) != [] or tim_sort([7]) != [7]:
        return False
    if tim_sort([2, 1], 1) != [1, 2]:
        return False
    if tim_sort([5, 4, 3, 2, 1], 2) != [1, 2, 3, 4, 5]:
        return False
    for essai in range(200):            # petits blocs : on force les fusions
        a = tableau_hasard(200)
        if tim_sort(list(a), 4) != sorted(a):
            return False
    return True


def lancer(nom, test):
    """Lance un test sans planter si la fonction n'est pas encore ecrite."""
    try:
        ok = test()
    except Exception:
        ok = False
    if ok:
        print(nom, ": OK")
    else:
        print(nom, ": A FAIRE ou ECHEC")


if __name__ == "__main__":
    lancer("tri_insertion", test_tri_insertion)
    lancer("fusion_en_place", test_fusion_en_place)
    lancer("tim_sort", test_tim_sort)
