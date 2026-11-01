# Défi Advent of Code — Squares With Three Sides (2016, jour 3)

Première NSI — Chapitre 7 — La recherche dichotomique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2016/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En explorant les bureaux du lapin de Pâques, vous trouvez des documents couverts de triangles, chacun décrit par les longueurs de ses trois côtés. Mais certains de ces « triangles » sont impossibles à construire : un côté est trop long pour que les deux autres puissent le rejoindre. Il faut trier le possible de l'impossible.

**Les données.** Le fichier liste ces triplets de longueurs. Chaque ligne contient trois longueurs entières, alignées en colonnes avec des espaces (il peut y avoir des espaces en début de ligne et plusieurs espaces entre deux nombres). Dans la partie 1, chaque ligne décrit un triangle.

**La règle.**
- Trois longueurs forment un triangle possible si la somme de deux quelconques d'entre elles est **strictement** plus grande que la troisième, et ce pour les trois choix possibles de « troisième » côté.
- Autrement dit, aucun côté n'est trop long pour être « rejoint » par les deux autres.
- Une égalité ne suffit pas : si deux côtés mis bout à bout ont exactement la longueur du troisième, le triangle est « aplati » et compte comme impossible.

**La réponse attendue.** Le nombre de lignes qui forment un triangle possible. Par exemple, pour les deux lignes `2 3 4` (2 + 3 > 4 : possible) et `1 2 3` (1 + 2 = 3 : impossible), la réponse serait 1.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** En regardant mieux les documents, vous comprenez que les triangles ne sont pas écrits en lignes, mais **en colonnes**. Le fichier et la condition sur les longueurs restent les mêmes ; seule la façon de regrouper les nombres change.

**La nouvelle règle.**
- On prend les lignes par paquets de trois lignes consécutives : lignes 1 à 3, puis 4 à 6, etc.
- Dans chaque paquet, chacune des trois colonnes donne un triangle : les trois nombres de la colonne de gauche forment un triangle, ceux du milieu un autre, ceux de droite un troisième.
- Chaque triangle est testé avec la même condition que dans la partie 1.

**La réponse attendue.** Le nombre de triangles possibles avec cette lecture. Par exemple, pour le paquet formé des lignes `2 1 5`, `3 2 5` et `4 3 5`, les colonnes donnent les triangles 2, 3, 4 (possible), 1, 2, 3 (impossible) et 5, 5, 5 (possible) : la réponse serait 2.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-07-defi-aoc-2016-03.zip](../../zips/premiere-07-defi-aoc-2016-03.zip).
