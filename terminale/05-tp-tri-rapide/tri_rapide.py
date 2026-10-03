"""Tri rapide (Quicksort) --- Diviser pour regner.
Trame du TP « Tri rapide » : completer les fonctions marquees A COMPLETER.
Lancer :  python3 tri_rapide.py    (chaque test affiche OK, ou A FAIRE ou ECHEC)
"""
import random


# ---------------------------------------------------------------------------
# Exercice 1 : la fonction partition
# ---------------------------------------------------------------------------
def partition(tab, bas, haut):
    """Partitionne tab[bas..haut] autour du pivot tab[haut].
    Renvoie l'indice final du pivot."""
    # A COMPLETER
    return None


# ---------------------------------------------------------------------------
# Exercice 2 : la fonction recursive tri_rapide
# ---------------------------------------------------------------------------
def tri_rapide(tab, bas, haut):
    """Trie tab entre les indices bas et haut (inclus), en place."""
    # A COMPLETER
    pass


# ---------------------------------------------------------------------------
# Exercice 3 (fourni) : rappel du tri fusion, qui modifie tab directement
# ---------------------------------------------------------------------------
def tri_fusion(tab):
    """Trie tab en le modifiant directement (recopie les deux moities)."""
    if len(tab) > 1:
        milieu = len(tab) // 2
        gauche = tab[:milieu]
        droite = tab[milieu:]
        tri_fusion(gauche)
        tri_fusion(droite)
        i = 0                    # indice dans gauche
        j = 0                    # indice dans droite
        k = 0                    # indice dans tab
        while i < len(gauche) and j < len(droite):   # fusion
            if gauche[i] <= droite[j]:
                tab[k] = gauche[i]
                i = i + 1
            else:
                tab[k] = droite[j]
                j = j + 1
            k = k + 1
        while i < len(gauche):   # reste de gauche
            tab[k] = gauche[i]
            i = i + 1
            k = k + 1
        while j < len(droite):   # reste de droite
            tab[k] = droite[j]
            j = j + 1
            k = k + 1


# ---------------------------------------------------------------------------
# Exercice 4 : generer un tableau aleatoire
# ---------------------------------------------------------------------------
def tableau_aleatoire(n):
    """Renvoie un tableau de n entiers aleatoires entre 0 et n."""
    # A COMPLETER
    return []


# ---------------------------------------------------------------------------
# Tests (ne pas modifier) : chaque test affiche OK, ou A FAIRE ou ECHEC
# ---------------------------------------------------------------------------
def trier(tab):
    """Trie tab avec tri_rapide et le renvoie (pour les tests)."""
    tri_rapide(tab, 0, len(tab) - 1)
    return tab


def test_partition():
    t = [10, 7, 8, 9, 1, 5]
    p = partition(t, 0, len(t) - 1)
    if p is None:
        return False
    for i in range(p):                  # a gauche : <= pivot
        if t[i] > t[p]:
            return False
    for i in range(p + 1, len(t)):      # a droite : > pivot
        if t[i] <= t[p]:
            return False
    return t[p] == 5


def test_tri_rapide():
    if trier([10, 7, 8, 9, 1, 5]) != [1, 5, 7, 8, 9, 10]:
        return False
    if trier([]) != [] or trier([42]) != [42] or trier([2, 1]) != [1, 2]:
        return False
    if trier([3, 3, 3]) != [3, 3, 3]:                   # doublons
        return False
    if trier([5, 4, 3, 2, 1]) != [1, 2, 3, 4, 5]:
        return False
    if trier([1, 2, 3, 4, 5]) != [1, 2, 3, 4, 5]:
        return False
    for essai in range(200):            # comparaison a sorted()
        a = []
        for k in range(random.randint(0, 40)):
            a.append(random.randint(-50, 50))
        if trier(list(a)) != sorted(a):
            return False
    return True


def test_tri_fusion():
    for essai in range(100):
        a = []
        for k in range(random.randint(0, 40)):
            a.append(random.randint(-50, 50))
        b = list(a)
        tri_fusion(b)
        if b != sorted(a):
            return False
    return True


def test_tableau_aleatoire():
    t = tableau_aleatoire(50)
    if t is None or len(t) != 50:
        return False
    for x in t:
        if x < 0 or x > 50:
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
    lancer("partition", test_partition)
    lancer("tri_rapide", test_tri_rapide)
    lancer("tri_fusion (fourni)", test_tri_fusion)
    lancer("tableau_aleatoire", test_tableau_aleatoire)
