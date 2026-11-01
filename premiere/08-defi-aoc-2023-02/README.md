# Défi Advent of Code — Cube Conundrum (2023, jour 2)

Première NSI — Chapitre 8 — Les données en tables.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2023/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Sur une île, un elfe vous propose un jeu. Il a mis dans un sac des cubes rouges, verts et bleus, sans dire combien. À chaque partie, il sort plusieurs poignées de cubes, les montre, puis les remet dans le sac. On veut savoir quelles parties auraient pu se dérouler avec un contenu de sac donné.

**Les données.** Chaque ligne du fichier raconte une partie et a la forme `Game n:` suivi des tirages, séparés par des points-virgules `;`. Un tirage est une liste de morceaux séparés par des virgules, chaque morceau ayant la forme `3 blue` : un nombre, une espace, une couleur (`red`, `green` ou `blue`). Une couleur peut être absente d'un tirage, et l'ordre des couleurs varie.

**La règle.**
- L'énoncé indique un contenu possible du sac : un nombre de cubes de chaque couleur.
- Une partie est **possible** avec ce sac si aucun tirage ne montre plus de cubes d'une couleur que le sac n'en contient (autant, c'est permis).
- Les cubes sont remis dans le sac entre deux tirages : on compare chaque tirage séparément, sans additionner les tirages d'une même partie.
- Il suffit d'un seul morceau qui dépasse pour que la partie soit impossible.

**La réponse attendue.** La somme des numéros des parties possibles. Par exemple, avec un sac (inventé) de 5 cubes de chaque couleur, `Game 7: 2 red, 4 blue; 5 green` est possible, mais pas `Game 8: 1 red; 6 blue` : si le fichier ne contenait que ces deux parties, la réponse serait 7.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On ne compare plus les parties à un sac donné : l'elfe se demande maintenant combien de cubes il fallait au minimum dans le sac pour chaque partie.

**La nouvelle règle.**
- Pour chaque partie, le plus petit sac qui la rend possible contient, pour chaque couleur, le plus grand nombre de cubes de cette couleur vus dans un même tirage de cette partie.
- La « puissance » d'une partie est le produit de ces trois nombres (rouges × verts × bleus).
- Toutes les parties comptent, plus seulement celles qui étaient possibles dans la partie 1.

**La réponse attendue.** La somme des puissances de toutes les parties. Par exemple, pour `Game 7: 2 red, 4 blue; 5 green`, il faut au moins 2 rouges, 5 verts et 4 bleus : la puissance est 2 × 5 × 4 = 40.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-08-defi-aoc-2023-02.zip](../../zips/premiere-08-defi-aoc-2023-02.zip).
