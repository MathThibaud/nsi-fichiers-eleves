"""
Programmation dynamique --- Le plus grand carre blanc.
Trame du TP : ecrire les fonctions marquees A COMPLETER (voir la fiche).

Convention : un pixel a pour coordonnees (x, y) ou x est la COLONNE et y la LIGNE
(comme dans PIL). pgcb(x, y) est la taille du plus grand carre entierement blanc
dont le pixel (x, y) est le coin INFERIEUR DROIT.

Lancer :  python3 carre_blanc.py    (chaque test affiche OK, ou A FAIRE ou ECHEC)
Necessite la bibliotheque Pillow (PIL) et l'image carre_blanc.png.
"""
from PIL import Image

# ---------------------------------------------------------------------------
# Chargement de l'image (fourni)
# Defi : remplacer "carre_blanc.png" par "carre_blanc_grand.png".
# ---------------------------------------------------------------------------
NOM_IMAGE = "carre_blanc.png"
img = Image.open(NOM_IMAGE).convert("RGB")
pixels = img.load()
largeur, hauteur = img.size          # (600, 600) pour carre_blanc.png


# ---------------------------------------------------------------------------
# La fonction est_noir
# ---------------------------------------------------------------------------
def est_noir(x, y):
    """Renvoie True si le pixel (x, y) est noir (couleur (0, 0, 0))."""
    # A COMPLETER
    return False


# ---------------------------------------------------------------------------
# Version recursive (tres lente sur de grandes coordonnees)
# ---------------------------------------------------------------------------
def pgcb(x, y):
    """Taille du plus grand carre blanc de coin inferieur droit (x, y)."""
    # A COMPLETER
    return 0


# ---------------------------------------------------------------------------
# Memoisation (top-down)
# ---------------------------------------------------------------------------
def pgcb_memo(x, y, memo={}):
    """Meme calcul que pgcb, en memorisant les resultats dans memo."""
    # A COMPLETER
    return 0


# ---------------------------------------------------------------------------
# Chercher le plus grand carre de l'image
# ---------------------------------------------------------------------------
def total_pgcb():
    """Parcourt tous les pixels ; renvoie (taille, (x, y) du coin inferieur droit)."""
    # A COMPLETER
    return (0, (0, 0))


# ---------------------------------------------------------------------------
# Bonus : tabulation (bottom-up)
# ---------------------------------------------------------------------------
def pgcb_bottom_up():
    """Remplit la table S ligne par ligne ; renvoie (taille, coin (x, y))."""
    # A COMPLETER
    return (0, (0, 0))


# ---------------------------------------------------------------------------
# Tests (ne pas modifier) : valables pour l'image carre_blanc.png
# ---------------------------------------------------------------------------
def test_est_noir():
    return est_noir(0, 0) is True and est_noir(250, 250) is False


def test_pgcb():
    # (x, y, valeur attendue) : pixels proches d'un bord noir, calcul rapide
    for (x, y, attendu) in [(10, 10, 0), (40, 40, 1), (42, 42, 3), (45, 45, 6)]:
        if pgcb(x, y) != attendu:
            return False
    return True


def test_pgcb_memo():
    return pgcb_memo(250, 250, {}) == 21


def test_total_pgcb():
    return total_pgcb() == (200, (559, 239))


def test_pgcb_bottom_up():
    return pgcb_bottom_up() == (200, (559, 239))


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
    if NOM_IMAGE == "carre_blanc.png":
        lancer("est_noir", test_est_noir)
        lancer("pgcb (petits pixels)", test_pgcb)
        lancer("pgcb_memo", test_pgcb_memo)
        lancer("total_pgcb", test_total_pgcb)
        lancer("pgcb_bottom_up", test_pgcb_bottom_up)
    else:
        print("Image", NOM_IMAGE)
        print("total_pgcb()     :", total_pgcb())
        print("pgcb_bottom_up() :", pgcb_bottom_up())
