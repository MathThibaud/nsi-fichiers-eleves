# Défi Advent of Code — Handy Haversacks (2020, jour 7)

Terminale NSI — Chapitre 1 — Récursivité.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/7>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Escale à l'aéroport : un nouveau règlement impose des sacs repérés par leur couleur, et chaque couleur de sac doit contenir un nombre précis de sacs d'autres couleurs. Le héros possède un sac `shiny gold` (or brillant) et se demande dans quels sacs il pourrait le ranger.

**Les données.** Chaque ligne du fichier est une règle qui décrit le contenu imposé d'une couleur de sac.
- Une règle a la forme `<couleur> bags contain <n> <couleur> bag(s), ...` ou bien `<couleur> bags contain no other bags.` (sac vide).
- Une couleur s'écrit en deux mots (`dull lime`) ; on lit `bag` ou `bags` selon le nombre, et la ligne se termine par un point.
- Chaque couleur possède exactement une règle.

**La règle.**
- Les sacs s'emboîtent : un sac contient des sacs, qui en contiennent d'autres, etc.
- On cherche les couleurs dont un sac contient au moins un sac `shiny gold`, directement ou à l'intérieur d'autres sacs, à n'importe quelle profondeur.
- Seule la possibilité compte : une couleur qui contient plusieurs sacs dorés n'est comptée qu'une fois, et les quantités ne jouent aucun rôle.
- `shiny gold` ne se compte pas lui-même.

**La réponse attendue.** Le nombre de ces couleurs. Par exemple, si un sac A contient un sac B, qui contient lui-même un sac doré, alors A et B comptent tous les deux : la réponse serait 2.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le héros se rend compte que son sac doré, une fois rempli selon le règlement, va peser lourd. On ne cherche plus les sacs qui contiennent le sac doré, mais ce que le sac doré contient ; et cette fois, les quantités comptent.

**La nouvelle règle.**
- On compte tous les sacs qu'un sac `shiny gold` doit contenir, à tous les niveaux d'emboîtement.
- On tient compte des quantités : si un sac contient 2 sacs B, et que chaque sac B contient d'autres sacs, il faut compter le contenu des deux sacs B.
- Le sac doré lui-même ne compte pas.

**La réponse attendue.** Le nombre total de sacs contenus dans le sac doré. Par exemple, si le sac doré contenait 2 sacs A, chacun contenant 3 sacs B vides, la réponse serait 2 + 2 × 3 = 8.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-01-defi-aoc-2020-07.zip](../../zips/terminale-01-defi-aoc-2020-07.zip).
