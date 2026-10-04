# Défi Advent of Code — Ticket Translation (2020, jour 16)

Terminale NSI — Chapitre 6 — Bases de données et SQL.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/16>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Votre trajet passe par un train à grande vitesse, mais le billet est écrit dans une langue inconnue : vous ne pouvez lire que les nombres. Vous avez rassemblé dans un fichier les règles de validité des différents champs d'un billet, votre billet, et ceux d'autres voyageurs aperçus à la gare.

**Ce qu'il faut faire.**
- Le fichier a trois blocs séparés par une ligne vide. D'abord les règles `nom: a-b or c-d` : la valeur de ce champ doit être dans l'un des deux intervalles, bornes comprises. Puis votre billet (`your ticket:` suivi d'une ligne). Enfin les billets voisins (`nearby tickets:` suivi d'une ligne par billet).
- Un billet est une suite d'entiers séparés par des virgules. Les champs sont dans le même ordre sur tous les billets, mais on ne sait pas quel champ est à quelle position.
- Une valeur est non valide si elle ne respecte **aucune** règle : elle ne peut correspondre à aucun champ, quelle que soit sa position.
- La réponse est la somme de toutes les valeurs non valides des billets voisins (votre propre billet est laissé de côté).

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Il s'agit maintenant de déchiffrer votre billet : savoir à quel champ correspond chaque position.
- Écarter d'abord les billets voisins qui contiennent au moins une valeur non valide.
- Avec les billets restants, déterminer la position de chaque champ (une seule attribution est possible).
- La réponse est le produit des valeurs de **votre** billet pour les champs dont le nom commence par `departure`.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-06-defi-aoc-2020-16.zip](../../zips/terminale-06-defi-aoc-2020-16.zip).
