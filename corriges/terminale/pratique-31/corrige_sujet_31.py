def lire_fichier(nom):
    """Renvoie le contenu du fichier texte nom, sans le saut de ligne final"""
    fichier = open(nom, "r", encoding="utf-8")
    texte = fichier.read()
    fichier.close()
    return texte.strip()


def recherche_naive(motif, texte):
    """Renvoie la liste, dans l'ordre croissant, de toutes les positions de
    texte où commence une occurrence de motif (méthode naïve)"""
    n = len(texte)
    m = len(motif)
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j = j + 1
        if j == m:
            positions.append(i)
    return positions


def table_decalage(motif):
    """Renvoie le dictionnaire des décalages de Boyer-Moore-Horspool : chaque
    lettre du motif, sauf la dernière, est associée à sa distance à la fin du
    motif (en cas de lettre répétée, on garde la plus proche de la fin)"""
    m = len(motif)
    dec = {}
    for k in range(m - 1):
        dec[motif[k]] = m - 1 - k
    return dec


def horspool(motif, texte):
    """Renvoie la liste, dans l'ordre croissant, de toutes les positions de
    texte où commence une occurrence de motif (algorithme de
    Boyer-Moore-Horspool)"""
    n = len(texte)
    m = len(motif)
    dec = table_decalage(motif)
    positions = []
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and texte[i + j] == motif[j]:
            j = j - 1
        if j < 0:
            positions.append(i)
        c = texte[i + m - 1]
        if c in dec:
            i = i + dec[c]
        else:
            i = i + m
    return positions


def comparaisons_naive(motif, texte):
    """Renvoie le nombre de comparaisons de caractères effectuées par la
    méthode naïve"""
    n = len(texte)
    m = len(motif)
    nb = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            nb = nb + 1
            if texte[i + j] != motif[j]:
                break
            j = j + 1
    return nb


def comparaisons_horspool(motif, texte):
    """Renvoie le nombre de comparaisons de caractères effectuées par
    l'algorithme de Boyer-Moore-Horspool"""
    n = len(texte)
    m = len(motif)
    dec = table_decalage(motif)
    nb = 0
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            nb = nb + 1
            if texte[i + j] != motif[j]:
                break
            j = j - 1
        c = texte[i + m - 1]
        if c in dec:
            i = i + dec[c]
        else:
            i = i + m
    return nb


#############################################################################
# Fonction nécessaire pour la question 4                                    #
#############################################################################


def comparer():
    """Compare le nombre de comparaisons des deux méthodes sur trois cas"""
    adn = lire_fichier("adn.txt")
    phrases = "UN PETIT CHAT GRIS DORT AU SOLEIL. " * 3000
    cas = [("GATTACA", adn),
           ("LE CHIEN NOIR", phrases),
           ("A" * 9 + "B", "A" * 100000)]
    for motif, texte in cas:
        print("motif de longueur", len(motif), "dans un texte de longueur", len(texte))
        print("  naïve    :", comparaisons_naive(motif, texte))
        print("  horspool :", comparaisons_horspool(motif, texte))


def test_recherche_naive():
    assert recherche_naive("ACG", "CAAGACG") == [4]
    assert recherche_naive("AA", "AAAA") == [0, 1, 2]
    assert recherche_naive("ABC", "AB") == []
    assert recherche_naive("ICI", "ICI ET LA, ICI") == [0, 11]


def test_table_decalage():
    assert table_decalage("MOTIF") == {"M": 4, "O": 3, "T": 2, "I": 1}
    assert table_decalage("GATTACA") == {"G": 6, "A": 2, "T": 3, "C": 1}
    assert table_decalage("A") == {}


def test_horspool():
    assert horspool("MOTIF", "UN TEXTE AVEC UN MOTIF ICI") == [17]
    assert horspool("ACGT", "GTACACGTAC") == [4]
    assert horspool("ABA", "ABABABA") == [0, 2, 4]
    assert horspool("AA", "AAAA") == [0, 1, 2]


def test_comparaisons():
    assert comparaisons_horspool("MOTIF", "UN TEXTE AVEC UN MOTIF ICI") == 9
    assert comparaisons_horspool("AB", "AAAA") == 3


test_recherche_naive()
test_table_decalage()
test_horspool()
test_comparaisons()
adn = lire_fichier("adn.txt")
print("GATTACA :", len(recherche_naive("GATTACA", adn)), "occurrences",
      recherche_naive("GATTACA", adn) == horspool("GATTACA", adn))
comparer()
