# Défi Advent of Code — Combo Breaker (2020, jour 25)

Terminale NSI — Chapitre 10 — Cryptographie.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/25>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dernier jour : votre carte de chambre ne fonctionne pas, et l'accueil est fermé. La carte et la porte s'authentifient par un petit protocole cryptographique ; en écoutant ce qu'elles s'échangent, vous allez retrouver leur clé secrète. Le fichier contient les deux nombres que vous avez interceptés.

**Ce qu'il faut faire.**
- Transformer un nombre s avec n tours : partir de 1 puis, n fois, multiplier par s et prendre le reste de la division par 20201227. Autrement dit, calculer s^n mod 20201227.
- La carte et la porte ont chacune un nombre de tours secret. Chacune publie la transformée de 7 avec son secret : sa clé publique. Le fichier contient les deux clés publiques (carte, puis porte).
- La clé de chiffrement est la transformée de la clé publique de la porte avec le secret de la carte ; c'est aussi la transformée de la clé publique de la carte avec le secret de la porte.
- Réponse : la clé de chiffrement.

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-10-defi-aoc-2020-25.zip](../../zips/terminale-10-defi-aoc-2020-25.zip).
