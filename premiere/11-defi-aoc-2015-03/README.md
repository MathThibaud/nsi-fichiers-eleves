# Défi Advent of Code — Perfectly Spherical Houses in a Vacuum (2015, jour 3)

Première NSI — Chapitre 11 — Les algorithmes gloutons.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2015/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le Père Noël livre des cadeaux dans des maisons disposées sur une grille infinie, une maison par case. Un elfe un peu distrait lui indique par radio la direction à prendre, case après case. Le Père Noël dépose un cadeau dans chaque maison où il passe ; comme il repasse parfois au même endroit, certaines maisons reçoivent plusieurs cadeaux. On veut savoir combien de maisons auront eu au moins un cadeau.

**Les données.** Le fichier contient **une seule ligne**, très longue : la suite de toutes les indications de l'elfe. Chaque caractère est une flèche : `^` (nord), `v` (sud), `>` (est) ou `<` (ouest).

**La règle.**
- Le Père Noël part d'une maison de départ, qui reçoit elle aussi un cadeau.
- On lit les caractères dans l'ordre ; chacun le fait avancer d'**une** case dans la direction indiquée, et il dépose un cadeau dans la maison où il arrive.
- Une maison visitée plusieurs fois (y compris la maison de départ, s'il y revient) ne compte qu'une fois.

**La réponse attendue.** Le nombre de maisons **différentes** visitées au moins une fois, départ compris. Par exemple, avec la ligne `>>`, trois maisons sont visitées ; avec la ligne `^v^v`, le Père Noël fait des allers-retours entre deux maisons : la réponse serait 2.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** L'année suivante, le Père Noël se fait aider par un robot livreur. Les deux partent de la même maison de départ et se partagent la même ligne d'indications.

**La nouvelle règle.**
- Les indications sont distribuées à tour de rôle : le 1ᵉʳ, le 3ᵉ, le 5ᵉ… caractère pour le Père Noël, le 2ᵉ, le 4ᵉ… pour le robot.
- Chacun se déplace uniquement avec ses propres indications, en partant de la maison de départ, selon la même règle que dans la partie 1.
- Une maison visitée par les deux, ou plusieurs fois, ne compte qu'une fois.

**La réponse attendue.** Le nombre de maisons différentes visitées par au moins l'un des deux, départ compris. Par exemple, avec la ligne `^v^v`, le Père Noël reçoit les deux `^` et le robot les deux `v` : ils s'éloignent chacun de deux cases, et la réponse serait 5 (contre 2 dans la partie 1).

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-11-defi-aoc-2015-03.zip](../../zips/premiere-11-defi-aoc-2015-03.zip).
