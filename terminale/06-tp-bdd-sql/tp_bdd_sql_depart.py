# -*- coding: utf-8 -*-
"""
TP de fin de chapitre "Bases de donnees et SQL" -- Partie 6 : SQL depuis Python.

Fichier de depart. Le placer dans le MEME dossier que tp_bdd_sql.db,
puis completer les fonctions marquees  A COMPLETER.
Lancer le fichier : les tests de la fin indiquent ce qui fonctionne.
"""

import sqlite3

connexion = sqlite3.connect("tp_bdd_sql.db")
# Sans la ligne suivante, Python N'APPLIQUE PAS les cles etrangeres !
connexion.execute("PRAGMA foreign_keys = ON")


def afficher(requete, parametres=()):
    """Execute une requete SELECT et affiche chaque ligne du resultat."""
    curseur = connexion.execute(requete, parametres)
    for ligne in curseur.fetchall():
        print(ligne)


# ---------------------------------------------------------------------
#  Exemple fourni : une requete avec un parametre (le point d'interrogation)
# ---------------------------------------------------------------------
def equipes_creees_avant(annee):
    """Liste des couples (nom, quartier) des equipes creees avant annee."""
    requete = """SELECT nom, quartier
                 FROM equipe
                 WHERE annee_creation < ?
                 ORDER BY annee_creation"""
    return connexion.execute(requete, (annee,)).fetchall()


# ---------------------------------------------------------------------
#  A COMPLETER
# ---------------------------------------------------------------------
def joueurs_de(nom_equipe):
    """Liste des triplets (prenom, nom, poste) des joueurs de l'equipe
    nommee nom_equipe, tries par nom."""
    requete = """ ... """
    return ...


def nb_buts(nom, prenom):
    """Nombre de buts marques par le joueur (un entier)."""
    ...


def classement():
    """Liste des equipes, de la premiere a la derniere.
    Chaque equipe est un dictionnaire : nom, J (joues), G, N, P,
    bp (buts pour), bc (buts contre), pts.
    Victoire = 3 points, nul = 1 point, defaite = 0 point."""
    stats = {}
    for (ident, nom) in connexion.execute("SELECT id, nom FROM equipe"):
        stats[ident] = {"nom": nom, "J": 0, "G": 0, "N": 0, "P": 0,
                        "bp": 0, "bc": 0, "pts": 0}
    requete = """ ... """          # les rencontres DEJA jouees
    for (dom, ext, bd, be) in connexion.execute(requete):
        ...                        # mettre a jour stats[dom] et stats[ext]
    lignes = [v for v in stats.values()]
    lignes.sort(key=critere_de_tri)      # tri fourni
    return lignes


def critere_de_tri(s):
    """Fournie. Cle de tri d'une equipe : points, puis difference de buts,
    puis buts marques, du plus grand au plus petit (d'ou les signes -),
    et enfin le nom par ordre alphabetique."""
    return (-s["pts"], -(s["bp"] - s["bc"]), -s["bp"], s["nom"])


def afficher_classement():
    """Fournie. Affiche le classement en colonnes alignees."""
    print(f"{'':3}{'Equipe':20}{'J':>3}{'G':>3}{'N':>3}{'P':>3}"
          f"{'bp':>4}{'bc':>4}{'diff':>5}{'Pts':>5}")
    rang = 1
    for s in classement():
        print(f"{rang:<3}{s['nom']:20}{s['J']:>3}{s['G']:>3}{s['N']:>3}{s['P']:>3}"
              f"{s['bp']:>4}{s['bc']:>4}{s['bp'] - s['bc']:>+5}{s['pts']:>5}")
        rang = rang + 1


def saisir_resultat(id_rencontre, buts):
    """DEFI. buts : liste de couples (id_joueur, minute).
    Insere les buts dans la table but ET met a jour le score de la rencontre,
    en TOUT OU RIEN : si un seul but est invalide, rien n'est enregistre."""
    dom, ext = connexion.execute(
        "SELECT id_domicile, id_exterieur FROM rencontre WHERE id = ?",
        (id_rencontre,)).fetchone()
    bd = 0
    be = 0
    with connexion:      # transaction : COMMIT a la fin si tout va bien,
        ...              # ROLLBACK automatique si une erreur survient


# ---------------------------------------------------------------------
#  Tests
# ---------------------------------------------------------------------
def test_equipes():
    assert equipes_creees_avant(2000) == [("Rocher Club", "Monaco-Ville"),
                                          ("AS Fontvieille", "Fontvieille")]


def test_joueurs_de():
    rocher = joueurs_de("Rocher Club")
    assert len(rocher) == 6 and rocher[0] == ("Andrea", "Bellini", "milieu")
    assert joueurs_de("x' OR '1'='1") == []     # pas d'injection SQL possible


def test_nb_buts():
    assert nb_buts("Barbier", "Tom") == 4 and nb_buts("Rossi", "Luca") == 0


def test_classement():
    c = classement()
    assert len(c) == 6
    assert sum(s["bp"] for s in c) == sum(s["bc"] for s in c)
    assert all(s["pts"] == 3 * s["G"] + s["N"] for s in c)
    assert all(s["J"] == s["G"] + s["N"] + s["P"] for s in c)
    assert sum(s["J"] for s in c) > 0


def tester():
    for test in (test_equipes, test_joueurs_de, test_nb_buts, test_classement):
        try:
            test()
            print(test.__name__, ": OK")
        except Exception as erreur:
            print(test.__name__, ": ECHEC (", type(erreur).__name__, erreur, ")")


if __name__ == "__main__":
    tester()
    # afficher_classement()     # a decommenter une fois classement() ecrite
