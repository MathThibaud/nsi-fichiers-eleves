# Défi Advent of Code — Mull It Over (2024, jour 3)

Première NSI — Chapitre 10 — Le Web : réseaux et interactions homme-machine.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2024/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** L'ordinateur d'un magasin de location de luges est en panne : sa mémoire a été abîmée et ressemble à un long texte plein de caractères au hasard. Quelques instructions de multiplication ont survécu au milieu de ce désordre. Le fichier contient cette mémoire, parfois sur plusieurs lignes, et il faut retrouver ce que le programme calculait.

**Ce qu'il faut faire.**
- Une instruction valide s'écrit **exactement** `mul(X,Y)`, où `X` et `Y` sont des entiers de **1 à 3 chiffres**, sans espace ni autre caractère. Elle calcule `X * Y`.
- Tout motif qui ressemble mais n'est pas exact (espace, crochet, 4 chiffres, nombre manquant…) est un débris : on l'ignore.
- Réponse : la somme des produits de toutes les instructions valides.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

En regardant mieux, la mémoire contient aussi des interrupteurs. L'instruction `do()` active les `mul` qui suivent, `don't()` les désactive ; seule la plus récente des deux compte, et au début du texte les `mul` sont actifs. Réponse : la somme des produits des seuls `mul` valides et actifs.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-10-defi-aoc-2024-03.zip](../../zips/premiere-10-defi-aoc-2024-03.zip).
