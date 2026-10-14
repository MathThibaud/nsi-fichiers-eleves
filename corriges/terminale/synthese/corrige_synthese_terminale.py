# Corrigé testé de la feuille « Problèmes de synthèse » (Terminale)
import random
import sqlite3


class Pile:
    def __init__(self):
        self._contenu = []

    def est_vide(self):
        return self._contenu == []

    def empiler(self, x):
        self._contenu.append(x)

    def depiler(self):
        return self._contenu.pop()

    def sommet(self):
        return self._contenu[-1]


class File:
    def __init__(self):
        self._contenu = []

    def est_vide(self):
        return self._contenu == []

    def enfiler(self, x):
        self._contenu.append(x)

    def defiler(self):
        return self._contenu.pop(0)


# ---------- Problème 1 : dérécursiver avec une pile ----------
def afficher_binaire(n):
    if n >= 2:
        afficher_binaire(n // 2)
    print(n % 2, end="")


def binaire(n):
    p = Pile()
    p.empiler(n % 2)
    n = n // 2
    while n > 0:
        p.empiler(n % 2)
        n = n // 2
    resultat = ""
    while not p.est_vide():
        resultat = resultat + str(p.depiler())
    return resultat


def binaire_avec_file(n):
    f = File()
    f.enfiler(n % 2)
    n = n // 2
    while n > 0:
        f.enfiler(n % 2)
        n = n // 2
    resultat = ""
    while not f.est_vide():
        resultat = resultat + str(f.defiler())
    return resultat


# ---------- Problème 2 : annuler et rétablir ----------
class Editeur:
    def __init__(self):
        self.texte = ""
        self.annulations = Pile()
        self.retablissements = Pile()

    def ecrire(self, mot):
        self.annulations.empiler(self.texte)
        self.texte = self.texte + mot
        self.retablissements = Pile()

    def annuler(self):
        if not self.annulations.est_vide():
            self.retablissements.empiler(self.texte)
            self.texte = self.annulations.depiler()

    def retablir(self):
        if not self.retablissements.est_vide():
            self.annulations.empiler(self.texte)
            self.texte = self.retablissements.depiler()


# ---------- Problème 3 : listes chaînées et récursivité ----------
class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s


def longueur(lst):
    if lst is None:
        return 0
    return 1 + longueur(lst.suivante)


def somme(lst):
    if lst is None:
        return 0
    return lst.valeur + somme(lst.suivante)


def contient(lst, x):
    if lst is None:
        return False
    if lst.valeur == x:
        return True
    return contient(lst.suivante, x)


def renverser_dans(lst, acc):
    if lst is None:
        return acc
    return renverser_dans(lst.suivante, Cellule(lst.valeur, acc))


def renverser(lst):
    return renverser_dans(lst, None)


def renverser_iteratif(lst):
    resultat = None
    while lst is not None:
        resultat = Cellule(lst.valeur, resultat)
        lst = lst.suivante
    return resultat


def en_liste(lst):
    if lst is None:
        return []
    return [lst.valeur] + en_liste(lst.suivante)


# ---------- Problème 4 : trier avec un ABR ----------
class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite


def inserer(a, x):
    """Insere x dans l'ABR a et renvoie l'arbre obtenu (fonction du cours)."""
    if a is None:
        return Noeud(x)
    if x < a.valeur:
        a.gauche = inserer(a.gauche, x)
    else:
        a.droite = inserer(a.droite, x)
    return a


def infixe_dans(a, resultat):
    if a is not None:
        infixe_dans(a.gauche, resultat)
        resultat.append(a.valeur)
        infixe_dans(a.droite, resultat)


def tri_abr(tab):
    a = None
    for x in tab:
        a = inserer(a, x)
    resultat = []
    infixe_dans(a, resultat)
    return resultat


def hauteur(a):
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droite))


def inserer_sans_doublon(a, x):
    """Variante : une valeur deja presente n'est pas ajoutee."""
    if a is None:
        return Noeud(x)
    if x < a.valeur:
        a.gauche = inserer_sans_doublon(a.gauche, x)
    elif x > a.valeur:
        a.droite = inserer_sans_doublon(a.droite, x)
    return a


# ---------- Problème 5 : la largeur d'un arbre ----------
def noeuds_par_niveau(a):
    compte = {}
    if a is None:
        return compte
    f = File()
    f.enfiler((a, 1))
    while not f.est_vide():
        n, niveau = f.defiler()
        if niveau in compte:
            compte[niveau] = compte[niveau] + 1
        else:
            compte[niveau] = 1
        if n.gauche is not None:
            f.enfiler((n.gauche, niveau + 1))
        if n.droite is not None:
            f.enfiler((n.droite, niveau + 1))
    return compte


def largeur_max(a):
    compte = noeuds_par_niveau(a)
    maxi = 0
    for niveau in compte:
        if compte[niveau] > maxi:
            maxi = compte[niveau]
    return maxi


def noeuds_par_niveau_pile(a):
    compte = {}
    if a is None:
        return compte
    p = Pile()
    p.empiler((a, 1))
    while not p.est_vide():
        n, niveau = p.depiler()
        if niveau in compte:
            compte[niveau] = compte[niveau] + 1
        else:
            compte[niveau] = 1
        if n.gauche is not None:
            p.empiler((n.gauche, niveau + 1))
        if n.droite is not None:
            p.empiler((n.droite, niveau + 1))
    return compte


# ---------- tests ----------
afficher_binaire(13); print()
assert binaire(13) == "1101" and binaire(0) == "0" and binaire(1) == "1" and binaire(8) == "1000"
assert binaire_avec_file(13) == "1011"
for n in range(200):
    assert binaire(n) == bin(n)[2:]

e = Editeur()
e.ecrire("Bon"); e.ecrire("jour"); assert e.texte == "Bonjour"
e.annuler(); assert e.texte == "Bon"
e.retablir(); assert e.texte == "Bonjour"
e.annuler(); e.ecrire("soir"); assert e.texte == "Bonsoir"
e.retablir(); assert e.texte == "Bonsoir"
e.annuler(); e.annuler(); assert e.texte == ""
e.annuler(); assert e.texte == ""

lst = Cellule(3, Cellule(1, Cellule(4, None)))
assert longueur(lst) == 3 and longueur(None) == 0
assert somme(lst) == 8 and contient(lst, 4) and not contient(lst, 5)
assert en_liste(renverser(lst)) == [4, 1, 3] and en_liste(lst) == [3, 1, 4]
assert renverser(None) is None
assert en_liste(renverser_iteratif(lst)) == [4, 1, 3] and renverser_iteratif(None) is None

assert tri_abr([5, 3, 8, 1, 4]) == [1, 3, 4, 5, 8]
assert tri_abr([3, 1, 3]) == [1, 3, 3]
a = None
for x in range(1, 101):
    a = inserer(a, x)
print("hauteur trié 100 :", hauteur(a))
random.seed(1)
t = [i for i in range(1, 101)]; random.shuffle(t)
a = None
for x in t:
    a = inserer(a, x)
print("hauteur mélangé 100 :", hauteur(a))
b = None
for x in [3, 1, 3]:
    b = inserer_sans_doublon(b, x)
r = []; infixe_dans(b, r); assert r == [1, 3]

arbre = Noeud(1, Noeud(2, Noeud(4), Noeud(5, Noeud(7))), Noeud(3, None, Noeud(6, Noeud(8), Noeud(9))))
print(noeuds_par_niveau(arbre), largeur_max(arbre))
assert noeuds_par_niveau(arbre) == {1: 1, 2: 2, 3: 3, 4: 3}
assert largeur_max(arbre) == 3 and largeur_max(None) == 0
assert noeuds_par_niveau_pile(arbre) == noeuds_par_niveau(arbre)
print("tests des problemes 1 a 5 : ok")


# ---------- Problème 6 : une médiathèque, de la table à l'objet ----------
SCHEMA = """
CREATE TABLE adherent (id_adherent INTEGER PRIMARY KEY, nom TEXT, prenom TEXT);
CREATE TABLE livre (id_livre INTEGER PRIMARY KEY, titre TEXT, auteur TEXT);
CREATE TABLE emprunt (id_emprunt INTEGER PRIMARY KEY,
                      id_adherent INTEGER REFERENCES adherent(id_adherent),
                      id_livre INTEGER REFERENCES livre(id_livre),
                      jour INTEGER, rendu INTEGER);
INSERT INTO adherent VALUES (1, 'Durand', 'Lina'), (2, 'Rossi', 'Marco'), (3, 'Durand', 'Paul');
INSERT INTO livre VALUES (10, 'Le Petit Prince', 'Saint-Exupéry'), (11, 'Vingt mille lieues sous les mers', 'Verne'),
                         (12, 'Les Misérables', 'Hugo'), (13, 'Le Tour du monde en 80 jours', 'Verne');
INSERT INTO emprunt VALUES (1, 1, 10, 3, 1), (2, 2, 11, 12, 0), (3, 1, 12, 20, 0),
                           (4, 3, 10, 25, 0), (5, 2, 13, 40, 0);
"""


class Emprunt:
    def __init__(self, numero, titre, jour):
        self.numero = numero
        self.titre = titre
        self.jour = jour

    def en_retard(self, aujourdhui):
        return aujourdhui - self.jour > 21


def titres_en_retard(lignes, aujourdhui):
    emprunts = [Emprunt(numero, titre, jour) for (numero, titre, jour) in lignes]
    return [e.titre for e in emprunts if e.en_retard(aujourdhui)]


# ---------- Problème 7 : ordonnancer des tâches dépendantes ----------
def successeurs(prerequis):
    succ = {}
    for t in prerequis:
        succ[t] = []
    for t in prerequis:
        for p in prerequis[t]:
            succ[p].append(t)
    return succ


def ordre_execution(prerequis):
    succ = successeurs(prerequis)
    attente = {}                      # nombre de prerequis non encore faits
    for t in prerequis:
        attente[t] = len(prerequis[t])
    f = File()
    for t in prerequis:
        if attente[t] == 0:
            f.enfiler(t)
    ordre = []
    while not f.est_vide():
        t = f.defiler()
        ordre.append(t)
        for s in succ[t]:
            attente[s] = attente[s] - 1
            if attente[s] == 0:
                f.enfiler(s)
    if len(ordre) < len(prerequis):
        return None                   # des taches s'attendent mutuellement
    return ordre


# ---------- Problème 8 : router des paquets ----------
reseau = {"R1": {"R2": 10, "R3": 100},
          "R2": {"R1": 10, "R4": 50, "R5": 100},
          "R3": {"R1": 100, "R4": 50},
          "R4": {"R2": 50, "R3": 50, "R5": 100},
          "R5": {"R2": 100, "R4": 100}}


def cout(debit):
    """debit en Mbit/s ; cout OSPF = 10**8 / debit en bit/s"""
    return 10**8 / (debit * 10**6)


def est_chemin(reseau, chemin):
    for i in range(len(chemin) - 1):
        if chemin[i + 1] not in reseau[chemin[i]]:
            return False
    return True


def cout_chemin(reseau, chemin):
    total = 0
    for i in range(len(chemin) - 1):
        total = total + cout(reseau[chemin[i]][chemin[i + 1]])
    return total


def meilleur_chemin(reseau, chemins):
    meilleur = None
    for c in chemins:
        if est_chemin(reseau, c):
            if meilleur is None or cout_chemin(reseau, c) < cout_chemin(reseau, meilleur):
                meilleur = c
    return meilleur


def sauts(reseau, depart):
    distance = {depart: 0}
    f = File()
    f.enfiler(depart)
    while not f.est_vide():
        r = f.defiler()
        for voisin in reseau[r]:
            if voisin not in distance:
                distance[voisin] = distance[r] + 1
                f.enfiler(voisin)
    return distance


# ---------- Problème 9 : RSA miniature et exponentiation rapide ----------
def expo_mod(a, k, n):
    if k == 0:
        return 1
    moitie = expo_mod(a, k // 2, n)
    carre = (moitie * moitie) % n
    if k % 2 == 0:
        return carre
    return (carre * a) % n


def nb_multiplications(k):
    if k == 0:
        return 0
    if k % 2 == 0:
        return nb_multiplications(k // 2) + 1
    return nb_multiplications(k // 2) + 2


# ---------- Problème 10 : détecter un plagiat ----------
def recherche_naive(motif, texte):
    """fonction du cours : liste des positions de motif dans texte"""
    n, m = len(texte), len(motif)
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and texte[i + j] == motif[j]:
            j += 1
        if j == m:
            positions.append(i)
    return positions


def plus_longue_naive(a, b):
    meilleure = ""
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            if j - i > len(meilleure) and recherche_naive(a[i:j], b) != []:
                meilleure = a[i:j]
    return meilleure


def plus_longue_dyn(a, b):
    n, m = len(a), len(b)
    L = [[0 for j in range(m + 1)] for i in range(n + 1)]
    lmax, fin = 0, 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                if L[i][j] > lmax:
                    lmax, fin = L[i][j], i
    return a[fin - lmax:fin]


# ---------- Problème 11 : une machine minuscule ----------
def executer(programme, x, max_pas):
    """renvoie la valeur finale du registre, ou None si plus de max_pas pas"""
    position = 0
    pas = 0
    while programme[position][0] != "stop" and pas < max_pas:
        instr = programme[position]
        if instr[0] == "ajoute":
            x = x + instr[1]
            position = position + 1
        elif instr[0] == "saute_si_nul":
            if x == 0:
                position = instr[1]
            else:
                position = position + 1
        elif instr[0] == "saute":
            position = instr[1]
        pas = pas + 1
    if programme[position][0] == "stop":
        return x
    return None


prog_a = [("saute_si_nul", 3), ("ajoute", -1), ("saute", 0), ("stop",)]
prog_b = [("saute_si_nul", 3), ("ajoute", -2), ("saute", 0), ("stop",)]


# ---------- tests des problèmes 6 à 11 ----------
base = sqlite3.connect(":memory:")
base.executescript(SCHEMA)
req2 = """SELECT livre.titre
FROM emprunt
JOIN adherent ON emprunt.id_adherent = adherent.id_adherent
JOIN livre ON emprunt.id_livre = livre.id_livre
WHERE adherent.nom = 'Durand' AND adherent.prenom = 'Lina';"""
print("P6 q2 :", base.execute(req2).fetchall())
assert base.execute(req2).fetchall() == [("Le Petit Prince",), ("Les Misérables",)]
req3 = """SELECT COUNT(*)
FROM emprunt
WHERE rendu = 0;"""
assert base.execute(req3).fetchall() == [(4,)]
req4 = """SELECT livre.auteur, COUNT(*)
FROM emprunt
JOIN livre ON emprunt.id_livre = livre.id_livre
GROUP BY livre.auteur
ORDER BY livre.auteur;"""
print("P6 q4 :", base.execute(req4).fetchall())
assert base.execute(req4).fetchall() == [("Hugo", 1), ("Saint-Exupéry", 2), ("Verne", 2)]
base.execute("""UPDATE emprunt
SET rendu = 1
WHERE id_emprunt = 2;""")
req5 = """SELECT emprunt.id_emprunt, livre.titre, emprunt.jour
FROM emprunt
JOIN livre ON emprunt.id_livre = livre.id_livre
WHERE emprunt.rendu = 0;"""
lignes = base.execute(req5).fetchall()
print("P6 q5 :", lignes)
assert lignes == [(3, "Les Misérables", 20), (4, "Le Petit Prince", 25), (5, "Le Tour du monde en 80 jours", 40)]
assert titres_en_retard(lignes, 47) == ["Les Misérables", "Le Petit Prince"]
assert titres_en_retard(lignes, 42) == ["Les Misérables"]
assert Emprunt(3, "x", 20).en_retard(42) and not Emprunt(3, "x", 21).en_retard(42)

taches = {"A": [], "B": ["A"], "C": ["A"], "D": ["B", "C"], "E": ["C"], "F": ["D", "E"]}
print("P7 :", successeurs(taches), ordre_execution(taches))
assert ordre_execution(taches) == ["A", "B", "C", "D", "E", "F"]
taches2 = {"A": ["F"], "B": ["A"], "C": ["A"], "D": ["B", "C"], "E": ["C"], "F": ["D", "E"]}
assert ordre_execution(taches2) is None
taches3 = {"G": [], "A": ["F"], "B": ["A"], "C": ["A"], "D": ["B", "C"], "E": ["C"], "F": ["D", "E"]}
assert ordre_execution(taches3) is None

print("P8 couts :", cout(10), cout(50), cout(100))
assert sauts(reseau, "R1") == {"R1": 0, "R2": 1, "R3": 1, "R4": 2, "R5": 2}
candidats = [["R1", "R2", "R5"], ["R1", "R3", "R4", "R5"], ["R1", "R2", "R4", "R5"],
             ["R1", "R3", "R4", "R2", "R5"], ["R1", "R4", "R5"]]
print("P8 :", [(c, cout_chemin(reseau, c)) for c in candidats if est_chemin(reseau, c)])
assert not est_chemin(reseau, ["R1", "R4", "R5"])
assert meilleur_chemin(reseau, candidats) == ["R1", "R3", "R4", "R5"]
assert cout_chemin(reseau, ["R1", "R3", "R4", "R5"]) == 4
assert cout_chemin(reseau, ["R1", "R2", "R5"]) == 11
del reseau["R3"]["R4"]
del reseau["R4"]["R3"]
print("P8 panne :", meilleur_chemin(reseau, candidats), sauts(reseau, "R1"))
assert meilleur_chemin(reseau, candidats) == ["R1", "R2", "R5"]

p, q, e = 11, 17, 7
n, phi = p * q, (p - 1) * (q - 1)
d = 23
assert (e * d) % phi == 1 and n == 187 and phi == 160
c = expo_mod(42, e, n)
print("P9 : c =", c, " dechiffre :", expo_mod(c, d, n), " mult(23) =", nb_multiplications(23), " mult(7) =", nb_multiplications(7))
assert c == pow(42, 7, 187) and expo_mod(c, d, n) == 42
for m in range(187):
    assert expo_mod(expo_mod(m, e, n), d, n) == m
for k in range(300):
    assert expo_mod(3, k, 1000) == pow(3, k, 1000)
message = [72, 105]
chiffre = [expo_mod(m, e, n) for m in message]
print("P9 message chiffre :", chiffre)
assert [expo_mod(x, d, n) for x in chiffre] == message

print("P10 :", plus_longue_dyn("ALGORITHME", "LOGARITHME"), plus_longue_naive("ALGORITHME", "LOGARITHME"))
assert plus_longue_dyn("ALGORITHME", "LOGARITHME") == "RITHME"
assert plus_longue_naive("ALGORITHME", "LOGARITHME") == "RITHME"
assert plus_longue_dyn("ABAB", "BABA") == "ABA" and plus_longue_naive("ABAB", "BABA") == "ABA"
assert plus_longue_dyn("abc", "xyz") == ""


def mot_aleatoire():
    """Mot aleatoire de 0 a 8 lettres prises dans "ab"."""
    mot = ""
    for _ in range(random.randint(0, 8)):
        mot = mot + random.choice("ab")
    return mot


random.seed(2)
for _ in range(300):
    a = mot_aleatoire()
    b = mot_aleatoire()
    assert len(plus_longue_dyn(a, b)) == len(plus_longue_naive(a, b))
    assert recherche_naive(plus_longue_dyn(a, b), a) != [] and recherche_naive(plus_longue_dyn(a, b), b) != []

print("P11 :", executer(prog_a, 3, 100), executer(prog_b, 4, 100), executer(prog_b, 3, 100), executer(prog_a, 0, 100))
assert executer(prog_a, 3, 100) == 0 and executer(prog_b, 4, 100) == 0
assert executer(prog_b, 3, 100) is None and executer(prog_b, 3, 10**5) is None
assert executer(prog_a, 50, 100) is None and executer(prog_a, 50, 1000) == 0
print("tous les tests passent")
