# Défi Advent of Code — Encoding Error (2020, jour 9)

Terminale NSI — Chapitre 5 — Diviser pour régner.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/9>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le héros branche son ordinateur sur une prise de données de l'avion. Il en sort une longue suite de nombres (le fichier, un entier par ligne), chiffrée avec un vieux procédé qui a une faille. Dans ce procédé, chaque nombre doit pouvoir s'obtenir à partir des nombres reçus juste avant lui : un nombre qui ne le peut pas trahit l'erreur.

**Ce qu'il faut faire.**
- Les 25 premiers nombres forment le *préambule* (le petit exemple de l'énoncé en utilise 5). Ils ne sont pas testés.
- Chaque nombre suivant doit être la somme de deux nombres de **valeurs différentes** pris parmi les 25 qui le précèdent immédiatement. Autrement dit, on regarde une fenêtre de 25 nombres qui glisse d'un cran à chaque nouveau nombre.
- Il faut renvoyer le premier nombre qui ne respecte pas la règle.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Pour exploiter la faille, il faut se servir du nombre fautif trouvé en partie 1.
- Trouver une suite d'**au moins deux** nombres consécutifs du fichier dont la somme vaut ce nombre.
- Il faut renvoyer la somme du plus petit et du plus grand nombre de cette suite (ce ne sont pas forcément le premier et le dernier).

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-05-defi-aoc-2020-09.zip](../../zips/terminale-05-defi-aoc-2020-09.zip).
