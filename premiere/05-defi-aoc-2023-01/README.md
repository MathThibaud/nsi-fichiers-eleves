# Défi Advent of Code — Trebuchet?! (2023, jour 1)

Première NSI — Chapitre 5 — Spécifier et mettre au point ses programmes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2023/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes s'apprêtent à vous envoyer dans le ciel avec un trébuchet, mais son document de réglage a été « décoré » par un jeune elfe : à chaque ligne, les nombres utiles sont noyés au milieu de lettres et d'autres chiffres. Il faut retrouver, pour chaque ligne, une valeur de réglage avant le lancement.

**Ce qu'il faut faire.**
- Chaque ligne est une chaîne mêlant lettres et chiffres, avec au moins un chiffre.
- La valeur d'une ligne est le nombre à deux chiffres formé par son **premier** chiffre suivi de son **dernier** chiffre. On accole les deux chiffres, on ne les additionne pas.
- S'il n'y a qu'un chiffre, il sert à la fois de premier et de dernier.
- Réponse : la somme des valeurs de toutes les lignes.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

On s'aperçoit que certains chiffres étaient écrits en toutes lettres. Les chiffres de 1 à 9 écrits en anglais (`one`, `two`, …, `nine`) comptent maintenant aussi comme des chiffres. La valeur d'une ligne se calcule comme avant, avec le premier et le dernier chiffre, qu'ils soient écrits avec un chiffre ou en lettres.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-05-defi-aoc-2023-01.zip](../../zips/premiere-05-defi-aoc-2023-01.zip).
