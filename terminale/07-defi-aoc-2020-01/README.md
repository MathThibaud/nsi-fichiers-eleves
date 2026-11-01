# Défi Advent of Code — Report Repair (2020, jour 1)

Terminale NSI — Chapitre 7 — Diviser pour régner.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Avant de partir en vacances, vous devez régler un dernier problème : les elfes de la comptabilité ont une note de frais qui ne tombe pas juste et vous demandent de les aider à la corriger. Il faut retrouver dans cette note les dépenses qui posent problème.

**Les données.** Le fichier est la note de frais. Chaque ligne contient **un seul entier positif** : le montant d'une dépense. Il y a environ deux cents lignes ; leur ordre ne joue aucun rôle.

**La règle.**
- Parmi toutes les dépenses, exactement **deux** lignes ont des valeurs dont la somme vaut **2020**. Autrement dit, il faut trouver la seule paire de lignes qui « complètent » 2020.
- Les deux lignes doivent être **différentes** : une valeur présente une seule fois dans le fichier ne peut pas être associée à elle-même.
- Il n'y a qu'une seule paire qui convient : dès qu'on l'a trouvée, on peut s'arrêter.

**La réponse attendue.** Le **produit** des deux valeurs trouvées (et non leur somme, qui vaut toujours 2020). Par exemple, pour les dépenses 1000, 300, 1020, 45, la paire est formée de 1000 et 1020 : la réponse serait 1020000.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les elfes sont ravis, mais il leur reste une ancienne note de frais à vérifier selon une autre règle. Le fichier est le même ; seul le nombre de dépenses à associer change.

**La nouvelle règle.**
- Il faut cette fois trouver les **trois** lignes différentes dont les valeurs ont pour somme 2020.
- Comme dans la partie 1, une ligne ne peut servir qu'une fois, et il n'y a qu'un seul triplet qui convient.

**La réponse attendue.** Le produit de ces trois valeurs. Par exemple, pour les dépenses 1000, 700, 320, 55, le triplet est formé de 1000, 700 et 320 : la réponse serait 224000000.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-07-defi-aoc-2020-01.zip](../../zips/terminale-07-defi-aoc-2020-01.zip).
