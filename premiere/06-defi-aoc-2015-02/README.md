# Défi Advent of Code — I Was Told There Would Be No Math (2015, jour 2)

Première NSI — Chapitre 6 — Les algorithmes de tri.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2015/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes vont manquer de papier cadeau et doivent en commander. Tous les cadeaux sont des boîtes en forme de pavé droit, et les elfes connaissent les trois dimensions de chacune. Pour commander juste ce qu'il faut, ni trop ni trop peu, ils ont besoin de la surface totale de papier.

**Les données.** Chaque ligne décrit une boîte : trois entiers séparés par la lettre `x`, sans espace, par exemple `3x5x2`. Ce sont la longueur L, la largeur l et la hauteur h de la boîte.

**La règle.**
- Une boîte a six faces, égales deux à deux : il faut de quoi les recouvrir toutes, soit l'aire totale 2Ll + 2lh + 2hL.
- On ajoute un peu de marge : l'aire de la **plus petite face** de la boîte, ajoutée une seule fois.
- On fait ce calcul pour chaque boîte, puis on additionne.

**La réponse attendue.** La somme de ces quantités sur toutes les boîtes. Par exemple, pour une seule boîte `1x2x3`, l'aire totale vaut 2 × 2 + 2 × 6 + 2 × 3 = 22 et la plus petite face a pour aire 2 : la réponse serait 24.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les elfes doivent aussi commander du ruban. Le fichier est le même ; on calcule maintenant une longueur de ruban pour chaque boîte, au lieu d'une aire de papier.

**La nouvelle règle.**
- Il faut de quoi faire le tour de la boîte par le côté le plus court, c'est-à-dire le **plus petit périmètre** parmi ceux des faces.
- Il faut en plus de quoi faire le nœud : une longueur égale au **volume** de la boîte.
- Le ruban d'une boîte est la somme de ces deux longueurs.

**La réponse attendue.** La somme des longueurs de ruban sur toutes les boîtes. Pour la boîte `1x2x3`, le plus petit périmètre de face vaut 2 × (1 + 2) = 6 et le volume vaut 6 : il faudrait 12.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-06-defi-aoc-2015-02.zip](../../zips/premiere-06-defi-aoc-2015-02.zip).
