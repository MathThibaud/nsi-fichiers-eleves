# Défi Advent of Code — Cube Conundrum (2023, jour 2)

Première NSI — Chapitre 8 — Les données en tables.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2023/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Sur une île, un elfe vous propose un jeu. Il a mis dans un sac des cubes rouges, verts et bleus, sans dire combien. À chaque partie, il sort plusieurs poignées de cubes, les montre, puis les remet dans le sac. Chaque ligne du fichier raconte une partie : son numéro, puis ce qu'on a vu à chaque poignée.

**Ce qu'il faut faire.**
- Format : `Game n:` puis les tirages séparés par `;`. Un tirage est une liste séparée par `,` de morceaux comme `3 blue` (couleurs `red`, `green`, `blue`).
- L'énoncé indique un contenu possible du sac (un nombre de cubes de chaque couleur). Une partie est **possible** avec ce sac si aucun tirage ne montre plus de cubes d'une couleur que le sac n'en contient. Les cubes étant remis entre deux tirages, on compare chaque tirage séparément.
- Réponse : la somme des numéros des parties possibles.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

L'elfe se demande maintenant combien de cubes il fallait au minimum. Pour chaque partie, le plus petit sac qui la rend possible contient, pour chaque couleur, le plus grand nombre vu dans un tirage de cette partie. La « puissance » d'une partie est le produit de ces trois nombres. Réponse : la somme des puissances de toutes les parties.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-08-defi-aoc-2023-02.zip](../../zips/premiere-08-defi-aoc-2023-02.zip).
