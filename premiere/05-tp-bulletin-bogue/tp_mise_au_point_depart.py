"""TP "Le bulletin bogue" --- fichier de depart (1re NSI).

Un programmeur presse a ecrit ce module pour le logiciel de vie scolaire.
Il affirme : "j'ai teste, tout passe". Lancez :  python3 tp_mise_au_point_depart.py

Votre mission : specifier, tester, deboguer et securiser ces fonctions.
Ne modifiez pas ce fichier : travaillez sur une copie nommee bulletin.py.
"""


# ------------------------------------------------------------------
# 1. Moyenne simple
# ------------------------------------------------------------------
def moyenne(notes):
    # moyenne des notes
    somme = 0
    for i in range(1, len(notes)):
        somme = somme + notes[i]
    return somme / len(notes)


# ------------------------------------------------------------------
# 2. Moyenne avec coefficients
# ------------------------------------------------------------------
def moyenne_ponderee(notes, coefs):
    # moyenne en tenant compte des coefficients
    somme = 0
    for i in range(len(notes)):
        somme = somme + notes[i] * coefs[i]
    return somme / len(notes)


# ------------------------------------------------------------------
# 3. Arrondi pour le bulletin
# ------------------------------------------------------------------
def arrondi_demi(x):
    # arrondi au demi-point
    return int(x * 2) / 2


# ------------------------------------------------------------------
# 4. Nombre de notes d'au moins 10
# ------------------------------------------------------------------
def nb_admis(notes):
    # combien de notes sont au moins egales a 10
    nb = 0
    for x in notes:
        if x > 10:
            nb = nb + 1
    return nb


# ------------------------------------------------------------------
# 5. Rang d'une moyenne dans la classe
# ------------------------------------------------------------------
def rang(moyennes, m):
    # rang de la moyenne m parmi les moyennes de la classe
    r = 0
    for x in moyennes:
        if x >= m:
            r = r + 1
    return r


# ------------------------------------------------------------------
# 6. Nombre de progressions
# ------------------------------------------------------------------
def nb_progressions(notes):
    # combien de fois une note est meilleure que la precedente
    nb = 0
    for i in range(len(notes)):
        if notes[i] > notes[i - 1]:
            nb = nb + 1
    return nb


# ------------------------------------------------------------------
# 7. Premiere note sous un seuil
# ------------------------------------------------------------------
def premiere_sous(notes, seuil):
    # indice de la premiere note strictement inferieure au seuil
    i = 0
    while i < len(notes):
        if notes[i] < seuil:
            return i
    i = i + 1
    return None


# ------------------------------------------------------------------
# Le bulletin d'une eleve
# ------------------------------------------------------------------
def bulletin(nom, notes, coefs, moyennes_classe):
    m = arrondi_demi(moyenne_ponderee(notes, coefs))
    print("Bulletin de", nom)
    print("Moyenne :", m, "/ 20")
    print("Notes d'au moins 10 :", nb_admis(notes), "sur", len(notes))
    print("Progressions :", nb_progressions(notes))
    print("Rang :", rang(moyennes_classe, m), "sur", len(moyennes_classe))


# ------------------------------------------------------------------
# Les tests du programmeur presse (ils passent tous !)
# ------------------------------------------------------------------
assert moyenne([0, 10, 20]) == 10
assert moyenne_ponderee([12, 14], [1, 1]) == 13
assert arrondi_demi(12.5) == 12.5
assert nb_admis([8, 12, 15]) == 2
assert rang([12, 15, 9], 12) == 2
assert nb_progressions([8, 10, 12]) == 2
assert premiere_sous([5, 12, 14], 10) == 0
print("Tous les tests passent.")

bulletin("Lina", [15, 9, 12, 10], [1, 2, 1, 2], [13.5, 11.0, 15.0, 11.0, 8.5, 9.5])
