# Défi Advent of Code — Camp Cleanup (2022, jour 4)

Première NSI — Chapitre 8 — Les données en tables.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/4>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Avant le départ du traîneau, les elfes doivent nettoyer le camp, découpé en zones numérotées. Chaque elfe reçoit une plage de numéros de zones, et les elfes travaillent par deux. En comparant les plages des deux membres d'un même binôme, on s'aperçoit que certains font en partie le même travail, et que parfois l'un des deux ne sert à rien.

**Les données.** Chaque ligne du fichier décrit un binôme et a la forme `a-b,c-d`, où `a`, `b`, `c`, `d` sont des entiers. La partie avant la virgule est la plage du premier elfe : les zones `a` à `b`. La partie après la virgule est celle du second : les zones `c` à `d`. Les **bornes sont comprises**, et l'on peut avoir `a = b` (une seule zone).

**La règle.**
- Pour chaque ligne, on regarde si l'une des deux plages est **entièrement incluse** dans l'autre : toutes ses zones font aussi partie de l'autre plage.
- On teste les deux sens : la plage du premier dans celle du second, ou celle du second dans celle du premier.
- Si c'est le cas, l'un des deux elfes est complètement inutile : la ligne compte (une seule fois, même si les deux plages sont identiques).

**La réponse attendue.** Le nombre de lignes où une plage est incluse dans l'autre. Par exemple, la ligne `2-9,4-6` compte (les zones 4 à 6 font partie des zones 2 à 9), mais pas la ligne `2-5,4-8` (les zones 6 à 8 du second elfe dépassent).

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les elfes veulent maintenant repérer tous les doublons de travail, même partiels : il n'est plus nécessaire qu'une plage soit entièrement dans l'autre.

**La nouvelle règle.**
- Une ligne compte si les deux plages ont **au moins une zone en commun** : elles se chevauchent, ne serait-ce que d'un numéro.
- Une inclusion est un cas particulier de chevauchement : les lignes comptées dans la partie 1 comptent donc aussi.

**La réponse attendue.** Le nombre de lignes où les deux plages se chevauchent. Par exemple, `2-5,4-8` compte maintenant (zones 4 et 5 en commun), mais pas `2-3,6-8`.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-08-defi-aoc-2022-04.zip](../../zips/premiere-08-defi-aoc-2022-04.zip).
