# Défi Advent of Code — I Was Told There Would Be No Math (2015, jour 2)

Première NSI — Chapitre 6 — Les algorithmes de tri.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2015/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes vont manquer de papier cadeau et doivent en commander. Tous les cadeaux sont des boîtes en forme de pavé droit, et les elfes connaissent les trois dimensions de chacune. Pour commander juste ce qu'il faut, ils ont besoin de la surface totale de papier.

**Ce qu'il faut faire.**
- Chaque ligne décrit une boîte : trois entiers séparés par la lettre `x`, la longueur L, la largeur l et la hauteur h.
- Pour une boîte, il faut de quoi recouvrir ses six faces, soit l'aire totale 2Ll + 2lh + 2hL, plus un peu de marge : l'aire de sa **plus petite face**.
- La réponse est la somme de ces quantités sur toutes les boîtes.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les elfes doivent aussi commander du ruban. Pour une boîte, il faut de quoi en faire le tour par le côté le plus court, c'est-à-dire le **plus petit périmètre** parmi ceux des faces, plus de quoi faire le nœud, une longueur égale au **volume** de la boîte. La réponse est la somme sur toutes les boîtes.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-06-defi-aoc-2015-02.zip](../../zips/premiere-06-defi-aoc-2015-02.zip).
