# Défi Advent of Code — Tuning Trouble (2022, jour 6)

Première NSI — Chapitre 10 — Le Web : réseaux et interactions homme-machine.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2022/day/6>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Un elfe vous confie un petit appareil de communication, qui doit d'abord se caler sur le signal radio des elfes. Le signal arrive comme une suite de lettres reçues l'une après l'autre. Pour comprendre ce signal, l'appareil doit repérer où commence un paquet de données : ce début est signalé par un groupe de lettres consécutives toutes différentes.

**Les données.** Le fichier contient tout le flux reçu sur **une seule ligne** : une longue suite de lettres minuscules, sans espace. Le premier caractère de la ligne est le premier reçu.

**La règle.**
- On lit les caractères de gauche à droite, un par un.
- Après chaque caractère lu, on regarde les **4 derniers caractères lus** (le caractère qu'on vient de lire et les trois précédents).
- Dès que ces 4 caractères sont tous différents, on a trouvé le marqueur de début de paquet, et l'on s'arrête.
- On ne peut pas répondre avant d'avoir lu au moins 4 caractères.

**La réponse attendue.** Le nombre de caractères lus depuis le début jusqu'au dernier caractère du marqueur inclus, positions comptées à partir de 1. Par exemple, pour le flux `xxyxzwq`, les 4 derniers caractères lus sont tous différents pour la première fois après la lecture du sixième caractère (`yxzw`) : la réponse serait 6.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** L'appareil doit aussi repérer le début des messages, signalé par un marqueur plus long que celui des paquets.

**La nouvelle règle.**
- Même lecture qu'à la partie 1, mais on regarde les **14** derniers caractères lus au lieu des 4 derniers.
- On s'arrête dès que ces 14 caractères sont tous différents.

**La réponse attendue.** Le nombre de caractères lus jusqu'au dernier caractère de ce premier groupe de 14, positions comptées à partir de 1 comme dans la partie 1.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-10-defi-aoc-2022-06.zip](../../zips/premiere-10-defi-aoc-2022-06.zip).
