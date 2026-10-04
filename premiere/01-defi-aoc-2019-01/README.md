# Défi Advent of Code — The Tyranny of the Rocket Equation (2019, jour 1)

Première NSI — Chapitre 1 — Les bases de la programmation Python.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2019/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le Père Noël est bloqué au bord du système solaire, et les elfes préparent une fusée pour aller le chercher. La fusée est faite de modules, et chaque module a besoin de carburant pour décoller, en quantité qui dépend de sa masse. Le fichier liste les masses des modules ; il faut calculer le carburant à embarquer.

**Ce qu'il faut faire.**
- Le fichier contient une masse (un entier positif) par ligne, une ligne par module.
- Le carburant d'un module s'obtient ainsi : diviser la masse par 3, **arrondir à l'entier inférieur**, puis retirer 2. Autrement dit, c'est le quotient de la division entière par 3, moins 2.
- La réponse est la somme des carburants de tous les modules.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

On avait oublié un détail : le carburant lui-même pèse, et il faut donc du carburant pour le transporter ! Pour chaque module, on calcule le carburant de ce carburant avec la même formule, puis le carburant de ce nouveau carburant, et ainsi de suite, en s'arrêtant dès qu'on obtient une valeur nulle ou négative (elle compte pour 0). Le carburant d'un module est la somme de toutes ces quantités ; ce calcul se fait **module par module**, et la réponse est la somme sur tous les modules.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-01-defi-aoc-2019-01.zip](../../zips/premiere-01-defi-aoc-2019-01.zip).
