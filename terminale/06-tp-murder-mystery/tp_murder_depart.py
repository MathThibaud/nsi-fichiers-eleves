"""TP « SQL Murder Mystery » : fichier de depart.

Enqueter depuis Python plutot que dans DB Browser ou sur le site.
Placer ce fichier dans le MEME dossier que la base sql-murder-mystery.db.

Base de donnees : SQL Murder Mystery, Joon Park et Cathy He, Knight Lab
(Northwestern University), https://github.com/NUKnightLab/sql-mysteries
Code sous licence MIT, textes et donnees sous licence CC BY-SA 4.0
(voir sql-murder-mystery_LICENCE.txt).
"""

import sqlite3
from pathlib import Path

# La base est cherchee a cote de ce fichier : sqlite3.connect cree une base
# VIDE (sans aucune table) si on lui donne un chemin qui n'existe pas.
CHEMIN_BASE = Path(__file__).with_name("sql-murder-mystery.db")
if not CHEMIN_BASE.exists():
    raise FileNotFoundError(f"Base introuvable : {CHEMIN_BASE}")

connexion = sqlite3.connect(str(CHEMIN_BASE))


def afficher(requete, parametres=(), maximum=30):
    """Execute la requete et affiche les noms de colonnes puis les lignes.

    parametres : tuple des valeurs qui remplacent les ? de la requete.
    maximum : nombre maximal de lignes affichees (le total est toujours donne).
    """
    curseur = connexion.execute(requete, parametres)
    if curseur.description is None:
        # INSERT, UPDATE, DELETE : rien a afficher, on enregistre dans le fichier
        connexion.commit()
        print("Requete executee.")
        return
    print(" | ".join(colonne[0] for colonne in curseur.description))
    lignes = curseur.fetchall()
    for ligne in lignes[:maximum]:
        print(" | ".join(str(valeur) for valeur in ligne))
    if len(lignes) > maximum:
        print(f"... ({len(lignes) - maximum} lignes non affichees)")
    print(f"-> {len(lignes)} ligne(s)\n")


# Exemple : la liste des tables de la base
afficher("SELECT name FROM sqlite_master WHERE type = 'table'")

# Exemple avec un parametre : le ? est remplace par la valeur du tuple
# afficher("SELECT COUNT(*) FROM person WHERE address_street_name = ?", ("Fisk Rd",))

# A vous : ecrire ici les requetes de l'enquete, une par appel a afficher.
