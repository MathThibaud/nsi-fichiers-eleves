# Corrigé testé de la feuille « Problèmes de synthèse » (Première)

# ---------- Problème 1 : le binaire avec des entiers ----------
def en_binaire(n):
    resultat = 0
    puissance = 1
    while n > 0:
        resultat = resultat + (n % 2) * puissance
        puissance = puissance * 10
        n = n // 2
    return resultat


def en_decimal(b):
    total = 0
    puissance = 1
    while b > 0:
        total = total + (b % 10) * puissance
        puissance = puissance * 2
        b = b // 10
    return total


def nb_bits(n):
    nb = 1
    while n >= 2:
        n = n // 2
        nb = nb + 1
    return nb


# ---------- Problème 2 : le bit de parité ----------
def nb_uns(n):
    nb = 0
    while n > 0:
        nb = nb + n % 2
        n = n // 2
    return nb


def bit_parite(n):
    return nb_uns(n) % 2


def emettre(n):
    return 2 * n + bit_parite(n)


def verifier(m):
    return nb_uns(m) % 2 == 0


# ---------- Problème 3 : entiers relatifs sur 8 bits ----------
def code_8bits(x):
    if x >= 0:
        return x
    return 256 + x


def valeur(v):
    if v < 128:
        return v
    return v - 256


def addition_8bits(a, b):
    return valeur((code_8bits(a) + code_8bits(b)) % 256)


# ---------- Problème 4 : le bulletin de notes ----------
def moyenne(t):
    s = 0
    for x in t:
        s = s + x
    return s / len(t)


def moyennes(notes):
    resultat = {}
    for nom in notes:
        resultat[nom] = moyenne(notes[nom])
    return resultat


def meilleur(notes):
    meilleur_nom = None
    meilleure_moy = -1
    for nom in notes:
        m = moyenne(notes[nom])
        if m > meilleure_moy:
            meilleur_nom = nom
            meilleure_moy = m
    return (meilleur_nom, meilleure_moy)


def nb_notes_sous(notes, seuil):
    nb = 0
    for nom in notes:
        for note in notes[nom]:
            if note < seuil:
                nb = nb + 1
    return nb


# ---------- Problème 5 : une image en noir et blanc ----------
def nb_noirs(image):
    nb = 0
    for ligne in image:
        for pixel in ligne:
            if pixel == 1:
                nb = nb + 1
    return nb


def negatif(image):
    return [[1 - pixel for pixel in ligne] for ligne in image]


def ligne_en_octet(ligne):
    v = 0
    for bit in ligne:
        v = 2 * v + bit
    return v


def compresser(image):
    return [ligne_en_octet(ligne) for ligne in image]


def octet_en_ligne(v):
    ligne = [0] * 8
    for i in range(7, -1, -1):
        ligne[i] = v % 2
        v = v // 2
    return ligne


def decompresser(octets):
    return [octet_en_ligne(v) for v in octets]


# ---------- tests ----------
assert en_binaire(13) == 1101 and en_binaire(0) == 0 and en_binaire(185) == 10111001
assert en_decimal(1101) == 13 and en_decimal(10111001) == 185 and en_decimal(0) == 0
for n in range(1, 300):
    assert en_decimal(en_binaire(n)) == n and nb_bits(n) == len(bin(n)) - 2
assert nb_bits(1) == 1 and nb_bits(255) == 8 and nb_bits(256) == 9

assert nb_uns(13) == 3 and nb_uns(0) == 0 and nb_uns(255) == 8
assert bit_parite(13) == 1 and emettre(13) == 27 and en_binaire(27) == 11011
assert verifier(27) and not verifier(27 ^ 4) and verifier(27 ^ 6)
for n in range(256):
    assert verifier(emettre(n))

assert code_8bits(-12) == 244 and en_binaire(244) == 11110100
assert code_8bits(-1) == 255 and code_8bits(-128) == 128 and code_8bits(127) == 127
assert valeur(244) == -12 and valeur(128) == -128
for x in range(-128, 128):
    assert valeur(code_8bits(x)) == x
    if x > 0:
        assert 255 - x + 1 == code_8bits(-x)
assert addition_8bits(12, -12) == 0 and addition_8bits(100, 50) == -106 and addition_8bits(127, 1) == -128

notes = {"Léa": [12, 15, 9], "Noé": [8, 11, 14, 10], "Zoé": [17, 13]}
assert moyennes(notes) == {"Léa": 12.0, "Noé": 10.75, "Zoé": 15.0}
assert meilleur(notes) == ("Zoé", 15.0)
assert nb_notes_sous(notes, 10) == 2

image = [[0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 1],
         [1, 0, 0, 1, 1, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 1, 0, 0]]
print("noirs", nb_noirs(image), "octets", compresser(image))
assert nb_noirs(negatif(image)) == 64 - nb_noirs(image)
assert decompresser(compresser(image)) == image
assert ligne_en_octet([1, 0, 1, 1, 1, 0, 0, 1]) == 185
assert octet_en_ligne(185) == [1, 0, 1, 1, 1, 0, 0, 1]
print("tous les tests passent")
