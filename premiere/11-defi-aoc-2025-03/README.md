# Défi Advent of Code — Lobby (2025, jour 3)

Première NSI — Chapitre 11 — Les algorithmes gloutons.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2025/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dans le hall d'un immeuble, les ascenseurs sont en panne, et même l'escalier mécanique est à l'arrêt faute de courant. Des batteries de secours peuvent l'alimenter. Elles sont rangées en groupes, et chaque batterie porte une tension de 1 à 9. Il faut tirer le maximum de chaque groupe.

**Les données.** Chaque ligne du fichier décrit un groupe de batteries : c'est une suite de chiffres de 1 à 9, sans espace, par exemple `4815`. Chaque chiffre est la tension d'une batterie, et les chiffres sont dans l'ordre où les batteries sont rangées.

**La règle.**
- Dans chaque groupe, on allume **exactement deux** batteries.
- Le groupe produit le nombre à deux chiffres formé par leurs tensions, **dans l'ordre de la ligne** : la batterie la plus à gauche donne le chiffre des dizaines. On ne peut pas réordonner les batteries.
- Pour chaque groupe, on cherche le plus grand nombre que l'on peut produire ainsi.

**La réponse attendue.** La somme de ces maxima sur toutes les lignes. Par exemple, dans le groupe `4815`, on peut former 48, 41, 45, 81, 85 ou 15 : le maximum est 85.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Deux batteries par groupe ne suffisent pas à faire repartir l'escalier : il faut en allumer beaucoup plus.

**La nouvelle règle.**
- Dans chaque groupe, on allume maintenant **exactement 12** batteries.
- Elles forment un nombre de 12 chiffres, toujours dans l'ordre de la ligne, sans réordonner les batteries.
- Pour chaque groupe, on cherche le plus grand nombre de 12 chiffres que l'on peut produire ainsi.

**La réponse attendue.** La somme de ces maxima sur toutes les lignes. Par exemple, pour un groupe de 13 batteries, cela revient à en laisser une seule éteinte : avec `1234567891234`, on éteint le premier `1` et l'on obtient 234567891234.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-11-defi-aoc-2025-03.zip](../../zips/premiere-11-defi-aoc-2025-03.zip).
