# Défi Advent of Code — Camp Cleanup (2022, jour 4)

Première NSI — Chapitre 8 — Les données en tables.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/4>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Avant le départ du traîneau, les elfes doivent nettoyer le camp, découpé en zones numérotées. Chaque elfe reçoit une plage de numéros de zones, et les elfes travaillent par deux. En comparant les plages, on s'aperçoit que certains binômes font en partie le même travail. Chaque ligne du fichier décrit un binôme : les deux plages de zones confiées à ses deux membres.

**Ce qu'il faut faire.**
- Une ligne a la forme `a-b,c-d` : le premier elfe s'occupe des zones `a` à `b`, le second des zones `c` à `d`, **bornes comprises** (on peut avoir `a = b` : une seule zone).
- On cherche les binômes où l'un des deux elfes est complètement inutile, autrement dit où l'une des plages est **entièrement incluse** dans l'autre, dans un sens ou dans l'autre.
- Réponse : le nombre de lignes concernées.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les elfes veulent maintenant repérer tous les doublons de travail, même partiels. On compte les lignes où les deux plages ont **au moins une zone en commun** (elles se chevauchent, ne serait-ce que d'un numéro). Une inclusion est un cas particulier de chevauchement, donc ces lignes comptent aussi.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-08-defi-aoc-2022-04.zip](../../zips/premiere-08-defi-aoc-2022-04.zip).
