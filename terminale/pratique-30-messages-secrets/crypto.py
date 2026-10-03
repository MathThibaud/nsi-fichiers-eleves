def lire_fichier(nom):
    """Renvoie le contenu du fichier texte nom, sans le saut de ligne final"""
    fichier = open(nom, "r", encoding="utf-8")
    texte = fichier.read()
    fichier.close()
    return texte.strip()


def cesar(message, k):
    """message est une chaîne en majuscules (sans accents). Renvoie le message
    dans lequel chaque lettre de A à Z est décalée de k rangs dans l'alphabet,
    de façon circulaire. Les autres caractères (espaces, ponctuation) restent
    inchangés."""
    pass  # A COMPLETER


def occurrences(texte):
    """Renvoie un dictionnaire dont les clés sont les lettres de A à Z
    présentes dans texte et les valeurs leur nombre d'apparitions"""
    pass  # A COMPLETER


def lettre_plus_frequente(texte):
    """Renvoie la lettre (de A à Z) la plus fréquente de texte"""
    occ = occurrences(texte)
    meilleure = ""
    nb_max = 0
    for lettre in occ:
        if occ[lettre] > nb_max:
            meilleure = lettre
            nb_max = occ[lettre]
    return meilleure


def vigenere(message, cle):
    """message et cle sont des chaînes de lettres majuscules, sans espace.
    Renvoie le message chiffré par Vigenère : la lettre d'indice i du message
    est décalée du rang (A=0, B=1, ..., Z=25) de la lettre d'indice
    i % len(cle) de la clé."""
    resultat = ""
    for i in range(len(message)):
        decalage = ord(cle[i % len(cle)])
        rang = ord(message[i]) - ord("A")
        nouveau = (rang + decalage) % 26
        resultat = resultat + chr(nouveau + ord("A"))
    return resultat


def dechiffre_vigenere(message, cle):
    """Renvoie le message déchiffré du message chiffré par Vigenère avec la
    clé cle"""
    pass  # A COMPLETER


def test_cesar():
    assert cesar("BONJOUR", 3) == "ERQMRXU"
    assert cesar("ZOO", 1) == "APP"
    assert cesar("SALUT, LES NSI !", 2) == "UCNWV, NGU PUK !"
    assert cesar(cesar("NSI", 5), -5) == "NSI"


def test_occurrences():
    assert occurrences("ABRACADABRA") == {"A": 5, "B": 2, "R": 2, "C": 1, "D": 1}
    assert occurrences("A B, A !") == {"A": 2, "B": 1}
    assert lettre_plus_frequente("ABRACADABRA") == "A"


def test_vigenere():
    assert vigenere("NSIROCKS", "CLE") == "PDMTZGMD"
    assert vigenere("AAAA", "BC") == "BCBC"


def test_dechiffre_vigenere():
    assert dechiffre_vigenere("PDMTZGMD", "CLE") == "NSIROCKS"
    assert dechiffre_vigenere(vigenere("TURING", "NSI"), "NSI") == "TURING"
