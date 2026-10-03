# TP "L'annuaire et le devin" -- fichier de depart
# A placer dans le meme dossier que tp_dichotomie_annuaire.py

import time
import random
import math
from tp_dichotomie_annuaire import charger_annuaire

# ------------------------------------------------------------------
# Partie A -- Le devin : l'ordinateur devine VOTRE nombre
# ------------------------------------------------------------------
def devin(bas, haut):
    """Devine un nombre entre bas et haut ; l'humain repond +, - ou =.
    Renvoie le nombre d'essais, ou -1 si les reponses sont contradictoires."""
    # A COMPLETER
    ...

# ------------------------------------------------------------------
# Partie B -- L'annuaire
# ------------------------------------------------------------------
def est_trie(t):
    """True si t est trie dans l'ordre croissant."""
    # A COMPLETER
    ...

def numero_sequentiel(noms, numeros, nom):
    """Renvoie (numero ou None, nombre de comparaisons)."""
    # A COMPLETER
    ...

def numero_dicho(noms, numeros, nom):
    """Meme resultat, par dichotomie (noms est trie)."""
    # A COMPLETER
    ...

def tester_partie_B(noms, numeros):
    try:
        assert est_trie(noms) == True
        assert est_trie(["B", "A"]) == False
        for nom in [noms[0], noms[1234], noms[-1], "ZORRO Zoe", "AAA", "MARTIN Hugo"]:
            assert numero_sequentiel(noms, numeros, nom)[0] == numero_dicho(noms, numeros, nom)[0]
        assert numero_dicho(noms, numeros, "ZORRO Zoe") == (None, 14)
        assert numero_sequentiel(noms, numeros, "ZORRO Zoe") == (None, 16000)
        assert numero_dicho(["A", "B", "C"], ["1", "2", "3"], "B") == ("2", 1)
        print("Partie B : OK, tous les tests passent.")
    except Exception:
        print("Partie B : A FAIRE (ou un test echoue)")

# ------------------------------------------------------------------
# Partie C -- Mesurer
# ------------------------------------------------------------------
def moyenne_comparaisons(noms, numeros, recherche, nb_essais):
    total = 0
    for k in range(nb_essais):
        nom = noms[random.randint(0, len(noms) - 1)]
        numero, c = recherche(noms, numeros, nom)
        total = total + c
    return total / nb_essais

def chrono_recherches(noms, numeros, recherche, cibles):
    """Duree totale (en s) de la recherche de chacun des noms de cibles."""
    # A COMPLETER
    ...

def courbe_moyennes(noms, numeros, tailles):
    """Pour chaque n, nombre moyen de comparaisons de numero_dicho sur noms[0:n]."""
    res = []
    for n in tailles:
        res.append(moyenne_comparaisons(noms[0:n], numeros[0:n], numero_dicho, 2000))
    return res

def tracer(tailles, moyennes):
    import matplotlib.pyplot as plt
    plt.plot(tailles, moyennes, "o-", label="dichotomie (mesuré)")
    logs = []
    for n in tailles:
        logs.append(math.log2(n))
    plt.plot(tailles, logs, "--", label="log2(n)")
    plt.xlabel("taille n de l'annuaire")
    plt.ylabel("comparaisons (moyenne)")
    plt.legend()
    plt.show()

# ------------------------------------------------------------------
# Partie D -- L'autocompletion
# ------------------------------------------------------------------
def premier_indice_au_moins(noms, debut_nom):
    """Plus petit indice i tel que noms[i] >= debut_nom (len(noms) si aucun)."""
    # A COMPLETER
    ...

def suggestions(noms, prefixe, k):
    """Au plus k noms commencant par prefixe, dans l'ordre alphabetique."""
    # A COMPLETER
    ...

def nb_commencant_par(noms, prefixe):
    """Nombre d'abonnes dont le nom commence par prefixe."""
    # A COMPLETER
    ...

def tester_partie_D(noms):
    try:
        assert premier_indice_au_moins(["A", "C", "E"], "B") == 1
        assert premier_indice_au_moins(["A", "C", "E"], "C") == 1
        assert premier_indice_au_moins(["A", "C", "E"], "Z") == 3
        assert suggestions(noms, "DUP", 2) == ["DUPONT Adam", "DUPONT Adele"]
        assert suggestions(noms, "ZZ", 5) == []
        assert nb_commencant_par(noms, "MAR") == 500
        print("Partie D : OK, tous les tests passent.")
    except Exception:
        print("Partie D : A FAIRE (ou un test echoue)")

# ------------------------------------------------------------------
# Partie E -- Bonus : la dichotomie sur les nombres a virgule
# ------------------------------------------------------------------
def racine(a, precision):
    """Encadre la racine carree de a (a >= 1) a precision pres ; renvoie (milieu, tours)."""
    # A COMPLETER
    ...

# ------------------------------------------------------------------
# Programme principal : decommentez les lignes au fur et a mesure
# ------------------------------------------------------------------
# devin(1, 100)
noms, numeros = charger_annuaire()
print(len(noms), "abonnés :", noms[0], "...", noms[-1])
# tester_partie_B(noms, numeros)
# print(numero_dicho(noms, numeros, "MARTIN Hugo"))
# print(moyenne_comparaisons(noms, numeros, numero_sequentiel, 1000))
# print(moyenne_comparaisons(noms, numeros, numero_dicho, 1000))
# tailles = [1000, 2000, 4000, 8000, 16000]
# moyennes = courbe_moyennes(noms, numeros, tailles)
# print(moyennes)
# tracer(tailles, moyennes)
# tester_partie_D(noms)
# print(suggestions(noms, "DUP", 5))
