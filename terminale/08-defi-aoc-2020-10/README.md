# Défi Advent of Code — Adapter Array (2020, jour 10)

Terminale NSI — Chapitre 8 — Programmation dynamique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/10>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En plein vol vers vos vacances, votre appareil n'a plus de batterie. La prise sous le siège ne fournit pas la bonne tension, mais votre sac déborde d'adaptateurs que l'on peut brancher les uns derrière les autres, comme des rallonges. Chaque ligne du fichier est la tension de sortie d'un de ces adaptateurs (l'unité, le *jolt*, est inventée).

**Ce qu'il faut faire.**
- La prise vaut `0`. L'appareil possède son propre adaptateur intégré, qui vaut la plus grande valeur du sac plus `3`. Dans les données, toutes les valeurs sont différentes.
- Un adaptateur de valeur v accepte une source de valeur v-1, v-2 ou v-3 : autrement dit, chaque maillon de la chaîne doit être plus grand que le précédent, d'au plus 3.
- Dans la partie 1, on utilise **tous** les adaptateurs pour former la chaîne prise → adaptateurs → appareil. On compte les écarts égaux à 1 et les écarts égaux à 3 entre éléments consécutifs ; la réponse est (nombre d'écarts de 1) × (nombre d'écarts de 3).

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Vous voulez maintenant savoir de combien de manières différentes on aurait pu brancher l'appareil, sans être obligé d'utiliser tout le sac.
- Compter les chaînes qui relient la prise à l'appareil en respectant toujours la règle des écarts de 1 à 3, avec n'importe quel sous-ensemble des adaptateurs.
- Deux chaînes sont différentes si elles n'utilisent pas exactement les mêmes adaptateurs. Le nombre obtenu est gigantesque.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-08-defi-aoc-2020-10.zip](../../zips/terminale-08-defi-aoc-2020-10.zip).
