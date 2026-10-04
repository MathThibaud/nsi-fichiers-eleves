# Défi Advent of Code — Rope Bridge (2022, jour 9)

Première NSI — Chapitre 12 — Les k plus proches voisins.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/9>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous traversez un vieux pont de corde, et pour ne pas regarder en bas vous imaginez une corde qui se déplace sur une grille. La corde a deux bouts, la tête et la queue ; quand on tire la tête, la queue finit par suivre. Le fichier donne la suite des déplacements de la tête, et l'on s'intéresse au chemin suivi par la queue.

**Ce qu'il faut faire.**
- Tête et queue partent de la même case. Chaque ligne `D n` déplace la tête de `n` cases, **une à la fois**, vers le haut, le bas, la gauche ou la droite (`U`, `D`, `L`, `R`).
- Après chaque pas de la tête, si la queue la touche encore (même case ou case voisine, diagonales comprises), elle ne bouge pas. Sinon, elle avance d'une case vers la tête : en ligne droite si elles sont sur la même ligne ou colonne, en diagonale sinon. Autrement dit, la queue rattrape la tête en restant collée à elle.
- Réponse : le nombre de cases différentes visitées par la queue, départ compris.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le pont tremble et la corde imaginaire s'allonge. Elle a maintenant **10 nœuds** : la tête, puis 9 nœuds qui suivent chacun celui qui le précède, avec exactement la même règle que la queue de la partie 1. Réponse : le nombre de cases différentes visitées par le **dernier** nœud.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-12-defi-aoc-2022-09.zip](../../zips/premiere-12-defi-aoc-2022-09.zip).
