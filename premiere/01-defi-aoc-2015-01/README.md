# Défi Advent of Code — Not Quite Lisp (2015, jour 1)

Première NSI — Chapitre 1 — Les bases de la programmation Python.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2015/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le Père Noël doit livrer des cadeaux dans un immeuble immense, avec des sous-sols très profonds. Les instructions qu'on lui a données sont une longue suite de parenthèses : chacune lui dit de monter ou de descendre d'un étage. Il les suit une par une, dans l'ordre, et veut savoir à quel étage il se retrouvera à la fin.

**Les données.** Le fichier ne contient qu'**une seule ligne**, formée uniquement des caractères `(` et `)`, collés les uns aux autres. Chaque caractère est une instruction.

**La règle.**
- On part du rez-de-chaussée, l'étage 0.
- On lit les caractères un par un, de gauche à droite : `(` fait monter d'un étage, `)` fait descendre d'un étage.
- L'immeuble n'a ni dernier étage ni sous-sol le plus bas : l'étage peut devenir aussi grand ou aussi négatif qu'on veut.
- Un étage négatif est un sous-sol : -1 est le premier sous-sol, -2 le deuxième, etc.

**La réponse attendue.** L'étage atteint après le dernier caractère (un entier, éventuellement négatif). Par exemple, avec `(()((`, on passe par les étages 1, 2, 1, 2 puis 3 : la réponse serait 3.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On s'intéresse maintenant au trajet lui-même, et non plus à l'étage d'arrivée : on veut savoir à quel moment le Père Noël descend pour la première fois au sous-sol.

**La nouvelle règle.**
- On suit les instructions exactement comme dans la partie 1, en partant de l'étage 0.
- On cherche le **premier** caractère qui amène le Père Noël à l'étage -1, c'est-à-dire son premier passage au sous-sol. La suite du trajet n'a plus d'importance.
- Les positions sont numérotées **à partir de 1** : le premier caractère est en position 1, le deuxième en position 2, etc.

**La réponse attendue.** La **position** de ce caractère. Par exemple, avec `(()))(`, on passe par les étages 1, 2, 1, 0, puis -1 au cinquième caractère : la réponse serait 5.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-01-defi-aoc-2015-01.zip](../../zips/premiere-01-defi-aoc-2015-01.zip).
