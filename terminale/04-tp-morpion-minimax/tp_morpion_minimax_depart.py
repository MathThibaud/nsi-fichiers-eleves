# TP -- Le morpion imbattable : l'algorithme minimax
# Fichier de depart : completer les parties marquees A COMPLETER,
# puis relancer le fichier : les tests de la fin indiquent ce qui fonctionne.
# (Certains tests explorent tout l'arbre du jeu : ils prennent quelques secondes.)

import time

VIDE = "."

# Les cases sont numerotees de 0 a 8 :
#    0 | 1 | 2
#   ---+---+---
#    3 | 4 | 5
#   ---+---+---
#    6 | 7 | 8
# Une grille est une liste de 9 caracteres : "X", "O" ou VIDE.

# Les 8 alignements gagnants : 3 lignes, 3 colonnes, 2 diagonales
LIGNES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
          (0, 3, 6), (1, 4, 7), (2, 5, 8),
          (0, 4, 8), (2, 4, 6)]


# ---------------------------------------------------------------------
# Fourni
# ---------------------------------------------------------------------
def grille_vide():
    return [VIDE] * 9


def depuis_texte(texte):
    """Construit une grille a partir d'une chaine de 9 caracteres, ex. "XOO.X....". """
    return [c for c in texte]


def afficher(grille):
    for i in range(0, 9, 3):
        print(" " + " | ".join(grille[i:i + 3]))
        if i < 6:
            print("---+---+---")


def adversaire(joueur):
    if joueur == "X":
        return "O"
    return "X"


# ---------------------------------------------------------------------
# Partie 1 -- Les regles du jeu
# ---------------------------------------------------------------------
def coups_possibles(grille):
    """A COMPLETER. Renvoie la liste croissante des numeros des cases vides."""
    ...


def gagnant(grille):
    """A COMPLETER. Renvoie "X" ou "O" si ce joueur a aligne trois symboles, None sinon."""
    ...


def est_finie(grille):
    """A COMPLETER. La partie est finie si quelqu'un a gagne ou si la grille est pleine."""
    ...


def jouer(grille, case, joueur):
    """A COMPLETER. Renvoie une NOUVELLE grille ou joueur a joue dans case.
    La grille de depart ne doit pas etre modifiee."""
    ...


# ---------------------------------------------------------------------
# Partie 3 -- Minimax (score_final sera modifiee a la partie 4)
# ---------------------------------------------------------------------
def score_final(grille):
    """A COMPLETER. Score d'une partie finie, du point de vue de X :
    1 si X a gagne, -1 si O a gagne, 0 en cas de match nul."""
    ...


def minimax(grille, joueur):
    """A COMPLETER. Valeur de la position quand joueur doit jouer et que les
    deux camps jouent parfaitement. X maximise le score, O le minimise."""
    ...


def minimax_compte(grille, joueur):
    """A COMPLETER. Comme minimax, mais renvoie le couple
    (score, nombre de positions examinees)."""
    ...


def nb_parties(grille, joueur):
    """A COMPLETER. Nombre de parties differentes possibles a partir de grille."""
    ...


def meilleur_coup(grille, joueur):
    """A COMPLETER. Renvoie la case a jouer : celle dont la valeur minimax est la
    meilleure pour joueur. En cas d'egalite, garder la premiere case trouvee."""
    ...


# ---------------------------------------------------------------------
# Defi 1 -- Elagage alpha-beta
# ---------------------------------------------------------------------
def alphabeta(grille, joueur, alpha, beta):
    """A COMPLETER (defi). Renvoie le couple (score, positions examinees).
    alpha : ce que X est deja sur d'obtenir ; beta : ce que O est deja sur d'obtenir.
    Appel initial : alphabeta(grille, joueur, -100, 100)."""
    ...


# ---------------------------------------------------------------------
# Defi 2 -- Profondeur limitee et fonction d'evaluation
# ---------------------------------------------------------------------
def evaluer(grille):
    """A COMPLETER (defi). Nombre d'alignements encore possibles pour X
    moins nombre d'alignements encore possibles pour O."""
    ...


def minimax_limite(grille, joueur, profondeur):
    """A COMPLETER (defi). Minimax qui s'arrete apres `profondeur` coups
    et estime alors la position avec evaluer."""
    ...


def meilleur_coup_limite(grille, joueur, profondeur):
    """A COMPLETER (defi). Comme meilleur_coup, mais avec minimax_limite."""
    ...


# ---------------------------------------------------------------------
# Fourni -- jouer contre la machine (a lancer apres la partie 3)
# ---------------------------------------------------------------------
def partie(humain="X"):
    grille = grille_vide()
    joueur = "X"
    while not est_finie(grille):
        afficher(grille)
        if joueur == humain:
            case = int(input(f"{joueur}, numero de case (0 a 8) : "))
            while case not in coups_possibles(grille):
                case = int(input("Case impossible, recommencer : "))
        else:
            debut = time.perf_counter()
            case = meilleur_coup(grille, joueur)
            print(f"La machine joue en {case} ({time.perf_counter() - debut:.2f} s)")
        grille = jouer(grille, case, joueur)
        joueur = adversaire(joueur)
        print()
    afficher(grille)
    g = gagnant(grille)
    if g is None:
        print("Match nul.")
    else:
        print(f"{g} a gagne.")


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

    def t_regles():
        g = depuis_texte("XOXOOX...")
        assert coups_possibles(g) == [6, 7, 8]
        assert coups_possibles(grille_vide()) == [i for i in range(9)]
        assert gagnant(g) is None
        assert gagnant(depuis_texte("XOXOOXX..")) is None
        assert gagnant(depuis_texte("XOX.OX.O.")) == "O"
        assert gagnant(depuis_texte("XO.OX...X")) == "X"
        assert est_finie(g) is False
        assert est_finie(depuis_texte("XOXXOOOXX")) is True      # grille pleine, nul
        assert est_finie(depuis_texte("XXXOO....")) is True
        h = jouer(g, 8, "X")
        assert h == depuis_texte("XOXOOX..X")
        assert g == depuis_texte("XOXOOX..."), "jouer ne doit pas modifier la grille de depart"

    def t_minimax():
        assert score_final(depuis_texte("XOX.OX.O.")) < 0
        assert score_final(depuis_texte("XOXXOOOXX")) == 0
        assert minimax(depuis_texte("XOXOOX..X"), "O") > 0      # partie deja gagnee par X
        assert minimax(depuis_texte("XOXOOX..."), "X") > 0
        assert minimax(depuis_texte("XOXOOXX.."), "O") < 0
        assert minimax(depuis_texte("X..OO.X.."), "X") == 0
        assert minimax(grille_vide(), "X") == 0

    def t_compter():
        assert minimax_compte(depuis_texte("XOXOOX..."), "X")[1] == 11
        assert nb_parties(depuis_texte("XOXOOX..."), "X") == 5
        s, v = minimax_compte(grille_vide(), "X")
        assert s == 0 and v == 549946
        assert nb_parties(grille_vide(), "X") == 255168

    def t_meilleur():
        assert meilleur_coup(depuis_texte("XOXOOX..."), "X") == 8   # gagner
        assert meilleur_coup(depuis_texte("X..OO.X.."), "X") == 5   # bloquer
        assert meilleur_coup(depuis_texte("XX..O...."), "O") == 2   # bloquer, cote O

    def t_rapide():
        assert score_final(depuis_texte("XO.OX...X")) == 10 + 4
        assert score_final(depuis_texte("XOX.OX.O.")) == -(10 + 3)
        assert meilleur_coup(depuis_texte("XOOX....."), "X") == 6   # gagner tout de suite
        assert meilleur_coup(depuis_texte("XXO..O..."), "X") == 8   # retarder la defaite

    def t_alphabeta():
        assert alphabeta(depuis_texte("XOXOOX..."), "X", -100, 100)[0] == minimax(depuis_texte("XOXOOX..."), "X")
        s, v = alphabeta(grille_vide(), "X", -100, 100)
        assert s == 0, "score faux sur la grille vide"
        assert v < 30000, "trop de positions examinees : " + str(v)

    def t_limite():
        assert evaluer(grille_vide()) == 0
        assert evaluer(jouer(grille_vide(), 4, "X")) == 4
        assert evaluer(jouer(grille_vide(), 0, "X")) == 3
        assert meilleur_coup_limite(grille_vide(), "X", 1) == 4
        assert meilleur_coup_limite(depuis_texte("X..OO.X.."), "X", 2) == 5
        assert minimax_limite(depuis_texte("XOXOOX..."), "X", 9) == minimax(depuis_texte("XOXOOX..."), "X")

    for nom, f in [("Partie 1 : regles du jeu", t_regles), ("Partie 3 : minimax", t_minimax),
                   ("Partie 3 : compter les positions", t_compter), ("Partie 3 : meilleur coup", t_meilleur),
                   ("Partie 4 : gagner vite, perdre tard", t_rapide), ("Defi 1 : alpha-beta", t_alphabeta),
                   ("Defi 2 : profondeur limitee", t_limite)]:
        essai(nom, f)


if __name__ == "__main__":
    lancer_tests()
