"""Vérifier ses réponses : Advent of Code 2020, jour 19 — Monster Messages

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

DEFI = "aoc2020_jour19"
EMPREINTES = {
    1: "2f3a5af10d650527aae9e19ac62c6c863cacb17bd6a19dc25a1e8a6da05f161f",
    2: "4135c44a8fcf2ac8cd4cf93ff9f27a3070647f3c3529c20209e4151cd6d3396e",
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
