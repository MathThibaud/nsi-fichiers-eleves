# Défi Advent of Code — Dive! (2021, jour 2)

Première NSI — Chapitre 2 — Le binaire et l'écriture des nombres.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous pilotez maintenant le sous-marin. Son ordinateur de bord contient un trajet déjà programmé : une liste de commandes qui le font avancer, plonger ou remonter. Avant de lancer le trajet, on veut savoir où il va mener le sous-marin.

**Les données.** Chaque ligne du fichier est une commande, exécutée dans l'ordre : un mot (`forward`, `down` ou `up`), une espace, puis un entier X, par exemple `down 4`.

**La règle.**
- On suit deux grandeurs, qui valent 0 au départ : la position horizontale et la profondeur.
- `forward X` fait avancer : la position horizontale augmente de X.
- `down X` fait plonger : la profondeur augmente de X.
- `up X` fait remonter : la profondeur *diminue* de X (c'est une profondeur, donc remonter la réduit).

**La réponse attendue.** Le produit position horizontale × profondeur à la fin du trajet. Par exemple, après `forward 5`, `down 2`, `up 1`, `forward 3`, la position horizontale vaut 8 et la profondeur 1 : la réponse serait 8 × 1 = 8.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** En relisant le manuel du sous-marin, on découvre que les commandes ne signifient pas tout à fait ce qu'on croyait. Une troisième grandeur entre en jeu, la *visée* (*aim*), qui vaut 0 au départ et indique l'inclinaison du sous-marin : plus elle est grande, plus le sous-marin descend quand il avance.

**La nouvelle règle.**
- `down X` augmente la visée de X, sans toucher à la profondeur.
- `up X` diminue la visée de X, sans toucher à la profondeur.
- `forward X` augmente la position horizontale de X **et** augmente la profondeur de visée × X.

**La réponse attendue.** Le même produit position horizontale × profondeur à la fin du trajet. Avec le même trajet inventé `forward 5`, `down 2`, `up 1`, `forward 3` : la visée vaut 0 au premier `forward`, puis 1 au second, qui fait donc descendre de 1 × 3 = 3. On arrive à la position 8 et à la profondeur 3 : la réponse serait 24.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-02-defi-aoc-2021-02.zip](../../zips/premiere-02-defi-aoc-2021-02.zip).
