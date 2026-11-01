# Défi Advent of Code — Trebuchet?! (2023, jour 1)

Première NSI — Chapitre 5 — Spécifier et mettre au point ses programmes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2023/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les elfes s'apprêtent à vous envoyer dans le ciel avec un trébuchet, mais son document de réglage a été « décoré » par un jeune elfe : à chaque ligne, les nombres utiles sont noyés au milieu de lettres et d'autres chiffres. Avant le lancement, il faut retrouver la valeur de réglage cachée dans chaque ligne.

**Les données.** Chaque ligne du fichier est une chaîne qui mêle des lettres minuscules et des chiffres, par exemple `x3yz7k`. Chaque ligne contient au moins un chiffre.

**La règle.**
- Dans une ligne, on repère le **premier** chiffre (le plus à gauche) et le **dernier** chiffre (le plus à droite) ; les chiffres du milieu ne servent pas.
- La valeur de la ligne est le nombre à deux chiffres obtenu en écrivant le premier chiffre puis le dernier. On accole les deux chiffres, on ne les additionne pas.
- S'il n'y a qu'un chiffre, il sert à la fois de premier et de dernier.

**La réponse attendue.** La somme des valeurs de toutes les lignes. Par exemple, la ligne `a4b7c2` vaut 42 (premier chiffre 4, dernier chiffre 2 ; le 7 ne sert pas) ; un fichier formé de cette seule ligne donnerait la réponse 42.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On s'aperçoit que certains chiffres étaient écrits en toutes lettres, en anglais, au milieu des autres lettres : ils comptaient eux aussi.

**La nouvelle règle.**
- Les mots `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine` comptent maintenant comme les chiffres 1 à 9.
- Le premier et le dernier chiffre d'une ligne peuvent donc être écrits avec un chiffre ou en lettres.
- La valeur d'une ligne se calcule comme avant, en accolant le premier et le dernier chiffre.

**La réponse attendue.** La somme des nouvelles valeurs de toutes les lignes. Par exemple, la ligne `xtwo3sevenx` vaut 27 : son premier chiffre est `two` et son dernier est `seven`.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-05-defi-aoc-2023-01.zip](../../zips/premiere-05-defi-aoc-2023-01.zip).
