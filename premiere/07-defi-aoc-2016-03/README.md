# Défi Advent of Code — Squares With Three Sides (2016, jour 3)

Première NSI — Chapitre 7 — La recherche dichotomique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2016/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En explorant les bureaux du lapin de Pâques, vous trouvez des documents couverts de triangles, chacun décrit par les longueurs de ses trois côtés. Mais certains de ces « triangles » sont impossibles à construire. Le fichier liste ces triplets de longueurs : il faut trier le possible de l'impossible.

**Ce qu'il faut faire.**
- Chaque ligne contient trois longueurs entières, alignées avec des espaces.
- Trois longueurs forment un triangle possible si la somme de deux quelconques d'entre elles est **strictement** plus grande que la troisième. Autrement dit, aucun côté n'est trop long pour être « rejoint » par les deux autres.
- La réponse est le nombre de lignes qui forment un triangle possible.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

En regardant mieux les documents, vous comprenez que les triangles ne sont pas écrits en lignes, mais **en colonnes**. On prend les lignes par paquets de trois lignes consécutives ; dans chaque paquet, chacune des trois colonnes donne un triangle. La réponse est le nombre de triangles possibles.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-07-defi-aoc-2016-03.zip](../../zips/premiere-07-defi-aoc-2016-03.zip).
