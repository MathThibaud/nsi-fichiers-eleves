# Défi Advent of Code — Historian Hysteria (2024, jour 1)

Première NSI — Chapitre 6 — Les algorithmes de tri.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2024/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les historiens du pôle Nord cherchent leur chef, introuvable. Dans son bureau, ils ont dressé deux listes de lieux à visiter, chaque lieu étant désigné par un numéro. Mais les deux listes ne concordent pas : avant de les mettre en accord, il faut mesurer à quel point elles diffèrent.

**Les données.** Le fichier présente les deux listes côte à côte. Chaque ligne contient deux entiers séparés par plusieurs espaces : le premier appartient à la liste de **gauche**, le second à la liste de **droite**. Les deux nombres d'une même ligne n'ont aucun lien entre eux.

**La règle.**
- On ne compare pas les nombres d'une même ligne : on trie chaque liste dans l'ordre croissant.
- On associe le plus petit nombre de gauche au plus petit de droite, le deuxième plus petit au deuxième plus petit, etc.
- L'écart d'une paire est la distance entre ses deux nombres, c'est-à-dire la valeur absolue de leur différence (on ne se soucie pas de savoir lequel est le plus grand).

**La réponse attendue.** La somme des écarts de toutes les paires. Par exemple, avec les deux lignes `4 9` et `1 3`, la liste de gauche triée est 1, 4 et celle de droite 3, 9 ; les écarts sont 2 et 5 : la réponse serait 7.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les historiens remarquent que beaucoup de numéros se retrouvent dans les deux listes : on ne mesure plus la différence, mais la **ressemblance** des deux listes, d'une autre façon. Le tri ne joue plus aucun rôle.

**La nouvelle règle.**
- Pour chaque nombre de la liste de gauche, on compte combien de fois il apparaît dans la liste de droite (ce compte peut valoir 0).
- On multiplie ce nombre par son compte.
- Un nombre présent deux fois à gauche est traité deux fois.

**La réponse attendue.** La somme de ces produits. Par exemple, avec à gauche 3, 5, 3 et à droite 3, 3, 1 : chaque 3 de gauche apparaît deux fois à droite et rapporte 3 × 2 = 6, le 5 n'y apparaît pas et rapporte 0 ; la réponse serait 12.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-06-defi-aoc-2024-01.zip](../../zips/premiere-06-defi-aoc-2024-01.zip).
