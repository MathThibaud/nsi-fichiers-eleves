"""
Lire une plaque d'immatriculation avec les k plus proches voisins.
Projet (suite de l'activite OCR) - 1re NSI.  TRAME a completer au fil de la fiche.

Ce fichier contient :
  - les fonctions FOURNIES (afficher_grille, decouper, redimensionner) ;
  - les fonctions A COMPLETER : remplacer chaque ... par votre code,
    en suivant les trous (a), (b), (c) de la fiche ;
  - des TESTS, en bas du fichier : chaque etape affiche [OK] ou [A FAIRE].
    Au debut, tout est A FAIRE : c'est normal.

Fichiers necessaires dans le meme dossier : votre ocr.py (complete lors du TP OCR),
image_vers_grille.py, caracteres_train.csv, plaque_photo.png
(et lettres/chiffres_train.csv pour l'experience "entrainement manuscrit").

    python3 plaque.py
"""

from ocr import charger, classer, afficher   # on REUTILISE le k-NN de l'activite
from image_vers_grille import charger_image_gris, enregistrer_grille


# =====================================================================
#  0. Binariser : gris (0-255) -> 0/1   (A COMPLETER)
# =====================================================================

def binariser(gris, seuil=100):
    """gris : grille de nombres 0-255. Renvoie une grille de 0/1."""
    grille = []
    for ligne in gris:
        nouvelle = []
        for valeur in ligne:
            if ...:                      # (a) A COMPLETER : le pixel est-il sombre ?
                nouvelle.append(1)       # encre
            else:
                nouvelle.append(0)       # fond
        grille.append(nouvelle)
    return grille


def afficher_grille(grille):
    """Affiche une grille de 0/1 (fourni)."""
    for ligne in grille:
        texte = ""
        for v in ligne:
            if v == 1:
                texte = texte + "#"     # encre
            else:
                texte = texte + "."     # fond
        print(texte)


# =====================================================================
#  1. Segmenter par projection   (A COMPLETER)
# =====================================================================

def segmenter(grille):
    """Renvoie la liste des (debut, fin) de colonnes de chaque caractere."""
    hauteur = len(grille)
    largeur = len(grille[0])
    encre = []
    for x in range(largeur):
        total = 0
        for y in range(hauteur):
            total = total + ...          # (b) A COMPLETER : le pixel (y, x)
        encre.append(total)
    segments = []
    x = 0
    while x < largeur:
        if encre[x] > 0:
            debut = x
            while x < largeur and encre[x] > 0:
                x = x + 1
            if x - debut >= 3:         # ignorer les traits trop fins (bruit)
                segments.append((debut, x))
        else:
            x = x + 1
    return segments


# =====================================================================
#  2. Normaliser en 14 x 14   (fourni)
# =====================================================================

def decouper(grille, debut, fin):
    """Extrait le caractere entre les colonnes debut et fin, recadre en hauteur."""
    colonnes = []
    for ligne in grille:
        colonnes.append(ligne[debut:fin])
    haut = 0
    while 1 not in colonnes[haut]:       # premiere ligne avec de l'encre
        haut = haut + 1
    bas = len(colonnes) - 1
    while 1 not in colonnes[bas]:        # derniere ligne avec de l'encre
        bas = bas - 1
    return colonnes[haut:bas + 1]


def redimensionner(sous_grille, N=14):
    """Ramene la sous-grille a N x N (moyenne par bloc) -> liste de N*N pixels."""
    h = len(sous_grille)
    w = len(sous_grille[0])
    vecteur = []
    for i in range(N):
        for j in range(N):
            # le bloc de la sous-grille qui devient le pixel (i, j)
            y0 = i * h // N
            y1 = max(y0 + 1, (i + 1) * h // N)
            x0 = j * w // N
            x1 = max(x0 + 1, (j + 1) * w // N)
            total = 0
            for y in range(y0, y1):
                for x in range(x0, x1):
                    total = total + sous_grille[y][x]
            aire = (y1 - y0) * (x1 - x0)
            if 2 * total >= aire:        # majorite d'encre
                vecteur.append(1)
            else:
                vecteur.append(0)
    return vecteur


# =====================================================================
#  3 et 4. Classer et assembler   (A COMPLETER)
# =====================================================================

def lire_plaque(fichier_image, exemples, seuil=100, k=3):
    grille = binariser(charger_image_gris(fichier_image), seuil)
    plaque = ""
    for debut, fin in segmenter(grille):
        caractere = redimensionner(decouper(grille, debut, fin))
        plaque = plaque + ...            # (c) A COMPLETER : la classe predite pour ce caractere
    return plaque


# =====================================================================
#  Tests (ne pas modifier)
# =====================================================================

T_GRIS = [[20, 20, 20, 20, 20, 20],
          [220, 220, 30, 30, 220, 220],
          [220, 220, 30, 30, 220, 220],
          [220, 220, 30, 30, 220, 220],
          [220, 220, 30, 30, 220, 220],
          [220, 220, 220, 220, 220, 220]]


def test_binariser():
    grille = binariser(T_GRIS, 100)
    assert grille[0] == [1, 1, 1, 1, 1, 1]
    assert grille[1] == [0, 0, 1, 1, 0, 0]
    assert grille[5] == [0, 0, 0, 0, 0, 0]


def test_segmenter():
    grille = [[1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 0]]
    assert segmenter(grille) == [(0, 3), (4, 9)]
    photo = binariser(charger_image_gris("plaque_photo.png"), 100)
    assert len(segmenter(photo)) == 7


def test_lire_plaque():
    imprime = charger("caracteres_train.csv")
    assert lire_plaque("plaque_photo.png", imprime) == "AB123CD"


def lancer(nom, test):
    try:
        test()
        print("[OK]      ", nom)
    except Exception:
        print("[A FAIRE] ", nom)


if __name__ == "__main__":
    lancer("Etape 0 : binariser", test_binariser)
    lancer("Etape 1 : segmenter (7 caracteres sur la photo)", test_segmenter)
    lancer("Etapes 3 et 4 : lire_plaque (necessite votre ocr.py complet)", test_lire_plaque)
    # Vos essais peuvent s'ecrire ci-dessous, dans ce bloc.
