"""
TP Recherche textuelle --- fichier de depart.

On mesure le travail des algorithmes de recherche en COMPTANT les comparaisons
de caracteres (texte[...] compare a motif[...]), puis en chronometrant.

Placer dans le meme dossier le fichier texte "verne.txt" (voir l'enonce).
Completer les fonctions marquees "A completer", puis lancer le fichier.
"""

import random
import time


# ---------- Outils fournis ----------
def lire_texte(nom_fichier):
    """Renvoie le contenu du fichier texte (encodage UTF-8) sous forme de chaine."""
    with open(nom_fichier, encoding="utf-8") as f:
        return f.read()


def genome(n, graine=2026):
    """Brin d'ADN aleatoire de n bases (A, C, G, T), toujours le meme pour une graine donnee."""
    random.seed(graine)
    brin = ""
    for i in range(n):
        brin = brin + random.choice("ACGT")
    return brin


def chrono(fonction, *arguments):
    """Execute fonction(*arguments) ; renvoie le couple (resultat, duree en secondes)."""
    debut = time.perf_counter()
    resultat = fonction(*arguments)
    return resultat, time.perf_counter() - debut


def table_decalage(motif):
    """Table de Horspool (cours) : lettre -> distance a la fin (sauf la derniere lettre)."""
    m = len(motif)
    dec = {}
    for k in range(m - 1):
        dec[motif[k]] = m - 1 - k
    return dec


# ---------- A completer ----------
def naive_compte(motif, texte):
    """Recherche naive. Renvoie le couple (liste des positions, nombre de comparaisons)."""
    positions = []
    comp = 0
    # A completer
    return positions, comp


def horspool_compte(motif, texte):
    """Recherche de Horspool. Renvoie le couple (liste des positions, nombre de comparaisons)."""
    positions = []
    comp = 0
    # A completer
    return positions, comp


def toutes_positions(motif, texte):
    """Toutes les positions du motif (chevauchements compris), avec la methode find des chaines."""
    positions = []
    # A completer
    return positions


def moyenne_comparaisons(algo, texte, m, essais=5, graine=1):
    """Choisit au hasard 'essais' motifs de longueur m DANS le texte, et renvoie
    le nombre moyen de comparaisons de algo, divise par la longueur du texte."""
    random.seed(graine)
    # A completer
    return 0


# ---------- Tests ----------
def test_naive_compte():
    return naive_compte("ACG", "CAAGACG") == ([4], 9)


def test_naive_chevauchement():
    return naive_compte("AA", "AAAA")[0] == [0, 1, 2]


def test_horspool_compte():
    return horspool_compte("ACG", "CAAGACG") == ([4], 5)


def test_horspool_cours():
    return horspool_compte("MOTIF", "UN TEXTE AVEC UN MOTIF ICI") == ([17], 9)


def test_toutes_positions():
    return toutes_positions("AA", "AAAA") == [0, 1, 2]


def test_accord_naif_horspool():
    adn = genome(20000)
    motif = adn[1234:1244]
    positions_naif = naive_compte(motif, adn)[0]
    positions_horspool = horspool_compte(motif, adn)[0]
    return positions_naif != [] and positions_naif == positions_horspool


def tester():
    tests = [
        ("naive_compte", test_naive_compte),
        ("naive (chevauchement)", test_naive_chevauchement),
        ("horspool_compte", test_horspool_compte),
        ("horspool (cours)", test_horspool_cours),
        ("toutes_positions", test_toutes_positions),
        ("accord naif/horspool", test_accord_naif_horspool),
    ]
    for (nom, test) in tests:
        try:
            if test():
                resultat = "OK"
            else:
                resultat = "ECHEC"
        except Exception as erreur:
            resultat = "ERREUR (" + type(erreur).__name__ + ")"
        print(nom.ljust(22), resultat)


if __name__ == "__main__":
    tester()
