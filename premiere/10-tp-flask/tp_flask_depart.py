# TP "Cote serveur : un formulaire avec Flask" -- fichier de depart
# Ce fichier et le dossier templates/ doivent etre dans le meme dossier.
# Lancer : F5 dans Spyder, puis ouvrir http://localhost:8080 dans le navigateur.
# Arreter le serveur : carre rouge de la console de Spyder (ou Ctrl+C dans la console).
# Apres CHAQUE modification de ce fichier : arreter le serveur, enregistrer, relancer.
# (Une modification d'un fichier de templates/ ne demande qu'une actualisation de la page.)

from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


# ------------------------------------------------------------------
# Partie 1 -- Un serveur sur ma machine
# ------------------------------------------------------------------
@app.route("/")
def accueil():
    return "<h1>Le serveur répond !</h1><p>Cette page a été envoyée par un programme Python.</p>"


# Exercice 2 : la route /apropos (sur le modele de la route ci-dessus)
# A COMPLETER


# ------------------------------------------------------------------
# Partie 2 -- Des pages fabriquees par le serveur
# ------------------------------------------------------------------
# Exercice 3 : modifier la route / ci-dessus pour qu'elle renvoie le modele accueil.html
# Exercice 4 : la route /heure (modele heure.html)
# A COMPLETER

# Exercice 5 : le compteur de visites
compteur = {"visites": 0}


# ------------------------------------------------------------------
# Partie 3 -- Un formulaire, en POST puis en GET
# ------------------------------------------------------------------
# Exercice 6 : la route /formulaire (affiche formulaire.html)
#              la route /bonjour (POST) : lit prenom et classe, renvoie bonjour.html
# A COMPLETER

# Exercice 7 : la route /formulaire_get (affiche formulaire_get.html)
#              la route /bonjour_get (GET) : meme travail, donnees lues dans l'URL
# A COMPLETER


# ------------------------------------------------------------------
# Partie 4 -- Defi : une page de connexion (comptes FICTIFS)
# Ne JAMAIS ecrire ici, ni dans le formulaire, un vrai mot de passe.
# ------------------------------------------------------------------
COMPTES_TEST = {"alice": "tournesol42", "bob": "pivoine7"}


def verifier_identifiants(comptes, identifiant, mot_de_passe):
    """Renvoie True si identifiant est une clef de comptes et que son
    mot de passe est mot_de_passe, False sinon."""
    # A COMPLETER
    ...


def tester_connexion():
    assert verifier_identifiants(COMPTES_TEST, "bob", "pivoine7")
    # A COMPLETER : vos trois assert (cas normal, cas limite, cas piege)
    print("verifier_identifiants : tous les tests passent.")


# Exercice 9 : la route /connexion (affiche connexion.html)
#              la route /verifier (POST) : appelle verifier_identifiants, renvoie resultat.html
# A COMPLETER


# ------------------------------------------------------------------
# Bonus -- Le livre d'or
# ------------------------------------------------------------------
livre = []      # liste de dictionnaires {"pseudo": ..., "texte": ...}


def ajouter_message(livre, pseudo, texte):
    """Ajoute {"pseudo": pseudo, "texte": texte} a la fin de livre et renvoie True,
    sauf si pseudo ou texte est vide, ou si texte depasse 200 caracteres :
    dans ce cas, livre n'est pas modifie et la fonction renvoie False."""
    # A COMPLETER
    ...


def tester_livre():
    essai = []
    assert ajouter_message(essai, "Léa", "Super site !")
    assert essai == [{"pseudo": "Léa", "texte": "Super site !"}]
    # A COMPLETER : vos trois assert (cas normal, cas limite, cas piege)
    print("ajouter_message : tous les tests passent.")


# Bonus : la route /livre (GET) et la route /livre/ecrire (POST), modele livre.html
# A COMPLETER


# ------------------------------------------------------------------
# Programme principal (le serveur demarre a la derniere ligne)
# ------------------------------------------------------------------
if __name__ == "__main__":
    # tester_connexion()      # a decommenter a l'exercice 8
    # tester_livre()          # a decommenter au bonus
    # debug=True : les erreurs Python s'affichent dans le navigateur ;
    # use_reloader=False : indispensable dans Spyder.
    app.run(port=8080, debug=True, use_reloader=False)
