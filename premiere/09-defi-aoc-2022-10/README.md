# Défi Advent of Code — Cathode-Ray Tube (2022, jour 10)

Première NSI — Chapitre 9 — Architecture des ordinateurs et systèmes d'exploitation.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/10>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** L'écran de votre appareil de communication est cassé, et pour le remplacer il faut comprendre le petit processeur qui le pilote. Ce processeur est cadencé par une horloge et possède un seul registre, `X`. On veut suivre la valeur de `X` au fil des cycles d'horloge, pour mesurer un signal à certains moments précis.

**Les données.** Le fichier est le programme exécuté par le processeur, une instruction par ligne. Une ligne est soit `noop`, soit `addx` suivi d'un espace et d'un entier, parfois négatif (par exemple `addx -2`).

**La règle.**
- `X` vaut **1** au départ ; les cycles sont numérotés à partir de 1, et les instructions s'exécutent l'une après l'autre.
- `noop` dure 1 cycle et ne fait rien.
- `addx n` dure 2 cycles ; `X` augmente de `n` seulement **à la fin** de ces deux cycles : pendant ces deux cycles, `X` garde son ancienne valeur.
- L'intensité du signal pendant le cycle c vaut c × (valeur de `X` **pendant** ce cycle).

**La réponse attendue.** La somme des intensités pendant les cycles 20, 60, 100, 140, 180 et 220. Par exemple, avec le programme `addx 3` puis `noop`, `X` vaut 1 pendant les cycles 1 et 2, puis 4 pendant le cycle 3 : l'intensité pendant le cycle 3 serait 3 × 4 = 12.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On découvre que `X` commande en fait la position d'un motif lumineux sur l'écran, et que l'écran se dessine pendant que le programme s'exécute.

**La nouvelle règle.**
- L'écran fait 40 pixels de large sur 6 lignes. Il se dessine un pixel par cycle, de gauche à droite, puis ligne par ligne : le cycle 1 dessine la colonne 0 de la première ligne, le cycle 40 la colonne 39, et le cycle 41 recommence au début de la ligne suivante.
- Le motif fait 3 pixels de large et il est centré sur la colonne `X` : il occupe les colonnes `X - 1`, `X` et `X + 1`.
- Le pixel dessiné pendant un cycle est allumé si sa colonne est l'une des trois colonnes du motif pendant ce cycle ; sinon il reste éteint.

**La réponse attendue.** Les 8 lettres majuscules qui apparaissent sur l'écran une fois dessiné. Par exemple, si `X` vaut 1 pendant le cycle 1, le motif occupe les colonnes 0, 1 et 2, et le pixel de la colonne 0 est allumé.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-09-defi-aoc-2022-10.zip](../../zips/premiere-09-defi-aoc-2022-10.zip).
