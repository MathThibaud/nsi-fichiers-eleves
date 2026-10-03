# Activite "Programmer l'arithmetique binaire" -- FICHIER DE DEPART
# Tous les nombres binaires sont des CHAINES de "0" et de "1",
# ecrites comme d'habitude : le bit de poids fort a gauche ("1011" vaut 11).
# Interdit : bin(), int(..., 2), format()... (seulement pour verifier en console).
# Quand une partie est finie, appelez sa fonction de tests tout en bas du fichier.


# ---------- Partie A : Les convertisseurs ----------

def binaire_vers_decimal(s):
    """Renvoie l'entier represente par la chaine binaire s."""
    # A COMPLETER
    return None


def decimal_vers_binaire(n):
    """Renvoie l'ecriture binaire (chaine) de l'entier n >= 0."""
    # A COMPLETER
    return None


def completer(s, nb_bits):
    """Ajoute des "0" a gauche de s jusqu'a obtenir nb_bits caracteres."""
    # A COMPLETER
    return None


def binaire_vers_hexa(s):
    """Renvoie l'ecriture hexadecimale de la chaine binaire s."""
    # A COMPLETER
    return None


def tester_A():
    try:
        assert binaire_vers_decimal("1011") == 11
        assert binaire_vers_decimal("0") == 0
        assert binaire_vers_decimal("11111111") == 255
        assert decimal_vers_binaire(13) == "1101"
        assert decimal_vers_binaire(0) == "0"
        assert decimal_vers_binaire(6) == "110"
        assert completer("101", 8) == "00000101"
        assert completer("1101", 4) == "1101"
        assert binaire_vers_hexa("11111010") == "FA"
        assert binaire_vers_hexa("101") == "5"
        print("Partie A : OK, tous les tests passent.")
    except Exception:
        print("Partie A : A FAIRE (ou un test echoue)")



# ---------- Partie B : Le complement a deux ----------

def inverser(s):
    """Remplace chaque 0 par 1 et chaque 1 par 0."""
    # A COMPLETER
    return None


def incrementer(s):
    """Ajoute 1 a s, sur le meme nombre de bits (la retenue finale est perdue)."""
    # A COMPLETER
    return None


def complement_a_deux(n, nb_bits):
    """Ecriture de l'entier relatif n en complement a deux sur nb_bits bits."""
    # A COMPLETER
    return None


def decoder_c2(s):
    """Entier relatif code par s en complement a deux."""
    # A COMPLETER
    return None


def tester_B():
    try:
        assert inverser("00000101") == "11111010"
        assert incrementer("0111") == "1000"
        assert incrementer("1010") == "1011"
        assert incrementer("1111") == "0000"
        assert complement_a_deux(5, 8) == "00000101"
        assert complement_a_deux(-5, 8) == "11111011"
        assert complement_a_deux(-1, 4) == "1111"
        assert complement_a_deux(-128, 8) == "10000000"
        assert decoder_c2("11111011") == -5
        assert decoder_c2("01111111") == 127
        assert decoder_c2("10000000") == -128
        assert decoder_c2(soustraire("0010", "0111")) == -5
        print("Partie B : OK, tous les tests passent.")
    except Exception:
        print("Partie B : A FAIRE (ou un test echoue)")



# ---------- Partie C : Les portes logiques (un bit = "0" ou "1") ----------

def non(a):
    """Renvoie "1" si a vaut "0", et "0" sinon."""
    # A COMPLETER
    return None


def et(a, b):
    """Renvoie "1" si a et b valent "1", "0" sinon."""
    # A COMPLETER
    return None


def ou(a, b):
    """Renvoie "1" si a ou b vaut "1", "0" sinon."""
    # A COMPLETER
    return None


def xor(a, b):
    """OU exclusif, construit UNIQUEMENT avec non, et, ou."""
    # A COMPLETER
    return None


def tester_C():
    try:
        for a in "01":
            for b in "01":
                assert xor(a, b) == str((int(a) + int(b)) % 2)
        print("Partie C : OK, tous les tests passent.")
    except Exception:
        print("Partie C : A FAIRE (ou un test echoue)")



# ---------- Partie D : Les additionneurs ----------

def demi_additionneur(a, b):
    """Renvoie la chaine retenue + somme (donc a + b ecrit sur 2 bits)."""
    # A COMPLETER
    return None


def additionneur_complet(a, b, r):
    """Renvoie retenue + somme de a + b + r (ecrit sur 2 bits)."""
    # A COMPLETER
    return None


def additionner(s1, s2):
    """s1 + s2 (meme longueur n) ; resultat sur n + 1 bits."""
    # A COMPLETER
    return None


def tester_D():
    try:
        assert demi_additionneur("1", "1") == "10"
        assert demi_additionneur("1", "0") == "01"
        assert additionneur_complet("1", "1", "1") == "11"
        assert additionneur_complet("1", "0", "1") == "10"
        assert additionner("0101", "0110") == "01011"
        assert additionner("1111", "0001") == "10000"
        print("Partie D : OK, tous les tests passent.")
    except Exception:
        print("Partie D : A FAIRE (ou un test echoue)")



# ---------- Partie E : La soustraction ----------

def soustraire(s1, s2):
    """s1 - s2 en complement a deux, sur le nombre de bits de s1."""
    # A COMPLETER
    return None


def depassement(s1, s2):
    """True si s1 + s2 (complement a deux) sort de la plage representable."""
    # A COMPLETER
    return None


def tester_E():
    try:
        assert soustraire("0111", "0010") == "0101"
        assert soustraire("0010", "0111") == "1011"
        assert depassement("0111", "0001") is True
        assert depassement("0011", "0010") is False
        assert depassement("1000", "1111") is True
        assert depassement("1111", "0001") is False
        print("Partie E : OK, tous les tests passent.")
    except Exception:
        print("Partie E : A FAIRE (ou un test echoue)")



# ---------- Partie F : La multiplication ----------

def decaler(s, k):
    """Multiplie s par 2**k : on ajoute k zeros a droite."""
    # A COMPLETER
    return None


def multiplier(s1, s2):
    """Produit de deux entiers positifs, sur len(s1) + len(s2) bits."""
    # A COMPLETER
    return None


def tester_F():
    try:
        assert decaler("101", 2) == "10100"
        assert multiplier("101", "11") == "01111"
        assert multiplier("1101", "1011") == "10001111"
        assert multiplier("0", "0") == "00"
        print("Partie F : OK, tous les tests passent.")
    except Exception:
        print("Partie F : A FAIRE (ou un test echoue)")



# ---------- Partie G : Comme la machine a billes (Turing Tumble) ----------

def ajouter_billes(registre, nb_billes):
    """Chaque bille ajoute 1 au registre : on incremente nb_billes fois."""
    # A COMPLETER
    return None


def tester_G():
    try:
        assert ajouter_billes("0101", 6) == "1011"
        assert ajouter_billes("1110", 3) == "0001"
        print("Partie G : OK, tous les tests passent.")
    except Exception:
        print("Partie G : A FAIRE (ou un test echoue)")



# ---------- Lancer les tests (decommenter au fur et a mesure) ----------

# tester_A()
# tester_B()
# tester_C()
# tester_D()
# tester_E()
# tester_F()
# tester_G()
