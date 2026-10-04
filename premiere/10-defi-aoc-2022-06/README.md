# Défi Advent of Code — Tuning Trouble (2022, jour 6)

Première NSI — Chapitre 10 — Le Web : réseaux et interactions homme-machine.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/6>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Un elfe vous confie un petit appareil de communication, qui doit d'abord se caler sur le signal radio des elfes. Le signal arrive comme une suite de lettres reçues l'une après l'autre ; le fichier contient tout ce flux sur une seule ligne. Le début d'un paquet de données est signalé par un groupe de lettres consécutives toutes différentes, qu'il faut repérer.

**Ce qu'il faut faire.**
- On lit les caractères de gauche à droite. On cherche le premier endroit où les **4 derniers caractères lus** sont tous différents : c'est le marqueur de début de paquet.
- Réponse : le nombre de caractères lus depuis le début jusqu'au dernier caractère de ce marqueur, positions comptées à partir de 1. Autrement dit, si le marqueur occupe les caractères 3 à 6, la réponse est 6.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

L'appareil doit aussi repérer le début des messages, signalé par un marqueur plus long. Même question, mais avec **14** caractères consécutifs tous différents au lieu de 4. Réponse : le nombre de caractères lus jusqu'à la fin de ce premier groupe de 14.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-10-defi-aoc-2022-06.zip](../../zips/premiere-10-defi-aoc-2022-06.zip).
