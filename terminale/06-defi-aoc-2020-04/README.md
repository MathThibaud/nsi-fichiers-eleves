# Défi Advent of Code — Passport Processing (2020, jour 4)

Terminale NSI — Chapitre 6 — Bases de données et SQL.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/4>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Arrivé à l'aéroport, le héros s'aperçoit qu'il a emporté une carte d'identité du pôle Nord, et non son passeport. La file devant les scanners automatiques est interminable, car ces machines vérifient mal les documents. Le fichier contient les données lues par un scanner : chaque passeport y est décrit par une suite de champs (année de naissance, taille, couleur des yeux…). Il faut écrire le programme qui décide si un document est acceptable.

**Ce qu'il faut faire.**
- Les passeports sont séparés par une **ligne vide** ; un même passeport peut s'étaler sur plusieurs lignes.
- Un passeport est une suite de champs `cle:valeur`, séparés par des espaces ou des retours à la ligne, dans un ordre quelconque.
- Il existe huit clés : `byr` (année de naissance), `iyr` (année de délivrance), `eyr` (année d'expiration), `hgt` (taille), `hcl` (couleur des cheveux), `ecl` (couleur des yeux), `pid` (numéro de passeport) et `cid` (pays).
- En partie 1, un passeport est valide si les sept premières clés sont présentes ; `cid` peut manquer, ce qui laisse passer la carte du héros. Les valeurs ne sont pas encore examinées.
- Il faut renvoyer le nombre de passeports valides.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Des documents absurdes passent encore : il faut maintenant contrôler aussi les valeurs. Un passeport est valide si les sept clés sont présentes **et** si :
- `byr` est entre 1920 et 2002, `iyr` entre 2010 et 2020, `eyr` entre 2020 et 2030 (quatre chiffres, bornes comprises) ;
- `hgt` est un nombre suivi de `cm` (de 150 à 193) ou de `in` (de 59 à 76) ;
- `hcl` est `#` suivi d'exactement six caractères parmi `0-9` et `a-f` ; `ecl` vaut exactement l'un de `amb blu brn gry grn hzl oth` ;
- `pid` compte exactement neuf chiffres (zéros de tête compris) ; `cid` est ignoré.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-06-defi-aoc-2020-04.zip](../../zips/terminale-06-defi-aoc-2020-04.zip).
