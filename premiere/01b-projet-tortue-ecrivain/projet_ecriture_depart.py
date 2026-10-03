# Projet "La tortue ecrivain" -- fichier de depart
# Nom, prenom : ...............................
#
# LE CONTRAT (a respecter par TOUTES les lettres, largeur larg) :
#   depart  : coin bas-gauche de la case, cap 0 (vers la droite), crayon leve
#   la lettre tient dans une case de largeur larg et de hauteur 2 * larg
#   arrivee : coin bas-gauche de la case SUIVANTE (larg + larg/2 plus a droite),
#             cap 0, crayon leve
# INTERDITS : goto, setposition, setpos, setx, sety, home, setheading, teleport.

import math
import turtle as t


# ------------------------------------------------------------ tests (fournis)
def case(larg):
    """Dessine en gris clair le quadrillage de la case et le point d'arrivee.
    Depart = arrivee : coin bas-gauche de la case, cap 0, crayon leve."""
    u = larg / 2
    couleur = t.pencolor()
    epaisseur = t.pensize()
    t.pencolor("lightgray")
    t.pensize(1)
    for i in range(5):            # 5 lignes verticales, tous les u/2
        t.left(90)
        t.pendown()
        t.forward(4 * u)
        t.penup()
        t.backward(4 * u)
        t.right(90)
        t.forward(u / 2)
    t.backward(5 * u / 2)         # retour au coin bas-gauche
    for i in range(9):            # 9 lignes horizontales, tous les u/2
        t.pendown()
        t.forward(2 * u)
        t.penup()
        t.backward(2 * u)
        t.left(90)
        t.forward(u / 2)
        t.right(90)
    t.right(90)
    t.forward(9 * u / 2)          # retour au coin bas-gauche
    t.left(90)
    t.forward(3 * u)
    t.dot(larg / 5, "lightgray")    # le point d'arrivee attendu
    t.backward(3 * u)
    t.pencolor(couleur)
    t.pensize(epaisseur)


def essayer(lettre, larg=50):
    """Test VISUEL : la case, la lettre, puis un tampon de la tortue.
    Contrat respecte si la fleche est sur le point gris et pointe vers la droite."""
    case(larg)
    lettre(larg)
    t.stamp()


def verifier(lettre, larg=50):
    """Test AUTOMATIQUE : dessine la lettre et verifie le contrat avec des assert.
    position() et heading() sont permis ICI, et nulle part ailleurs.
    On tolere 0.5 pixel d'ecart : les calculs a virgule sont approches."""
    x0, y0 = t.position()
    lettre(larg)
    x1, y1 = t.position()
    assert abs(x1 - (x0 + 3 * larg / 2)) < 0.5 and abs(y1 - y0) < 0.5, \
        "mauvaise position d'arrivee"
    ecart = t.heading() % 360
    assert ecart < 0.5 or ecart > 359.5, "la tortue ne regarde pas vers la droite"
    assert not t.isdown(), "le crayon doit etre leve a l'arrivee"


# ------------------------------------------------------------ outils (etape 3)
def trait(dx, dy):
    """Trace un segment de dx vers la droite et dy vers le haut.
    Le cap doit etre 0 avant ; il est de nouveau 0 apres."""
    angle = math.degrees(math.atan2(dy, dx))
    t.pendown()
    t.left(angle)
    t.forward(math.sqrt(dx ** 2 + dy ** 2))
    t.right(angle)


def saut(dx, dy):
    """Comme trait, mais sans tracer (crayon leve)."""
    t.penup()
    angle = math.degrees(math.atan2(dy, dx))
    t.left(angle)
    t.forward(math.sqrt(dx ** 2 + dy ** 2))
    t.right(angle)


# ------------------------------------------------------------ les lettres
def lettre_L(larg):
    """Dessine un L de largeur larg (contrat respecte)."""
    haut = 2 * larg    # hauteur de la lettre
    ecart = larg / 2   # espace avant la lettre suivante
    t.left(90)         # je regarde vers le haut
    t.forward(haut)    # je monte en haut de la case (crayon leve)
    t.pendown()
    t.backward(haut)   # je redescends en tracant la barre verticale
    t.right(90)        # je regarde de nouveau vers la droite
    t.forward(larg)    # barre du bas
    t.penup()
    t.forward(ecart)   # je rejoins la case suivante


def espace(larg):
    """Une case vide."""
    t.penup()
    t.forward(larg + larg / 2)


# A vous : lettre_E, lettre_H, lettre_I, lettre_T...


# ------------------------------------------------------------ programme principal
t.speed(0)             # 0 = le plus rapide (1 = lent, 10 = rapide)
t.penup()
t.backward(200)        # un peu a gauche du centre : je sais ou je suis !

essayer(lettre_L)      # test visuel
essayer(espace)
verifier(lettre_L)     # test automatique (rien ne s'affiche si tout va bien)

t.done()
