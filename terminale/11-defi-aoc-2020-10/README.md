# Défi Advent of Code — Adapter Array (2020, jour 10)

Terminale NSI — Chapitre 11 — Programmation dynamique.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/10>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** En plein vol vers vos vacances, votre appareil n'a plus de batterie. La prise sous le siège ne fournit pas la bonne tension, mais votre sac déborde d'adaptateurs que l'on peut brancher les uns derrière les autres, comme des rallonges. Il s'agit de vérifier qu'on peut tous les enchaîner, et de décrire les écarts de tension le long de la chaîne.

**Les données.** Chaque ligne du fichier contient **un entier** : la tension de sortie d'un adaptateur (l'unité, le *jolt*, est inventée). Les lignes ne sont pas rangées, et dans les données toutes les valeurs sont différentes.

**La règle.**
- La prise vaut `0`. L'appareil possède son propre adaptateur intégré, qui vaut la plus grande valeur du sac plus `3`.
- Un adaptateur de valeur v accepte une source de valeur v-1, v-2 ou v-3 : chaque maillon de la chaîne doit être plus grand que le précédent, d'au plus 3.
- Dans la partie 1, on utilise **tous** les adaptateurs pour former la chaîne prise → adaptateurs → appareil.
- On calcule les écarts entre éléments consécutifs de cette chaîne, y compris l'écart entre la prise et le premier adaptateur, et celui entre le dernier adaptateur et l'appareil. On compte les écarts égaux à 1 et les écarts égaux à 3.

**La réponse attendue.** Le produit (nombre d'écarts de 1) × (nombre d'écarts de 3). Par exemple, avec les adaptateurs 2, 3 et 6, la chaîne est 0, 2, 3, 6, 9 : les écarts sont 2, 1, 3, 3, soit un écart de 1 et deux écarts de 3, et la réponse serait 1 × 2 = 2.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Vous voulez maintenant savoir de combien de manières différentes on aurait pu brancher l'appareil, sans être obligé d'utiliser tout le sac.

**La nouvelle règle.**
- On compte les chaînes qui relient la prise à l'appareil en respectant toujours la règle des écarts de 1 à 3, avec n'importe quel sous-ensemble des adaptateurs.
- Deux chaînes sont différentes si elles n'utilisent pas exactement les mêmes adaptateurs.
- Le nombre obtenu est gigantesque : il faut le compter, pas construire les chaînes une à une.

**La réponse attendue.** Le nombre total de chaînes possibles. Par exemple, avec les adaptateurs 1, 2 et 3 (appareil 6), l'adaptateur 3 est obligatoire, mais 1 et 2 sont facultatifs : il y a 4 chaînes.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-11-defi-aoc-2020-10.zip](../../zips/terminale-11-defi-aoc-2020-10.zip).
