# Défi Advent of Code — Historian Hysteria (2024, jour 1)

Première NSI — Chapitre 6 — Les algorithmes de tri.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2024/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les historiens du pôle Nord cherchent leur chef, introuvable. Dans son bureau, ils ont dressé deux listes de lieux à visiter, chaque lieu étant désigné par un numéro. Mais les deux listes ne concordent pas, et il faut mesurer à quel point elles diffèrent. Le fichier présente les deux listes côte à côte.

**Ce qu'il faut faire.**
- Chaque ligne contient deux entiers séparés par plusieurs espaces : le premier appartient à la liste de gauche, le second à la liste de droite.
- On ne compare pas les nombres d'une même ligne : on trie chaque liste, puis on associe le plus petit nombre de gauche au plus petit de droite, le deuxième au deuxième, etc.
- L'écart d'une paire est la distance entre ses deux nombres, c'est-à-dire la valeur absolue de leur différence.
- La réponse est la somme des écarts de toutes les paires.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les historiens remarquent que beaucoup de numéros se retrouvent dans les deux listes : on mesure maintenant leur ressemblance autrement. Pour chaque nombre de la liste de gauche, on compte combien de fois il apparaît dans la liste de droite, et on multiplie le nombre par ce compte. La réponse est la somme de ces produits ; un nombre présent deux fois à gauche est compté deux fois.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-06-defi-aoc-2024-01.zip](../../zips/premiere-06-defi-aoc-2024-01.zip).
