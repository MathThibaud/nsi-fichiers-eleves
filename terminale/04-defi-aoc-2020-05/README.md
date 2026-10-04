# Défi Advent of Code — Binary Boarding (2020, jour 5)

Terminale NSI — Chapitre 4 — Arbres.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/5>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le héros est enfin dans l'avion…{} mais il a perdu sa carte d'embarquement. Il photographie celles des autres passagers pour retrouver sa place par élimination. Chaque ligne du fichier est le code de place imprimé sur une carte ; ce code désigne un rang et une colonne de l'avion, avec un système de découpages successifs en deux.

**Ce qu'il faut faire.**
- Un code compte 10 lettres. Les 7 premières (`F` ou `B`) donnent le rang, numéroté de 0 à 127 ; les 3 dernières (`L` ou `R`) donnent la colonne, de 0 à 7.
- Pour décoder, on part de l'intervalle complet des rangs. `F` garde la moitié basse et `B` la moitié haute ; après la septième lettre il ne reste qu'un rang. On procède de même pour la colonne avec `L` (moitié basse) et `R` (moitié haute).
- Chaque siège a un numéro : rang × 8 + colonne.
- Il faut renvoyer le plus grand numéro de siège présent dans le fichier.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Il reste à trouver la place du héros, puisque c'est la seule dont la carte manque.
- L'avion est plein, sauf quelques sièges tout à l'avant et tout à l'arrière qui n'existent pas. Votre siège est absent de la liste, mais les numéros juste avant et juste après le vôtre y figurent.
- Il faut renvoyer le numéro de votre siège.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-04-defi-aoc-2020-05.zip](../../zips/terminale-04-defi-aoc-2020-05.zip).
