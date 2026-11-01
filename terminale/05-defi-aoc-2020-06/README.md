# Défi Advent of Code — Custom Customs (2020, jour 6)

Terminale NSI — Chapitre 5 — Arbres.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/6>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Pendant le vol, on distribue des formulaires de douane comportant 26 questions fermées, repérées par les lettres de `a` à `z`. Le héros aide les autres passagers, regroupés par groupes de voyage, à les remplir. On veut résumer leurs réponses groupe par groupe.

**Les données.** Le fichier recense les réponses.
- Les groupes sont séparés par une **ligne vide** ; à l'intérieur d'un groupe, il y a une ligne par personne.
- Une ligne contient, sans doublon et dans un ordre quelconque, les lettres des questions où la personne a répondu oui. Une question absente de la ligne correspond donc à un non.

**La règle.**
- Pour chaque groupe, on compte les lettres différentes cochées par **au moins une** personne du groupe.
- Une même lettre cochée par plusieurs personnes du groupe ne compte qu'une fois.
- On fait ce calcul pour chaque groupe séparément, puis on additionne.

**La réponse attendue.** La somme de ces nombres sur tous les groupes. Par exemple, pour un groupe formé des lignes `ab` et `bc`, les lettres cochées sont `a`, `b`, `c` : ce groupe compte pour 3.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le héros a mal lu la consigne : ce qui compte n'est pas ce que quelqu'un a coché, mais ce que tout le groupe a coché. Le fichier et le découpage en groupes restent les mêmes.

**La nouvelle règle.**
- Pour chaque groupe, on compte les lettres cochées par **toutes** les personnes du groupe.
- Une lettre oubliée par une seule personne du groupe ne compte plus.

**La réponse attendue.** La somme de ces nombres sur tous les groupes. Par exemple, le groupe formé des lignes `ab` et `bc` ne compte plus que pour 1 : seule la lettre `b` est cochée par les deux personnes.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-05-defi-aoc-2020-06.zip](../../zips/terminale-05-defi-aoc-2020-06.zip).
