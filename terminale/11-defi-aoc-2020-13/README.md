# Défi Advent of Code — Shuttle Search (2020, jour 13)

Terminale NSI — Chapitre 11 — Réseaux.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/13>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Arrivé au port, vous devez rejoindre l'aéroport en navette. Chaque navette fait une boucle de durée fixe et repasse donc régulièrement au port ; son numéro est justement la durée de sa boucle, en minutes. Le fichier contient vos notes : l'heure à laquelle vous serez prêt, et la liste des navettes de la compagnie.

**Ce qu'il faut faire.**
- Ligne 1 : l'instant a (en minutes) à partir duquel vous pouvez partir. Ligne 2 : les numéros des navettes séparés par des virgules ; un `x` désigne une navette hors service, à ignorer.
- Toutes les navettes sont parties ensemble à l'instant 0 : la navette numéro b part donc aux instants 0, b, 2b, 3b…{} autrement dit aux multiples de b.
- Il faut trouver la navette qui part le plus tôt à partir de l'instant a (un départ à l'instant a lui-même convient). La réponse est son numéro multiplié par le nombre de minutes d'attente.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

La compagnie propose un concours : trouver le moment où les navettes partent les unes après les autres, minute après minute, dans l'ordre de la liste.
- La première ligne ne sert plus. Les positions dans la liste sont numérotées à partir de 0, `x` compris ; un `x` n'impose aucune condition.
- Trouver le plus petit instant t tel que la navette en position i parte exactement à l'instant t + i, pour toutes les navettes en service.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-11-defi-aoc-2020-13.zip](../../zips/terminale-11-defi-aoc-2020-13.zip).
