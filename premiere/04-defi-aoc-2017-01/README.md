# Défi Advent of Code — Inverse Captcha (2017, jour 1)

Première NSI — Chapitre 4 — Algorithmique : le parcours séquentiel.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2017/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous êtes aspiré dans un ordinateur, devant une porte verrouillée. Pour sortir, il faut résoudre un « captcha » inversé : au lieu de prouver que vous êtes un humain, il doit prouver que vous *n'êtes pas* un humain, en faisant un calcul long et fastidieux sans se tromper.

**Les données.** Le fichier ne contient qu'**une seule ligne**, formée de chiffres collés les uns aux autres, sans espace. Chaque chiffre se traite séparément : il faut voir cette ligne comme une suite de caractères, et non comme un seul (immense) nombre.

**La règle.**
- On compare chaque chiffre au chiffre **suivant**.
- Quand ils sont égaux, on ajoute la valeur de ce chiffre à une somme ; sinon, on n'ajoute rien.
- La suite est **circulaire** : on imagine les chiffres disposés en cercle, si bien que le suivant du dernier chiffre est le premier.
- Chaque chiffre est comparé exactement une fois à son suivant : un chiffre peut donc être ajouté plusieurs fois s'il apparaît à plusieurs endroits.

**La réponse attendue.** La somme obtenue après avoir fait le tour complet du cercle. Par exemple, pour `4114`, les deux `1` se suivent (on ajoute 1) et le dernier `4` est suivi, en revenant au début, du premier `4` (on ajoute 4) : la réponse serait 5.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le système demande maintenant une vérification plus difficile. On compare toujours chaque chiffre à un autre chiffre de la suite, mais ce n'est plus son voisin immédiat.

**La nouvelle règle.**
- Chaque chiffre est comparé au chiffre situé **une demi-longueur plus loin**, en tournant toujours en cercle. La longueur de la suite est paire, donc cette demi-longueur est un entier.
- Autrement dit, sur le cercle, on compare chaque chiffre à celui qui lui fait face.
- Comme dans la partie 1, quand les deux chiffres sont égaux, on ajoute la valeur du chiffre à la somme.

**La réponse attendue.** La somme obtenue avec cette nouvelle règle. Par exemple, pour `1414` (longueur 4, on compare donc chaque chiffre à celui situé 2 places plus loin), chaque chiffre est égal à celui qui lui fait face : la réponse serait 1 + 4 + 1 + 4 = 10.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-04-defi-aoc-2017-01.zip](../../zips/premiere-04-defi-aoc-2017-01.zip).
