# Corrigé testé de la feuille « Problèmes de synthèse » (Terminale)
import random


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


def insere(a, x):
    if a is None:
        return Noeud(x)
    if x < a.valeur:
        a.gauche = insere(a.gauche, x)
    elif x > a.valeur:
        a.droite = insere(a.droite, x)
    return a


def infixe_dans(a, resultat):
    if a is not None:
        infixe_dans(a.gauche, resultat)
        resultat.append(a.valeur)
        infixe_dans(a.droite, resultat)


def tri_abr(tab):
    a = None
    for x in tab:
        a = insere(a, x)
    resultat = []
    infixe_dans(a, resultat)
    return resultat


def hauteur(a):
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droite))


def insere_doublons(a, x):
    if a is None:
        return Noeud(x)
    if x < a.valeur:
        a.gauche = insere_doublons(a.gauche, x)
    else:
        a.droite = insere_doublons(a.droite, x)
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

assert tri_abr([5, 3, 8, 1, 4]) == [1, 3, 4, 5, 8]
assert tri_abr([3, 1, 3]) == [1, 3]
a = None
for x in range(1, 101):
    a = insere(a, x)
print("hauteur trié 100 :", hauteur(a))
random.seed(1)
t = list(range(1, 101)); random.shuffle(t)
a = None
for x in t:
    a = insere(a, x)
print("hauteur mélangé 100 :", hauteur(a))
b = None
for x in [3, 1, 3]:
    b = insere_doublons(b, x)
r = []; infixe_dans(b, r); assert r == [1, 3, 3]

arbre = Noeud(1, Noeud(2, Noeud(4), Noeud(5, Noeud(7))), Noeud(3, None, Noeud(6, Noeud(8), Noeud(9))))
print(noeuds_par_niveau(arbre), largeur_max(arbre))
assert noeuds_par_niveau(arbre) == {1: 1, 2: 2, 3: 3, 4: 3}
assert largeur_max(arbre) == 3 and largeur_max(None) == 0
assert noeuds_par_niveau_pile(arbre) == noeuds_par_niveau(arbre)
print("tous les tests passent")
