# TP "Un an de meteo a la loupe" -- fichier de depart
# Placez ce fichier dans le meme dossier que tp_parcours_meteo.csv.
# Regle du TP : on n'utilise PAS sum, max, min (on ecrit les parcours soi-meme).

import time
import random

# ------------------------------------------------------------------
# Fourni : lecture du fichier de releves (ne pas modifier)
# ------------------------------------------------------------------
def charger_releves(nom_fichier):
    """Renvoie quatre tableaux : dates, tmin, tmax, pluie (365 jours)."""
    dates = []
    tmin = []
    tmax = []
    pluie = []
    fichier = open(nom_fichier, encoding="utf-8")
    fichier.readline()                      # on saute la ligne d'en-tete
    for ligne in fichier:
        champs = ligne.strip().split(",")
        dates.append(champs[0])
        tmin.append(float(champs[1]))
        tmax.append(float(champs[2]))
        pluie.append(float(champs[3]))
    fichier.close()
    return dates, tmin, tmax, pluie

def mois_de(date):
    """'2025-07-14' -> 7"""
    return int(date[5:7])

# ------------------------------------------------------------------
# Partie B -- Le bulletin climatique (parcours)
# ------------------------------------------------------------------
def somme(t):
    # A COMPLETER
    ...

def moyenne(t):
    """t non vide"""
    # A COMPLETER (une ligne, en utilisant somme)
    ...

def nb_au_moins(t, seuil):
    """Nombre d'elements de t superieurs ou egaux a seuil."""
    # A COMPLETER
    ...

def indice_min(t):
    """Indice du plus petit element de t (t non vide)."""
    # A COMPLETER
    ...

def indice_ecart_max(tmin, tmax):
    """Indice du jour ou tmax - tmin est le plus grand."""
    # A COMPLETER
    ...

def premier_jour_au_moins(t, seuil):
    """Indice du premier jour ou t[i] >= seuil, ou -1 s'il n'y en a pas."""
    # A COMPLETER
    ...

def moyenne_mois(dates, t, mois):
    """Moyenne des t[i] pour les jours du mois donne (1 a 12)."""
    # A COMPLETER
    ...

def tester_partie_B():
    try:
        assert somme([2, 5, 1]) == 8
        assert moyenne([10, 12, 14]) == 12
        assert nb_au_moins([3, 8, 5, 8], 5) == 3
        assert indice_min([4, -2, 7, -2]) == 1
        assert indice_ecart_max([10, 12, 9], [15, 20, 13]) == 1
        assert premier_jour_au_moins([18, 25, 31, 33], 30) == 2
        assert premier_jour_au_moins([18, 25], 30) == -1
        assert moyenne_mois(["2025-01-31", "2025-02-01", "2025-02-02"], [5, 8, 10], 2) == 9
        print("Partie B : OK, tous les tests passent.")
    except Exception:
        print("Partie B : A FAIRE (ou un test echoue)")

def bulletin(dates, tmin, tmax, pluie):
    print("=== Bulletin climatique 2025 ===")
    print("Moyenne des maximales :", round(moyenne(tmax), 1), "°C")
    print("Cumul de pluie        :", round(somme(pluie)), "mm")
    # A COMPLETER : jours de pluie, jours de chaleur, nuits tropicales,
    # nuit la plus froide (date), plus grand ecart (date),
    # premier jour a 30 °C, moyennes mensuelles, mois le plus chaud

# ------------------------------------------------------------------
# Partie C -- Le piege quadratique, chronometre en main
# ------------------------------------------------------------------
def variance_naive(t):
    n = len(t)
    s = 0
    for x in t:
        s = s + (x - moyenne(t)) ** 2     # moyenne(t) recalculee a chaque tour
    return s / n

def variance(t):
    n = len(t)
    m = moyenne(t)                        # calculee une seule fois
    s = 0
    for x in t:
        s = s + (x - m) ** 2
    return s / n

def chronometre(f, t):
    """Duree (en secondes) de l'appel f(t)."""
    # A COMPLETER avec time.perf_counter()
    ...

def tableau_aleatoire(n):
    """Tableau de n temperatures au hasard entre 0 et 40."""
    t = []
    for k in range(n):
        t.append(random.uniform(0, 40))
    return t

def mesures(tailles):
    temps_naif = []
    temps_lin = []
    for n in tailles:
        t = tableau_aleatoire(n)
        # A COMPLETER : chronometrer variance_naive et variance sur t
        ...
    return temps_naif, temps_lin

def tracer(tailles, temps_naif, temps_lin):
    import matplotlib.pyplot as plt
    plt.plot(tailles, temps_naif, "o-", label="variance_naive")
    plt.plot(tailles, temps_lin, "s-", label="variance")
    plt.xlabel("taille n du tableau")
    plt.ylabel("temps (s)")
    plt.legend()
    plt.title("Linéaire contre quadratique")
    plt.show()

# ------------------------------------------------------------------
# Partie D -- Defi : la moyenne glissante sur k jours
# ------------------------------------------------------------------
def glissante_naive(t, k):
    # A COMPLETER
    ...

def glissante(t, k):
    # A COMPLETER
    ...

# ------------------------------------------------------------------
# Programme principal : decommentez les lignes au fur et a mesure
# ------------------------------------------------------------------
dates, tmin, tmax, pluie = charger_releves("tp_parcours_meteo.csv")
print(len(dates), "jours chargés ; premier jour :", dates[0], tmin[0], tmax[0], pluie[0])
# tester_partie_B()
# bulletin(dates, tmin, tmax, pluie)
# tailles = [250, 500, 1000, 2000, 4000]
# temps_naif, temps_lin = mesures(tailles)
# print(temps_naif)
# print(temps_lin)
# tracer(tailles, temps_naif, temps_lin)
