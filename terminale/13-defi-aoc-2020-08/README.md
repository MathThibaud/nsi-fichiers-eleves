# Défi Advent of Code — Handheld Halting (2020, jour 8)

Terminale NSI — Chapitre 13 — Calculabilité et décidabilité.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/8>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En plein vol, un enfant assis à côté du héros n'arrive plus à démarrer sa console de jeu portable : son programme de démarrage tourne en rond. Le fichier contient ce programme, écrit dans un langage très simple, avec une instruction par ligne. La machine ne possède qu'une seule mémoire, l'*accumulateur*, qui vaut 0 au départ.

**Ce qu'il faut faire.**
- Une instruction est formée d'une opération (`acc`, `jmp` ou `nop`) et d'un entier signé (`+4`, `-20`).
- `acc n` ajoute `n` à l'accumulateur, puis passe à la ligne suivante.
- `jmp n` est un saut de `n` lignes compté à partir de l'instruction courante : `jmp +1` va à la ligne suivante, `jmp -2` remonte de deux lignes.
- `nop n` ne fait rien (l'argument est ignoré) et passe à la ligne suivante.
- On commence à la première ligne. Le programme finit par boucler : dès qu'une instruction est sur le point d'être exécutée une deuxième fois, on s'arrête **avant** de l'exécuter. Il faut renvoyer la valeur de l'accumulateur à ce moment.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Il faut maintenant réparer la console pour que le programme aille jusqu'au bout.
- Exactement une instruction est fautive : un `jmp` devrait être un `nop`, ou un `nop` un `jmp`. Les `acc` sont corrects.
- Le programme réparé se termine, c'est-à-dire qu'il cherche à exécuter la ligne qui suit immédiatement la dernière. Il faut renvoyer la valeur de l'accumulateur à ce moment.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-13-defi-aoc-2020-08.zip](../../zips/terminale-13-defi-aoc-2020-08.zip).
