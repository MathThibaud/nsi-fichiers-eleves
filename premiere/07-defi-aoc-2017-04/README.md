# Défi Advent of Code — High-Entropy Passphrases (2017, jour 4)

Première NSI — Chapitre 7 — La recherche dichotomique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2017/day/4>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Un nouveau système informatique protège ses comptes par des « phrases de passe » : plusieurs mots en minuscules séparés par des espaces. Pour qu'une phrase soit assez sûre, elle doit respecter une règle de construction. Le fichier contient une liste de phrases de passe, une par ligne, et l'on veut savoir combien sont acceptables.

**Ce qu'il faut faire.**
- Une phrase est valide si elle ne contient **jamais deux fois le même mot**, exactement le même (une ressemblance ne suffit pas à la rendre invalide).
- Réponse : le nombre de lignes valides.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le service de sécurité durcit la règle : un mot ne doit pas pouvoir s'obtenir en mélangeant les lettres d'un autre mot de la même ligne. Une phrase est valide si aucun mot n'est une **anagramme** d'un autre (mêmes lettres, en même nombre, dans un ordre éventuellement différent). Deux mots identiques sont aussi anagrammes. Réponse : le nombre de lignes valides.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-07-defi-aoc-2017-04.zip](../../zips/premiere-07-defi-aoc-2017-04.zip).
