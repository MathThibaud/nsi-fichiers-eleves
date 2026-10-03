"""
TP Cryptographie --- fichier de depart.

Completer les fonctions marquees "A completer" dans l'ordre de l'enonce,
puis lancer le fichier : la fonction tester() indique ce qui fonctionne.

ATTENTION : ce code sert a COMPRENDRE les algorithmes. On ne fabrique jamais
sa propre cryptographie pour proteger de vraies donnees : on utilise des
bibliotheques eprouvees.
"""

import random
import time
import unicodedata
import hashlib

# Un texte en francais (ecrit pour ce TP), qui servira de message clair.
TEXTE = """Depuis l'Antiquité, les hommes cherchent à cacher leurs messages. Les généraux
de Rome décalaient les lettres de l'alphabet, les diplomates de la Renaissance
inventaient des tables compliquées, et les espions de toutes les époques ont
dissimulé des secrets dans des lettres d'apparence banale. Pendant longtemps,
chaque progrès des faiseurs de codes a été suivi d'un progrès des casseurs de
codes. Un message chiffré par décalage ne résiste pas à celui qui compte les
lettres : dans un texte écrit en français, la lettre E revient bien plus souvent
que les autres, et elle trahit la clé. Le chiffre de Vigenère, qui change de
décalage à chaque lettre, a tenu trois siècles avant de tomber à son tour, quand
on a compris que la clé se répétait et qu'il suffisait de découper le texte en
paquets de lettres chiffrées avec le même décalage. Au siècle dernier, les
machines à rotors de la Seconde Guerre mondiale semblaient invincibles ; une
équipe de mathématiciens les a pourtant percées, en partie grâce aux erreurs des
opérateurs qui répétaient les mêmes formules au début de chaque message. La
leçon est toujours la même : un système de chiffrement n'est jamais plus solide
que la façon dont on l'utilise. Aujourd'hui, nos téléphones et nos ordinateurs
chiffrent en permanence ce qu'ils envoient sur le réseau. Les codes modernes ne
travaillent plus sur des lettres mais sur des suites de bits, et leur sécurité
repose sur des problèmes mathématiques que personne ne sait résoudre rapidement,
comme la décomposition d'un très grand nombre en produit de facteurs premiers.
Personne n'a prouvé que ces problèmes sont vraiment difficiles : on sait
seulement que les meilleurs chercheurs du monde y travaillent depuis des
décennies sans trouver de raccourci. La cryptographie est donc une science
étrange, où la confiance se construit sur l'échec répété des attaques."""

# Frequences approchees (en %) des lettres dans un texte francais.
FREQ_FR = {"A": 7.6, "B": 0.9, "C": 3.3, "D": 3.7, "E": 14.7, "F": 1.1, "G": 0.9,
           "H": 0.7, "I": 7.5, "J": 0.5, "K": 0.05, "L": 5.5, "M": 3.0, "N": 7.1,
           "O": 5.4, "P": 3.0, "Q": 1.4, "R": 6.6, "S": 7.9, "T": 7.2, "U": 6.3,
           "V": 1.6, "W": 0.05, "X": 0.4, "Y": 0.3, "Z": 0.1}



def normaliser(texte):
    """Met le texte en majuscules et retire les accents ('é' -> 'E')."""
    sans_accents = unicodedata.normalize("NFD", texte)
    resultat = ""
    for c in sans_accents:
        if unicodedata.category(c) != "Mn":      # "Mn" : un accent detache de sa lettre
            resultat = resultat + c
    return resultat.upper().replace("Œ", "OE")


def empreinte(message, n):
    """Empreinte (hachage SHA-256) du message, ramenee entre 0 et n - 1."""
    return int(hashlib.sha256(message.encode()).hexdigest(), 16) % n


# ======================= Partie A : Cesar =======================
def decaler(lettre, k):
    """Decale une majuscule de k rangs (circulairement) ; tout autre caractere est inchange."""
    # A completer
    return lettre


def cesar(texte, k):
    # A completer
    return texte


def frequences(texte):
    """Dictionnaire lettre -> nombre d'apparitions (majuscules A a Z seulement)."""
    # A completer
    return {}


def plus_frequente(texte):
    # A completer
    return None


def casser_cesar(chiffre):
    """Cle supposee, en admettant que la lettre la plus frequente du chiffre est un E."""
    # A completer
    return 0


def score(texte):
    """Somme des frequences FREQ_FR des lettres du texte."""
    # A completer
    return 0


def casser_cesar_score(chiffre):
    """Cle k (0 a 25) pour laquelle cesar(chiffre, -k) a le plus grand score."""
    # A completer
    return 0


# ======================= Partie B : Vigenere =======================
def vigenere(texte, cle, sens=1):
    """sens = 1 pour chiffrer, -1 pour dechiffrer. Seules les lettres font avancer la cle."""
    # A completer
    return texte


def colonnes(chiffre, L):
    """Liste de L chaines : les lettres de rang 0, L, 2L... ; puis 1, L+1, ... ; etc."""
    # A completer
    return []


def casser_vigenere(chiffre, L):
    # A completer
    return ""


# ======================= Partie C : XOR =======================
def xor_octets(a, b):
    """XOR octet par octet de deux suites d'octets de meme longueur (type bytes)."""
    # A completer
    return a


# ======================= Partie D : RSA =======================
def pgcd(a, b):
    # A completer
    return 1


def euclide_etendu(a, b):
    """Renvoie (g, u, v) avec g = pgcd(a, b) = a*u + b*v."""
    # A completer
    return (1, 0, 0)


def inverse_modulaire(e, phi):
    """Inverse de e modulo phi (None s'il n'existe pas)."""
    # A completer
    return None


def est_premier(n):
    # A completer
    return False


def factoriser(n):
    """Renvoie un couple (p, q) avec p * q == n et p le plus petit diviseur > 1,
    ou None si n est premier."""
    # A completer
    return None


# ======================= Tests =======================
def test_decaler():
    return decaler("Z", 3) == "C" and decaler(" ", 3) == " "


def test_cesar():
    return cesar("BONJOUR !", 3) == "ERQMRXU !"


def test_frequences():
    return frequences("ABBA, C") == {"A": 2, "B": 2, "C": 1}


def test_casser_cesar():
    return casser_cesar(cesar(normaliser(TEXTE), 11)) == 11


def test_casser_cesar_score():
    return casser_cesar_score(cesar("ATTAQUE A L AUBE", 7)) == 7


def test_vigenere():
    return (vigenere("NSI ROCKS", "CLE") == "PDM TZGMD"
            and vigenere("PDM TZGMD", "CLE", -1) == "NSI ROCKS")


def test_colonnes():
    return colonnes("AB CDE", 2) == ["ACE", "BD"]


def test_casser_vigenere():
    return casser_vigenere(vigenere(normaliser(TEXTE), "MONACO"), 6) == "MONACO"


def test_xor_octets():
    return xor_octets(b"AB", bytes([3, 3])) == b"BA"


def test_pgcd():
    return pgcd(240, 46) == 2


def test_euclide_etendu():
    return euclide_etendu(240, 46) == (2, -9, 47)


def test_inverse_modulaire():
    return inverse_modulaire(3, 20) == 7 and inverse_modulaire(4, 20) is None


def test_est_premier():
    return [n for n in range(20) if est_premier(n)] == [2, 3, 5, 7, 11, 13, 17, 19]


def test_factoriser():
    return factoriser(3233) == (53, 61) and factoriser(13) is None


def tester():
    tests = [
        ("decaler", test_decaler),
        ("cesar", test_cesar),
        ("frequences", test_frequences),
        ("casser_cesar", test_casser_cesar),
        ("casser_cesar_score", test_casser_cesar_score),
        ("vigenere", test_vigenere),
        ("colonnes", test_colonnes),
        ("casser_vigenere", test_casser_vigenere),
        ("xor_octets", test_xor_octets),
        ("pgcd", test_pgcd),
        ("euclide_etendu", test_euclide_etendu),
        ("inverse_modulaire", test_inverse_modulaire),
        ("est_premier", test_est_premier),
        ("factoriser", test_factoriser),
    ]
    for (nom, test) in tests:
        try:
            if test():
                resultat = "OK"
            else:
                resultat = "ECHEC"
        except Exception as erreur:
            resultat = "ERREUR (" + type(erreur).__name__ + ")"
        print(nom.ljust(20), resultat)


if __name__ == "__main__":
    tester()
