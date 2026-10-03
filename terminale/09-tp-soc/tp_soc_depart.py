"""
TP Systemes sur puce --- fichier de depart (partie C : tester la logique sur ordinateur).

Ce fichier s'execute sur l'ordinateur (Python habituel), PAS sur la carte micro:bit.
Les capteurs y sont SIMULES par des listes de mesures : on peut ainsi tester la
partie "decision" d'un programme embarque sans la carte, avec des donnees
reproductibles.

Completer les fonctions marquees "A completer", puis lancer le fichier.
"""

import math
import random


# ---------- Donnees simulees (fournies) ----------
def marche_simulee(duree=10, cadence=2, frequence=50, graine=1):
    """Liste des normes d'acceleration (en milli-g) mesurees pendant une marche :
    duree en secondes, cadence en pas par seconde, frequence = mesures par seconde.
    Au repos, la norme vaut environ 1000 (la pesanteur) ; chaque pas la fait
    osciller, et le capteur ajoute du bruit."""
    random.seed(graine)
    mesures = []
    for k in range(duree * frequence):
        t = k / frequence
        a = 1000 + 400 * math.sin(2 * math.pi * cadence * t) + random.randint(-120, 120)
        mesures.append(round(a))
    return mesures


def lumiere_simulee(graine=2):
    """Niveaux de lumiere (0 = noir, 255 = plein jour) releves en fin de journee :
    le jour baisse, puis le crepuscule hesite autour de 60, puis c'est la nuit."""
    random.seed(graine)
    niveaux = []
    for k in range(20):
        niveaux.append(200 - 7 * k)
    for k in range(30):
        niveaux.append(60 + random.randint(-15, 15))
    for k in range(20):
        niveaux.append(10 + random.randint(0, 10))
    return niveaux


# ---------- 1. Veilleuse ----------
def veilleuse_naive(lumiere, seuil=60):
    """Allumee (True) si et seulement si la lumiere est sous le seuil."""
    return lumiere < seuil


def veilleuse(lumiere, allumee, seuil_bas=40, seuil_haut=80):
    """Veilleuse a hysteresis : renvoie le nouvel etat (True = allumee).
    Sous seuil_bas on allume, au-dessus de seuil_haut on eteint,
    entre les deux on garde l'etat actuel."""
    # A completer
    return False


def simuler_veilleuse(niveaux, hysteresis):
    """Renvoie la liste des etats successifs de la veilleuse (fournie)."""
    etats = []
    allumee = False
    for n in niveaux:
        if hysteresis:
            allumee = veilleuse(n, allumee)
        else:
            allumee = veilleuse_naive(n)
        etats.append(allumee)
    return etats


def nb_basculements(etats):
    """Nombre de fois ou l'etat change entre deux mesures consecutives."""
    # A completer
    return 0


def nb_led(lumiere):
    """Nombre de LED a allumer (de 0 a 25) : 0 en plein jour (255), 25 dans le noir (0).
    Formule : (255 - lumiere) * 25 // 255."""
    # A completer
    return 0


# ---------- 2. Alarme de temperature ----------
def alarme(temp, en_alarme, seuil=30, retour=28):
    """Renvoie le nouvel etat de l'alarme : elle se declenche a partir de seuil,
    ne s'arrete qu'en redescendant a retour ou moins."""
    # A completer
    return False


def mise_a_jour(mini, maxi, temp):
    """Renvoie le couple (mini, maxi) mis a jour avec la nouvelle mesure temp."""
    # A completer
    return (mini, maxi)


# ---------- 3. Podometre ----------
def norme(x, y, z):
    """Norme du vecteur acceleration : racine carree de x^2 + y^2 + z^2."""
    # A completer
    return 0


def compter_pas_naif(normes, seuil=1200):
    """Compte un pas chaque fois que la norme FRANCHIT le seuil en montant."""
    # A completer
    return 0


def compter_pas(normes, haut=1250, bas=1050):
    """Compte un pas en passant au-dessus de haut ; on n'en compte un nouveau
    qu'apres etre redescendu sous bas."""
    # A completer
    return 0


# ---------- Tests ----------
def test_veilleuse():
    return (veilleuse(30, False) and not veilleuse(90, True)
            and veilleuse(60, True) and not veilleuse(60, False))


def test_nb_basculements():
    return nb_basculements([False, True, True, False]) == 2


def test_nb_led():
    return (nb_led(255), nb_led(0), nb_led(128)) == (0, 25, 12)


def test_alarme():
    return (alarme(31, False) and alarme(29, True)
            and not alarme(29, False) and not alarme(28, True))


def test_mise_a_jour():
    return mise_a_jour(20, 25, 27) == (20, 27) and mise_a_jour(20, 25, 18) == (18, 25)


def test_norme():
    return norme(0, 0, -1024) == 1024 and norme(300, 400, 0) == 500


def test_compter_pas_naif():
    return compter_pas_naif([1000, 1300, 1100, 1250, 900]) == 2


def test_compter_pas():
    return compter_pas([1000, 1300, 1100, 1300, 1000, 1300]) == 2


def tester():
    tests = [
        ("veilleuse", test_veilleuse),
        ("nb_basculements", test_nb_basculements),
        ("nb_led", test_nb_led),
        ("alarme", test_alarme),
        ("mise_a_jour", test_mise_a_jour),
        ("norme", test_norme),
        ("compter_pas_naif", test_compter_pas_naif),
        ("compter_pas", test_compter_pas),
    ]
    for (nom, test) in tests:
        try:
            if test():
                resultat = "OK"
            else:
                resultat = "ECHEC"
        except Exception as erreur:
            resultat = "ERREUR (" + type(erreur).__name__ + ")"
        print(nom.ljust(18), resultat)


if __name__ == "__main__":
    tester()
