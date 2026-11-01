# Défi Advent of Code — Shuttle Search (2020, jour 13)

Terminale NSI — Chapitre 10 — Cryptographie.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/13>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Arrivé au port, vous devez rejoindre l'aéroport en navette. Chaque navette fait une boucle de durée fixe et repasse donc régulièrement au port ; son numéro est justement la durée de sa boucle, en minutes. Vous voulez savoir laquelle prendre pour attendre le moins.

**Les données.** Le fichier contient deux lignes. Ligne 1 : l'instant a (en minutes) à partir duquel vous pouvez partir. Ligne 2 : les numéros des navettes séparés par des virgules ; un `x` désigne une navette hors service, à ignorer dans la partie 1.

**La règle.**
- Toutes les navettes sont parties ensemble à l'instant 0 : la navette numéro b part donc aux instants 0, b, 2b, 3b… autrement dit aux multiples de b.
- Pour chaque navette, on cherche son premier départ à partir de l'instant a ; un départ à l'instant a lui-même convient (attente nulle).
- L'attente est la différence entre ce départ et a. On retient la navette dont l'attente est la plus courte.

**La réponse attendue.** Le numéro de cette navette multiplié par le nombre de minutes d'attente. Par exemple, avec a = 10 et les navettes 3 et 7, la navette 3 part à 12 (attente 2) et la navette 7 à 14 (attente 4) : la réponse serait 3 × 2 = 6.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** La compagnie propose un concours : trouver le moment où les navettes partent les unes après les autres, minute après minute, dans l'ordre de la liste. La première ligne du fichier ne sert plus.

**La nouvelle règle.**
- Les positions dans la liste sont numérotées à partir de 0, `x` compris : les `x` ne sont plus ignorés, ils occupent une position.
- Un `x` n'impose aucune condition.
- La navette en position i doit partir exactement à l'instant t + i, et cela pour toutes les navettes en service.

**La réponse attendue.** Le plus petit instant t qui convient. Par exemple, avec la liste `3,x,5`, il faut que 3 parte à t et 5 à t + 2 : t = 3 convient (3 est multiple de 3, 5 de 5) et la réponse serait 3.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-10-defi-aoc-2020-13.zip](../../zips/terminale-10-defi-aoc-2020-13.zip).
