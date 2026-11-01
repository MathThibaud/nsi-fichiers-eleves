# Défi Advent of Code — Monster Messages (2020, jour 19)

Terminale NSI — Chapitre 12 — Recherche textuelle.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/19>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Arrivé dans une forêt, vous êtes contacté par les elfes : un satellite leur envoie des messages, mais la liaison est mauvaise et beaucoup arrivent abîmés. Pour faire le tri, ils disposent de règles qui décrivent exactement à quoi ressemble un message correct. Il faut leur dire combien de messages sont utilisables.

**Les données.** Le fichier a deux parties séparées par une ligne vide. D'abord les règles, une par ligne, sous la forme `numéro: définition` (par exemple `2: 4 3 | 3 1`), pas forcément rangées dans l'ordre des numéros. Ensuite les messages reçus, un par ligne, formés uniquement des lettres `a` et `b`.

**La règle.**
- Une règle « lettre », écrite entre guillemets comme `"a"`, reconnaît exactement ce caractère.
- Une règle composée est une suite de numéros : le texte doit se découper en morceaux consécutifs reconnus, dans l'ordre, par ces sous-règles.
- Le symbole `|` sépare des alternatives : il suffit que l'une d'elles convienne. Les règles s'emboîtent ainsi comme des briques, de la lettre jusqu'à la règle `0`.
- En partie 1, aucune règle ne fait appel à elle-même, directement ou par l'intermédiaire d'autres règles.
- Un message est valide si la règle `0` le reconnaît **en entier**, sans caractère en trop.

**La réponse attendue.** Le nombre de messages valides. Par exemple, avec les règles `0: 1 2 | 2 1`, `1: "a"` et `2: "b"`, la règle `0` reconnaît `ab` et `ba` seulement : parmi les messages `ab`, `ba`, `aba` et `bb`, la réponse serait 2 (`aba` a une lettre en trop).

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Les elfes s'aperçoivent que deux de leurs règles étaient fausses et vous envoient les bonnes : `8: 42 | 42 8` et `11: 42 31 | 42 11 31`. Ces deux règles remplacent les anciennes règles `8` et `11` ; toutes les autres sont inchangées.

**La nouvelle règle.**
- Ces règles font appel à elles-mêmes : le nombre de mots qu'elles reconnaissent devient infini.
- La règle `8` reconnaît une ou plusieurs répétitions de la règle `42`.
- La règle `11` reconnaît k fois la règle `42` suivie de k fois la règle `31`, avec le même k ≥ 1 des deux côtés. Par exemple, si `42` reconnaissait `a` et `31` reconnaissait `b`, la règle `11` reconnaîtrait `ab`, `aabb`, `aaabbb`… mais pas `aab`.
- Un message est toujours valide si la règle `0` le reconnaît en entier.

**La réponse attendue.** Le nouveau nombre de messages valides.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-12-defi-aoc-2020-19.zip](../../zips/terminale-12-defi-aoc-2020-19.zip).
