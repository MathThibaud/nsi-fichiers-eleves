# TP de fin de chapitre -- Piles et files au travail
# Fichier de depart : completer les parties marquees A COMPLETER.
# Lancer le fichier : les tests de la fin indiquent ce qui fonctionne deja.

import random
import time


# =====================================================================
# Partie 1 -- Deux implementations pour une meme interface
# =====================================================================

class Cellule:
    """Un maillon de liste chainee (comme dans le cours)."""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s


class PileListe:
    """La pile du cours, qui cache une list Python (fournie)."""
    def __init__(self):
        self._contenu = []
    def est_vide(self):
        return self._contenu == []
    def empiler(self, x):
        self._contenu.append(x)
    def depiler(self):
        if self.est_vide():
            raise IndexError("pile vide")
        return self._contenu.pop()
    def sommet(self):
        if self.est_vide():
            raise IndexError("pile vide")
        return self._contenu[-1]
    def taille(self):
        return len(self._contenu)


class FileListe:
    """La file du cours, qui cache une list Python (fournie)."""
    def __init__(self):
        self._contenu = []
    def est_vide(self):
        return self._contenu == []
    def enfiler(self, x):
        self._contenu.append(x)
    def defiler(self):
        if self.est_vide():
            raise IndexError("file vide")
        return self._contenu.pop(0)
    def taille(self):
        return len(self._contenu)


class PileChainee:
    """A COMPLETER : une pile qui cache une liste chainee de Cellule."""
    def __init__(self):
        self._tete = None
        self._taille = 0
    def est_vide(self):
        ...
    def empiler(self, x):
        ...
    def depiler(self):
        ...
    def sommet(self):
        ...
    def taille(self):
        ...


class FileChainee:
    """A COMPLETER : une file qui cache une liste chainee,
    avec un acces direct a la premiere ET a la derniere cellule."""
    def __init__(self):
        self._tete = None      # premiere cellule : on defile ici
        self._queue = None     # derniere cellule : on enfile ici
        self._taille = 0
    def est_vide(self):
        ...
    def enfiler(self, x):
        ...
    def defiler(self):
        ...
    def tete(self):
        ...
    def taille(self):
        ...


def tester_pile(Classe):
    """Teste n'importe quelle classe qui respecte l'interface d'une pile."""
    p = Classe()
    assert p.est_vide()
    for x in [5, 8, 3]:
        p.empiler(x)
    assert p.taille() == 3 and p.sommet() == 3
    assert p.depiler() == 3 and p.depiler() == 8
    p.empiler(1)
    assert p.depiler() == 1 and p.depiler() == 5
    assert p.est_vide() and p.taille() == 0
    try:
        p.depiler()
        assert False, "depiler une pile vide doit lever IndexError"
    except IndexError:
        pass
    return "OK"


def tester_file(Classe):
    """Teste n'importe quelle classe qui respecte l'interface d'une file."""
    f = Classe()
    assert f.est_vide()
    for x in [5, 8, 3]:
        f.enfiler(x)
    assert f.taille() == 3
    assert f.defiler() == 5 and f.defiler() == 8
    f.enfiler(1)
    assert f.defiler() == 3 and f.defiler() == 1
    assert f.est_vide()
    f.enfiler(9)           # la file doit rester utilisable une fois videe
    assert f.defiler() == 9
    try:
        f.defiler()
        assert False, "defiler une file vide doit lever IndexError"
    except IndexError:
        pass
    return "OK"


def chronometrer_file(Classe, n):
    """Temps (en secondes) pour enfiler puis defiler n entiers (fournie)."""
    f = Classe()
    debut = time.perf_counter()
    for i in range(n):
        f.enfiler(i)
    while not f.est_vide():
        f.defiler()
    return time.perf_counter() - debut


# =====================================================================
# Partie 2 -- Un verificateur de code et de pages HTML
# =====================================================================

def verifier_code(code):
    """A COMPLETER. Renvoie None si les ( ) [ ] { } du code Python sont bien
    apparies, sinon un message du type
    "ligne 2, colonne 16 : ']' ferme '(' ouvert ligne 2, colonne 11".
    Les chaines "..." ou '...' et les commentaires # sont ignores."""
    ...


ORPHELINES = ["br", "img", "hr", "input", "meta", "link"]

def extraire_balises(html):
    """Fournie. Liste des noms de balises d'une page HTML, en minuscules,
    precedes de '/' pour les fermantes, sans attributs ; les balises
    orphelines (sans fermante) sont ignorees.
    '<p class="x">Un <b>mot</b><br></p>' -> ['p', 'b', '/b', '/p']"""
    balises = []
    i = 0
    while i < len(html):
        if html[i] == "<":
            j = html.index(">", i)
            nom = html[i + 1:j].split()[0].rstrip("/")
            if nom.lstrip("/").lower() not in ORPHELINES:
                balises.append(nom.lower())
            i = j + 1
        else:
            i = i + 1
    return balises


def verifier_html(html):
    """A COMPLETER : True si les balises de la page sont bien imbriquees."""
    ...


# =====================================================================
# Partie 3 -- Une calculatrice
# =====================================================================

PRIORITE = {'+': 1, '-': 1, '*': 2, '/': 2}

def calculer(a, op, b):
    """Fournie : applique l'operateur op a a et b."""
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if b == 0:
        raise ZeroDivisionError("division par zero")
    return a / b


def evaluer_npi(expr):
    """A COMPLETER : evalue une expression en notation polonaise inverse
    ("5 1 2 + 4 * +" -> 17.0). Leve ValueError si l'expression est mal formee."""
    ...


def decouper(expr):
    """Fournie. '3*(4+12)' -> ['3', '*', '(', '4', '+', '12', ')']"""
    jetons = []
    nombre = ""
    for c in expr:
        if c.isdigit() or c == ".":
            nombre = nombre + c
        else:
            if nombre != "":
                jetons.append(nombre)
                nombre = ""
            if c in "+-*/()":
                jetons.append(c)
    if nombre != "":
        jetons.append(nombre)
    return jetons


def infixe_vers_npi(expr):
    """A COMPLETER : '(3 + 4) * 2' -> '3 4 + 2 *'"""
    ...


def calculatrice(expr):
    return evaluer_npi(infixe_vers_npi(expr))


# =====================================================================
# Partie 4 -- Annuler / Retablir
# =====================================================================

class Editeur:
    """A COMPLETER : un mini-editeur avec Ctrl+Z (annuler) et Ctrl+Y (retablir)."""
    def __init__(self):
        self.texte = ""
        self._annuler = PileChainee()     # les etats precedents du texte
        self._retablir = PileChainee()    # les etats annules
    def ecrire(self, s):
        ...
    def effacer(self, k):
        ...
    def annuler(self):
        ...
    def retablir(self):
        ...


# =====================================================================
# Partie 5 -- Simuler la file d'attente d'un guichet
# =====================================================================

# (heure d'arrivee en minutes, duree de service en minutes), par arrivee croissante
CLIENTS = [(0, 4), (1, 3), (2, 2), (3, 5), (5, 1),
           (6, 3), (6, 2), (9, 4), (12, 1), (13, 2)]


def simuler(clients, nb_guichets=1):
    """A COMPLETER. Renvoie le triplet
    (attente moyenne, attente maximale, longueur maximale de la file)."""
    ...


def generer_clients(n, proba, duree_max, graine):
    """Fournie : n clients ; a chaque minute, un client arrive avec la
    probabilite proba ; son service dure entre 1 et duree_max minutes.
    La graine rend le tirage reproductible."""
    random.seed(graine)
    clients = []
    t = 0
    while len(clients) < n:
        if random.random() < proba:
            clients.append((t, random.randint(1, duree_max)))
        t = t + 1
    return clients


# =====================================================================
# Tests : relancer le fichier apres chaque partie
# =====================================================================

def lancer_tests():
    def essai(nom, f):
        try:
            f()
            print("[OK]     ", nom)
        except Exception as e:
            print("[A FAIRE]", nom, "->", type(e).__name__, e)

    def t_pile():
        assert tester_pile(PileListe) == "OK"
        assert tester_pile(PileChainee) == "OK"

    def t_file():
        assert tester_file(FileListe) == "OK"
        assert tester_file(FileChainee) == "OK"

    def t_code():
        assert verifier_code("t = [x * (x + 1) for x in L]  # (\n") is None
        assert verifier_code('print("(" + str(len([1, 2)))') == \
            "ligne 1, colonne 26 : ')' ferme '[' ouvert ligne 1, colonne 21"
        assert verifier_code("x = (1 + 2\ny = 3\n") == \
            "ligne 1, colonne 5 : '(' jamais ferme"
        assert verifier_code("y = 3)") == "ligne 1, colonne 6 : ')' ne ferme rien"

    def t_html():
        assert verifier_html('<p class="a">Un <b>mot</b><br></p>') is True
        assert verifier_html('<p>Un <b>gras <i>italique</b></i></p>') is False
        assert verifier_html('<ul><li>un</li><li>deux</ul>') is False

    def t_npi():
        assert evaluer_npi("5 1 2 + 4 * +") == 17
        assert evaluer_npi("10 4 /") == 2.5
        assert evaluer_npi("7 2 - 3 *") == 15
        for mauvaise in ["3 +", "3 4 5 +"]:
            try:
                evaluer_npi(mauvaise)
                assert False, mauvaise + " devrait lever ValueError"
            except ValueError:
                pass

    def t_infixe():
        assert infixe_vers_npi("3 + 4 * 2") == "3 4 2 * +"
        assert infixe_vers_npi("(3 + 4) * 2") == "3 4 + 2 *"
        assert infixe_vers_npi("10 - 4 - 3") == "10 4 - 3 -"
        assert calculatrice("2 * (3 + 4) - 5 / (1 + 4)") == 13

    def t_editeur():
        ed = Editeur()
        for mot in ["Le", " chat", " dort", " bien"]:
            ed.ecrire(mot)
        ed.annuler()
        ed.annuler()
        assert ed.texte == "Le chat"
        ed.retablir()
        assert ed.texte == "Le chat dort"
        ed.ecrire(" mal")
        ed.retablir()                    # sans effet : l'avenir a ete efface
        assert ed.texte == "Le chat dort mal"
        ed.effacer(4)
        assert ed.texte == "Le chat dort"
        ed.annuler()
        assert ed.texte == "Le chat dort mal"

    def t_guichet():
        assert simuler(CLIENTS) == (7.9, 12, 6)
        assert simuler(CLIENTS, 2) == (0.9, 3, 2)

    for nom, f in [("Partie 1 : PileChainee", t_pile), ("Partie 1 : FileChainee", t_file),
                   ("Partie 2 : verifier_code", t_code), ("Partie 2 : verifier_html", t_html),
                   ("Partie 3 : evaluer_npi", t_npi), ("Partie 3 : infixe_vers_npi", t_infixe),
                   ("Partie 4 : Editeur", t_editeur), ("Partie 5 : simuler", t_guichet)]:
        essai(nom, f)


if __name__ == "__main__":
    lancer_tests()
