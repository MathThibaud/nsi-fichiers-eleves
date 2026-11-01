# Défi Advent of Code — Sonar Sweep (2021, jour 1)

Première NSI — Chapitre 4 — Algorithmique : le parcours séquentiel.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2021/day/1>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Les clés du traîneau sont tombées à la mer, et vous voilà dans un sous-marin pour les récupérer. Pendant que le sous-marin avance, son sonar mesure la profondeur du fond marin, point après point. Avant de plonger plus loin, on veut savoir à quel point le fond descend : est-ce qu'il s'enfonce souvent, ou est-ce qu'il reste plat ?

**Les données.** Le fichier est le relevé du sonar. Chaque ligne contient **un seul entier** : une profondeur, en mètres. Les lignes sont dans l'ordre où les mesures ont été faites : la ligne 2 a été mesurée juste après la ligne 1, et ainsi de suite. Plus le nombre est grand, plus le fond est profond.

**La règle.**
- On compare chaque mesure à la mesure **juste avant elle** (et seulement à celle-là).
- Si elle est **strictement** plus grande, le fond s'est enfoncé : on compte une augmentation.
- Si elle est plus petite ou égale, on ne compte rien.
- La première mesure n'a pas de mesure avant elle : elle ne peut pas compter.

**La réponse attendue.** Le nombre total d'augmentations dans tout le fichier. Par exemple, pour les quatre mesures 10, 12, 12, 15, il y a deux augmentations (de 10 à 12, puis de 12 à 15) : la réponse serait 2.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Une mesure isolée peut être faussée par le bruit du sonar : un poisson qui passe, une vague. Pour avoir une idée plus fiable du relief, on ne compare plus les mesures une à une, mais des **groupes de trois mesures consécutives**.

**La nouvelle règle.**
- On calcule la somme des mesures 1, 2 et 3 ; puis celle des mesures 2, 3 et 4 ; puis 3, 4 et 5, et ainsi de suite. Les groupes se **chevauchent** : chaque nouveau groupe perd la plus ancienne mesure et gagne la suivante.
- On s'arrête quand il ne reste plus trois mesures pour former un groupe complet.
- On compte, comme dans la partie 1, combien de fois une somme est strictement plus grande que la somme juste avant elle.

**La réponse attendue.** Ce nombre d'augmentations entre sommes consécutives.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-04-defi-aoc-2021-01.zip](../../zips/premiere-04-defi-aoc-2021-01.zip).
