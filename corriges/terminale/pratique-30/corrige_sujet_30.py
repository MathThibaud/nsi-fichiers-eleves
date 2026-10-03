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
    resultat = ""
    for lettre in message:
        if "A" <= lettre <= "Z":
            rang = ord(lettre) - ord("A")
            nouveau = (rang + k) % 26
            resultat = resultat + chr(nouveau + ord("A"))
        else:
            resultat = resultat + lettre
    return resultat


def occurrences(texte):
    """Renvoie un dictionnaire dont les clés sont les lettres de A à Z
    présentes dans texte et les valeurs leur nombre d'apparitions"""
    occ = {}
    for lettre in texte:
        if "A" <= lettre <= "Z":
            if lettre in occ:
                occ[lettre] = occ[lettre] + 1
            else:
                occ[lettre] = 1
    return occ


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
        decalage = ord(cle[i % len(cle)]) - ord("A")
        rang = ord(message[i]) - ord("A")
        nouveau = (rang + decalage) % 26
        resultat = resultat + chr(nouveau + ord("A"))
    return resultat


def dechiffre_vigenere(message, cle):
    """Renvoie le message déchiffré du message chiffré par Vigenère avec la
    clé cle"""
    resultat = ""
    for i in range(len(message)):
        decalage = ord(cle[i % len(cle)]) - ord("A")
        rang = ord(message[i]) - ord("A")
        nouveau = (rang - decalage) % 26
        resultat = resultat + chr(nouveau + ord("A"))
    return resultat


def trouver_cle(chiffre):
    """Question 2 : la lettre la plus fréquente du chiffré est un E décalé"""
    lettre = lettre_plus_frequente(chiffre)
    return (ord(lettre) - ord("E")) % 26


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


test_cesar()
test_occurrences()
test_vigenere()
test_dechiffre_vigenere()
secret = lire_fichier("message_secret.txt")
k = trouver_cle(secret)
print("lettre la plus fréquente :", lettre_plus_frequente(secret), "-> clé", k)
print(cesar(secret, -k))
