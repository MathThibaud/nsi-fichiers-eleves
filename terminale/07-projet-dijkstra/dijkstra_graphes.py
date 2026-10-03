"""
Algorithme de Dijkstra --- plus court chemin dans un graphe pondere (poids >= 0).
Projet « L'algorithme de Dijkstra » (Terminale NSI).
Trame a completer : remplacer chaque ... (trous (a), (b), ... de la fiche)
et ecrire les fonctions marquees A COMPLETER.

Ce fichier contient :
  - deux graphes deja saisis (un petit, un plus gros) ;
  - dijkstra         : version avec listes d'adjacence (dictionnaire) ;
  - chemin           : reconstruction d'un plus court chemin ;
  - dijkstra_matrice : version avec matrice d'adjacence ;
  - des tests et l'affichage des resultats (quand vos fonctions sont justes,
    le fichier affiche les distances et les chemins : comparez avec vos tableaux).

Lancer :  python3 dijkstra_graphes.py    (chaque test affiche OK, ou A FAIRE ou ECHEC)
"""

# =====================================================================
#  1. LES GRAPHES (fournis)
# =====================================================================

# --- Petit graphe de la fiche (5 sommets) : dict sommet -> liste (voisin, poids)
G_petit = {
    'A': [('B', 6), ('D', 1)],
    'B': [('A', 6), ('D', 2), ('E', 2), ('C', 5)],
    'C': [('B', 5), ('E', 5)],
    'D': [('A', 1), ('B', 2), ('E', 1)],
    'E': [('D', 1), ('B', 2), ('C', 5)],
}

# --- Graphe plus lourd (8 sommets). On le construit a partir de la liste
#     des aretes, pour ne pas se tromper en recopiant (chaque arete
#     est ajoutee dans les deux sens : graphe NON oriente).
aretes = [
    ('A', 'B', 4), ('A', 'C', 3), ('B', 'C', 1), ('B', 'E', 4),
    ('C', 'D', 2), ('C', 'E', 5), ('D', 'E', 1), ('D', 'F', 6),
    ('E', 'F', 3), ('E', 'G', 2), ('F', 'G', 2), ('F', 'H', 3),
    ('G', 'H', 4),
]

sommets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def construire_graphe(sommets, aretes):
    """Renvoie un dictionnaire de listes d'adjacence (voisin, poids)."""
    G = {}
    for s in sommets:
        G[s] = []
    for (a, b, poids) in aretes:
        G[a].append((b, poids))
        G[b].append((a, poids))   # NON oriente : les deux sens
    return G


G_gros = construire_graphe(sommets, aretes)


# =====================================================================
#  2. DIJKSTRA --- version LISTES d'adjacence (dictionnaire)
# =====================================================================

def dijkstra(graphe, depart):
    """
    graphe : dict sommet -> liste de (voisin, poids), poids >= 0.
    Renvoie (distance, precedent) : deux dictionnaires.
    """
    distance = {s: float('inf') for s in graphe}
    distance[depart] = ...                       # (a)
    precedent = {s: None for s in graphe}
    a_traiter = list(graphe.keys())          # sommets pas encore fixes
    while a_traiter != []:
        # 1) choisir le sommet non traite de plus petite distance
        u = a_traiter[0]
        for s in a_traiter:
            if distance[s] < distance[u]:
                u = ...                          # (b)
        a_traiter.remove(u)
        # 2) relacher les aretes issues de u
        for (v, poids) in graphe[u]:
            if distance[u] + poids < ... :       # (c)
                distance[v] = ...                # (d)
                precedent[v] = ...               # (e)
    return distance, precedent


def chemin(precedent, depart, arrivee):
    """Reconstruit la liste des sommets d'un plus court chemin de depart
    a arrivee en remontant les precedents (None si arrivee non atteinte)."""
    # A COMPLETER
    return []


# =====================================================================
#  3. DIJKSTRA --- version MATRICE d'adjacence
# =====================================================================
#  La matrice M est carree : M[i][j] = poids de l'arete i--j, et 0 s'il
#  n'y a pas d'arete. Les sommets sont donc des INDICES (0, 1, 2, ...).

def matrice_depuis_aretes(sommets, aretes):
    """Construit la matrice d'adjacence ponderee (0 = pas d'arete). Fournie."""
    n = len(sommets)
    M = []
    for i in range(n):
        M.append([0] * n)
    for (a, b, poids) in aretes:
        i = sommets.index(a)
        j = sommets.index(b)
        M[i][j] = poids
        M[j][i] = poids
    return M


def dijkstra_matrice(M, depart):
    """
    M : matrice d'adjacence ponderee (M[u][v] = poids, 0 = pas d'arete).
    depart : indice du sommet de depart.
    Renvoie (distance, precedent) : deux listes indexees par les sommets.
    """
    n = len(M)
    distance = [float('inf')] * n
    distance[depart] = ...            # (a)
    precedent = [None] * n
    traite = [False] * n
    for etape in range(n):
        # 1) sommet non traite de plus petite distance
        u = -1
        for s in range(n):
            if not traite[s] and (u == -1 or distance[s] < distance[u]):
                u = ...               # (b)
        traite[u] = True
        # 2) relacher : on parcourt la ligne u de la matrice
        for v in range(n):
            if M[...][...] != 0 and not traite[v]:   # (c) : l'arete u--v existe-t-elle ?
                if distance[u] + M[u][v] < ... :      # (d)
                    distance[v] = ...                  # (e)
                    precedent[v] = ...                 # (f)
    return distance, precedent


# =====================================================================
#  4. TESTS ET AFFICHAGE (ne pas modifier)
# =====================================================================

M_gros = matrice_depuis_aretes(sommets, aretes)


def test_dijkstra():
    distance, precedent = dijkstra(G_petit, 'A')
    if distance != {'A': 0, 'B': 3, 'C': 7, 'D': 1, 'E': 2}:
        return False
    distance, precedent = dijkstra(G_gros, 'A')
    return distance == {'A': 0, 'B': 4, 'C': 3, 'D': 5, 'E': 6,
                        'F': 9, 'G': 8, 'H': 12}


def test_chemin():
    precedent = {'A': None, 'B': 'D', 'C': 'E', 'D': 'A', 'E': 'D'}
    if chemin(precedent, 'A', 'C') != ['A', 'D', 'E', 'C']:
        return False
    if chemin(precedent, 'A', 'A') != ['A']:
        return False
    precedent = {'A': None, 'B': 'A', 'Z': None}    # Z non atteint
    return chemin(precedent, 'A', 'Z') is None


def test_dijkstra_matrice():
    distance, precedent = dijkstra_matrice(M_gros, 0)
    return distance == [0, 4, 3, 5, 6, 9, 8, 12]


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
    return ok


if __name__ == "__main__":
    ok_dijkstra = lancer("dijkstra", test_dijkstra)
    ok_chemin = lancer("chemin", test_chemin)
    ok_matrice = lancer("dijkstra_matrice", test_dijkstra_matrice)

    if ok_dijkstra and ok_chemin:
        print()
        print("=== Petit graphe, depart A ===")
        distance, precedent = dijkstra(G_petit, 'A')
        print("distances :", distance)
        print("chemin A -> C :", chemin(precedent, 'A', 'C'))
        print()
        print("=== Gros graphe (8 sommets), depart A ===")
        distance, precedent = dijkstra(G_gros, 'A')
        for s in sommets:
            print("  A ->", s, ": cout", distance[s],
                  " chemin", "-".join(chemin(precedent, 'A', s)))

    if ok_dijkstra and ok_matrice:
        print()
        print("=== Meme gros graphe, version MATRICE ===")
        distance_M, precedent_M = dijkstra_matrice(M_gros, sommets.index('A'))
        distance, precedent = dijkstra(G_gros, 'A')
        memes = True
        for i in range(len(sommets)):
            print("  A ->", sommets[i], ": cout", distance_M[i])
            if distance[sommets[i]] != distance_M[i]:
                memes = False
        print("Les deux versions donnent-elles le meme resultat ?", memes)
