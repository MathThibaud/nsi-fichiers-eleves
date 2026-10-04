# Défi Advent of Code — Toboggan Trajectory (2020, jour 3)

Terminale NSI — Chapitre 2 — Programmation orientée objet et paradigmes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/3>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Toujours en route vers l'aéroport, le héros dévale une pente boisée en luge, sans pouvoir vraiment la diriger. Il dispose d'une carte de la forêt vue de dessus : chaque ligne du fichier représente une rangée de la pente, chaque caractère une case, libre ou occupée par un arbre. Il veut savoir combien d'arbres il va percuter en suivant une trajectoire fixée.

**Ce qu'il faut faire.**
- Dans la carte, `.` désigne une case libre et `#` un arbre ; toutes les lignes ont la même longueur.
- La forêt est bien plus large que la carte : le même motif se répète indéfiniment vers la **droite** (mais pas vers le bas). Autrement dit, après la dernière colonne, on retrouve la première.
- On part de la case en haut à gauche (ligne 0, colonne 0). À chaque pas, on se déplace de 3 colonnes vers la droite et de 1 ligne vers le bas, et l'on s'arrête quand on dépasse la dernière ligne de la carte.
- Il faut renvoyer le nombre d'arbres sur les cases atteintes à chaque pas.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le héros veut comparer plusieurs trajectoires avant de choisir la moins dangereuse.
- Refaire le comptage pour cinq pentes : (1 à droite, 1 en bas), (3, 1), (5, 1), (7, 1) et (1 à droite, **2** en bas). Pour cette dernière, on saute donc une ligne sur deux.
- Il faut renvoyer le **produit** des cinq nombres d'arbres obtenus.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-02-defi-aoc-2020-03.zip](../../zips/terminale-02-defi-aoc-2020-03.zip).
