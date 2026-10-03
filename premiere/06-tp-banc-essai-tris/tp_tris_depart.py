# TP "Le banc d'essai des tris" -- fichier de depart
# Regle du TP : pas de sort() ni sorted() pour ecrire les tris (sorted sert seulement d'etalon).

import time
import random

# ------------------------------------------------------------------
# Partie A -- Des tris qui comptent leur travail
# ------------------------------------------------------------------
def tri_selection_compte(t):
    """Trie t en place par selection ; renvoie (comparaisons, echanges)."""
    # A COMPLETER
    ...

def tri_insertion_compte(t):
    """Trie t en place par insertion ; renvoie (comparaisons, decalages)."""
    # A COMPLETER
    ...

def est_trie(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True

# ------------------------------------------------------------------
# Les jeux d'essai
# ------------------------------------------------------------------
def aleatoire(n):
    """Liste de n entiers au hasard entre 0 et 1000."""
    t = []
    for k in range(n):
        t.append(random.randint(0, 1000))
    return t

def triee(n):
    """[0, 1, ..., n-1]"""
    # A COMPLETER
    ...

def inversee(n):
    """[n, n-1, ..., 1]"""
    # A COMPLETER
    ...

def presque_triee(n, k):
    """Liste triee de n elements dans laquelle on a echange k paires de voisins."""
    t = list(range(n))
    for m in range(k):
        i = random.randint(0, n - 2)
        temp = t[i]
        t[i] = t[i + 1]
        t[i + 1] = temp
    return t

def tester_partie_A():
    try:
        for n in [0, 1, 2, 7, 50]:
            for fabrique in [aleatoire, triee, inversee]:
                t = fabrique(n)
                ref = sorted(t)
                a = list(t)
                tri_selection_compte(a)
                assert a == ref
                b = list(t)
                tri_insertion_compte(b)
                assert b == ref
        assert tri_selection_compte([5, 3, 8, 1, 9, 2]) == (15, 4)
        assert tri_insertion_compte([5, 3, 8, 1, 9, 2]) == (11, 8)
        assert tri_insertion_compte([1, 2, 3, 4, 5]) == (4, 0)
        assert tri_insertion_compte([5, 4, 3, 2, 1]) == (10, 10)
        assert triee(4) == [0, 1, 2, 3]
        assert inversee(4) == [4, 3, 2, 1]
        print("Partie A : OK, tous les tests passent.")
    except Exception:
        print("Partie A : A FAIRE (ou un test echoue)")

# ------------------------------------------------------------------
# Partie B -- Le banc d'essai (compter)
# ------------------------------------------------------------------
def banc_essai(tailles):
    print("n     | liste     | sélection (comp, éch) | insertion (comp, déc)")
    for n in tailles:
        for nom, fabrique in [("aléatoire", aleatoire), ("triée", triee), ("inversée", inversee)]:
            t = fabrique(n)
            s = tri_selection_compte(list(t))
            i = tri_insertion_compte(list(t))
            print(n, "|", nom, "|", s, "|", i)

# ------------------------------------------------------------------
# Partie C -- Le chronometre (et sorted)
# ------------------------------------------------------------------
def chronometre(tri, t):
    """Duree (en s) du tri d'une COPIE de t par la fonction tri."""
    # A COMPLETER
    ...

def course(tailles):
    ts = []
    ti = []
    tp = []
    for n in tailles:
        t = aleatoire(n)
        ts.append(chronometre(tri_selection_compte, t))
        ti.append(chronometre(tri_insertion_compte, t))
        tp.append(chronometre(sorted, t))
    return ts, ti, tp

def tracer(tailles, ts, ti, tp):
    import matplotlib.pyplot as plt
    plt.plot(tailles, ts, "o-", label="sélection")
    plt.plot(tailles, ti, "s-", label="insertion")
    plt.plot(tailles, tp, "^-", label="sorted")
    plt.xlabel("taille n")
    plt.ylabel("temps (s)")
    plt.legend()
    plt.show()

# ------------------------------------------------------------------
# Partie D -- Voir le tri travailler
# ------------------------------------------------------------------
def afficher_barres(t, i_actif):
    """Affiche t en barres de # ; marque la case i_actif d'une fleche."""
    # A COMPLETER
    ...

def tri_insertion_visu(t, pause=0.5):
    """Tri par insertion qui affiche le tableau apres chaque insertion."""
    # A COMPLETER
    ...

def tri_selection_visu(t, pause=0.5):
    """Tri par selection qui affiche le tableau apres chaque etape."""
    # A COMPLETER
    ...

# ------------------------------------------------------------------
# Partie E -- Defi : le classement en direct
# ------------------------------------------------------------------
def inserer(classement, x):
    """classement est trie ; y insere x a sa place. Renvoie le nb de comparaisons."""
    # A COMPLETER
    ...

def direct_par_insertion(arrivees):
    """Classement tenu a jour par insertion ; renvoie (classement, total des comparaisons)."""
    # A COMPLETER
    ...

def direct_en_retriant(arrivees):
    """Classement retrie par selection a chaque arrivee ; renvoie (classement, total)."""
    classement = []
    total = 0
    for x in arrivees:
        classement.append(x)
        c, e = tri_selection_compte(classement)
        total = total + c
    return classement, total

# ------------------------------------------------------------------
# Programme principal : decommentez les lignes au fur et a mesure
# ------------------------------------------------------------------
print(aleatoire(10))
# tester_partie_A()
# banc_essai([100, 200, 400])
# tailles = [500, 1000, 2000, 4000]
# ts, ti, tp = course(tailles)
# print(ts, ti, tp)
# tracer(tailles, ts, ti, tp)
# tri_insertion_visu([5, 3, 8, 1, 9, 2])
