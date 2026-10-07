"""
TP Processus --- fichier de depart (partie B : simulateur d'ordonnancement).

Un processus est un triplet (nom, arrivee, duree), par exemple ("A", 0, 4).
Un CHRONOGRAMME est une liste : la case d'indice t contient le nom du
processus elu pendant l'unite de temps [t, t+1], ou "." si le processeur
ne fait rien (aucun processus pret).

    Exemple (premier arrive, premier servi sur le jeu du cours) :
    ["A", "A", "A", "A", "B", "B", "B", "C", "D", "D"]

Completer les fonctions dans l'ordre, puis lancer le fichier : la fonction
tester() indique ce qui fonctionne deja.
"""

JEU_COURS = [("A", 0, 4), ("B", 1, 3), ("C", 2, 1), ("D", 3, 2)]
JEU_TP = [("A", 0, 8), ("B", 1, 2), ("C", 2, 5), ("D", 4, 1), ("E", 18, 3), ("F", 19, 1)]


# ---------- 1. Premier arrive, premier servi ----------
def fcfs(procs):
    """Renvoie le chronogramme FCFS : chacun jusqu'au bout, dans l'ordre d'arrivee."""
    chrono = []
    t = 0
    # A completer
    return chrono


# ---------- 2. Lire un chronogramme ----------
def gantt_ligne(chrono):
    """Renvoie le chronogramme sous forme d'une chaine, ex. 'AAAABBBCDD'."""
    # A completer
    return ""


def statistiques(chrono, procs):
    """Renvoie un dictionnaire nom -> (temps de sejour, temps d'attente).
    sejour = instant de fin - instant d'arrivee ; attente = sejour - duree."""
    stats = {}
    # A completer
    return stats


def moyennes(stats):
    """Renvoie le couple (sejour moyen, attente moyenne)."""
    # A completer
    return (0, 0)


# ---------- 3. Plus court d'abord (non preemptif) ----------
def sjf(procs):
    """A chaque fois que le processeur se libere, on elit le processus pret
    de plus petite duree (en cas d'egalite : le premier de la liste)."""
    chrono = []
    # A completer
    return chrono


# ---------- 4. Tourniquet ----------
def tourniquet(procs, quantum):
    """Round-robin. Convention du cours : les processus arrives pendant un
    quantum entrent dans la file AVANT celui qui vient de perdre le processeur."""
    chrono = []
    # A completer
    return chrono


def commutations(chrono):
    """Nombre de passages d'un processus a un AUTRE processus (les "." ne comptent pas)."""
    # A completer
    return 0


# ---------- 5. Diagramme de Gantt detaille ----------
def gantt(chrono, procs):
    """Une ligne par processus : '#' s'il est elu, '.' s'il attend (arrive,
    pas fini), ' ' sinon ; puis une ligne d'axe graduee de 5 en 5."""
    # A completer
    return ""


# ---------- Tests ----------
def test_fcfs():
    return "".join(fcfs(JEU_COURS)) == "AAAABBBCDD"


def test_fcfs_trou():
    return "".join(fcfs([("X", 2, 1)])) == "..X"


def test_gantt_ligne():
    return gantt_ligne(["A", "A", ".", "B"]) == "AA.B"


def test_statistiques():
    return statistiques(fcfs(JEU_COURS), JEU_COURS)["C"] == (6, 5)


def test_moyennes():
    return moyennes(statistiques(fcfs(JEU_COURS), JEU_COURS)) == (5.75, 3.25)


def test_sjf():
    return "".join(sjf(JEU_COURS)) == "AAAACDDBBB"


def test_tourniquet_q_1():
    return "".join(tourniquet(JEU_COURS, 1)) == "ABACBDABDA"


def test_tourniquet_q_2():
    return "".join(tourniquet(JEU_COURS, 2)) == "AABBCAADDB"


def test_commutations():
    return commutations([c for c in "AAB..BCA"]) == 3


def tester():
    tests = [
        ("fcfs", test_fcfs),
        ("fcfs (trou)", test_fcfs_trou),
        ("gantt_ligne", test_gantt_ligne),
        ("statistiques", test_statistiques),
        ("moyennes", test_moyennes),
        ("sjf", test_sjf),
        ("tourniquet q=1", test_tourniquet_q_1),
        ("tourniquet q=2", test_tourniquet_q_2),
        ("commutations", test_commutations),
    ]
    for (nom, test) in tests:
        try:
            if test():
                resultat = "OK"
            else:
                resultat = "ECHEC"
        except Exception as erreur:
            resultat = "ERREUR (" + type(erreur).__name__ + ")"
        print(nom.ljust(16), resultat)


if __name__ == "__main__":
    tester()
