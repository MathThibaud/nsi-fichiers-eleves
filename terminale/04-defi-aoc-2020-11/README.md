# Défi Advent of Code — Seating System (2020, jour 11)

Terminale NSI — Chapitre 4 — Processus et ordonnancement.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/11>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Vous attendez un ferry dans une salle encore vide et vous voulez prévoir où les voyageurs vont s'asseoir, pour choisir la meilleure place. Leur comportement est très prévisible : on le simule comme un *automate cellulaire*, où l'état de chaque case au tour suivant ne dépend que de son état et de celui de ses voisines.

**Les données.** Le fichier est le plan de la salle : toutes les lignes ont la même longueur, et chaque caractère est une case. `.` représente le sol, `L` un siège libre, `#` un siège occupé. Au départ, tous les sièges sont libres.

**La règle.**
- Les voisins d'une case sont les 8 cases qui l'entourent (même ligne, même colonne et diagonales), sans sortir du plan : une case du bord en a donc moins.
- À chaque tour, **toutes** les cases changent en même temps, d'après l'état du tour précédent.
- Un siège libre dont aucun voisin n'est occupé devient occupé (on aime être tranquille).
- Un siège occupé qui a au moins 4 voisins occupés se libère (trop de monde).
- Dans les autres cas, rien ne change ; le sol ne change jamais.
- On répète les tours jusqu'à ce qu'un tour ne modifie plus aucune case.

**La réponse attendue.** Le nombre de sièges occupés quand plus rien ne bouge. Par exemple, une salle de 3 × 3 sièges tous libres se remplit entièrement au premier tour ; au deuxième, seuls les 4 coins restent occupés, puis plus rien ne change : la réponse serait 4.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** En observant mieux, on comprend que les voyageurs ne regardent pas seulement les places juste à côté : ils regardent aussi plus loin, à travers les cases de sol.

**La nouvelle règle.**
- Dans chacune des 8 directions, on prend en compte le **premier siège visible** (libre ou occupé), en sautant les cases de sol.
- S'il n'y a que du sol jusqu'au bord dans une direction, cette direction ne compte pas.
- Un siège occupé se libère désormais s'il voit au moins **5** sièges occupés.
- La règle pour s'asseoir (aucun siège occupé visible) et le déroulement des tours ne changent pas.

**La réponse attendue.** Comme en partie 1 : le nombre de sièges occupés quand plus rien ne bouge.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-04-defi-aoc-2020-11.zip](../../zips/terminale-04-defi-aoc-2020-11.zip).
