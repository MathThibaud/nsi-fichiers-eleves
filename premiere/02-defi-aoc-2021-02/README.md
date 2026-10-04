# Défi Advent of Code — Dive! (2021, jour 2)

Première NSI — Chapitre 2 — Le binaire et l'écriture des nombres.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous pilotez maintenant le sous-marin. Son ordinateur de bord contient un trajet déjà programmé : une liste de commandes qui le font avancer, plonger ou remonter. On veut savoir où ce trajet va mener le sous-marin.

**Ce qu'il faut faire.**
- Chaque ligne est une commande : un mot (`forward`, `down` ou `up`), une espace, puis un entier X.
- On suit deux grandeurs, qui valent 0 au départ : la position horizontale et la profondeur.
- `forward X` fait avancer : la position horizontale augmente de X. `down X` fait plonger : la profondeur augmente de X. `up X` fait remonter : la profondeur *diminue* de X (c'est une profondeur, donc remonter la réduit).
- La réponse est le produit position horizontale × profondeur à la fin du trajet.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

En relisant le manuel du sous-marin, on découvre que les commandes ne signifient pas tout à fait ce qu'on croyait. Une troisième grandeur entre en jeu, la *visée* (*aim*), qui vaut 0 au départ et indique l'inclinaison du sous-marin. Désormais, `down X` augmente la visée de X et `up X` la diminue de X, sans toucher à la profondeur. `forward X` augmente la position horizontale de X **et** la profondeur de visée × X. La réponse est le même produit.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-02-defi-aoc-2021-02.zip](../../zips/premiere-02-defi-aoc-2021-02.zip).
