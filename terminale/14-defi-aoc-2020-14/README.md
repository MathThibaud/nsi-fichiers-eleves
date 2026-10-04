# Défi Advent of Code — Docking Data (2020, jour 14)

Terminale NSI — Chapitre 14 — Systèmes sur puce et informatique embarquée.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/14>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** À l'approche du port, l'ordinateur du ferry doit initialiser sa mémoire, mais il ne comprend pas le système de masques de bits utilisé par le port. Vous allez émuler ce système. Le fichier est un petit programme : chaque ligne change le masque courant ou écrit une valeur en mémoire.

**Ce qu'il faut faire.**
- Une ligne `mask = ` est suivie de 36 caractères parmi `0`, `1`, `X` ; une ligne `mem[a] = v` écrit la valeur v à l'adresse a. Adresses et valeurs sont des entiers positifs sur 36 bits.
- Le masque s'écrit bit de poids fort à gauche (2^35) et reste en vigueur jusqu'au `mask` suivant.
- Juste avant chaque écriture, on applique le masque à la valeur : un `0` ou un `1` du masque impose ce bit, un `X` laisse le bit de v tel quel. Autrement dit, le masque ne retouche que certains bits.
- Toutes les cases valent 0 au départ ; écrire à nouveau à la même adresse remplace l'ancienne valeur. La réponse est la somme de toutes les valeurs présentes en mémoire à la fin.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le programme ne fonctionne toujours pas : la version du système utilisée par le port est en fait un « décodeur d'adresses ».
- Le masque agit maintenant sur l'**adresse**, et la valeur est écrite telle quelle : un `0` laisse le bit de l'adresse inchangé, un `1` le force à 1, un `X` est *flottant* et prend les deux valeurs.
- Avec k bits flottants, la valeur est donc écrite dans 2^k adresses. La réponse demandée est la même.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-14-defi-aoc-2020-14.zip](../../zips/terminale-14-defi-aoc-2020-14.zip).
