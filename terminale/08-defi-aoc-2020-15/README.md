# Défi Advent of Code — Rambunctious Recitation (2020, jour 15)

Terminale NSI — Chapitre 8 — Programmation dynamique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/15>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En attendant votre avion, vous appelez les elfes du pôle Nord : ils jouent à un jeu de mémoire où chacun, à son tour, annonce un nombre qui dépend de ce qui a déjà été dit. Le fichier contient seulement les nombres par lesquels la partie commence.

**Ce qu'il faut faire.**
- Le fichier est une ligne de nombres de départ séparés par des virgules.
- Les tours sont numérotés à partir de 1. Les premiers tours servent à annoncer les nombres de départ, dans l'ordre.
- Ensuite, à chaque tour, on regarde le nombre annoncé au tour précédent. S'il était annoncé pour la première fois, on annonce `0`. Sinon, on annonce l'écart entre le tour où il vient d'être annoncé et le tour où il l'avait été la fois d'avant : autrement dit, « il y a combien de tours qu'on l'avait déjà dit ? ».
- La réponse est le nombre annoncé au tour 2020.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les elfes sont infatigables : ils continuent la partie beaucoup plus longtemps.
- Même jeu, mêmes nombres de départ. La réponse est le nombre annoncé au tour 30 000 000.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-08-defi-aoc-2020-15.zip](../../zips/terminale-08-defi-aoc-2020-15.zip).
