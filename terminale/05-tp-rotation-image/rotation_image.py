"""Rotation d'une image d'un quart de tour, facon diviser pour regner.
Trame du TP « Faire tourner une image » : remplacer chaque ... (A COMPLETER).
On represente une image carree n x n (n puissance de 2) par un tableau 2D :
image[i][j] est le pixel ligne i, colonne j.
Lancer :  python3 rotation_image.py    (chaque test affiche OK, ou A FAIRE ou ECHEC)
"""


# ---------------------------------------------------------------------------
# Exercice 2 : la fonction recursive rotation
# ---------------------------------------------------------------------------
def rotation(image, ligne, col, taille):
    """Fait tourner d'un quart de tour horaire, EN PLACE, le carre de cote
    taille dont le coin haut-gauche est (ligne, col)."""
    if taille == 1:              # condition d'arret : un seul pixel
        return
    demi = taille // 2
    # 1. tourner recursivement les 4 quadrants
    rotation(image, ligne,        col,        demi)   # haut-gauche
    rotation(image, ...,          ...,        demi)   # haut-droite  A COMPLETER
    rotation(image, ...,          ...,        demi)   # bas-gauche   A COMPLETER
    rotation(image, ligne + demi, col + demi, demi)   # bas-droite
    # 2. permuter les blocs (rotation horaire) : HG -> HD -> BD -> BG -> HG
    for i in range(demi):
        for j in range(demi):
            hg = image[ligne + i][col + j]
            hd = image[ligne + i][col + demi + j]
            bd = image[ligne + demi + i][col + demi + j]
            bg = image[ligne + demi + i][col + j]
            image[ligne + i][col + demi + j]        = hg    # HD <- HG
            image[ligne + demi + i][col + demi + j] = ...   # A COMPLETER
            image[ligne + demi + i][col + j]        = ...   # A COMPLETER
            image[ligne + i][col + j]               = bg    # HG <- BG


# ---------------------------------------------------------------------------
# Tests (ne pas modifier) : chaque test affiche OK, ou A FAIRE ou ECHEC
# ---------------------------------------------------------------------------
def rotation_reference(image):
    """Rotation horaire simple (hors diviser pour regner) : renvoie une
    NOUVELLE image ; sert a verifier la fonction rotation."""
    n = len(image)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(image[n - 1 - j][i])
        resultat.append(ligne)
    return resultat


def image_numerotee(n):
    """Image n x n dont les pixels sont numerotes 0, 1, 2, ..."""
    image = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(i * n + j)
        image.append(ligne)
    return image


def copie(image):
    """Copie d'une image (tableau 2D)."""
    resultat = []
    for ligne in image:
        resultat.append(list(ligne))
    return resultat


def test_rotation_2x2():
    img = [["A", "B"],
           ["C", "D"]]
    rotation(img, 0, 0, 2)
    return img == [["C", "A"],
                   ["D", "B"]]


def test_rotation_reference():
    for n in [2, 4, 8]:
        base = image_numerotee(n)
        travail = copie(base)
        rotation(travail, 0, 0, n)
        if travail != rotation_reference(base):
            return False
    return True


def test_quatre_rotations():
    n = 8
    base = image_numerotee(n)
    travail = copie(base)
    for k in range(4):
        rotation(travail, 0, 0, n)
    return travail == base and rotation_reference(base) != base


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
    lancer("rotation sur une image 2x2", test_rotation_2x2)
    lancer("rotation pour n = 2, 4, 8", test_rotation_reference)
    lancer("quatre rotations = image de depart", test_quatre_rotations)
