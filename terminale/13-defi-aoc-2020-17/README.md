# Défi Advent of Code — Conway Cubes (2020, jour 17)

Terminale NSI — Chapitre 13 — Calculabilité et décidabilité.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/17>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes vous demandent de l'aide pour une source d'énergie expérimentale : une grille infinie de cubes, chacun actif ou inactif, qui évolue par cycles selon l'état de ses voisins. C'est une version en trois dimensions du célèbre *jeu de la vie* de Conway. Avant de démarrer la source, il faut prévoir son état après la phase de démarrage, qui dure six cycles.

**Les données.** Le fichier est une petite grille de `#` (actif) et de `.` (inactif), toutes les lignes ayant la même longueur. C'est la tranche z = 0 de l'espace : le caractère de la ligne y, colonne x (en numérotant à partir de 0), donne l'état du cube (x, y, 0). Tous les autres cubes de l'espace, en nombre infini, sont inactifs au départ.

**La règle.**
- Les voisins d'un cube sont les 26 cubes dont chaque coordonnée diffère d'au plus 1 de la sienne : les cubes qui le touchent par une face, une arête ou un coin. Un cube n'est pas son propre voisin.
- À chaque cycle, on compte les voisins actifs de chaque cube **dans l'état d'avant le cycle**, puis tous les cubes changent **en même temps**.
- Un cube actif reste actif s'il a exactement 2 ou 3 voisins actifs ; sinon, il devient inactif.
- Un cube inactif devient actif s'il a exactement 3 voisins actifs ; sinon, il reste inactif.
- Des cubes situés hors de la grille de départ (y compris hors du plan z = 0) peuvent donc s'allumer : la zone active grandit.

**La réponse attendue.** Le nombre de cubes actifs après 6 cycles. Par exemple, avec trois cubes actifs alignés au départ, le cube du milieu reste seul actif parmi eux (2 voisins actifs), les deux bouts s'éteignent (1 seul voisin actif) et 8 cubes qui entourent le milieu s'allument : après un cycle, il y a 9 cubes actifs.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Mauvaise surprise : la source d'énergie fonctionne en réalité dans un espace à quatre dimensions. Chaque cube a donc une quatrième coordonnée w, et beaucoup plus de voisins.

**La nouvelle règle.**
- Les points sont des quadruplets (x, y, z, w) ; la grille du fichier donne l'état des points (x, y, 0, 0), tous les autres sont inactifs.
- Les voisins sont définis de la même façon : chaque coordonnée diffère d'au plus 1, le point lui-même exclu.
- Les règles d'allumage et d'extinction sont exactement les mêmes qu'en partie 1.

**La réponse attendue.** Le nombre de cubes actifs après 6 cycles, en dimension 4.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-13-defi-aoc-2020-17.zip](../../zips/terminale-13-defi-aoc-2020-17.zip).
