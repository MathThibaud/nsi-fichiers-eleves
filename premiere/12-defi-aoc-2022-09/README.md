# Défi Advent of Code — Rope Bridge (2022, jour 9)

Première NSI — Chapitre 12 — Les k plus proches voisins.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/9>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous traversez un vieux pont de corde, et pour ne pas regarder en bas vous imaginez une corde qui se déplace sur une grille. La corde a deux bouts, la tête et la queue, qui restent toujours proches l'un de l'autre : quand on tire la tête, la queue finit par suivre. On s'intéresse au chemin suivi par la queue.

**Les données.** Chaque ligne du fichier est un mouvement de la tête, de la forme `D n` : une lettre qui donne la direction (`U` vers le haut, `D` vers le bas, `L` vers la gauche, `R` vers la droite), un espace, puis le nombre `n` de cases à parcourir. Par exemple, `R 4` fait avancer la tête de quatre cases vers la droite.

**La règle.**
- Tête et queue partent de la même case.
- Chaque mouvement `D n` se fait **une case à la fois**, en `n` pas.
- Après chaque pas de la tête, si la queue la touche encore (même case ou case voisine, diagonales comprises), elle ne bouge pas.
- Sinon, la queue avance d'une case vers la tête : en ligne droite si elles sont sur la même ligne ou la même colonne, en diagonale sinon. Autrement dit, la queue rattrape la tête en restant collée à elle.

**La réponse attendue.** Le nombre de cases différentes visitées par la queue, départ compris. Par exemple, avec le seul mouvement `R 3`, la tête arrive trois cases à droite ; la queue reste sur place au premier pas, puis avance d'une case à chacun des deux pas suivants : elle a visité 3 cases, la réponse serait 3.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le pont tremble et la corde imaginaire s'allonge : elle n'a plus deux bouts seulement, mais **10 nœuds** alignés les uns derrière les autres.

**La nouvelle règle.**
- Le premier nœud est la tête ; il se déplace comme dans la partie 1, selon les mouvements du fichier, une case à la fois.
- Chacun des 9 autres nœuds suit le nœud qui le précède, avec exactement la même règle que la queue de la partie 1.
- Tous les nœuds partent de la même case.

**La réponse attendue.** Le nombre de cases différentes visitées par le **dernier** nœud, départ compris. Par exemple, avec le seul mouvement `R 3`, le mouvement s'amortit le long de la corde avant d'arriver au bout : le dernier nœud ne bouge pas, et la réponse serait 1.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-12-defi-aoc-2022-09.zip](../../zips/premiere-12-defi-aoc-2022-09.zip).
