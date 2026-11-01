# Défi Advent of Code — The Tyranny of the Rocket Equation (2019, jour 1)

Première NSI — Chapitre 1 — Les bases de la programmation Python.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2019/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le Père Noël est bloqué au bord du système solaire, et les elfes préparent une fusée pour aller le chercher. La fusée est faite de modules, et chaque module a besoin de carburant pour décoller, en quantité qui dépend de sa masse. Avant le décollage, il faut savoir combien de carburant embarquer en tout.

**Les données.** Le fichier liste les masses des modules : chaque ligne contient **un seul entier positif**, la masse d'un module. Il y a une ligne par module, et l'ordre des lignes n'a pas d'importance.

**La règle.**
- Pour un module, on divise sa masse par 3 et on **arrondit à l'entier inférieur**.
- On retire 2 au résultat : c'est le carburant de ce module. Autrement dit, c'est le quotient de la division entière par 3, moins 2.
- On fait ce calcul séparément pour chaque module, puis on additionne les résultats.

**La réponse attendue.** La somme des carburants de tous les modules. Par exemple, pour deux modules de masses 12 et 21, les carburants sont 12 // 3 - 2 = 2 et 21 // 3 - 2 = 5 : la réponse serait 7.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On avait oublié un détail : le carburant lui-même pèse, et il faut donc du carburant pour le transporter ! Et ce carburant supplémentaire pèse à son tour…

**La nouvelle règle.**
- Pour un module, on calcule son carburant avec la formule de la partie 1.
- On calcule ensuite le carburant de ce carburant, avec la même formule, puis le carburant de ce nouveau carburant, et ainsi de suite.
- On s'arrête dès qu'on obtient une valeur nulle ou négative : elle compte pour 0.
- Le carburant du module est la somme de toutes ces quantités. Ce calcul se fait **module par module**.

**La réponse attendue.** La somme, sur tous les modules, de ces carburants. Par exemple, pour un module de masse 60 : on trouve 18, puis 4 (carburant de 18), puis une valeur négative (carburant de 4) qui arrête le calcul ; le carburant de ce module est 18 + 4 = 22.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-01-defi-aoc-2019-01.zip](../../zips/premiere-01-defi-aoc-2019-01.zip).
