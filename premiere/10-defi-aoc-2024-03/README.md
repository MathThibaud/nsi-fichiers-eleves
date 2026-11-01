# Défi Advent of Code — Mull It Over (2024, jour 3)

Première NSI — Chapitre 10 — Le Web : réseaux et interactions homme-machine.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2024/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** L'ordinateur d'un magasin de location de luges est en panne : sa mémoire a été abîmée et ressemble à un long texte plein de caractères au hasard. Quelques instructions de multiplication ont survécu au milieu de ce désordre. Il faut les retrouver pour savoir ce que le programme calculait.

**Les données.** Le fichier contient cette mémoire : un texte formé de caractères quelconques (lettres, chiffres, parenthèses, ponctuation, espaces), parfois réparti sur plusieurs lignes. Il n'y a pas de séparateur régulier : on ne peut pas découper le texte avec `split`.

**La règle.**
- Une instruction valide s'écrit **exactement** `mul(X,Y)` : les lettres `mul`, une parenthèse ouvrante, un entier `X`, une virgule, un entier `Y`, une parenthèse fermante.
- `X` et `Y` s'écrivent avec **1 à 3 chiffres**, sans espace ni autre caractère nulle part dans l'instruction. Elle calcule `X * Y`.
- Tout motif qui ressemble mais n'est pas exact (espace, crochet à la place d'une parenthèse, nombre de 4 chiffres, nombre manquant…) est un débris : on l'ignore.
- Deux instructions valides peuvent être collées l'une à l'autre, ou noyées au milieu d'autres caractères : elles comptent toutes.

**La réponse attendue.** La somme des produits de toutes les instructions valides. Par exemple, dans le texte `amul(2,3)bmul(4,5 )`, seule la première instruction est valide (la seconde contient une espace) : la réponse serait 6.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** En regardant mieux, on s'aperçoit que la mémoire contient aussi des interrupteurs, qui activent ou désactivent les multiplications.

**La nouvelle règle.**
- L'instruction `do()` active les `mul` qui la suivent ; l'instruction `don't()` les désactive.
- Seul le plus récent des deux interrupteurs rencontrés compte.
- Au début du texte, avant tout interrupteur, les `mul` sont actifs.
- Les `mul` valides restent ceux de la partie 1 ; un `mul` désactivé est simplement ignoré.

**La réponse attendue.** La somme des produits des seuls `mul` valides et actifs. Par exemple, dans `mul(2,3)don't()mul(4,5)do()mul(1,7)`, la deuxième instruction est désactivée : la réponse serait 6 + 7 = 13.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-10-defi-aoc-2024-03.zip](../../zips/premiere-10-defi-aoc-2024-03.zip).
