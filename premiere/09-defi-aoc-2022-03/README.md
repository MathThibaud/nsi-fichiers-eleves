# Défi Advent of Code — Rucksack Reorganization (2022, jour 3)

Première NSI — Chapitre 9 — Architecture des ordinateurs et systèmes d'exploitation.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Un elfe a rempli les sacs à dos de l'expédition, mais n'a pas bien respecté la consigne. Chaque sac a deux poches de même taille, et chaque type d'objet aurait dû se trouver dans une seule des deux poches. Dans chaque sac, il y a exactement un type d'objet mal rangé, et il faut le retrouver.

**Ce qu'il faut faire.**
- Chaque ligne décrit un sac : une chaîne de lettres de longueur paire, où chaque lettre est un type d'objet (`a` et `A` sont des types différents).
- La première moitié de la chaîne est le contenu de la première poche, la seconde moitié celui de la seconde.
- Exactement une lettre apparaît dans les deux moitiés (elle peut y apparaître plusieurs fois) : c'est l'objet mal rangé.
- Chaque lettre a une priorité : `a` à `z` valent 1 à 26, `A` à `Z` valent 27 à 52. La réponse est la somme des priorités des lettres communes, une par sac.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les elfes voyagent en groupes de trois, et chaque groupe porte un badge, le seul type d'objet commun à leurs trois sacs. Les lignes forment donc des groupes de **trois lignes consécutives** ; dans chaque groupe, une seule lettre est présente dans les trois lignes. La réponse est la somme des priorités de ces lettres, une par groupe.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-09-defi-aoc-2022-03.zip](../../zips/premiere-09-defi-aoc-2022-03.zip).
