# Défi Advent of Code — Hydrothermal Venture (2021, jour 5)

Première NSI — Chapitre 12 — Les k plus proches voisins.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/5>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Au fond de l'océan, le sous-marin longe des champs de cheminées hydrothermales qui forment des lignes droites et dégagent des nuages dangereux. Là où plusieurs lignes de cheminées se croisent, les nuages s'accumulent : il faut repérer ces endroits pour les éviter.

**Les données.** Chaque ligne du fichier décrit une ligne de cheminées sous la forme `x1,y1 -> x2,y2` : c'est un segment sur une grille, qui va de la case (x_1, y_1) à la case (x_2, y_2). Ici x est le numéro de colonne et y le numéro de ligne. Les deux extrémités peuvent être données dans n'importe quel ordre.

**La règle.**
- Un segment couvre toutes les cases entre ses deux extrémités, extrémités **comprises**.
- Pour la partie 1, on ne prend en compte que les segments **horizontaux** (y_1 = y_2) ou **verticaux** (x_1 = x_2) ; les autres sont ignorés.
- Une case est dangereuse si au moins **deux** segments la couvrent.

**La réponse attendue.** Le nombre de cases dangereuses. Par exemple, avec les deux segments `0,0 -> 2,0` (horizontal) et `1,0 -> 1,3` (vertical), seule la case (1, 0) est couverte deux fois : la réponse serait 1.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les lignes de cheminées en biais existent aussi et sont tout aussi dangereuses : on ne les ignore plus.

**La nouvelle règle.**
- On prend désormais en compte tous les segments : horizontaux, verticaux et en **diagonale**.
- Les diagonales sont toujours à exactement 45° : d'une case du segment à la suivante, x et y changent tous les deux de 1 (en plus ou en moins).
- Une case reste dangereuse si au moins deux segments la couvrent, extrémités comprises.

**La réponse attendue.** Le nouveau nombre de cases dangereuses. Par exemple, les diagonales `0,0 -> 2,2` et `2,0 -> 0,2` se croisent en (1, 1) : la réponse serait 1, alors qu'elle était 0 dans la partie 1, qui les ignorait.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-12-defi-aoc-2021-05.zip](../../zips/premiere-12-defi-aoc-2021-05.zip).
