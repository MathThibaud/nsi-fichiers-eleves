# Défi Advent of Code — Binary Diagnostic (2021, jour 3)

Première NSI — Chapitre 3 — Les types construits.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le sous-marin fait des bruits inquiétants, et l'on demande son rapport de diagnostic. Ce rapport est une liste de nombres binaires, tous de même longueur, un par ligne. On ne lit pas ces nombres un par un : on les étudie colonne par colonne pour en déduire deux nombres qui mesurent la consommation électrique du sous-marin.

**Ce qu'il faut faire.**
- Le nombre γ (*gamma*) se construit bit par bit : son bit en position k est le bit **le plus fréquent** dans la colonne k du rapport.
- Le nombre ε (*epsilon*) se construit de même avec le bit **le moins fréquent** de chaque colonne. Autrement dit, ε s'écrit avec les bits contraires de ceux de γ.
- Réponse : le produit des valeurs **en base 10** de γ et ε.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

On vérifie ensuite le système de survie, à partir de deux valeurs obtenues par élimination. On examine les colonnes de gauche à droite ; à chaque colonne, on ne garde que les nombres dont le bit vaut le bit le plus fréquent (première valeur) ou le moins fréquent (seconde valeur), **calculé sur les nombres restants**. On s'arrête quand il n'en reste qu'un. En cas d'égalité, on garde `1` pour la première valeur et `0` pour la seconde. Réponse : le produit des deux valeurs en base 10.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-03-defi-aoc-2021-03.zip](../../zips/premiere-03-defi-aoc-2021-03.zip).
