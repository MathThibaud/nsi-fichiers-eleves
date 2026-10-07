# Défi Advent of Code — Allergen Assessment (2020, jour 21)

Terminale NSI — Chapitre 8 — Graphes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/21>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Pour rejoindre votre île, vous construisez un radeau et devez emporter des provisions. Problème : les étiquettes des aliments sont écrites dans une langue inconnue, seuls certains allergènes sont indiqués dans une langue que vous comprenez. Chaque ligne du fichier décrit un aliment : sa liste d'ingrédients (illisibles) et quelques-uns des allergènes qu'il contient.

**Ce qu'il faut faire.**
- Une ligne contient des ingrédients séparés par des espaces, puis `(contains` suivi d'allergènes séparés par des virgules, et `)`.
- Chaque allergène se trouve dans exactement un ingrédient ; un ingrédient contient zéro ou un allergène.
- Si un allergène est indiqué sur une ligne, l'ingrédient qui le contient figure sur cette ligne. Mais un allergène peut être présent dans un aliment sans y être indiqué : l'absence de mention ne prouve rien.
- Trouver les ingrédients qui ne peuvent contenir aucun allergène. Réponse : le nombre total de leurs apparitions (un ingrédient présent sur trois lignes compte trois fois).

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Il reste à identifier les ingrédients dangereux pour pouvoir les éviter. Déterminer, pour chaque allergène, l'ingrédient qui le contient (la solution est unique). Réponse : la liste de ces ingrédients, rangés dans l'ordre alphabétique de leur **allergène** (et non de leur nom), séparés par des virgules sans espace.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-08-defi-aoc-2020-21.zip](../../zips/terminale-08-defi-aoc-2020-21.zip).
