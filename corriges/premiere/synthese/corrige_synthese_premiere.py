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


# ---------- Problème 6 : le classement d'un cross ----------
def plus_rapide(table):
    """Renvoie le nom du coureur au plus petit temps.
    Precondition : table est une liste non vide de fiches {"nom", "classe", "temps"},
    les temps etant des entiers positifs (en secondes).
    Postcondition : le temps de la fiche renvoyee est inferieur ou egal a tous les autres."""
    assert len(table) > 0, "table vide"
    meilleur = table[0]
    for fiche in table:
        if fiche["temps"] < meilleur["temps"]:
            meilleur = fiche
    return meilleur["nom"]


def trier_par_temps(table):
    """Trie la table en place, par temps croissant (tri par insertion)."""
    for i in range(1, len(table)):
        fiche = table[i]
        j = i - 1
        while j >= 0 and table[j]["temps"] > fiche["temps"]:
            table[j + 1] = table[j]
            j = j - 1
        table[j + 1] = fiche


def position(t, x):
    """t est un tableau TRIE ; renvoie un indice de x dans t, ou -1 si x est absent."""
    deb = 0
    fin = len(t) - 1
    while deb <= fin:
        mil = (deb + fin) // 2
        if t[mil] == x:
            return mil
        elif x > t[mil]:
            deb = mil + 1
        else:
            fin = mil - 1
    return -1


# ---------- Problème 7 : les doublons d'une liste d'inscriptions ----------
def a_un_doublon(t):
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] == t[j]:
                return True
    return False


def a_un_doublon_trie(t):
    """t est trie ; renvoie True si deux cases sont egales."""
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False


def a_un_doublon_rapide(t):
    return a_un_doublon_trie(sorted(t))


def doublons(t):
    """t est un tableau TRIE ; renvoie, une seule fois chacune, les valeurs presentes au moins deux fois."""
    resultat = []
    for i in range(1, len(t)):
        nouveau = len(resultat) == 0 or resultat[-1] != t[i]
        if t[i] == t[i - 1] and nouveau:
            resultat.append(t[i])
    return resultat


# ---------- Problème 8 : les droits d'un fichier, en binaire ----------
def triplet_en_chiffre(triplet):
    """triplet : chaine de 3 caracteres comme "r-x" ; renvoie le chiffre (de 0 a 7)."""
    v = 0
    for c in triplet:
        bit = 0
        if c != "-":
            bit = 1
        v = 2 * v + bit
    return v


def code_droits(ligne):
    """ligne : les 10 caracteres de ls -l, par exemple "-rwxr-x---" ; renvoie "750"."""
    proprietaire = triplet_en_chiffre(ligne[1:4])
    groupe = triplet_en_chiffre(ligne[4:7])
    autres = triplet_en_chiffre(ligne[7:10])
    return str(proprietaire) + str(groupe) + str(autres)


def chiffre_en_triplet(d):
    triplet = ""
    if d // 4 == 1:
        triplet = triplet + "r"
    else:
        triplet = triplet + "-"
    if (d // 2) % 2 == 1:
        triplet = triplet + "w"
    else:
        triplet = triplet + "-"
    if d % 2 == 1:
        triplet = triplet + "x"
    else:
        triplet = triplet + "-"
    return triplet


def droits(code):
    """code : chaine de 3 chiffres comme "754" ; renvoie "rwxr-xr--"."""
    resultat = ""
    for c in code:
        resultat = resultat + chiffre_en_triplet(int(c))
    return resultat


# ---------- Problème 9 : un conseil de film ----------
def lire_reponses(url):
    reponses = {}
    for paire in url.split("?")[1].split("&"):
        morceaux = paire.split("=")
        reponses[morceaux[0]] = int(morceaux[1])
    return reponses


def distance2(film, profil):
    """Distance au carre entre un film et un profil (dictionnaires)."""
    somme = 0
    for critere in ["action", "humour", "emotion"]:
        somme = somme + (film[critere] - profil[critere]) ** 2
    return somme


def k_plus_proches(films, profil, k):
    dists = []
    for film in films:
        dists.append((distance2(film, profil), film))
    dists.sort(key=lambda couple: couple[0])
    return [film for (d, film) in dists[:k]]


def vote(classes):
    compte = {}
    for c in classes:
        if c in compte:
            compte[c] = compte[c] + 1
        else:
            compte[c] = 1
    meilleure = None
    for c in compte:
        if meilleure is None or compte[c] > compte[meilleure]:
            meilleure = c
    return meilleure


def conseils(films, profil, k):
    return [film["titre"] for film in k_plus_proches(films, profil, k)]


def genre_conseille(films, profil, k):
    voisins = k_plus_proches(films, profil, k)
    return vote([film["genre"] for film in voisins])


# ---------- Problème 10 : la soirée cinéma ----------
def soiree_gloutonne(duree_max, ordre):
    """ordre : liste de (titre, duree, points), deja rangee selon le critere."""
    choisis = []
    reste = duree_max
    for (titre, duree, pts) in ordre:
        if duree <= reste:
            choisis.append(titre)
            reste = reste - duree
    return choisis


def points_de(films, titres):
    total = 0
    for (titre, duree, points) in films:
        if titre in titres:
            total = total + points
    return total


def meilleure_soiree(films, duree_max):
    n = len(films)
    meilleur_choix = []
    meilleurs_points = 0
    for code in range(2 ** n):
        choix = []
        duree_totale = 0
        total_points = 0
        for i in range(n):
            if (code // 2 ** i) % 2 == 1:      # bit numero i du code
                titre, duree, pts = films[i]
                choix.append(titre)
                duree_totale = duree_totale + duree
                total_points = total_points + pts
        if duree_totale <= duree_max and total_points > meilleurs_points:
            meilleur_choix = choix
            meilleurs_points = total_points
    return meilleur_choix, meilleurs_points


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

# ---------- tests (problèmes 6 à 10) ----------
coureurs = [{"nom": "Inès", "classe": "1G1", "temps": 754},
            {"nom": "Hugo", "classe": "1G2", "temps": 712},
            {"nom": "Léna", "classe": "1G1", "temps": 803},
            {"nom": "Tom", "classe": "1G3", "temps": 698},
            {"nom": "Maël", "classe": "1G2", "temps": 745},
            {"nom": "Sara", "classe": "1G3", "temps": 731}]
assert plus_rapide(coureurs) == "Tom"
assert plus_rapide([{"nom": "Ana", "classe": "1G1", "temps": 900}]) == "Ana"
assert plus_rapide([{"nom": "A", "classe": "1G1", "temps": 900},
                    {"nom": "B", "classe": "1G1", "temps": 600}]) == "B"
trier_par_temps(coureurs)
assert [f["nom"] for f in coureurs] == ["Tom", "Hugo", "Sara", "Maël", "Inès", "Léna"]
temps = [f["temps"] for f in coureurs]
assert temps == [698, 712, 731, 745, 754, 803]
assert position(temps, 745) == 3 and position(temps, 760) == -1 and position(temps, 698) == 0

inscrits = ["lea.m", "tom.b", "ines.k", "hugo.p",
            "tom.b", "sara.d", "tom.b", "ines.k"]
assert a_un_doublon(inscrits) and not a_un_doublon(["a", "b", "c"]) and not a_un_doublon([])
assert not a_un_doublon_trie([])
assert not a_un_doublon_trie(["a"])
assert a_un_doublon_trie(["a", "a", "b"])
assert a_un_doublon_trie(["a", "b", "b"])
assert not a_un_doublon_trie(["a", "b", "c"])
assert a_un_doublon_rapide(inscrits)
assert doublons(sorted(inscrits)) == ["ines.k", "tom.b"]
assert doublons([]) == [] and doublons(["a"]) == []

assert triplet_en_chiffre("rwx") == 7 and triplet_en_chiffre("r-x") == 5 and triplet_en_chiffre("---") == 0
assert code_droits("-rwxr-x---") == "750" and code_droits("-rw-r-----") == "640"
assert code_droits("drwxr-xr-x") == "755"
assert droits("754") == "rwxr-xr--" and droits("640") == "rw-r-----"
for a in range(8):
    for b in range(8):
        for c in range(8):
            code = str(a) + str(b) + str(c)
            assert code_droits("-" + droits(code)) == code

profil = lire_reponses("https://www.cine.mc/conseil?action=8&humour=2&emotion=6")
assert profil == {"action": 8, "humour": 2, "emotion": 6}
films = [
    {"titre": "Les Pirates du lagon", "genre": "aventure", "action": 9, "humour": 4, "emotion": 3},
    {"titre": "Mission Mistral", "genre": "aventure", "action": 8, "humour": 1, "emotion": 5},
    {"titre": "Le Dîner raté", "genre": "comédie", "action": 1, "humour": 9, "emotion": 3},
    {"titre": "Coloc en folie", "genre": "comédie", "action": 3, "humour": 8, "emotion": 2},
    {"titre": "La Lettre", "genre": "drame", "action": 1, "humour": 2, "emotion": 9},
    {"titre": "Après l'orage", "genre": "drame", "action": 4, "humour": 1, "emotion": 8},
    {"titre": "Course contre la nuit", "genre": "aventure", "action": 9, "humour": 2, "emotion": 7}]
assert distance2(films[1], profil) == 2 and distance2(films[5], profil) == 21
assert conseils(films, profil, 3) == ["Mission Mistral", "Course contre la nuit", "Les Pirates du lagon"]
assert genre_conseille(films, profil, 3) == "aventure"
profil2 = {"action": 3, "humour": 4, "emotion": 7}
assert conseils(films, profil2, 3) == ["Après l'orage", "La Lettre", "Mission Mistral"]
assert genre_conseille(films, profil2, 3) == "drame"
assert [f["genre"] for f in k_plus_proches(films, profil2, 4)] == ["drame", "drame", "aventure", "aventure"]
assert genre_conseille(films, profil2, 4) == "drame"

soiree = [("Les Pirates du lagon", 60, 6), ("Le Dîner raté", 120, 9),
          ("La Lettre", 70, 5), ("Coloc en folie", 85, 6),
          ("Mission Mistral", 90, 8)]
g1 = soiree_gloutonne(240, sorted(soiree, key=lambda f: f[2], reverse=True))
g2 = soiree_gloutonne(240, sorted(soiree, key=lambda f: f[2] / f[1], reverse=True))
assert g1 == ["Le Dîner raté", "Mission Mistral"] and points_de(soiree, g1) == 17
assert g2 == ["Les Pirates du lagon", "Mission Mistral", "La Lettre"] and points_de(soiree, g2) == 19
assert meilleure_soiree(soiree, 240) == (["Les Pirates du lagon", "Coloc en folie", "Mission Mistral"], 20)
print("problèmes 6 à 10 : tous les tests passent")
