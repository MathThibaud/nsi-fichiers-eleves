def lire_escalier(nom):
    """Renvoie la liste des efforts des marches lus dans le fichier nom
    (un entier par ligne, de la marche du bas vers celle du haut)"""
    fichier = open(nom, "r", encoding="utf-8")
    couts = []
    for ligne in fichier:
        if ligne.strip() != "":
            couts.append(int(ligne))
    fichier.close()
    return couts


def effort_rec(couts, i):
    """Renvoie l'effort minimal pour arriver sur la marche i (effort de la
    marche i compris), en montant d'une ou de deux marches à la fois.
    Version récursive."""
    if i == 0 or i == 1:
        return couts[i]
    return couts[i] + min(effort_rec(couts, i - 1), effort_rec(couts, i - 2))


def effort_total_rec(couts):
    """Renvoie l'effort minimal pour atteindre le sommet, situé juste
    au-dessus de la dernière marche (escalier d'au moins 2 marches)"""
    n = len(couts)
    return min(effort_rec(couts, n - 1), effort_rec(couts, n - 2))


def effort_memo(couts, i, memo):
    """Même résultat que effort_rec(couts, i), mais chaque valeur calculée
    est mémorisée dans le dictionnaire memo (clé : i)"""
    if i == 0 or i == 1:
        return couts[i]
    if i in memo:
        return memo[i]
    memo[i] = couts[i] + min(effort_memo(couts, i - 1, memo), effort_memo(couts, i - 2, memo))
    return memo[i]


def effort_total_memo(couts):
    """Effort minimal pour atteindre le sommet, avec mémoïsation"""
    n = len(couts)
    memo = {}
    return min(effort_memo(couts, n - 1, memo), effort_memo(couts, n - 2, memo))


def effort_tab(couts):
    """Renvoie l'effort minimal pour atteindre le sommet, sans récursivité,
    en remplissant un tableau du bas vers le haut de l'escalier"""
    n = len(couts)
    e = [0] * n               # e[i] : effort minimal pour arriver sur la marche i
    e[0] = couts[0]
    e[1] = couts[1]
    for i in range(2, n):
        e[i] = couts[i] + min(e[i - 1], e[i - 2])
    return min(e[n - 1], e[n - 2])


def effort_glouton(couts):
    """Stratégie gloutonne : on commence par la moins pénible des deux
    premières marches, puis on pose toujours le pied sur la moins pénible
    des deux marches suivantes. Renvoie l'effort total obtenu."""
    n = len(couts)
    if couts[0] <= couts[1]:
        i = 0
    else:
        i = 1
    total = couts[i]
    while i < n - 2:
        if couts[i + 1] <= couts[i + 2]:
            i = i + 1
        else:
            i = i + 2
        total = total + couts[i]
    return total


#############################################################################
# Fonction nécessaire pour la question 2                                    #
#############################################################################

APPELS = [0]   # APPELS[0] compte les appels de la fonction effort_compte


def effort_compte(couts, i):
    """Version récursive naïve qui compte ses propres appels"""
    APPELS[0] = APPELS[0] + 1
    if i == 0 or i == 1:
        return couts[i]
    return couts[i] + min(effort_compte(couts, i - 1), effort_compte(couts, i - 2))


def compter_appels(n):
    """Renvoie le nombre d'appels récursifs nécessaires à la version naïve
    pour un escalier de n marches"""
    APPELS[0] = 0
    couts = [1] * n
    min(effort_compte(couts, n - 1), effort_compte(couts, n - 2))
    return APPELS[0]


def test_effort_rec():
    assert effort_rec([3, 2, 5], 0) == 3
    assert effort_rec([3, 2, 5], 2) == 7
    assert effort_total_rec([10, 15, 20]) == 15
    assert effort_total_rec([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_effort_memo():
    assert effort_total_memo([10, 15, 20]) == 15
    assert effort_total_memo([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert effort_total_memo([2, 1] * 50) == 50


def test_effort_tab():
    assert effort_tab([10, 15, 20]) == 15
    assert effort_tab([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert effort_tab([5, 5]) == 5
    assert effort_tab([2, 1] * 50) == 50


test_effort_rec()
test_effort_memo()
test_effort_tab()
for n in [10, 20, 25]:
    print(n, "marches :", compter_appels(n), "appels")
couts = lire_escalier("escalier.txt")
print("optimal (memo) :", effort_total_memo(couts))
print("optimal (tab)  :", effort_tab(couts))
print("glouton        :", effort_glouton(couts))
print("glouton [10, 15, 20] :", effort_glouton([10, 15, 20]))
