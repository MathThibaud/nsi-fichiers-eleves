# Défi Advent of Code — Lobby Layout (2020, jour 24)

Terminale NSI — Chapitre 9 — Réseaux.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/24>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Enfin arrivé à l'hôtel, vous trouvez le hall en travaux : il faut poser un carrelage hexagonal formant un motif précis. Chaque carreau est blanc d'un côté et noir de l'autre. Les ouvriers ont une liste des carreaux à retourner, mais ils ont besoin de vous pour savoir à quoi ressemblera le motif.

**Les données.** Le sol est un pavage infini de carreaux hexagonaux, disposés en rangées horizontales : chaque carreau a six voisins, dans les directions `e` (est), `se` (sud-est), `sw` (sud-ouest), `w` (ouest), `nw` (nord-ouest) et `ne` (nord-est). Chaque ligne du fichier est un chemin : une suite de ces directions collées, sans séparateur, comme `seswnee`.

**La règle.**
- Au départ, tous les carreaux sont blancs.
- Pour chaque ligne, on part toujours du même carreau de référence et l'on suit les directions une à une, de voisin en voisin.
- Le carreau d'arrivée est retourné : blanc devient noir, noir devient blanc. Les carreaux traversés en chemin ne changent pas.
- Plusieurs lignes peuvent désigner le même carreau par des chemins différents : il est alors retourné plusieurs fois.

**La réponse attendue.** Le nombre de carreaux noirs une fois toutes les lignes traitées. Par exemple, avec les trois lignes `ee`, `w` et `ee`, le carreau désigné par `ee` est retourné deux fois et redevient blanc ; seul celui désigné par `w` est noir : la réponse serait 1.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le motif n'est pas figé : il évolue de jour en jour selon une règle simple. On part du carrelage obtenu en partie 1.

**La nouvelle règle.**
- Chaque jour, on compte les voisins noirs de chaque carreau dans l'état de la veille, puis tous les carreaux changent **en même temps**.
- Un carreau noir ayant 0 ou plus de 2 voisins noirs devient blanc.
- Un carreau blanc ayant exactement 2 voisins noirs devient noir.
- Les autres carreaux ne changent pas.

**La réponse attendue.** Le nombre de carreaux noirs après 100 jours. Par exemple, si seuls deux carreaux voisins étaient noirs, ils le resteraient (un voisin noir chacun) et les deux carreaux qui les touchent tous les deux deviendraient noirs : 4 carreaux noirs le lendemain.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-09-defi-aoc-2020-24.zip](../../zips/terminale-09-defi-aoc-2020-24.zip).
