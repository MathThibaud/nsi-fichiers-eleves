# Défi Advent of Code — Not Quite Lisp (2015, jour 1)

Première NSI — Chapitre 1 — Les bases de la programmation Python.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2015/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le Père Noël doit livrer des cadeaux dans un immeuble immense, avec des sous-sols très profonds. Les instructions qu'on lui a données sont une longue suite de parenthèses : chacune lui dit de monter ou de descendre d'un étage. Le fichier contient cette suite ; il faut trouver où il arrive.

**Ce qu'il faut faire.**
- Le fichier ne contient qu'**une seule ligne**, formée des caractères `(` et `)`.
- On part du rez-de-chaussée, l'étage 0, et on lit les caractères un par un : `(` fait monter d'un étage, `)` fait descendre d'un étage.
- L'immeuble n'a ni dernier étage ni sous-sol le plus bas : l'étage peut devenir aussi grand ou aussi négatif qu'on veut. Un étage négatif est un sous-sol (-1 est le premier sous-sol).
- La réponse est l'étage atteint après le dernier caractère.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

On s'intéresse maintenant au trajet lui-même, et non plus à l'arrivée. La réponse est la **position** du premier caractère qui amène le Père Noël à l'étage -1, c'est-à-dire son premier passage au sous-sol. Attention : les positions sont numérotées **à partir de 1** (le premier caractère est en position 1).

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-01-defi-aoc-2015-01.zip](../../zips/premiere-01-defi-aoc-2015-01.zip).
