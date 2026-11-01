# Défi Advent of Code — Jurassic Jigsaw (2020, jour 20)

Terminale NSI — Chapitre 8 — Graphes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/20>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les messages du satellite contiennent en fait une photo, mais l'appareil l'a envoyée découpée en petits carrés (des « tuiles »), mélangés et, pire, tournés ou retournés au hasard. Il faut reconstituer ce puzzle. Pour commencer, il suffit de trouver les quatre tuiles des coins.

**Les données.** Le fichier est une suite de blocs séparés par une ligne vide. Chaque bloc est une tuile : une ligne `Tile <numéro>:` qui donne son numéro, suivie d'une grille carrée de 10 × 10 caractères, `.` (blanc) ou `#` (noir). Le nombre de tuiles est un carré parfait : l'image complète est un carré de tuiles.

**La règle.**
- Chaque tuile a pu être tournée d'un nombre quelconque de quarts de tour et/ou retournée en miroir.
- Deux tuiles voisines dans l'image ont, une fois bien orientées, des bords identiques : c'est ce qui permet de les raccorder.
- Les bords extérieurs de l'image ne correspondent à aucune autre tuile.
- En pratique, deux tuiles non voisines n'ont jamais de bord commun : un bord partagé désigne donc sans ambiguïté deux voisines.

**La réponse attendue.** Le produit des numéros des quatre tuiles placées aux coins de l'image. Par exemple, si les coins portaient les numéros 2, 3, 5 et 7, la réponse serait 2 × 3 × 5 × 7 = 210.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Il faut maintenant reconstituer vraiment l'image, puis y chercher des monstres marins, dont le dessin (un motif de `#`) est donné sur le site.

**La nouvelle règle.**
- Assembler l'image en orientant chaque tuile pour que ses bords coïncident avec ceux de ses voisines.
- Retirer le bord (première et dernière lignes et colonnes) de chaque tuile, puis recoller les tuiles : chacune devient un carré 8 × 8.
- Chercher le motif dans l'une des 8 orientations de l'image : chaque `#` du motif doit tomber sur un `#` de l'image, les autres cases du motif sont quelconques.
- Une seule orientation de l'image contient des monstres.

**La réponse attendue.** Le nombre de `#` de l'image qui n'appartiennent à aucun monstre. Par exemple, si l'image contenait 100 `#` dont 30 couverts par des monstres, la réponse serait 70.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-08-defi-aoc-2020-20.zip](../../zips/terminale-08-defi-aoc-2020-20.zip).
