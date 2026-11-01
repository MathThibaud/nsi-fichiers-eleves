# Défi Advent of Code — Red-Nosed Reports (2024, jour 2)

Première NSI — Chapitre 4 — Algorithmique : le parcours séquentiel.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2024/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dans une centrale nucléaire du pôle Nord, les ingénieurs vous demandent d'analyser des relevés étranges du réacteur. Chaque relevé est une suite de mesures (des « niveaux »). Le réacteur ne supporte que des niveaux qui évoluent régulièrement, sans à-coups : il faut repérer les relevés rassurants.

**Les données.** Chaque ligne du fichier est un relevé : des entiers séparés par une espace, par exemple `3 5 6 9`. Le nombre de niveaux varie d'une ligne à l'autre. Les relevés sont indépendants les uns des autres.

**La règle.** Un relevé est **sûr** si les deux conditions suivantes sont vraies à la fois :
- les niveaux sont tous croissants, ou bien tous décroissants (pas de changement de sens) ;
- deux niveaux voisins diffèrent d'**au moins 1** et d'**au plus 3** (deux voisins égaux rendent donc le relevé dangereux).

Autrement dit, d'un niveau au suivant, le relevé avance toujours dans le même sens, par petits pas, sans jamais stagner.

**La réponse attendue.** Le nombre de relevés sûrs du fichier. Par exemple, parmi les trois relevés `3 5 6 9` (écarts +2, +1, +3 : sûr), `4 4 5` (écart nul : dangereux) et `1 6 7` (écart +5 : dangereux), un seul est sûr : la réponse serait 1.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les ingénieurs signalent que le réacteur dispose d'un « amortisseur » capable d'ignorer une seule mesure aberrante. Certains relevés jugés dangereux dans la partie 1 deviennent donc acceptables.

**La nouvelle règle.**
- Un relevé déjà sûr selon la partie 1 reste sûr.
- Un relevé dangereux compte maintenant aussi comme sûr s'il devient sûr quand on lui retire **un seul** de ses niveaux, n'importe lequel (le premier, le dernier ou un niveau du milieu).
- Les conditions pour être sûr sont les mêmes que dans la partie 1.

**La réponse attendue.** Le nouveau nombre de relevés sûrs. Avec les trois relevés inventés ci-dessus, `4 4 5` devient sûr en retirant un `4`, et `1 6 7` en retirant le `1` : la réponse serait 3.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-04-defi-aoc-2024-02.zip](../../zips/premiere-04-defi-aoc-2024-02.zip).
