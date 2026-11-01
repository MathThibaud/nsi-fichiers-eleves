# Défi Advent of Code — Encoding Error (2020, jour 9)

Terminale NSI — Chapitre 7 — Diviser pour régner.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/9>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le héros branche son ordinateur sur une prise de données de l'avion. Il en sort une longue suite de nombres, chiffrée avec un vieux procédé qui comporte une faille. Dans ce procédé, chaque nombre doit pouvoir s'obtenir à partir des nombres reçus juste avant lui : un nombre qui ne le peut pas trahit l'erreur, et c'est lui qu'on cherche.

**Les données.** Le fichier contient **un entier positif par ligne**, dans l'ordre de réception. Seule la position compte : le nombre de la ligne 30 est testé à l'aide des nombres des lignes qui le précèdent immédiatement.

**La règle.**
- Les 25 premiers nombres forment le *préambule* (le petit exemple de l'énoncé en utilise 5). Ils ne sont pas testés : ils servent seulement de point de départ.
- Chaque nombre suivant doit être la somme de deux nombres de **valeurs différentes** pris parmi les 25 nombres qui le précèdent immédiatement. Deux nombres égaux ne forment donc pas une paire valable.
- On regarde ainsi une *fenêtre* de 25 nombres qui glisse d'un cran à chaque nouveau nombre : le plus ancien en sort, le nombre qu'on vient de tester y entre. Un nombre sorti de la fenêtre ne peut plus servir.
- Le premier nombre pour lequel aucune paire ne convient est le nombre fautif.

**La réponse attendue.** Ce premier nombre qui ne respecte pas la règle. Par exemple, avec un préambule de 3 et la suite 2, 5, 4, 7, 9, 30 : 7 vaut 2 + 5, 9 vaut 5 + 4, mais 30 ne s'obtient pas avec 4, 7 et 9 : la réponse serait 30.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Pour exploiter la faille, on se sert du nombre fautif trouvé en partie 1 : on ne cherche plus une paire, mais une **suite contiguë** de nombres du fichier, c'est-à-dire des nombres qui se suivent sans trou.

**La nouvelle règle.**
- Trouver une suite d'**au moins deux** nombres consécutifs du fichier dont la somme vaut exactement le nombre fautif. Le nombre fautif seul ne compte donc pas comme une suite.
- Dans cette suite, repérer le plus petit et le plus grand nombre. Attention : ce ne sont pas forcément le premier et le dernier de la suite.

**La réponse attendue.** La somme du plus petit et du plus grand nombre de cette suite. Par exemple, si le nombre fautif était 18 et que le fichier contenait 2, 5, 4, 7 à la suite, la suite serait 2, 5, 4, 7 et la réponse 2 + 7 = 9.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-07-defi-aoc-2020-09.zip](../../zips/terminale-07-defi-aoc-2020-09.zip).
