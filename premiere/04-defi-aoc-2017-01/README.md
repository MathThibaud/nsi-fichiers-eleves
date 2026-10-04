# Défi Advent of Code — Inverse Captcha (2017, jour 1)

Première NSI — Chapitre 4 — Algorithmique : le parcours séquentiel.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2017/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous êtes aspiré dans un ordinateur, devant une porte verrouillée. Pour sortir, il faut résoudre un « captcha » inversé, censé prouver que vous *n'êtes pas* un humain. Le fichier contient ce captcha : une très longue suite de chiffres, à traiter comme une suite de caractères.

**Ce qu'il faut faire.**
- Le fichier ne contient qu'**une seule ligne**, formée de chiffres collés les uns aux autres.
- On compare chaque chiffre au chiffre **suivant**. Quand ils sont égaux, on ajoute la valeur de ce chiffre à une somme ; sinon, on n'ajoute rien.
- La suite est **circulaire** : on imagine les chiffres disposés en cercle, si bien que le suivant du dernier chiffre est le premier.
- La réponse est la somme obtenue.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le système demande maintenant une vérification plus difficile. Même calcul, mais chaque chiffre est comparé au chiffre situé **une demi-longueur plus loin**, toujours en tournant en cercle (la longueur de la suite est paire). Autrement dit, sur le cercle, on compare chaque chiffre à celui qui lui fait face.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-04-defi-aoc-2017-01.zip](../../zips/premiere-04-defi-aoc-2017-01.zip).
