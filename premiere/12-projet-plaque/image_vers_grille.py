"""
Outil : transformer une vraie IMAGE en grille de pixels.
Extension OCR - 1re NSI.  (Necessite la bibliotheque Pillow : PIL.)

Ce fichier fournit deux fonctions "boite a outils" :
  - charger_image_gris(fichier) : ouvre une image et renvoie une grille de
    niveaux de gris (des nombres de 0 = noir a 255 = blanc) ;
  - enregistrer_grille(grille, fichier) : sauvegarde une grille de 0/1 en .txt
    (utile pour garder une trace de la grille binarisee).

L'etape interessante -- la BINARISATION (gris -> 0/1 par un seuil) -- est
volontairement laissee a l'eleve dans l'activite.
"""

from PIL import Image


def charger_image_gris(fichier, hauteur_cible=40):
    """Ouvre l'image, la met en niveaux de gris, la reduit a une hauteur
    raisonnable, et renvoie une grille de nombres (0 a 255)."""
    im = Image.open(fichier).convert("L")          # "L" = niveaux de gris
    largeur, hauteur = im.size
    largeur_cible = largeur * hauteur_cible // hauteur
    im = im.resize((largeur_cible, hauteur_cible))
    gris = []
    for y in range(hauteur_cible):
        ligne = []
        for x in range(largeur_cible):
            ligne.append(im.getpixel((x, y)))
        gris.append(ligne)
    return gris


def enregistrer_grille(grille, fichier):
    """Sauvegarde une grille de 0/1 en texte ('#' = 1, '.' = 0)."""
    with open(fichier, "w", encoding="utf-8") as f:
        for ligne in grille:
            texte = ""
            for v in ligne:
                if v == 1:
                    texte = texte + "#"
                else:
                    texte = texte + "."
            f.write(texte + "\n")
