"""Projet de fin de chapitre "Donnees en tables" -- Les prenoms de l'INSEE.

Fichiers necessaires, dans le meme dossier que ce programme :
    prenoms_insee_extrait.csv     extrait du Fichier des prenoms de l'Insee
                                  (edition 2025, naissances 1950-2025, effectifs >= 100)
    projet_prenoms_evenements.csv petite table d'evenements (partie 6)

Source : Insee, Fichier des prenoms, edition 2025, licence ouverte Etalab 2.0,
https://www.insee.fr/fr/statistiques/8595130

Completer les fonctions dans l'ordre des parties du projet (remplacer les ...),
puis lancer le programme : en bas du fichier, chaque partie est testee et affiche
"OK" ou "ECHEC". Au debut, tout est en ECHEC : c'est normal.
"""

import csv

FICHIER = "prenoms_insee_extrait.csv"
EVENEMENTS = "projet_prenoms_evenements.csv"


# ============================================ Partie 2 : importer, nettoyer
def charger(fichier, separateur):
    """Table (liste de dictionnaires) lue dans le fichier CSV ;
    toutes les valeurs sont des chaines."""
    ...


def est_valide(ligne):
    """False pour les lignes qui ne decrivent pas un vrai prenom une annee
    connue (anciennes editions : prenom '_PRENOMS_RARES', annee 'XXXX')."""
    ...


def convertir(ligne):
    """Nouvelle fiche : sexe 'G' ou 'F', prenom ecrit 'Leo' et non 'LEO',
    annee, nombre et rang convertis en entiers."""
    ...


def nettoyer(table):
    """Table des fiches converties, pour les seules lignes valides."""
    ...


# ============================================ Partie 3 : interroger
def nombre_de(table, prenom, sexe, annee):
    """Nombre de naissances pour ce prenom, ce sexe, cette annee (0 si absent)."""
    ...


def evolution(table, prenom, sexe):
    """Dictionnaire {annee: nombre} des annees ou le prenom figure dans la table."""
    ...


def annee_record(table, prenom, sexe):
    """Couple (annee, nombre) de l'annee ou le prenom a ete le plus donne."""
    ...


def top(table, annee, sexe, n):
    """Liste des n couples (prenom, nombre) les plus donnes cette annee-la."""
    ...


# ============================================ Partie 4 : regrouper
def total_par_prenom(table, sexe, debut, fin):
    """Dictionnaire {prenom: total des naissances de debut a fin inclus}."""
    totaux = {}
    for ligne in table:
        ...
    return totaux


def champion(dico):
    """Couple (cle, valeur) de la plus grande valeur du dictionnaire."""
    ...


def plus_donne_par_decennie(table, sexe):
    """Dictionnaire {1950: (prenom, total), 1960: ..., ..., 2020: ...}."""
    ...


def diversite(table, annee, sexe):
    """Triplet (nombre de prenoms, total des naissances,
    part du top 10 en pourcentage arrondie au dixieme)."""
    ...


# ============================================ Partie 5 : trier
def palmares(totaux, n):
    """Les n couples (prenom, total) du dictionnaire ayant les plus grands totaux."""
    ...


def classement(table, annee, sexe):
    """Liste des prenoms de l'annee, du plus donne au moins donne ;
    a egalite de nombre, ordre alphabetique."""
    ...


# ============================================ Partie 6 : croiser
def jointure(gauche, droite, cle):
    """La jointure du cours (fournie)."""
    resultat = []
    for lg in gauche:
        for ld in droite:
            if lg[cle] == ld[cle]:
                fusion = dict(lg)
                for c in ld:
                    fusion[c] = ld[c]
                resultat.append(fusion)
    return resultat


def colonne_annee(table, annee, sexe):
    """Table de fiches {'prenom': ..., 'n2015': ...} (si annee vaut 2015)."""
    ...


def montees(table, sexe, a1, a2):
    """Jointure des deux annees sur le prenom ; chaque fiche recoit un
    descripteur 'gain' (nombre en a2 moins nombre en a1) ;
    le resultat est trie du plus grand gain au plus petit."""
    ...


def nouveaux(table, sexe, a1, a2):
    """Couples (prenom, nombre en a2) des prenoms presents en a2 mais pas en a1,
    du plus donne au moins donne."""
    ...


def avant_apres(fusion, prenom):
    """Dans la jointure evenements x prenoms : triplet (nombre l'annee avant
    l'evenement, plus grand nombre de l'annee de l'evenement aux 5 suivantes,
    annee de ce maximum)."""
    ...


# ============================================ Partie 7 : tracer
def tracer(table, prenoms, fichier_image):
    """prenoms : liste de couples (prenom, sexe). Trace une courbe par prenom."""
    import matplotlib.pyplot as plt
    annees = list(range(1950, 2026))
    for prenom, sexe in prenoms:
        evo = evolution(table, prenom, sexe)
        nombres = ...          # une valeur par annee (0 si absente)
        plt.plot(annees, nombres, label=prenom)
    plt.xlabel("année de naissance")
    plt.ylabel("nombre de naissances")
    plt.legend()
    plt.savefig(fichier_image)
    plt.show()


# ============================================ Tests (ne pas modifier)
def verifier(nom, test):
    try:
        test()
        print(nom, ": OK")
    except AssertionError:
        print(nom, ": ECHEC (un résultat n'est pas celui attendu)")
    except Exception as erreur:
        print(nom, ": ECHEC (erreur", type(erreur).__name__, ":", erreur, ")")


def propre():
    return nettoyer(charger(FICHIER, ";"))


def test_partie2():
    brut = charger(FICHIER, ";")
    assert len(brut) == 57391
    assert brut[0]["prenom"] == "GABRIEL" and brut[0]["valeur"] == "4625"
    assert est_valide({"sexe": "1", "prenom": "_PRENOMS_RARES", "periode": "1950",
                       "valeur": "5000", "rang": ""}) == False
    assert est_valide({"sexe": "2", "prenom": "MARIE", "periode": "XXXX",
                       "valeur": "905", "rang": ""}) == False
    assert est_valide({"sexe": "1", "prenom": "RARES", "periode": "2025",
                       "valeur": "15", "rang": "2053"}) == True
    assert convertir(brut[2]) == {"sexe": "G", "prenom": "Léo", "annee": 2025,
                                  "nombre": 3420, "rang": 3}
    table = nettoyer(brut)
    assert len(table) == 57391 and table[0]["nombre"] == 4625


def test_partie3():
    table = propre()
    assert nombre_de(table, "Louise", "F", 2000) == 2595
    assert nombre_de(table, "Léo", "G", 1980) == 0
    assert evolution(table, "Kevin", "G")[1991] == 13255
    assert len(evolution(table, "Kevin", "G")) == 48
    assert annee_record(table, "Jade", "F") == (2009, 5500)
    assert top(table, 2025, "G", 3) == [("Gabriel", 4625), ("Noah", 3465), ("Léo", 3420)]


def test_partie4():
    table = propre()
    assert total_par_prenom(table, "F", 2020, 2025)["Louise"] == 20370
    assert champion({"a": 3, "b": 7, "c": 5}) == ("b", 7)
    assert plus_donne_par_decennie(table, "G")[1960] == ("Philippe", 229580)
    assert diversite(table, 2025, "F") == (493, 198715, 12.5)


def test_partie5():
    table = propre()
    totaux = total_par_prenom(table, "G", 1950, 2025)
    assert palmares(totaux, 2) == [("Jean", 496810), ("Philippe", 483080)]
    assert classement(table, 2025, "F")[17:21] == ["Charlie", "Julia", "Olivia", "Mia"]


def test_partie6():
    table = propre()
    assert colonne_annee(table, 2015, "F")[0] == {"prenom": "Louise", "n2015": 4545}
    m = montees(table, "F", 2015, 2025)
    assert len(m) == 395
    assert m[0] == {"prenom": "Alma", "n2015": 195, "n2025": 2500, "gain": 2305}
    assert nouveaux(table, "G", 2015, 2025)[0] == ("Zayn", 1245)
    evenements = charger(EVENEMENTS, ";")
    for e in evenements:
        e["annee_evt"] = int(e["annee_evt"])
    fusion = jointure(evenements, table, "prenom")
    assert len(fusion) == 171
    assert avant_apres(fusion, "Thierry") == (15745, 25515, 1964)


verifier("Partie 2", test_partie2)
verifier("Partie 3", test_partie3)
verifier("Partie 4", test_partie4)
verifier("Partie 5", test_partie5)
verifier("Partie 6", test_partie6)

# Partie 7 : decommenter quand evolution est ecrite
# tracer(propre(), [("Marie", "F"), ("Lea", "F"), ("Kevin", "G")], "courbes.png")
