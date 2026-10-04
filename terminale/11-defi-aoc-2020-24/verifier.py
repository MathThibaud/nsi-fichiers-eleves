"""Vérifier ses réponses : Advent of Code 2020, jour 24 — Lobby Layout

Le fichier input.txt de ce dossier contient des données fabriquées pour le manuel,
au même format que celles du site adventofcode.com. Les réponses sont donc
différentes de celles que le site vous demanderait avec vos propres données.

Deux façons de s'en servir :
  - lancer ce programme, puis taper sa réponse à chaque question ;
  - ou, dans son propre programme :  from verifier import verifier
                                      print(verifier(1, ma_reponse))
Les bonnes réponses ne sont pas écrites ici : seule leur empreinte (SHA-256) l'est.
"""
import hashlib

DEFI = "aoc2020_jour24"
EMPREINTES = {
    1: "4869d0ebabfe5df30b6994c3893980164c2a58e662a0b0a3125e7308dc1cfe53",
    2: "6d3908b6a6f711590152e6989fa1979cc1452ac3048b42b3ef0b9a4cb69f9a6b",
}


def empreinte(partie, reponse):
    texte = DEFI + ":" + str(partie) + ":" + str(reponse).strip()
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def verifier(partie, reponse):
    """Renvoie True si la réponse (nombre ou texte) à la partie 1 ou 2 est juste."""
    return empreinte(partie, reponse) == EMPREINTES[partie]


if __name__ == "__main__":
    for partie in EMPREINTES:
        reponse = input("Réponse à la partie " + str(partie) + " : ")
        if verifier(partie, reponse):
            print("Bravo, c'est la bonne réponse !")
        else:
            print("Ce n'est pas la bonne réponse : relire le résumé, tester sur l'exemple de la fiche, puis réessayer.")
