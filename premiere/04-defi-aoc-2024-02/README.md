# Défi Advent of Code — Red-Nosed Reports (2024, jour 2)

Première NSI — Chapitre 4 — Algorithmique : le parcours séquentiel.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2024/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dans une centrale nucléaire du pôle Nord, les ingénieurs vous demandent d'analyser des relevés étranges du réacteur. Chaque relevé est une suite de mesures (des « niveaux »). Le réacteur ne supporte que des niveaux qui évoluent régulièrement, sans à-coups : il faut repérer les relevés rassurants.

**Ce qu'il faut faire.**
- Chaque ligne est un relevé : des entiers séparés par une espace. Le nombre de niveaux varie d'une ligne à l'autre.
- Un relevé est **sûr** si deux conditions sont vraies à la fois. Première condition : les niveaux sont tous croissants ou tous décroissants. Seconde condition : deux niveaux voisins diffèrent d'**au moins 1** et d'**au plus 3**.
- Autrement dit, d'un niveau au suivant, le relevé avance toujours dans le même sens, par petits pas, sans jamais stagner.
- La réponse est le nombre de relevés sûrs.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les ingénieurs signalent que le réacteur dispose d'un « amortisseur » capable d'ignorer une seule mesure aberrante. Un relevé compte donc maintenant aussi comme sûr s'il devient sûr quand on lui retire **un seul** de ses niveaux, n'importe lequel. La réponse est le nouveau nombre de relevés sûrs.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-04-defi-aoc-2024-02.zip](../../zips/premiere-04-defi-aoc-2024-02.zip).
