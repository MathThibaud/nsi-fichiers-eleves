# Défi Advent of Code — Inventory Management System (2018, jour 2)

Première NSI — Chapitre 5 — Spécifier et mettre au point ses programmes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2018/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dans l'entrepôt des elfes, on cherche deux boîtes qui contiennent un tissu précieux. Chaque boîte porte un identifiant. Avant de chercher les boîtes, on calcule une « somme de contrôle » de la liste des identifiants : un nombre qui résume la liste et sert à vérifier qu'on l'a bien recopiée en entier.

**Les données.** Le fichier contient un identifiant par ligne : un mot fait uniquement de lettres minuscules, sans espace. Tous les identifiants ont la même longueur.

**La règle.**
- On compte A, le nombre d'identifiants dans lesquels **au moins une** lettre apparaît **exactement deux fois**.
- On compte B, le nombre d'identifiants dans lesquels au moins une lettre apparaît **exactement trois fois**.
- « Exactement » compte : une lettre présente quatre fois n'est ni double ni triple.
- Un identifiant compte au plus une fois dans A, même s'il a plusieurs lettres doubles (et de même pour B) ; il peut en revanche compter à la fois dans A et dans B.

**La réponse attendue.** Le produit A × B. Par exemple, pour les trois identifiants `abcabd`, `xyzxzx` et `klmnop`, on a A = 2 (les deux premiers), B = 1 (le deuxième), et la réponse serait 2.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** On ne calcule plus une somme de contrôle : il faut maintenant trouver les deux boîtes au tissu précieux, en comparant les identifiants entre eux.

**La nouvelle règle.**
- Les deux boîtes cherchées sont les deux seules dont les identifiants diffèrent d'**exactement un caractère**, à la même position.
- Toutes les autres positions sont identiques : on compare les caractères position par position, sans décaler les mots.

**La réponse attendue.** La chaîne des caractères communs aux deux identifiants, autrement dit l'un des deux identifiants privé du caractère qui diffère. Par exemple, si les deux identifiants étaient `porte` et `parte`, la réponse serait `prte`.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-05-defi-aoc-2018-02.zip](../../zips/premiere-05-defi-aoc-2018-02.zip).
