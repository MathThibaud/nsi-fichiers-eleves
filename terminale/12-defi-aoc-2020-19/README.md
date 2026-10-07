# Défi Advent of Code — Monster Messages (2020, jour 19)

Terminale NSI — Chapitre 12 — Recherche textuelle.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/19>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Arrivé dans une forêt, vous êtes contacté par les elfes : un satellite leur envoie des messages, mais la liaison est mauvaise et beaucoup arrivent abîmés. Pour trier, ils disposent de règles qui décrivent exactement à quoi ressemble un message correct. Le fichier contient ces règles, puis les messages reçus.

**Ce qu'il faut faire.**
- Les règles sont numérotées (`numéro: définition`, une par ligne) ; une ligne vide les sépare des messages, formés des lettres `a` et `b`.
- Une règle « lettre » (`"a"`) reconnaît exactement ce caractère.
- Une règle composée est une suite de numéros : le texte doit se découper en morceaux consécutifs reconnus, dans l'ordre, par ces sous-règles. Le symbole `|` sépare des alternatives : il suffit que l'une d'elles convienne. Autrement dit, les règles s'emboîtent comme des briques, de la lettre jusqu'à la règle `0`.
- En partie 1, aucune règle ne fait appel à elle-même, directement ou par l'intermédiaire d'autres règles.
- Un message est valide si la règle `0` le reconnaît **en entier**, sans caractère en trop. Réponse : le nombre de messages valides.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Les elfes s'aperçoivent que deux de leurs règles étaient fausses et vous envoient les bonnes : `8: 42 | 42 8` et `11: 42 31 | 42 11 31`. Ces règles font appel à elles-mêmes : la règle `8` reconnaît une ou plusieurs répétitions de la règle `42`, et la règle `11` reconnaît k fois la règle `42` suivie de k fois la règle `31` (k ≥ 1). Réponse : le nouveau nombre de messages valides.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-12-defi-aoc-2020-19.zip](../../zips/terminale-12-defi-aoc-2020-19.zip).
