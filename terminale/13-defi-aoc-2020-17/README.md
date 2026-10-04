# Défi Advent of Code — Conway Cubes (2020, jour 17)

Terminale NSI — Chapitre 13 — Calculabilité et décidabilité.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/17>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes vous demandent de l'aide pour une source d'énergie expérimentale : une grille infinie de cubes, chacun actif ou inactif, qui évolue par cycles selon l'état de ses voisins. C'est une version en trois dimensions du célèbre *jeu de la vie* de Conway. Le fichier donne l'état d'une petite zone plate au départ.

**Ce qu'il faut faire.**
- Le fichier est une grille de `#` (actif) et de `.` (inactif). C'est la tranche z = 0 de l'espace : le caractère de la ligne y, colonne x, donne l'état du cube (x, y, 0). Tous les autres cubes de l'espace sont inactifs.
- Les voisins d'un cube sont les 26 cubes dont chaque coordonnée diffère d'au plus 1 de la sienne : les cubes qui le touchent par une face, une arête ou un coin.
- À chaque cycle, tous les cubes changent en même temps. Un cube actif reste actif s'il a exactement 2 ou 3 voisins actifs, sinon il s'éteint. Un cube inactif s'allume s'il a exactement 3 voisins actifs.
- La réponse est le nombre de cubes actifs après 6 cycles.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Mauvaise surprise : la source d'énergie fonctionne en réalité dans un espace à quatre dimensions.
- Même simulation avec des points (x, y, z, w) : l'état initial est dans le plan z = w = 0, et les voisins sont définis de la même façon (chaque coordonnée diffère d'au plus 1).
- La réponse est le nombre de cubes actifs après 6 cycles.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-13-defi-aoc-2020-17.zip](../../zips/terminale-13-defi-aoc-2020-17.zip).
