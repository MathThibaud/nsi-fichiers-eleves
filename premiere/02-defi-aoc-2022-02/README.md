# Défi Advent of Code — Rock Paper Scissors (2022, jour 2)

Première NSI — Chapitre 2 — Le binaire et l'écriture des nombres.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes organisent un grand tournoi de pierre-feuille-ciseaux pour décider qui plantera sa tente le plus près des provisions. Un elfe vous confie un guide « secret » qui annonce, manche par manche, ce que jouera votre adversaire et ce que vous devriez jouer. Avant de lui faire confiance, vous voulez savoir quel score vous obtiendriez en le suivant.

**Ce qu'il faut faire.**
- Chaque ligne décrit une manche : deux lettres séparées par une espace. La première est le coup de l'adversaire (`A` pierre, `B` feuille, `C` ciseaux). Dans la partie 1, on suppose que la seconde est votre coup (`X` pierre, `Y` feuille, `Z` ciseaux).
- La pierre bat les ciseaux, les ciseaux battent la feuille, la feuille bat la pierre ; deux formes identiques donnent un match nul.
- Le score d'une manche additionne les points de **votre** forme (pierre 1, feuille 2, ciseaux 3) et les points du résultat pour vous (défaite 0, nul 3, victoire 6).
- La réponse est la somme des scores de toutes les manches.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

L'elfe revient et explique que vous aviez mal compris sa seconde colonne : elle n'indique pas quoi jouer, mais comment la manche doit se terminer (`X` perdre, `Y` faire match nul, `Z` gagner). Il faut donc en déduire la forme à jouer face au coup de l'adversaire ; le score d'une manche se calcule ensuite comme dans la partie 1.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-02-defi-aoc-2022-02.zip](../../zips/premiere-02-defi-aoc-2022-02.zip).
