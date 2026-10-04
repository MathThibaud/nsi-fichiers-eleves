# Défi Advent of Code — Inventory Management System (2018, jour 2)

Première NSI — Chapitre 5 — Spécifier et mettre au point ses programmes.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2018/day/2>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Dans l'entrepôt des elfes, on cherche deux boîtes qui contiennent un tissu précieux. Chaque boîte porte un identifiant fait de lettres minuscules, et le fichier donne la liste de ces identifiants, un par ligne. Avant de chercher les boîtes, on calcule une « somme de contrôle » de la liste, qui sert à vérifier qu'on a bien recopié tous les identifiants.

**Ce qu'il faut faire.**
- On compte A, le nombre d'identifiants dans lesquels **au moins une** lettre apparaît **exactement deux fois**.
- On compte B, le nombre d'identifiants dans lesquels au moins une lettre apparaît **exactement trois fois**.
- Un identifiant compte au plus une fois dans A, même s'il a plusieurs lettres doubles ; il peut en revanche compter à la fois dans A et dans B.
- Réponse : le produit A × B.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Il reste à trouver les deux boîtes au tissu précieux : ce sont les deux seules dont les identifiants diffèrent d'**exactement un caractère**, à la même position (toutes les autres positions sont identiques). La réponse est la chaîne des caractères communs, autrement dit l'un des deux identifiants privé du caractère qui diffère.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive premiere-05-defi-aoc-2018-02.zip](../../zips/premiere-05-defi-aoc-2018-02.zip).
