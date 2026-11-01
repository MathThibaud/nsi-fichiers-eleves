# Défi Advent of Code — Binary Boarding (2020, jour 5)

Terminale NSI — Chapitre 5 — Arbres.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/5>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le héros est enfin dans l'avion… mais il a perdu sa carte d'embarquement. Il photographie celles des autres passagers pour retrouver sa place par élimination. La première étape est de savoir lire ces cartes.

**Les données.** Chaque ligne du fichier est le code de place imprimé sur une carte : 10 lettres. Les 7 premières (`F` ou `B`) donnent le rang, numéroté de 0 à 127 ; les 3 dernières (`L` ou `R`) donnent la colonne, de 0 à 7.

**La règle.**
- Pour le rang, on part de l'intervalle complet des rangs, de 0 à 127.
- Chaque lettre coupe l'intervalle restant en deux moitiés égales : `F` garde la moitié basse, `B` la moitié haute. Après la septième lettre, il ne reste qu'un rang.
- On procède de même pour la colonne, de 0 à 7, avec `L` (moitié basse) et `R` (moitié haute) : après trois lettres, il ne reste qu'une colonne.
- Chaque siège a un numéro : rang × 8 + colonne.

**La réponse attendue.** Le plus grand numéro de siège présent dans le fichier. Par exemple, le code `FFFFFFBRLL` désigne le rang 1 et la colonne 4, donc le siège numéro 1 × 8 + 4 = 12.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Il reste à trouver la place du héros, puisque c'est la seule dont la carte manque. On utilise les mêmes numéros de siège que dans la partie 1.

**La nouvelle règle.**
- L'avion est plein, sauf quelques sièges tout à l'avant et tout à l'arrière qui n'existent pas : ces numéros-là manquent aussi dans la liste, mais ce ne sont pas des places.
- Votre siège est absent de la liste, mais les numéros juste avant et juste après le vôtre y figurent.

**La réponse attendue.** Le numéro de votre siège. Par exemple, si les numéros présents étaient 40, 41, 43 et 44, votre place serait la 42.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-05-defi-aoc-2020-05.zip](../../zips/terminale-05-defi-aoc-2020-05.zip).
