# Défi Advent of Code — Ticket Translation (2020, jour 16)

Terminale NSI — Chapitre 6 — Bases de données et SQL.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/16>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Votre trajet passe par un train à grande vitesse, mais le billet est écrit dans une langue inconnue : vous ne pouvez lire que les nombres. Vous avez rassemblé dans un fichier les règles de validité des différents champs d'un billet, votre billet, et ceux d'autres voyageurs aperçus à la gare.

**Les données.** Le fichier a trois blocs séparés par une ligne vide.
- D'abord les règles, une par ligne, de la forme `nom: a-b or c-d` : la valeur de ce champ doit être dans l'un des deux intervalles, bornes comprises.
- Puis votre billet : la ligne `your ticket:` suivie d'une ligne.
- Enfin les billets voisins : la ligne `nearby tickets:` suivie d'une ligne par billet.

Un billet est une suite d'entiers séparés par des virgules. Les champs sont dans le même ordre sur tous les billets, mais on ne sait pas quel champ est à quelle position.

**La règle.**
- Une valeur est non valide si elle ne respecte **aucune** règle : elle ne peut correspondre à aucun champ, quelle que soit sa position.
- Il suffit qu'elle respecte une seule règle (n'importe laquelle) pour ne pas être comptée.
- On examine seulement les billets voisins : votre propre billet est laissé de côté.

**La réponse attendue.** La somme de toutes les valeurs non valides des billets voisins. Par exemple, avec les deux règles `1-3 or 7-9` et `4-6 or 10-12` et les billets voisins `2,5`, `8,13` et `20,4`, seules 13 et 20 ne respectent aucune règle : la réponse serait 13 + 20 = 33.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Il s'agit maintenant de déchiffrer votre billet : savoir à quel champ correspond chaque position.

**La nouvelle règle.**
- Écarter d'abord les billets voisins qui contiennent au moins une valeur non valide (même si cette valeur vaut 0).
- Avec les billets restants, déterminer la position de chaque champ : un champ ne peut être à une position que si **toutes** les valeurs des billets restants à cette position respectent sa règle. Une seule attribution est possible.
- Repérer les champs dont le nom commence par `departure`.

**La réponse attendue.** Le produit des valeurs de **votre** billet pour les champs dont le nom commence par `departure`. Par exemple, s'il n'y avait que deux tels champs et que votre billet portait 7 et 11 à leurs positions, la réponse serait 77.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-06-defi-aoc-2020-16.zip](../../zips/terminale-06-defi-aoc-2020-16.zip).
