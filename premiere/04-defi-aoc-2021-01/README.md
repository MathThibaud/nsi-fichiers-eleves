# Défi Advent of Code — Sonar Sweep (2021, jour 1)

Première NSI — Chapitre 4 — Algorithmique : le parcours séquentiel.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les clés du traîneau sont tombées à la mer, et vous voilà dans un sous-marin pour les récupérer. En s'éloignant, le sonar du sous-marin mesure la profondeur du fond marin, point après point. Le fichier est ce relevé : chaque ligne est une profondeur, dans l'ordre où elles ont été mesurées. On veut savoir si le fond descend vite.

**Ce qu'il faut faire.**
- Le fichier contient une mesure (un entier) par ligne.
- Il faut compter combien de fois une mesure est **strictement** plus grande que la mesure juste avant elle ; autrement dit, combien de fois le fond s'enfonce d'un point au suivant.
- La première mesure n'a pas de précédente : elle n'est jamais comptée. Deux mesures égales ne comptent pas non plus.
- La réponse est ce nombre d'augmentations.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les mesures isolées sont trop sensibles au bruit du sonar : on les lisse en les regroupant. On remplace la liste par les sommes de **trois mesures consécutives** : mesures 1-2-3, puis 2-3-4, puis 3-4-5…{} Ces groupes se chevauchent, et l'on s'arrête quand il ne reste plus trois mesures. La réponse est le nombre de sommes strictement plus grandes que la somme précédente.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-04-defi-aoc-2021-01.zip](../../zips/premiere-04-defi-aoc-2021-01.zip).
