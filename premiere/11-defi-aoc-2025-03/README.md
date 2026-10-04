# Défi Advent of Code — Lobby (2025, jour 3)

Première NSI — Chapitre 11 — Les algorithmes gloutons.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2025/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dans le hall d'un immeuble, les ascenseurs sont en panne, et même l'escalier mécanique est à l'arrêt faute de courant. Des batteries de secours peuvent l'alimenter. Elles sont rangées en groupes, et chaque batterie porte une tension de 1 à 9. Chaque ligne du fichier décrit un groupe : la suite des tensions de ses batteries, dans l'ordre où elles sont rangées.

**Ce qu'il faut faire.**
- Dans chaque groupe, on allume **exactement deux** batteries. Le groupe produit le nombre à deux chiffres formé par leurs tensions, **dans l'ordre de la ligne** : on ne peut pas réordonner les batteries.
- On veut, pour chaque groupe, le plus grand nombre possible.
- Réponse : la somme de ces maxima sur toutes les lignes.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Deux batteries par groupe ne suffisent pas à faire repartir l'escalier. On allume maintenant **exactement 12** batteries dans chaque groupe, toujours sans changer leur ordre, pour former le plus grand nombre de 12 chiffres possible. Réponse : la somme de ces maxima sur toutes les lignes.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-11-defi-aoc-2025-03.zip](../../zips/premiere-11-defi-aoc-2025-03.zip).
