# Défi Advent of Code — Crab Cups (2020, jour 23)

Terminale NSI — Chapitre 3 — Structures linéaires : piles, files, listes chaînées.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/23>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le crabe vous défie maintenant à un jeu de bonneteau : il déplace des gobelets numérotés disposés en cercle, et vous devez prédire où ils seront à la fin. Le fichier est une simple suite de chiffres : les numéros des gobelets dans l'ordre du cercle.

**Ce qu'il faut faire.**
- Les données sont 9 chiffres (de 1 à 9, chacun une fois) : les étiquettes des gobelets dans le sens horaire. Le premier est le gobelet « courant ».
- Un coup : retirer les 3 gobelets qui suivent le courant ; la destination est l'étiquette du courant moins 1, en sautant les étiquettes retirées et en repartant de la plus grande étiquette si l'on passe sous la plus petite ; replacer les 3 gobelets, dans le même ordre, juste après la destination ; le nouveau courant est le gobelet qui suit alors le courant. Autrement dit, le crabe déplace un paquet de trois gobelets vers le plus grand numéro inférieur disponible.
- Jouer 100 coups. Réponse : les étiquettes lues dans le sens horaire à partir du gobelet 1 (sans lui), écrites en une seule chaîne.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le crabe sort beaucoup plus de gobelets et joue beaucoup plus longtemps. Après vos 9 chiffres, le cercle est complété par les étiquettes 10, 11, … jusqu'à 1 000 000, dans l'ordre. Jouer 10 000 000 coups avec les mêmes règles. Réponse : le produit des deux étiquettes qui suivent le gobelet 1.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-03-defi-aoc-2020-23.zip](../../zips/terminale-03-defi-aoc-2020-23.zip).
