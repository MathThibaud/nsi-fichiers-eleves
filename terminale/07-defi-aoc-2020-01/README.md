# Défi Advent of Code — Report Repair (2020, jour 1)

Terminale NSI — Chapitre 7 — Diviser pour régner.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Avant de partir en vacances, vous devez régler un dernier problème : les elfes de la comptabilité ont une note de frais qui ne tombe pas juste et vous demandent de les aider à la corriger. Le fichier de données est cette note de frais : chaque ligne est une dépense, c'est-à-dire un entier positif.

**Ce qu'il faut faire.**
- Parmi toutes les dépenses, exactement **deux** lignes ont des valeurs dont la somme vaut **2020**. Autrement dit, il faut trouver la seule paire de lignes différentes qui « complètent » 2020.
- La réponse à donner sur le site est le **produit** de ces deux valeurs.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les elfes sont ravis, mais il leur reste une ancienne note de frais à vérifier selon une autre règle. Même fichier : il faut cette fois trouver les **trois** lignes différentes dont les valeurs ont pour somme 2020, et donner le produit de ces trois valeurs.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-07-defi-aoc-2020-01.zip](../../zips/terminale-07-defi-aoc-2020-01.zip).
