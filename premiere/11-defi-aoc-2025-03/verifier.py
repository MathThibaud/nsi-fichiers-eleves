"""Vérifier ses réponses : Advent of Code 2025, jour 3 — Lobby

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

DEFI = "aoc_25_2025_jour03"
EMPREINTES = {
    1: "fd5807084abed4488001791d9eba38b31ec3c89eacabd38dd328bf5c79883bf8",
    2: "288845418811ce718c10bd21d70f77072f9cbcc13f7de51e0669b9b3f543e70c",
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
