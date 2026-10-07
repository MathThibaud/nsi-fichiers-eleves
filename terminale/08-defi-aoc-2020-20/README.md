# Défi Advent of Code — Jurassic Jigsaw (2020, jour 20)

Terminale NSI — Chapitre 8 — Graphes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/20>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les messages du satellite contiennent en fait une photo, mais l'appareil l'a envoyée découpée en petits carrés (des « tuiles »), mélangés et, pire, tournés ou retournés au hasard. Il faut reconstituer ce puzzle. Chaque bloc du fichier est une tuile en noir et blanc, avec son numéro.

**Ce qu'il faut faire.**
- Un bloc est une ligne `Tile <numéro>:` suivie d'une grille carrée de 10 × 10 caractères `.` ou `#` ; les blocs sont séparés par une ligne vide.
- Remises dans le bon sens, les tuiles forment une image carrée. Chaque tuile a pu être tournée d'un nombre quelconque de quarts de tour et/ou retournée en miroir.
- Deux tuiles voisines dans l'image ont, une fois bien orientées, des bords identiques : c'est ce qui permet de les raccorder. Les bords extérieurs de l'image ne correspondent à aucune autre tuile (en pratique, deux tuiles non voisines n'ont jamais de bord commun).
- Réponse : le produit des numéros des quatre tuiles placées aux coins de l'image.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Une fois l'image reconstituée, on y cherche des monstres marins.
- Assembler l'image, retirer le bord (première et dernière lignes et colonnes) de chaque tuile, puis recoller les tuiles : chacune devient un carré 8 × 8.
- Chercher un motif (le « monstre », dessiné sur le site) dans l'une des 8 orientations de l'image : chaque `#` du motif doit tomber sur un `#` de l'image, les autres cases sont quelconques.
- Réponse : le nombre de `#` de l'image qui n'appartiennent à aucun monstre.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-08-defi-aoc-2020-20.zip](../../zips/terminale-08-defi-aoc-2020-20.zip).
