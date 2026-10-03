def lire_labyrinthe(nom_fichier):
    """Renvoie la grille du labyrinthe : une liste de chaînes de caractères,
    une par ligne du fichier"""
    grille = []
    with open(nom_fichier, encoding="utf-8") as fichier:
        for ligne in fichier:
            ligne = ligne.rstrip("\n")
            if ligne != "":
                grille.append(ligne)
    return grille


def trouver(grille, caractere):
    """Renvoie le couple (ligne, colonne) de la première case de la grille
    contenant caractere, ou None s'il n'y en a pas"""
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne] == caractere:
                return (ligne, colonne)
    return None


def cases_voisines(grille, case):
    """Renvoie la liste des cases qui ne sont pas des murs parmi les quatre
    cases voisines (haut, bas, gauche, droite) de case"""
    ligne, colonne = case
    candidates = [(ligne - 1, colonne), (ligne + 1, colonne),
                  (ligne, colonne - 1), (ligne, colonne + 1)]
    voisines = []
    for (l, c) in candidates:
        if 0 <= l < len(grille) and 0 <= c < len(grille[l]) and grille[l][c] != "#":
            voisines.append((l, c))
    return voisines


def construire_graphe(grille):
    """Renvoie le graphe du labyrinthe sous forme de dictionnaire : chaque case
    qui n'est pas un mur est associée à la liste de ses cases voisines"""
    graphe = {}
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if grille[ligne][colonne] != "#":
                graphe[(ligne, colonne)] = cases_voisines(grille, (ligne, colonne))
    return graphe


def plus_court_chemin(graphe, depart, arrivee):
    """Renvoie un plus court chemin (liste de cases) de depart à arrivee dans
    le graphe, ou None s'il n'y en a pas"""
    decouverts = [depart]
    en_attente = [depart]
    parent = {depart: None}
    while en_attente != []:
        sommet = en_attente.pop(0)
        if sommet == arrivee:
            chemin = [arrivee]
            while parent[chemin[0]] is not None:
                chemin.insert(0, parent[chemin[0]])
            return chemin
        for voisin in graphe[sommet]:
            if voisin not in decouverts:
                decouverts.append(voisin)       # question 2
                en_attente.append(voisin)       # on enfile
                parent[voisin] = sommet         # on note qui l'a découvert
    return None


def afficher_chemin(grille, chemin):
    """Affiche la grille en marquant par 'o' les cases du chemin (sauf
    l'entrée E et la sortie S)"""
    for ligne in range(len(grille)):
        texte = ""
        for colonne in range(len(grille[ligne])):
            caractere = grille[ligne][colonne]
            if (ligne, colonne) in chemin and caractere == " ":
                texte = texte + "o"
            else:
                texte = texte + caractere
        print(texte)


#############################################################################
# Fonction nécessaire pour la question 3                                    #
#############################################################################


def sortir(nom_fichier):
    """Cherche un plus court chemin de E à S dans le labyrinthe du fichier,
    l'affiche et renvoie le nombre de déplacements"""
    grille = lire_labyrinthe(nom_fichier)
    graphe = construire_graphe(grille)
    chemin = plus_court_chemin(graphe, trouver(grille, "E"), trouver(grille, "S"))
    if chemin is None:
        print("Pas de sortie !")
        return None
    afficher_chemin(grille, chemin)
    return len(chemin) - 1


def test_voisines():
    grille = lire_labyrinthe("petit.txt")
    assert cases_voisines(grille, (1, 1)) == [(2, 1), (1, 2)]
    assert cases_voisines(grille, (2, 5)) == [(1, 5), (3, 5)]
    assert cases_voisines(grille, (3, 3)) == [(3, 2)]
    assert cases_voisines(grille, (1, 3)) == [(1, 2), (1, 4)]


def test_chemin():
    grille = lire_labyrinthe("petit.txt")
    graphe = construire_graphe(grille)
    chemin = plus_court_chemin(graphe, (1, 1), (3, 5))
    assert chemin == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5)]
    assert plus_court_chemin(graphe, (1, 1), (1, 1)) == [(1, 1)]
    assert plus_court_chemin(graphe, (1, 1), (3, 3)) == [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
    # une case isolée : pas de chemin
    graphe[(9, 9)] = []
    assert plus_court_chemin(graphe, (1, 1), (9, 9)) is None


if __name__ == "__main__":
    test_voisines()
    test_chemin()
    print(sortir("labyrinthe.txt"), "déplacements")
