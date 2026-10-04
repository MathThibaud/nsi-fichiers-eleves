# Défi Advent of Code — Perfectly Spherical Houses in a Vacuum (2015, jour 3)

Première NSI — Chapitre 11 — Les algorithmes gloutons.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2015/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le Père Noël livre des cadeaux dans des maisons disposées sur une grille infinie, une maison par case. Un elfe un peu distrait lui indique par radio la direction à prendre, case après case ; le fichier contient toute la suite de ces indications sur une seule ligne. Le Père Noël dépose un cadeau à chaque maison où il passe, et l'on veut savoir combien de maisons auront eu au moins un cadeau.

**Ce qu'il faut faire.**
- Les caractères `^`, `v`, `>`, `<` font avancer d'une case vers le nord, le sud, l'est ou l'ouest.
- La maison de départ reçoit elle aussi un cadeau.
- Réponse : le nombre de maisons **différentes** visitées au moins une fois ; une maison visitée plusieurs fois ne compte qu'une fois.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

L'année suivante, le Père Noël se fait aider par un robot livreur. Les deux partent de la même maison et se partagent les indications à tour de rôle : le 1ᵉʳ, le 3ᵉ, le 5ᵉ… caractère pour l'un, le 2ᵉ, le 4ᵉ… pour l'autre. Réponse : le nombre de maisons différentes visitées par au moins l'un des deux, départ compris.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-11-defi-aoc-2015-03.zip](../../zips/premiere-11-defi-aoc-2015-03.zip).
