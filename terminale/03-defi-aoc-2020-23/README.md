# Défi Advent of Code — Crab Cups (2020, jour 23)

Terminale NSI — Chapitre 3 — Structures linéaires : piles, files, listes chaînées.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/23>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le crabe vous défie maintenant à un jeu de bonneteau : il déplace des gobelets numérotés disposés en cercle, et vous devez prédire où ils seront à la fin. Comme ses déplacements suivent une règle fixe, on peut les simuler.

**Les données.** Le fichier est une simple suite de 9 chiffres, de 1 à 9, chacun une fois : les étiquettes des gobelets dans l'ordre du cercle, dans le sens horaire. Après le dernier chiffre, on revient au premier. Le premier gobelet de la suite est le gobelet « courant » au début du jeu.

**La règle.** Un coup se déroule ainsi :
- Retirer du cercle les 3 gobelets qui suivent le gobelet courant (dans le sens horaire).
- Choisir la destination : c'est l'étiquette du courant moins 1 ; si cette étiquette fait partie des gobelets retirés, on enlève encore 1, et ainsi de suite. Si l'on passe sous la plus petite étiquette, on repart de la plus grande.
- Replacer les 3 gobelets retirés, dans le même ordre, juste après la destination.
- Le nouveau gobelet courant est celui qui suit alors l'ancien courant.

Autrement dit, le crabe déplace un paquet de trois gobelets vers le plus grand numéro inférieur disponible.

**La réponse attendue.** Après 100 coups, les étiquettes lues dans le sens horaire à partir du gobelet 1, sans lui, écrites en une seule chaîne. Par exemple, si le cercle lu à partir du 1 était alors 1, 4, 7, 2, 9, 3, 5, 8, 6, la réponse serait `47293586`.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le crabe sort beaucoup plus de gobelets et joue beaucoup plus longtemps : un million de gobelets et dix millions de coups.

**La nouvelle règle.**
- Après vos 9 chiffres, le cercle est complété par les étiquettes 10, 11, … jusqu'à 1 000 000, dans l'ordre ; après le gobelet 1 000 000, on revient au premier de vos chiffres.
- Le gobelet courant de départ est toujours le premier de vos chiffres.
- On joue 10 000 000 coups avec exactement les mêmes règles (la plus grande étiquette vaut maintenant 1 000 000).

**La réponse attendue.** Le produit des deux étiquettes qui suivent le gobelet 1. Par exemple, si ces deux gobelets portaient les étiquettes 12 et 1000, la réponse serait 12000.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-03-defi-aoc-2020-23.zip](../../zips/terminale-03-defi-aoc-2020-23.zip).
