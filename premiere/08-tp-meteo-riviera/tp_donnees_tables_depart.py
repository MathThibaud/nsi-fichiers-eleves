"""TP de fin de chapitre "Donnees en tables" -- Les releves meteo de la Riviera.

Fichiers necessaires, dans le meme dossier que ce programme :
    releves_aout.csv  (releves quotidiens, separateur ;)
    stations.csv      (description des stations, separateur ;)
Les donnees sont fictives mais realistes (aout 2025).

Completer les fonctions dans l'ordre des parties du TP (remplacer les ...),
puis lancer le programme : en bas du fichier, chaque partie est testee et
affiche [OK] ou [A FAIRE]. Au debut, tout est A FAIRE : c'est normal.
"""

import csv


# ===================================================== Partie 1 : importer
def charger(fichier, separateur):
    """Renvoie la table (liste de dictionnaires) lue dans le fichier CSV."""
    with open(fichier, encoding="utf-8", newline="") as f:
        lecteur = csv.DictReader(f, delimiter=separateur)
        table = [ligne for ligne in lecteur]
    return table


def en_nombre(texte):
    """'23,4' -> 23.4 ; '' -> None (valeur manquante)."""
    ...


# ============================================= Partie 2 : controle qualite
def est_complete(ligne):
    """True si tmin, tmax et pluie sont toutes renseignees (non vides)."""
    ...


def compter_par_cle(table):
    """Dictionnaire {(station, date): nombre de lignes ayant cette cle}."""
    compteur = {}
    for ligne in table:
        cle = (ligne["station"], ligne["date"])
        ...
    return compteur


def doublons(table):
    """Liste des cles (station, date) presentes plus d'une fois."""
    ...


def est_coherente(ligne):
    """True si la ligne est complete, si tmin <= tmax, et si les deux
    temperatures sont entre -30 et 50 degres."""
    ...


def nettoyer(table):
    """Nouvelle table : lignes completes et coherentes seulement, une seule
    ligne par (station, date) (la premiere rencontree), valeurs numeriques
    converties en float."""
    propre = []
    deja_vus = {}
    for ligne in table:
        cle = (ligne["station"], ligne["date"])
        ...
    return propre


# ============================================ Partie 3 : interroger la table
def releves_de(table, station):
    """Les lignes de la table qui concernent cette station."""
    ...


def moyenne(table, descripteur):
    """Moyenne de la colonne descripteur (valeurs deja converties)."""
    ...


def jour_le_plus_chaud(table):
    """Triplet (station, date, tmax) de la ligne de tmax maximale."""
    ...


def compter_si(table, descripteur, seuil):
    """Nombre de lignes dont la valeur du descripteur est >= seuil."""
    ...


# ================================================ Partie 5 : croiser (cours)
def jointure(gauche, droite, cle):
    resultat = []
    for lg in gauche:
        for ld in droite:
            if lg[cle] == ld[cle]:
                fusion = dict(lg)
                for c in ld:
                    fusion[c] = ld[c]
                resultat.append(fusion)
    return resultat


# ================================================ Partie 6 : exporter
def en_texte(nombre):
    """23.4 -> '23,4' (virgule decimale, pour un tableur regle en francais)."""
    ...


def exporter(table, fichier, separateur):
    """Ecrit la table (liste de dictionnaires) dans un fichier CSV."""
    with open(fichier, "w", encoding="utf-8", newline="") as f:
        ecrivain = csv.DictWriter(f, fieldnames=[cle for cle in table[0]],
                                  delimiter=separateur)
        ecrivain.writeheader()
        ...


# ================================================ Tests (ne pas modifier)
def test_partie1():
    releves = charger("releves_aout.csv", ";")
    assert len(releves) == 193
    assert en_nombre("23,4") == 23.4
    assert en_nombre("0") == 0.0
    assert en_nombre("") is None


def test_partie2():
    releves = charger("releves_aout.csv", ";")
    assert est_complete({"tmin": "21,0", "tmax": "", "pluie": "0"}) == False
    assert len(doublons(releves)) == 3
    assert est_coherente({"tmin": "25,8", "tmax": "21,0", "pluie": "0"}) == False
    assert est_coherente({"tmin": "12,0", "tmax": "99,9", "pluie": "0"}) == False
    propre = nettoyer(releves)
    assert len(propre) == 185
    assert propre[0]["tmax"] == 29.0          # un float, plus une chaine


def test_partie3():
    propre = nettoyer(charger("releves_aout.csv", ";"))
    monaco = releves_de(propre, "MON")
    assert len(monaco) == 31
    assert round(moyenne(monaco, "tmax"), 1) == 29.1
    assert jour_le_plus_chaud(monaco) == ("MON", "2025-08-13", 32.1)
    assert compter_si(monaco, "tmin", 20) == 31


def test_partie6():
    assert en_texte(23.4) == "23,4"
    assert en_texte(31) == "31"


# ================================================ Lancement des tests (ne pas modifier)
def lancer(nom, test):
    try:
        test()
        print("[OK]      ", nom)
    except Exception:
        print("[A FAIRE] ", nom)


lancer("Partie 1 : charger, en_nombre", test_partie1)
lancer("Partie 2 : controle qualite, nettoyer", test_partie2)
lancer("Partie 3 : interroger la table", test_partie3)
lancer("Partie 6 : en_texte", test_partie6)
