# Défi Advent of Code — Binary Diagnostic (2021, jour 3)

Première NSI — Chapitre 3 — Les types construits.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le sous-marin fait des bruits inquiétants, et l'on demande son rapport de diagnostic. Ce rapport ne se lit pas nombre par nombre : on l'étudie colonne par colonne pour en déduire deux nombres, γ (*gamma*) et ε (*epsilon*), qui permettent de calculer la consommation électrique du sous-marin.

**Les données.** Chaque ligne du fichier est un nombre écrit en binaire, c'est-à-dire une suite de `0` et de `1`, comme `00110`. Toutes les lignes ont la même longueur ; on peut donc les écrire les unes sous les autres et lire des **colonnes** : la colonne k réunit les bits en position k de tous les nombres.

**La règle.**
- Le nombre γ se construit bit par bit : son bit en position k est le bit **le plus fréquent** dans la colonne k du rapport.
- Le nombre ε se construit de même avec le bit **le moins fréquent** de chaque colonne. Autrement dit, ε s'écrit avec les bits contraires de ceux de γ.
- On convertit ensuite γ et ε de la base 2 vers la base 10.

**La réponse attendue.** Le produit des valeurs **en base 10** de γ et ε. Par exemple, pour les trois nombres `110`, `100` et `011`, les bits les plus fréquents des trois colonnes sont `1`, `1` et `0` : γ s'écrit `110` (soit 6) et ε s'écrit `001` (soit 1), donc la réponse serait 6 × 1 = 6.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On vérifie maintenant le système de survie du sous-marin. Il faut encore deux valeurs, mais elles ne se construisent plus bit par bit : chacune est l'un des nombres du rapport, trouvé par **élimination**.

**La nouvelle règle.**
- On part de la liste complète et l'on examine les colonnes de gauche à droite.
- Pour la première valeur, à chaque colonne, on ne garde que les nombres dont le bit vaut le bit **le plus fréquent** de cette colonne ; en cas d'égalité, on garde ceux qui ont un `1`.
- Pour la seconde valeur, on garde au contraire ceux dont le bit vaut le bit **le moins fréquent** ; en cas d'égalité, on garde ceux qui ont un `0`.
- Le bit le plus ou le moins fréquent se calcule **sur les nombres restants**, pas sur la liste de départ.
- On s'arrête dès qu'il ne reste qu'un nombre : c'est la valeur cherchée.

**La réponse attendue.** Le produit des deux valeurs en base 10. Par exemple, avec `110`, `100` et `011` : pour la première valeur, la colonne 0 fait garder `110` et `100`, puis la colonne 1 est à égalité, on garde `110` (soit 6) ; pour la seconde, la colonne 0 ne laisse que `011` (soit 3). La réponse serait 6 × 3 = 18.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-03-defi-aoc-2021-03.zip](../../zips/premiere-03-defi-aoc-2021-03.zip).
