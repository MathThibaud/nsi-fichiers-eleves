# Défi Advent of Code — High-Entropy Passphrases (2017, jour 4)

Première NSI — Chapitre 7 — La recherche dichotomique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2017/day/4>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Un nouveau système informatique protège ses comptes par des « phrases de passe » plutôt que par des mots de passe. Pour qu'une phrase soit assez sûre, elle doit respecter une règle de construction. On dispose d'une liste de phrases de passe et l'on veut savoir combien d'entre elles sont acceptables.

**Les données.** Le fichier contient une phrase de passe par ligne. Une phrase est formée de plusieurs mots en lettres minuscules, séparés par des espaces. Le nombre de mots varie d'une ligne à l'autre.

**La règle.**
- Une phrase est valide si elle ne contient **jamais deux fois le même mot**.
- Il faut que les deux mots soient exactement identiques pour faire un doublon : une simple ressemblance (un mot contenu dans un autre, les mêmes lettres dans un autre ordre) ne rend pas la phrase invalide.
- Une phrase d'un seul mot est donc toujours valide.

**La réponse attendue.** Le nombre de lignes valides du fichier. Par exemple, la ligne `vert bleu vert` est invalide (`vert` deux fois), alors que `vert verte` est valide.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le service de sécurité durcit la règle : un mot ne doit pas pouvoir s'obtenir en mélangeant les lettres d'un autre mot de la même ligne.

**La nouvelle règle.**
- Une phrase est valide si aucun de ses mots n'est une **anagramme** d'un autre de ses mots.
- Deux mots sont anagrammes s'ils ont les mêmes lettres, chacune en même nombre, dans un ordre éventuellement différent.
- Deux mots identiques sont aussi anagrammes : une ligne invalide dans la partie 1 reste invalide.

**La réponse attendue.** Le nombre de lignes valides avec cette nouvelle règle. Par exemple, `pot top` est maintenant invalide, mais `pot pots` reste valide (un `s` de plus).

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-07-defi-aoc-2017-04.zip](../../zips/premiere-07-defi-aoc-2017-04.zip).
