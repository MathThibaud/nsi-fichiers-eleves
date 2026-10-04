# Défi Advent of Code — Calorie Counting (2022, jour 1)

Première NSI — Chapitre 3 — Les types construits.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Une expédition d'elfes part à pied dans la jungle chercher des fruits magiques. Avant le départ, chaque elfe a noté la valeur énergétique (en calories) de chacun des aliments qu'il emporte. Le fichier rassemble toutes ces notes : chaque nombre est un aliment, et chaque bloc de nombres correspond aux provisions d'un même elfe.

**Ce qu'il faut faire.**
- Le fichier contient un entier par ligne. Une **ligne vide** marque le passage d'un elfe au suivant ; il n'y en a pas après le dernier elfe.
- Le total d'un elfe est la somme des nombres de son bloc (un elfe peut n'avoir qu'un seul aliment).
- On veut savoir quel elfe est le mieux approvisionné : la réponse est le **plus grand total**, c'est-à-dire la valeur de ce total, et non le numéro de l'elfe.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

On ne veut plus dépendre d'un seul elfe en cas de fringale : on s'intéresse maintenant aux trois elfes les mieux approvisionnés. Le fichier se découpe en elfes exactement comme avant ; la réponse est la **somme des trois plus grands totaux**.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-03-defi-aoc-2022-01.zip](../../zips/premiere-03-defi-aoc-2022-01.zip).
