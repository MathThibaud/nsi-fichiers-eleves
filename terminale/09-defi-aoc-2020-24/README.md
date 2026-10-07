# Défi Advent of Code — Lobby Layout (2020, jour 24)

Terminale NSI — Chapitre 9 — Réseaux.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/24>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Enfin arrivé à l'hôtel, vous trouvez le hall en travaux : il faut poser un carrelage hexagonal formant un motif précis. Chaque carreau est blanc d'un côté et noir de l'autre. Le fichier est la liste des carreaux à retourner, chacun repéré par un chemin à suivre depuis le carreau central.

**Ce qu'il faut faire.**
- Le sol est un pavage infini de carreaux hexagonaux, tous blancs au départ, disposés en rangées horizontales : chaque carreau a six voisins, notés `e`, `se`, `sw`, `w`, `nw`, `ne`.
- Chaque ligne est une suite de directions collées, sans séparateur, à suivre en partant toujours du même carreau de référence. Le carreau d'arrivée est retourné (blanc devient noir, noir devient blanc).
- Réponse : le nombre de carreaux noirs une fois toutes les lignes traitées.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le motif n'est pas figé : il évolue de jour en jour selon une règle simple. Partir du carrelage obtenu. Chaque jour, tous les carreaux changent **en même temps** : un carreau noir ayant 0 ou plus de 2 voisins noirs devient blanc ; un carreau blanc ayant exactement 2 voisins noirs devient noir ; les autres ne changent pas. Réponse : le nombre de carreaux noirs après 100 jours.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-09-defi-aoc-2020-24.zip](../../zips/terminale-09-defi-aoc-2020-24.zip).
