# Défi Advent of Code — Cathode-Ray Tube (2022, jour 10)

Première NSI — Chapitre 9 — Architecture des ordinateurs et systèmes d'exploitation.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/10>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** L'écran de votre appareil de communication est cassé, et pour le remplacer il faut comprendre le petit processeur qui le pilote. Ce processeur est cadencé par une horloge et possède un seul registre, `X`. Le fichier est le programme qu'il exécute, une instruction par ligne. On veut suivre la valeur de `X` au fil des cycles d'horloge.

**Ce qu'il faut faire.**
- `X` vaut **1** au départ ; les cycles sont numérotés à partir de 1.
- `noop` dure 1 cycle et ne fait rien. `addx n` dure 2 cycles, et `X` augmente de `n` (entier, parfois négatif) seulement **à la fin** de ces deux cycles : pendant ces cycles, `X` garde son ancienne valeur.
- L'intensité du signal pendant le cycle c vaut c × (valeur de `X` **pendant** ce cycle).
- Réponse : la somme des intensités pendant les cycles 20, 60, 100, 140, 180 et 220.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

On découvre que `X` commande en fait la position d'un motif sur l'écran. L'écran fait 40 pixels de large sur 6 lignes et se dessine pendant les cycles, un pixel par cycle, de gauche à droite puis ligne par ligne (le cycle 1 dessine la colonne 0, le cycle 41 recommence au début de la ligne suivante). Le motif fait 3 pixels de large, centré sur la colonne `X`. Le pixel dessiné est allumé si sa colonne est l'une des trois du motif. Réponse : les 8 lettres majuscules lues à l'écran.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-09-defi-aoc-2022-10.zip](../../zips/premiere-09-defi-aoc-2022-10.zip).
