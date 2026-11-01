# Défi Advent of Code — Allergen Assessment (2020, jour 21)

Terminale NSI — Chapitre 8 — Graphes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/21>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Pour rejoindre votre île, vous construisez un radeau et devez emporter des provisions. Problème : les étiquettes des aliments sont écrites dans une langue inconnue ; seuls certains allergènes sont indiqués dans une langue que vous comprenez. Avant de choisir vos provisions, vous voulez repérer les ingrédients qui sont certainement sans danger.

**Les données.** Chaque ligne du fichier décrit un aliment. Elle commence par sa liste d'ingrédients (des mots illisibles), séparés par des espaces, puis vient `(contains` suivi de quelques allergènes séparés par des virgules, et une parenthèse fermante. Par exemple, `kesa zuli brak (contains milk)` : trois ingrédients et un allergène indiqué.

**La règle.**
- Chaque allergène se trouve dans exactement un ingrédient ; un ingrédient contient zéro ou un allergène.
- Si un allergène est indiqué sur une ligne, l'ingrédient qui le contient figure forcément sur cette ligne.
- Mais un allergène peut être présent dans un aliment sans y être indiqué : l'absence de mention ne prouve rien.
- Un ingrédient est sans danger s'il ne peut contenir aucun des allergènes, compte tenu de toutes les lignes.

**La réponse attendue.** Le nombre total d'apparitions des ingrédients sans danger : un ingrédient présent sur trois lignes compte trois fois. Par exemple, avec les deux lignes `rel mux tap (contains soy)` et `mux dov (contains soy)`, seul `mux` peut contenir `soy` ; `rel`, `tap` et `dov` sont sans danger et apparaissent une fois chacun : la réponse serait 3.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Il reste à identifier précisément les ingrédients dangereux, pour pouvoir les éviter.

**La nouvelle règle.**
- Déterminer, pour chaque allergène, l'ingrédient qui le contient ; avec les données fournies, la solution est unique.
- Ranger ces ingrédients dans l'ordre alphabétique de leur **allergène** (et non de leur propre nom).

**La réponse attendue.** La liste de ces ingrédients, séparés par des virgules sans espace. Par exemple, si `soy` était dans `mux` et `fish` dans `dov`, la réponse serait `dov,mux`, car `fish` vient avant `soy`.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-08-defi-aoc-2020-21.zip](../../zips/terminale-08-defi-aoc-2020-21.zip).
