# TP -- Balles rebondissantes : la POO a la rescousse
# Fichier de depart : completer les parties marquees A COMPLETER ou A ECRIRE,
# puis relancer le fichier : les tests de la fin indiquent ce qui fonctionne.
#
# Lancer depuis Spyder : Executer > Configuration par fichier (Ctrl+F6),
# cocher "Executer dans une nouvelle console dediee", valider, puis F5.
# La constante ANIMATION choisit ce qui s'affiche apres les tests.

import random
import tkinter as tk

ANIMATION = 0      # 0 : tests seuls ; 1, 2 ou 3 : animation de la partie 1, 2 ou 3 ; 4 : partie 3 + collisions
LARGEUR = 600      # dimensions de la zone de jeu, en pixels
HAUTEUR = 400
DELAI = 20         # millisecondes entre deux images (50 images par seconde)
RAYON = 20         # rayon des balles des parties 1 et 2
NB_BALLES = 20     # nombre de balles de la partie 3
PESANTEUR = 0      # exercice 7 : essayer 0.3
COULEURS = ["tomato", "gold", "orange", "sky blue", "pale green", "orchid", "turquoise", "salmon"]
VITESSES = [v for v in range(-5, 6) if v != 0]      # -5 a 5, sauf 0


# ---------------------------------------------------------------------
# Fourni : la fenetre et les disques
# ---------------------------------------------------------------------
def creer_fenetre(titre):
    """Ouvre une fenetre contenant un canevas noir ; renvoie le couple (fenetre, canevas)."""
    fenetre = tk.Tk()
    fenetre.title(titre)
    canevas = tk.Canvas(fenetre, width=LARGEUR, height=HAUTEUR, bg="black", highlightthickness=0)
    canevas.pack()
    return fenetre, canevas


def dessiner_disque(canevas, x, y, rayon, couleur):
    """Dessine un disque de centre (x, y) ; renvoie son numero, qui sert a le deplacer ensuite."""
    return canevas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=couleur, outline="")


def placer_disque(canevas, disque, x, y, rayon):
    """Deplace le disque de numero disque pour que son centre soit en (x, y)."""
    canevas.coords(disque, x - rayon, y - rayon, x + rayon, y + rayon)


# ---------------------------------------------------------------------
# Partie 1 -- Une balle, sans objet
# ---------------------------------------------------------------------
def animer1(fenetre, canevas, disque, x, y, vx, vy):
    """Calcule l'image suivante, puis se reprogramme dans DELAI millisecondes."""
    # A COMPLETER (exercice 1) : deplacer la balle, puis la faire rebondir sur les quatre bords

    placer_disque(canevas, disque, x, y, RAYON)
    fenetre.after(DELAI, animer1, fenetre, canevas, disque, x, y, vx, vy)


def lancer1():
    """Partie 1 : une balle."""
    fenetre, canevas = creer_fenetre("Partie 1 : une balle")
    x, y, vx, vy = 300, 200, 4, -3
    disque = dessiner_disque(canevas, x, y, RAYON, "sky blue")
    fenetre.after(DELAI, animer1, fenetre, canevas, disque, x, y, vx, vy)
    fenetre.mainloop()


# ---------------------------------------------------------------------
# Partie 2 -- Deux balles, puis trois
# ---------------------------------------------------------------------
# A ECRIRE (exercice 2) : une fonction animer2 et la fonction lancer2 ci-dessous,
# en partant d'une copie de animer1 et de lancer1.

def lancer2():
    """A ECRIRE (exercice 2). Partie 2 : deux balles."""
    print("lancer2 n'est pas encore ecrite")


# ---------------------------------------------------------------------
# Partie 3 -- La POO a la rescousse
# ---------------------------------------------------------------------
class Balle:
    """Une balle : position (x, y), vitesse (vx, vy) en pixels par image, rayon et couleur."""

    def __init__(self, x, y, vx, vy, rayon, couleur):
        """A COMPLETER (exercice 4). Cree les six attributs de la balle."""
        ...

    def deplacer(self):
        """A COMPLETER (exercice 5). Avance d'un pas : la position augmente de la vitesse."""
        ...

    def rebondir_murs(self, largeur, hauteur):
        """A COMPLETER (exercice 5). Inverse vx (ou vy) si la balle touche un bord en allant vers lui."""
        ...

    # A ECRIRE (exercice 7) : la methode subir_pesanteur(self, g)

    # A ECRIRE (exercice 8) : les methodes touche(self, autre) et se_rapprochent(self, autre)


def balle_au_hasard(largeur, hauteur):
    """A COMPLETER (exercice 6). Renvoie une Balle au hasard, entierement dans la zone largeur x hauteur."""
    ...


def creer_balles(nb, largeur, hauteur):
    """A COMPLETER (exercice 6). Renvoie une liste de nb balles au hasard, toutes differentes."""
    ...


# ---------------------------------------------------------------------
# Partie 4 -- Collisions entre balles
# ---------------------------------------------------------------------
def gerer_collisions(balles):
    """A COMPLETER (exercice 8). Echange les vitesses de chaque paire de balles qui se touchent en se rapprochant."""
    ...


# ---------------------------------------------------------------------
# Vos tests (exercice 5) : pour chaque methode ecrite, trois assert
# (un cas normal, un cas limite, un cas piege)
# ---------------------------------------------------------------------
def mes_tests():
    """A COMPLETER : vos propres assert, par exemple
    b = Balle(...) ; b.rebondir_murs(600, 400) ; assert b.vx == ..."""
    ...


# ---------------------------------------------------------------------
# Fourni : l'animation de la partie 3 (et 4)
# ---------------------------------------------------------------------
def animer3(fenetre, canevas, balles, disques, collisions):
    """Image suivante pour toute la liste de balles, puis se reprogramme."""
    for i in range(len(balles)):
        b = balles[i]
        # exercice 7 : ajouter ici l'appel a subir_pesanteur
        b.deplacer()
        b.rebondir_murs(LARGEUR, HAUTEUR)
        placer_disque(canevas, disques[i], b.x, b.y, b.rayon)
    if collisions:
        gerer_collisions(balles)
    fenetre.after(DELAI, animer3, fenetre, canevas, balles, disques, collisions)


def lancer3(collisions):
    """Partie 3 (et 4 si collisions vaut True) : NB_BALLES balles."""
    balles = creer_balles(NB_BALLES, LARGEUR, HAUTEUR)
    fenetre, canevas = creer_fenetre(f"{NB_BALLES} balles")
    disques = [dessiner_disque(canevas, b.x, b.y, b.rayon, b.couleur) for b in balles]
    fenetre.after(DELAI, animer3, fenetre, canevas, balles, disques, collisions)
    fenetre.mainloop()


# ---------------------------------------------------------------------
# Tests (ne pas modifier)
# ---------------------------------------------------------------------
def lancer_tests():
    def essai(nom, f):
        try:
            f()
            print("[OK]     ", nom)
        except Exception as e:
            print("[A FAIRE]", nom, "->", type(e).__name__, e)

    def t_constructeur():
        b = Balle(100, 50, 3, -2, 10, "gold")
        assert (b.x, b.y, b.vx, b.vy) == (100, 50, 3, -2)
        assert b.rayon == 10 and b.couleur == "gold"
        c = Balle(0, 0, 1, 1, 5, "red")
        assert b.x == 100, "deux balles doivent avoir chacune leurs attributs"
        assert c.x == 0

    def t_deplacer_rebondir():
        b = Balle(100, 50, 3, -2, 10, "gold")
        b.deplacer()
        assert (b.x, b.y) == (103, 48)
        assert (b.vx, b.vy) == (3, -2), "deplacer ne change pas la vitesse"
        b.rebondir_murs(600, 400)
        assert (b.vx, b.vy) == (3, -2), "loin des bords : pas de rebond"
        b = Balle(10, 200, -4, 1, 10, "gold")          # tangente au bord gauche, va vers lui
        b.rebondir_murs(600, 400)
        assert (b.vx, b.vy) == (4, 1)
        b = Balle(595, 395, 2, 3, 10, "gold")          # coin bas droit : deux rebonds
        b.rebondir_murs(600, 400)
        assert (b.vx, b.vy) == (-2, -3)
        b = Balle(598, 200, -3, 1, 10, "gold")         # deborde a droite mais repart deja
        b.rebondir_murs(600, 400)
        assert b.vx == -3, "une balle qui s'eloigne deja du bord ne doit pas rebondir"
        b = Balle(300, 5, 0, -2, 10, "gold")           # bord haut
        b.rebondir_murs(600, 400)
        assert b.vy == 2

    def t_hasard():
        for k in range(200):
            b = balle_au_hasard(600, 400)
            assert isinstance(b, Balle)
            assert 8 <= b.rayon <= 25
            assert b.rayon <= b.x <= 600 - b.rayon and b.rayon <= b.y <= 400 - b.rayon
            assert b.vx in VITESSES and b.vy in VITESSES
            assert b.couleur in COULEURS
        balles = creer_balles(20, 600, 400)
        assert len(balles) == 20
        assert balles[0] is not balles[1], "les 20 balles doivent etre 20 objets differents"
        assert len({(b.x, b.y, b.vx, b.vy) for b in balles}) > 1

    def t_pesanteur():
        b = Balle(100, 50, 3, -2, 10, "gold")
        b.subir_pesanteur(0.5)
        assert (b.vx, b.vy) == (3, -1.5)
        assert (b.x, b.y) == (100, 50), "la pesanteur change la vitesse, pas la position"
        b = Balle(300, 397, 1, 2, 10, "gold")          # enfoncee dans le sol, descend encore
        b.rebondir_murs(600, 400)
        assert b.vy == -2
        assert b.y == 390, "apres un rebond, la balle doit etre replacee contre le bord"
        b = Balle(-4, 200, -3, 0, 10, "gold")           # meme chose a gauche
        b.rebondir_murs(600, 400)
        assert (b.x, b.vx) == (10, 3)

    def t_touche():
        a = Balle(100, 100, 0, 0, 10, "gold")
        assert a.touche(Balle(125, 100, 0, 0, 15, "red"))          # tangentes
        assert not a.touche(Balle(126, 100, 0, 0, 15, "red"))
        assert a.touche(Balle(103, 104, 0, 0, 1, "red"))           # l'une dans l'autre
        assert not a.touche(Balle(120, 120, 0, 0, 10, "red"))      # 28,3 > 20 en diagonale
        assert a.touche(Balle(112, 116, 0, 0, 10, "red"))          # distance 20 en diagonale

    def t_collisions():
        a = Balle(100, 100, 3, 0, 10, "gold")
        b = Balle(118, 100, -2, 1, 10, "red")
        assert a.se_rapprochent(b) and b.se_rapprochent(a)
        gerer_collisions([a, b])
        assert (a.vx, a.vy, b.vx, b.vy) == (-2, 1, 3, 0), "les vitesses doivent etre echangees"
        gerer_collisions([a, b])                                    # elles s'eloignent maintenant
        assert (a.vx, a.vy, b.vx, b.vy) == (-2, 1, 3, 0), "pas de second echange"
        c = Balle(500, 300, 1, 1, 10, "blue")                       # loin des deux autres
        a = Balle(100, 100, 3, 0, 10, "gold")
        b = Balle(118, 100, -2, 1, 10, "red")
        gerer_collisions([c, a, b])
        assert (c.vx, c.vy) == (1, 1)
        assert (a.vx, b.vx) == (-2, 3)

    for nom, f in [("Exercice 4 : constructeur", t_constructeur),
                   ("Exercice 5 : deplacer et rebondir_murs", t_deplacer_rebondir),
                   ("Exercice 6 : balles au hasard", t_hasard),
                   ("Exercice 7 : pesanteur", t_pesanteur),
                   ("Exercice 8 : touche", t_touche),
                   ("Exercice 8 : collisions", t_collisions)]:
        essai(nom, f)


if __name__ == "__main__":
    mes_tests()
    lancer_tests()
    if ANIMATION == 1:
        lancer1()
    elif ANIMATION == 2:
        lancer2()
    elif ANIMATION == 3:
        lancer3(False)
    elif ANIMATION == 4:
        lancer3(True)
