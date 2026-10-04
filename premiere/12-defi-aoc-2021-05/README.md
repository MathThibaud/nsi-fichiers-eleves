# Défi Advent of Code — Hydrothermal Venture (2021, jour 5)

Première NSI — Chapitre 12 — Les k plus proches voisins.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/5>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Au fond de l'océan, le sous-marin longe des champs de cheminées hydrothermales qui forment des lignes droites et dégagent des nuages dangereux. Le fichier décrit ces lignes de cheminées, une par ligne, par leurs deux extrémités. Il faut repérer les endroits où plusieurs lignes se croisent, pour les éviter.

**Ce qu'il faut faire.**
- Chaque ligne a la forme `x1,y1 -> x2,y2` : un segment sur une grille, extrémités **comprises** ; x est la colonne, y la ligne.
- Pour la partie 1, on ne prend en compte que les segments **horizontaux** (y_1 = y_2) ou **verticaux** (x_1 = x_2) ; les autres sont ignorés.
- Une case est dangereuse si au moins **deux** segments la couvrent.
- Réponse : le nombre de cases dangereuses.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les lignes en biais existent aussi et sont tout aussi dangereuses. On prend désormais aussi en compte les segments en **diagonale**, qui sont toujours à exactement 45° (à chaque pas, x et y changent de 1). Même question : nombre de cases couvertes par au moins deux segments.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-12-defi-aoc-2021-05.zip](../../zips/premiere-12-defi-aoc-2021-05.zip).
