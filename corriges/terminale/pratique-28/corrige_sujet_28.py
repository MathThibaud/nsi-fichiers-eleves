import csv


class File:
    """Une file, implémentée à l'aide d'une liste Python"""

    def __init__(self):
        self._contenu = []

    def est_vide(self):
        return self._contenu == []

    def enfiler(self, x):
        self._contenu.append(x)

    def defiler(self):
        return self._contenu.pop(0)

    def tete(self):
        return self._contenu[0]

    def taille(self):
        return len(self._contenu)


def lire_taches(nom_fichier):
    """Renvoie la liste des tâches du fichier CSV, dans l'ordre du fichier,
    sous forme de couples (nom, duree)"""
    taches = []
    with open(nom_fichier, encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            taches.append((ligne["nom"], int(ligne["duree"])))
    return taches


def premier_arrive(taches):
    """Ordonnancement « premier arrivé, premier servi » : chaque tâche s'exécute
    jusqu'au bout, dans l'ordre de la liste. Renvoie la liste des couples
    (nom, instant de fin), dans l'ordre où les tâches se terminent."""
    f = File()
    for tache in taches:
        f.enfiler(tache)
    instant = 0
    fins = []
    while not f.est_vide():
        nom, duree = f.defiler()
        instant = instant + duree
        fins.append((nom, instant))
    return fins


def tourniquet(taches, quantum):
    """Ordonnancement « tourniquet » : chaque tâche s'exécute au plus pendant
    quantum unités de temps, puis, si elle n'est pas terminée, retourne en fin
    de file avec sa durée restante. Renvoie la liste des couples
    (nom, instant de fin), dans l'ordre où les tâches se terminent."""
    f = File()
    for tache in taches:
        f.enfiler(tache)
    instant = 0
    fins = []
    while not f.est_vide():
        nom, reste = f.defiler()
        execution = min(quantum, reste)     # au plus quantum unités de temps
        instant = instant + execution
        reste = reste - execution
        if reste > 0:
            f.enfiler((nom, reste))         # pas finie : retour en fin de file
        else:
            fins.append((nom, instant))
    return fins


def temps_moyen(fins):
    """Renvoie la moyenne des instants de fin de la liste fins"""
    total = 0
    for nom, instant in fins:
        total = total + instant
    return total / len(fins)


#############################################################################
# Fonction nécessaire pour la question 4                                    #
#############################################################################


def comparer(nom_fichier):
    """Affiche le temps moyen de fin des tâches du fichier pour plusieurs
    ordonnancements"""
    taches = lire_taches(nom_fichier)
    print("premier arrivé :", temps_moyen(premier_arrive(taches)))
    for quantum in [1, 2, 5, 10, 100]:
        print("tourniquet, quantum", quantum, ":", temps_moyen(tourniquet(taches, quantum)))


def test_premier_arrive():
    taches = [("A", 3), ("B", 1), ("C", 4)]
    assert premier_arrive(taches) == [("A", 3), ("B", 4), ("C", 8)]


def test_tourniquet():
    taches = [("A", 3), ("B", 1), ("C", 4)]
    assert tourniquet(taches, 2) == [("B", 3), ("A", 6), ("C", 8)]
    assert tourniquet(taches, 1) == [("B", 2), ("A", 6), ("C", 8)]
    assert tourniquet(taches, 10) == premier_arrive(taches)
    assert tourniquet([], 2) == []


def test_temps_moyen():
    assert temps_moyen([("A", 3), ("B", 4), ("C", 8)]) == 5
    assert temps_moyen([("B", 3), ("A", 6), ("C", 8)]) == 17 / 3


if __name__ == "__main__":
    test_premier_arrive()
    test_tourniquet()
    test_temps_moyen()
    comparer("taches.csv")
