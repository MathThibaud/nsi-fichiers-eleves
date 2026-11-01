# Défi Advent of Code — Rucksack Reorganization (2022, jour 3)

Première NSI — Chapitre 9 — Architecture des ordinateurs et systèmes d'exploitation.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Un elfe a rempli les sacs à dos de l'expédition, mais n'a pas bien respecté la consigne. Chaque sac a deux poches de même taille, et chaque type d'objet aurait dû se trouver dans une seule des deux poches. Dans chaque sac, l'elfe s'est trompé pour exactement un type d'objet, qu'on retrouve dans les deux poches. Pour réorganiser les sacs, il faut d'abord repérer ces objets mal rangés.

**Les données.** Chaque ligne du fichier décrit un sac : une chaîne de lettres, sans espace, de longueur paire. Chaque lettre représente un type d'objet ; majuscules et minuscules sont différentes (`a` et `A` sont deux types distincts). La première moitié de la chaîne est le contenu de la première poche, la seconde moitié celui de la seconde poche.

**La règle.**
- On coupe chaque ligne en deux moitiés de même longueur.
- Exactement une lettre apparaît dans les deux moitiés : c'est l'objet mal rangé. Elle peut apparaître plusieurs fois dans une moitié, mais on ne la compte qu'une fois par sac.
- Chaque lettre a une priorité : les minuscules `a` à `z` valent 1 à 26, les majuscules `A` à `Z` valent 27 à 52.
- On ajoute la priorité de la lettre commune de chaque sac.

**La réponse attendue.** La somme des priorités des lettres communes, une par sac. Par exemple, le sac `kPmwPz` se coupe en `kPm` et `wPz` ; la lettre commune est `P`, de priorité 42 : ce sac apporte 42 à la somme.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les elfes voyagent en groupes de trois, et chaque groupe porte un badge : c'est le seul type d'objet présent dans les sacs des trois elfes du groupe. On ne coupe plus les sacs en deux : on compare des sacs entiers entre eux.

**La nouvelle règle.**
- Les lignes forment des groupes de **trois lignes consécutives** : lignes 1 à 3, puis 4 à 6, et ainsi de suite (les groupes ne se chevauchent pas).
- Dans chaque groupe, une seule lettre est présente dans les trois lignes : c'est le badge du groupe.
- Les priorités sont les mêmes que dans la partie 1.

**La réponse attendue.** La somme des priorités des badges, une par groupe. Par exemple, pour le groupe `abXc`, `dXef`, `ghiX`, le badge est `X`, de priorité 50.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-09-defi-aoc-2022-03.zip](../../zips/premiere-09-defi-aoc-2022-03.zip).
