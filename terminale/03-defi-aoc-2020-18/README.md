# Défi Advent of Code — Operation Order (2020, jour 18)

Terminale NSI — Chapitre 3 — Structures linéaires : piles, files, listes chaînées.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/18>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En 2020, les elfes vous ont laissé partir en vacances sous les tropiques. Pendant un vol, un enfant assis à côté de vous vous demande de l'aide pour ses devoirs de calcul... mais dans son école, les règles de priorité ne sont pas celles que vous connaissez. Chaque ligne du fichier est un calcul de son cahier.

**Ce qu'il faut faire.**
- Une expression contient des entiers positifs (d'un seul chiffre dans les données), les opérateurs `+` et `*`, et des parenthèses ; les symboles sont séparés par des espaces.
- Les parenthèses gardent leur rôle : leur contenu se calcule d'abord, et elles peuvent être imbriquées.
- En revanche, `*` n'est **pas** prioritaire sur `+` : en dehors des parenthèses, on effectue les opérations dans l'ordre où on les lit, de gauche à droite. Autrement dit, `2 + 3 * 4` se calcule comme `(2 + 3) * 4`.
- Réponse : la somme des valeurs de toutes les lignes.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Vous avez mal compris : dans cette école, il existe bien une priorité, mais à l'envers de la vôtre. L'**addition est prioritaire** sur la multiplication. Les parenthèses passent toujours en premier ; à priorité égale, on calcule de gauche à droite. Ainsi `2 * 3 + 4` vaut maintenant 2 × 7 = 14. Réponse : la somme des valeurs des lignes.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-03-defi-aoc-2020-18.zip](../../zips/terminale-03-defi-aoc-2020-18.zip).
