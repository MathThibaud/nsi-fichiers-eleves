# Défi Advent of Code — Rain Risk (2020, jour 12)

Terminale NSI — Chapitre 2 — Programmation orientée objet et paradigmes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/12>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le ferry est pris dans une tempête et son ordinateur de navigation a produit une liste d'ordres très tortueuse. Vous aidez le capitaine à savoir où ces ordres mènent le bateau, pour estimer l'écart avec la route prévue.

**Les données.** Chaque ligne du fichier est un ordre : **une lettre** (l'action) immédiatement suivie d'**un entier** (la quantité), par exemple `N4` ou `R90`. Les ordres s'exécutent dans l'ordre des lignes.

**La règle.**
- Au départ, le navire est à l'origine et pointe vers l'est.
- `N`, `S`, `E`, `W` déplacent le navire de la quantité indiquée vers le nord, le sud, l'est ou l'ouest, **sans** changer la direction vers laquelle il pointe : il se décale comme un crabe.
- `L` et `R` le font pivoter sur place vers la gauche ou la droite du nombre de degrés indiqué (toujours un multiple de 90 dans les données). Il ne se déplace pas.
- `F` le fait avancer de la quantité indiquée, droit devant lui, dans la direction vers laquelle il pointe.

**La réponse attendue.** La distance de Manhattan entre l'arrivée et le départ, c'est-à-dire |x| + |y| (comme dans une ville quadrillée, on ne coupe pas en diagonale). Par exemple, avec les ordres `F2`, `R90`, `F3`, le navire avance de 2 vers l'est, pivote vers le sud, avance de 3 : il finit en (2, -3) et la réponse serait 2 + 3 = 5.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** En relisant le manuel, on découvre que la plupart des ordres ne concernent pas le navire lui-même, mais un point de repère (*waypoint*) qu'il poursuit.

**La nouvelle règle.**
- Le waypoint est repéré **par rapport au navire** ; au départ, il est à 10 unités à l'est et 1 au nord du navire.
- `N`, `S`, `E`, `W` déplacent le waypoint (pas le navire).
- `L`, `R` font tourner le waypoint autour du navire, du nombre de degrés indiqué.
- `F` k déplace le navire k fois du vecteur navire → waypoint ; le waypoint suit le navire et garde sa position relative.

**La réponse attendue.** La même qu'en partie 1 : la distance de Manhattan entre l'arrivée du navire et son départ. Avec les ordres `F2`, `R90`, `F3`, le navire va en (20, 2), le waypoint pivote en (1, -10), puis le navire finit en (23, -28) : la réponse serait 51.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-02-defi-aoc-2020-12.zip](../../zips/terminale-02-defi-aoc-2020-12.zip).
