# -*- coding: utf-8 -*-
"""
TP de fin de chapitre "Bases de donnees et SQL" (Terminale NSI).

Ce script FABRIQUE la base SQLite `tp_bdd_sql.db` du TP :
une ligue (fictive) de futsal entre six quartiers de Monaco.
Toutes les personnes et tous les resultats sont inventes.

Lancer :  python3 tp_bdd_sql_creation.py
  -> (re)cree tp_bdd_sql.db dans le dossier courant.
  Relancer le script remet la base dans son etat de depart
  (utile apres des UPDATE / DELETE malheureux).

La construction est reproductible : les buteurs et les minutes des buts
sont tires au hasard avec une graine fixe (random.seed(2026)).
"""

import os
import random
import sqlite3

NOM_BASE = "tp_bdd_sql.db"

SCHEMA = """
CREATE TABLE equipe (
    id             INTEGER PRIMARY KEY,
    nom            TEXT NOT NULL UNIQUE,
    quartier       TEXT NOT NULL,
    annee_creation INTEGER
);

CREATE TABLE joueur (
    id              INTEGER PRIMARY KEY,
    nom             TEXT NOT NULL,
    prenom          TEXT NOT NULL,
    annee_naissance INTEGER CHECK (annee_naissance BETWEEN 1950 AND 2015),
    poste           TEXT CHECK (poste IN ('gardien', 'defenseur', 'milieu', 'attaquant')),
    id_equipe       INTEGER NOT NULL REFERENCES equipe(id)
);

CREATE TABLE rencontre (
    id           INTEGER PRIMARY KEY,
    journee      INTEGER NOT NULL,
    date_match   TEXT NOT NULL,
    id_domicile  INTEGER NOT NULL REFERENCES equipe(id),
    id_exterieur INTEGER NOT NULL REFERENCES equipe(id),
    buts_dom     INTEGER CHECK (buts_dom >= 0),
    buts_ext     INTEGER CHECK (buts_ext >= 0),
    CHECK (id_domicile <> id_exterieur)
);

CREATE TABLE but (
    id           INTEGER PRIMARY KEY,
    id_rencontre INTEGER NOT NULL REFERENCES rencontre(id),
    id_joueur    INTEGER NOT NULL REFERENCES joueur(id),
    minute       INTEGER CHECK (minute BETWEEN 1 AND 40)
);
"""

EQUIPES = [
    (1, "AS Fontvieille", "Fontvieille", 1998),
    (2, "Condamine FC", "La Condamine", 2004),
    (3, "Moneghetti Futsal", "Moneghetti", 2011),
    (4, "Monte-Carlo United", "Monte-Carlo", 2001),
    (5, "Rocher Club", "Monaco-Ville", 1995),
    (6, "Larvotto Sporting", "Larvotto", 2016),
]

# 6 joueurs par equipe : 1 gardien, 2 defenseurs, 1 milieu, 2 attaquants
POSTES = ["gardien", "defenseur", "defenseur", "milieu", "attaquant", "attaquant"]
NOMS = [
    # AS Fontvieille
    ("Rossi", "Luca", 1996), ("Bertrand", "Hugo", 2001), ("Garnier", "Théo", 1999),
    ("Lambert", "Noah", 2004), ("Bianchi", "Enzo", 2002), ("Moreau", "Yanis", 2008),
    # Condamine FC
    ("Fabre", "Louis", 1993), ("Giordano", "Matteo", 2000), ("Blanc", "Adam", 2006),
    ("Roux", "Gabriel", 1998), ("Carvalho", "Diego", 2003), ("Brun", "Sacha", 2009),
    # Moneghetti Futsal
    ("Mercier", "Arthur", 2005), ("Fontana", "Leo", 1997), ("Durand", "Nathan", 2002),
    ("Silva", "Rafael", 2007), ("Barbier", "Tom", 1995), ("Colombo", "Marco", 2004),
    # Monte-Carlo United
    ("Lefebvre", "Paul", 1991), ("Martin", "Lucas", 2003), ("Ricci", "Pietro", 2001),
    ("Bonnet", "Jules", 1999), ("Benali", "Karim", 2000), ("Moretti", "Alessio", 2006),
    # Rocher Club
    ("Girard", "Antoine", 1990), ("Costa", "Bruno", 1994), ("Faure", "Maxime", 2008),
    ("Bellini", "Andrea", 2002), ("Blanchard", "Ethan", 2005), ("Ferraro", "Nicolo", 1998),
    # Larvotto Sporting
    ("Petit", "Raphaël", 2007), ("Gallo", "Simone", 2009), ("Chevalier", "Mathis", 2004),
    ("Bruno", "Elio", 2000), ("Benoit", "Clément", 2003), ("Esposito", "Gianni", 2010),
]

# (id, journee, date, domicile, exterieur, buts_dom, buts_ext) ; None = pas encore joue
RENCONTRES = [
    (1, 1, "2026-09-05", 1, 2, 3, 2),
    (2, 1, "2026-09-05", 3, 4, 1, 4),
    (3, 1, "2026-09-06", 5, 6, 2, 2),
    (4, 2, "2026-09-12", 2, 3, 5, 1),
    (5, 2, "2026-09-12", 4, 5, 3, 3),
    (6, 2, "2026-09-13", 6, 1, 0, 2),
    (7, 3, "2026-09-19", 1, 3, 4, 4),
    (8, 3, "2026-09-19", 2, 5, 1, 0),
    (9, 3, "2026-09-20", 4, 6, 6, 2),
    (10, 4, "2026-09-26", 5, 1, 2, 1),
    (11, 4, "2026-09-26", 3, 6, 3, 1),
    (12, 4, "2026-09-27", 2, 4, 2, 2),
    (13, 5, "2026-10-03", 1, 4, None, None),
    (14, 5, "2026-10-03", 6, 2, None, None),
    (15, 5, "2026-10-04", 3, 5, None, None),
]

# chances de marquer selon le poste (un attaquant marque plus souvent)
POIDS_POSTE = {"gardien": 0, "defenseur": 1, "milieu": 2, "attaquant": 4}


def joueurs_de(id_equipe):
    """Liste des (id_joueur, poste) d'une equipe."""
    debut = (id_equipe - 1) * 6
    return [(debut + k + 1, POSTES[k]) for k in range(6)]


def tirer_buts(id_rencontre, id_equipe, nb, hasard):
    """Fabrique nb buts (id_rencontre, id_joueur, minute) pour une equipe."""
    candidats = joueurs_de(id_equipe)
    ids = []
    poids = []
    for (id_joueur, poste) in candidats:
        ids.append(id_joueur)
        poids.append(POIDS_POSTE[poste])
    buts = []
    for _ in range(nb):
        id_joueur = hasard.choices(ids, weights=poids)[0]
        buts.append((id_rencontre, id_joueur, hasard.randint(1, 40)))
    return buts


def minute_du_but(but):
    """Minute d'un but (id_rencontre, id_joueur, minute) : sert de cle de tri."""
    return but[2]


def creer_base(nom_fichier=NOM_BASE):
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
    connexion = sqlite3.connect(nom_fichier)
    connexion.execute("PRAGMA foreign_keys = ON")
    connexion.executescript(SCHEMA)

    connexion.executemany("INSERT INTO equipe VALUES (?, ?, ?, ?)", EQUIPES)

    joueurs = []
    for i in range(len(NOMS)):
        nom = NOMS[i][0]
        prenom = NOMS[i][1]
        annee = NOMS[i][2]
        id_equipe = i // 6 + 1
        joueurs.append((i + 1, nom, prenom, annee, POSTES[i % 6], id_equipe))
    connexion.executemany("INSERT INTO joueur VALUES (?, ?, ?, ?, ?, ?)", joueurs)

    connexion.executemany("INSERT INTO rencontre VALUES (?, ?, ?, ?, ?, ?, ?)",
                          RENCONTRES)

    hasard = random.Random(2026)
    buts = []
    for (idr, journee, date_match, dom, ext, bd, be) in RENCONTRES:
        if bd is not None:        # rencontre deja jouee
            buts_match = tirer_buts(idr, dom, bd, hasard) + tirer_buts(idr, ext, be, hasard)
            buts_match.sort(key=minute_du_but)     # dans l'ordre des minutes
            buts.extend(buts_match)
    connexion.executemany(
        "INSERT INTO but (id_rencontre, id_joueur, minute) VALUES (?, ?, ?)", buts)

    connexion.commit()
    connexion.close()
    return len(EQUIPES), len(joueurs), len(RENCONTRES), len(buts)


if __name__ == "__main__":
    e, j, r, b = creer_base()
    print(f"Base {NOM_BASE} creee : {e} equipes, {j} joueurs, "
          f"{r} rencontres, {b} buts.")
