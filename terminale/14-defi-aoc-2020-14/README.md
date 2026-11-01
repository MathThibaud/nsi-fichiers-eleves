# Défi Advent of Code — Docking Data (2020, jour 14)

Terminale NSI — Chapitre 14 — Systèmes sur puce et informatique embarquée.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/14>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** À l'approche du port, l'ordinateur du ferry doit initialiser sa mémoire, mais il ne comprend pas le système de masques de bits utilisé par le port. Vous allez émuler ce système, c'est-à-dire le reproduire par un programme.

**Les données.** Le fichier est un petit programme ; chaque ligne est de l'une des deux formes suivantes.
- `mask = ` suivi de 36 caractères parmi `0`, `1`, `X` : elle change le masque courant. Le masque s'écrit bit de poids fort à gauche (2^35) et reste en vigueur jusqu'au `mask` suivant.
- `mem[a] = v` : elle écrit la valeur v à l'adresse a. Adresses et valeurs sont des entiers positifs sur 36 bits, écrits en décimal.

**La règle.**
- Juste avant chaque écriture, on applique le masque à la **valeur** : un `0` ou un `1` du masque impose ce bit, un `X` laisse le bit de v tel quel. Autrement dit, le masque ne retouche que certains bits.
- Toutes les cases de la mémoire valent 0 au départ.
- Écrire à nouveau à la même adresse remplace l'ancienne valeur.

**La réponse attendue.** La somme de toutes les valeurs présentes en mémoire à la fin du programme. Par exemple, si le masque se termine par `10XX` (et ne contient que des `X` avant), écrire 7 (`0111`) donne `1011`, soit 11, et écrire 1 (`0001`) donne `1001`, soit 9 ; à deux adresses différentes, la réponse serait 11 + 9 = 20.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le programme ne fonctionne toujours pas : la version du système utilisée par le port est en fait un « décodeur d'adresses ». Le masque agit maintenant sur l'**adresse**, et la valeur est écrite telle quelle.

**La nouvelle règle.**
- Un `0` du masque laisse le bit de l'adresse inchangé (attention : ce n'est plus comme en partie 1).
- Un `1` force le bit de l'adresse à 1.
- Un `X` est *flottant* : il prend les deux valeurs 0 et 1. Avec k bits flottants, la valeur est donc écrite dans 2^k adresses.

**La réponse attendue.** La même qu'en partie 1 : la somme des valeurs en mémoire à la fin. Par exemple, si le masque se termine par `0X1` (que des `0` avant), écrire 7 à l'adresse 4 (`100`) donne le modèle `1X1` : la valeur 7 est écrite aux adresses 5 et 7, ce qui apporte 14 à la somme.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-14-defi-aoc-2020-14.zip](../../zips/terminale-14-defi-aoc-2020-14.zip).
