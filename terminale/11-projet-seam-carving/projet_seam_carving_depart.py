"""
Projet -- Seam carving : redimensionner une image sans la deformer.
Fichier de depart : completer les fonctions marquees A COMPLETER (voir la fiche),
puis relancer le fichier : les tests de la fin indiquent ce qui fonctionne.

Convention : une image est une liste de lignes, image[y][x] = (r, g, b),
ou x est la COLONNE et y la LIGNE (comme pixels[x, y] dans PIL).
Une matrice de nombres (niveaux de gris, energies, table M) suit la meme
convention : matrice[y][x].

Lancer :  python3 projet_seam_carving_depart.py
Necessite la bibliotheque Pillow (PIL) et l'image seam_carving_ballons.png.
"""
import time
from PIL import Image

NOM_IMAGE = "seam_carving_ballons.png"


# ---------------------------------------------------------------------
# Lecture et ecriture des images (fourni)
# ---------------------------------------------------------------------
def charger_image(nom):
    """Renvoie l'image sous forme de liste de lignes : image[y][x] = (r, g, b)."""
    img = Image.open(nom).convert("RGB")
    largeur, hauteur = img.size
    pixels = img.load()
    return [[pixels[x, y] for x in range(largeur)] for y in range(hauteur)]


def sauver_image(image, nom):
    """Enregistre une image donnee sous forme de liste de lignes de (r, g, b)."""
    hauteur, largeur = len(image), len(image[0])
    img = Image.new("RGB", (largeur, hauteur))
    pixels = img.load()
    for y in range(hauteur):
        for x in range(largeur):
            pixels[x, y] = image[y][x]
    img.save(nom)


def sauver_carte(matrice, nom):
    """Enregistre une matrice de nombres positifs en niveaux de gris
    (valeurs multipliees par 4 pour mieux voir, plafonnees a 255 = blanc)."""
    image = [[(min(4 * v, 255),) * 3 for v in ligne] for ligne in matrice]
    sauver_image(image, nom)


def marquer_couture(image, couture, couleur=(255, 0, 0)):
    """Renvoie une copie de l'image ou les pixels de la couture sont colories."""
    copie = [[p for p in ligne] for ligne in image]
    for y in range(len(copie)):
        copie[y][couture[y]] = couleur
    return copie


# ---------------------------------------------------------------------
# Partie 1 -- L'energie d'un pixel
# ---------------------------------------------------------------------
def gris(image):
    """Matrice des niveaux de gris : moyenne entiere (r + g + b) // 3."""
    # A COMPLETER
    ...


def energie(G):
    """Matrice des energies : |gris(droite) - gris(gauche)| + |gris(dessous) - gris(dessus)|.
    Au bord, un voisin absent est remplace par le pixel lui-meme."""
    # A COMPLETER
    ...


# ---------------------------------------------------------------------
# Partie 3 -- La table de programmation dynamique
# ---------------------------------------------------------------------
def table_cumul(E):
    """M[y][x] : energie minimale d'une couture qui part de la ligne 0
    et descend jusqu'au pixel (x, y)."""
    # A COMPLETER
    ...


# ---------------------------------------------------------------------
# Partie 4 -- Retrouver la couture (la remontee)
# ---------------------------------------------------------------------
def indice_du_min(ligne, debut, fin):
    """Indice du plus petit element de ligne[debut..fin] (bornes incluses) ;
    en cas d'egalite, le plus a gauche."""
    # A COMPLETER
    ...


def couture_min(M):
    """Liste des abscisses de la couture d'energie minimale, de la ligne 0
    a la derniere : couture[y] est la colonne du pixel retire a la ligne y."""
    # A COMPLETER
    ...


# ---------------------------------------------------------------------
# Partie 5 -- Supprimer des coutures, et comparer
# ---------------------------------------------------------------------
def supprimer_couture(matrice, couture):
    """Nouvelle matrice (image ou nombres) privee d'un element par ligne."""
    # A COMPLETER
    ...


def reduire_largeur(image, k):
    """Retire k coutures verticales, une par une, en recalculant tout a chaque fois."""
    # A COMPLETER
    ...


def recadrer(image, k):
    """Retire k colonnes sur les bords : k // 2 a gauche, le reste a droite."""
    # A COMPLETER
    ...


def mise_a_echelle(image, nouvelle_largeur):
    """Redimensionnement naif : la colonne x de la nouvelle image recopie
    la colonne x * largeur // nouvelle_largeur de l'ancienne."""
    # A COMPLETER
    ...


# =====================================================================
# Approfondissements : chaque groupe ne traite QUE sa partie
# =====================================================================

# --- Groupe A : coutures horizontales ---------------------------------
def transposer(matrice):
    """Echange lignes et colonnes : t[x][y] = matrice[y][x]."""
    # A COMPLETER
    ...


def reduire_hauteur(image, k):
    """Retire k coutures horizontales : on transpose, on reduit la largeur,
    on transpose a nouveau."""
    # A COMPLETER
    ...


def table_cumul_horizontale(E):
    """Version directe : M[y][x] = energie minimale d'une couture horizontale
    qui part de la colonne 0 et arrive au pixel (x, y)."""
    # A COMPLETER
    ...


# --- Groupe B : elargir une image -------------------------------------
def coutures_a_dupliquer(image, k):
    """Positions, dans l'image d'origine, des k coutures que l'on retirerait
    une a une : liste de k coutures (chacune : une abscisse d'origine par ligne)."""
    # A COMPLETER
    ...


def moyenne_pixels(p, q):
    """Pixel moyen de deux pixels (r, g, b)."""
    return ((p[0] + q[0]) // 2, (p[1] + q[1]) // 2, (p[2] + q[2]) // 2)


def elargir(image, k):
    """Ajoute k colonnes en dedoublant les k coutures de plus faible energie."""
    # A COMPLETER
    ...


def elargir_naif(image, k):
    """Premiere idee : k fois de suite, dedoubler la couture d'energie minimale."""
    # A COMPLETER
    ...


# --- Groupe C : proteger ou effacer une zone --------------------------
PROTECTION = 10 ** 6


def energie_modifiee(E, masque):
    """masque[y][x] vaut 1 (proteger), -1 (effacer) ou 0 (ne rien changer)."""
    # A COMPLETER
    ...


def masque_rectangle(hauteur, largeur, x1, y1, x2, y2, valeur):
    """Masque qui vaut valeur dans le rectangle [x1, x2] x [y1, y2], 0 ailleurs."""
    # A COMPLETER
    ...


def reduire_largeur_masque(image, k, masque):
    """Comme reduire_largeur, mais avec une energie modifiee par le masque."""
    # A COMPLETER
    ...


def effacer_zone(image, masque):
    """Retire des coutures tant qu'il reste un pixel marque -1 ; renvoie l'image
    et le nombre de coutures retirees."""
    # A COMPLETER
    ...


# --- Groupe D : glouton, recursif naif, memoise ---------------------
def couture_gloutonne(E):
    """On part du pixel le moins energetique de la ligne du haut, puis on
    descend vers le voisin du dessous le moins energetique."""
    # A COMPLETER
    ...


def energie_couture(E, couture):
    """Energie totale d'une couture."""
    # A COMPLETER
    ...


def cumul_rec(E, x, y):
    """Version recursive de M[y][x], sans memoire."""
    # A COMPLETER
    ...


def cumul_memo(E, x, y, memo=None):
    """Version recursive memoisee de M[y][x] (top-down)."""
    # A COMPLETER
    ...


def reduire_largeur_glouton(image, k):
    """Comme reduire_largeur, mais avec la couture gloutonne."""
    # A COMPLETER
    ...


# =====================================================================
# Tests (ne pas modifier)
# =====================================================================
E_MAIN = [[3, 1, 4, 1, 5],          # la table d'energies de l'exercice a la main
          [9, 2, 6, 5, 3],
          [5, 8, 9, 7, 9],
          [3, 2, 3, 8, 4]]

E_PIEGE = [[0, 5, 5, 5],            # groupe D
           [9, 9, 5, 5],
           [9, 9, 5, 5],
           [9, 9, 5, 5]]


def lancer_tests():
    """Lance tous les tests ; une ligne [OK] ou [A FAIRE] par partie."""
    def essai(nom, f):
        try:
            f()
            print("[OK]     ", nom)
        except Exception as e:
            print("[A FAIRE]", nom, "->", type(e).__name__, e)

    def t_gris():
        assert gris([[(10, 20, 31), (255, 255, 255)]]) == [[20, 255]]
        G = gris(photo)
        assert len(G) == 200 and len(G[0]) == 300

    def t_energie():
        G = [[10, 10, 50],
             [10, 20, 90],
             [10, 30, 90]]
        assert energie(G) == [[0, 50, 80], [10, 100, 110], [20, 90, 60]]
        assert energie([[7]]) == [[0]]

    def t_table():
        assert table_cumul(E_MAIN) == [[3, 1, 4, 1, 5],
                                       [10, 3, 7, 6, 4],
                                       [8, 11, 12, 11, 13],
                                       [11, 10, 14, 19, 15]]
        assert table_cumul([[7]]) == [[7]]

    def t_couture():
        assert indice_du_min([4, 2, 9, 2], 0, 3) == 1        # egalite : le plus a gauche
        assert indice_du_min([4, 2, 9, 2], 2, 3) == 3
        assert couture_min(table_cumul(E_MAIN)) == [1, 1, 0, 1]
        c = couture_min(table_cumul(energie(gris(photo))))
        assert len(c) == 200
        assert all([abs(c[y + 1] - c[y]) <= 1 for y in range(199)]), "couture non connexe"

    def t_supprimer():
        assert supprimer_couture([[1, 2, 3], [4, 5, 6]], [2, 0]) == [[1, 2], [5, 6]]
        petite = reduire_largeur(photo, 3)
        assert len(petite) == 200 and len(petite[0]) == 297

    def t_comparer():
        assert recadrer([[0, 1, 2, 3, 4, 5]], 3) == [[1, 2, 3]]
        assert mise_a_echelle([[0, 1, 2, 3, 4, 5]], 3) == [[0, 2, 4]]

    def t_groupe_a():
        assert transposer([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        petite = reduire_hauteur(photo, 2)
        assert len(petite) == 198 and len(petite[0]) == 300

    def t_groupe_b():
        c1, c2 = coutures_a_dupliquer(photo, 2)
        assert c1 == couture_min(table_cumul(energie(gris(photo))))
        assert all([c1[y] != c2[y] for y in range(200)]), "deux fois le meme pixel"
        grande = elargir(photo, 2)
        assert len(grande) == 200 and len(grande[0]) == 302

    def t_groupe_c():
        assert energie_modifiee([[1, 2]], [[1, -1]]) == [[1 + PROTECTION, 2 - PROTECTION]]
        assert masque_rectangle(2, 3, 1, 0, 2, 0, 1) == [[0, 1, 1], [0, 0, 0]]
        image, nb = effacer_zone(photo, masque_rectangle(200, 300, 10, 10, 11, 12, -1))
        assert nb == 2 and len(image[0]) == 298

    def t_groupe_d():
        assert couture_gloutonne(E_MAIN) == [1, 1, 0, 1]
        assert couture_gloutonne(E_PIEGE) == [0, 0, 0, 0]
        assert energie_couture(E_PIEGE, [0, 0, 0, 0]) == 27
        assert cumul_rec(E_MAIN, 1, 3) == 10
        assert [cumul_memo(E_MAIN, x, 3) for x in range(5)] == [11, 10, 14, 19, 15]

    for nom, f in [("Partie 1 : gris", t_gris), ("Partie 1 : energie", t_energie),
                   ("Partie 3 : table_cumul", t_table),
                   ("Partie 4 : indice_du_min et couture_min", t_couture),
                   ("Partie 5 : supprimer_couture et reduire_largeur", t_supprimer),
                   ("Partie 5 : recadrer et mise_a_echelle", t_comparer),
                   ("Groupe A : coutures horizontales", t_groupe_a),
                   ("Groupe B : elargir", t_groupe_b),
                   ("Groupe C : proteger, effacer", t_groupe_c),
                   ("Groupe D : glouton, recursif, memoise", t_groupe_d)]:
        essai(nom, f)


# ---------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------
photo = charger_image(NOM_IMAGE)      # la photo : 200 lignes de 300 pixels

if __name__ == "__main__":
    lancer_tests()
