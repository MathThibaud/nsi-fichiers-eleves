# Défi Advent of Code — Calorie Counting (2022, jour 1)

Première NSI — Chapitre 3 — Les types construits.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Une expédition d'elfes part à pied dans la jungle chercher des fruits magiques. Avant le départ, chaque elfe a noté la valeur énergétique (en calories) de chacun des aliments qu'il emporte dans son sac. Pour prévoir les pauses, on veut savoir quel elfe transporte le plus de calories.

**Les données.** Le fichier rassemble toutes ces notes. Chaque ligne non vide contient **un seul entier** : les calories d'un aliment. Les aliments d'un même elfe sont écrits les uns sous les autres, en un bloc. Une **ligne vide** sépare le bloc d'un elfe de celui de l'elfe suivant ; il n'y en a pas après le dernier elfe.

**La règle.**
- On découpe le fichier en blocs, aux lignes vides : chaque bloc correspond à un elfe.
- Le total d'un elfe est la somme des nombres de son bloc. Un elfe peut n'avoir qu'un seul aliment : son total est alors ce nombre.
- Le dernier bloc n'est suivi d'aucune ligne vide, mais c'est bien un elfe comme les autres.
- On cherche le plus grand de tous ces totaux.

**La réponse attendue.** La **valeur** du plus grand total, et non le numéro de l'elfe qui le porte. Par exemple, pour trois elfes portant 100 et 200, puis 500, puis 150, 150 et 150, les totaux sont 300, 500 et 450 : la réponse serait 500.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Compter sur un seul elfe est risqué : s'il a une fringale et mange ses provisions, la réserve disparaît. Pour ne plus dépendre d'un seul elfe, on s'intéresse maintenant aux **trois** elfes les mieux approvisionnés.

**La nouvelle règle.**
- Le fichier se découpe en elfes exactement comme dans la partie 1, et le total de chaque elfe se calcule de la même façon.
- On repère les trois plus grands totaux (le plus grand, le deuxième plus grand, le troisième plus grand).
- On additionne ces trois totaux.

**La réponse attendue.** La **somme des trois plus grands totaux**. Avec les totaux 300, 500, 450 et 200, par exemple, on garderait 500, 450 et 300 : la réponse serait 1250.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-03-defi-aoc-2022-01.zip](../../zips/premiere-03-defi-aoc-2022-01.zip).
