# Défi Advent of Code — Password Philosophy (2020, jour 2)

Terminale NSI — Chapitre 1 — Récursivité.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Le héros part en vacances et doit descendre jusqu'à la côte en luge. Le loueur de luges ne parvient plus à se connecter : sa base de mots de passe est en partie abîmée. Chaque ligne du fichier décrit un mot de passe enregistré, accompagné de la règle de sécurité qui était en vigueur quand il a été choisi. Il s'agit de repérer les mots de passe qui respectent leur propre règle.

**Ce qu'il faut faire.**
- Une ligne a la forme `a-b l: motdepasse` : deux entiers a ⩽ b, une lettre `l`, puis le mot de passe, écrit en lettres minuscules.
- La règle se lit ainsi : la lettre `l` doit apparaître dans le mot de passe au moins a fois et au plus b fois, bornes comprises. Autrement dit, le nombre d'occurrences de `l` doit appartenir à l'intervalle [a, b].
- Il faut renvoyer le nombre de lignes dont le mot de passe respecte sa règle.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le loueur s'aperçoit qu'il s'est trompé de règlement : les deux nombres n'ont pas le sens qu'on leur a donné.
- Ils désignent maintenant deux **positions** dans le mot de passe, numérotées **à partir de 1** (il n'y a pas de position 0).
- Le mot de passe est valide si la lettre se trouve à exactement une de ces deux positions : ni à aucune, ni aux deux. Les occurrences ailleurs dans le mot ne comptent plus.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-01-defi-aoc-2020-02.zip](../../zips/terminale-01-defi-aoc-2020-02.zip).
