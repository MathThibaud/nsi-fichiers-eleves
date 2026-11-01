# Défi Advent of Code — Crab Combat (2020, jour 22)

Terminale NSI — Chapitre 4 — Processus et ordonnancement.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/22>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Sur le radeau, l'ennui guette ; heureusement, un petit crabe est monté à bord et accepte de jouer aux cartes avec vous, à un jeu proche de la bataille. Avant de jouer, vous voulez prévoir l'issue de la partie à partir des paquets distribués.

**Les données.** Le fichier contient deux blocs séparés par une ligne vide : le paquet du joueur 1 (vous), puis celui du joueur 2 (le crabe). Chaque bloc commence par une ligne d'en-tête, puis donne une carte par ligne, la carte du **dessus** en premier. Les cartes sont des entiers, tous différents.

**La règle.**
- À chaque manche, chaque joueur retire sa carte du dessus ; la plus forte gagne la manche (il ne peut pas y avoir d'égalité).
- Le gagnant place les deux cartes sous son paquet : la sienne d'abord, puis celle de l'adversaire.
- La partie s'arrête quand un joueur a toutes les cartes.
- Score du gagnant : la carte du dessous est multipliée par 1, celle juste au-dessus par 2, etc., jusqu'à la carte du dessus, multipliée par le nombre de cartes ; on additionne ces produits. Plus une carte est haut dans le paquet, plus elle compte.

**La réponse attendue.** Le score du gagnant. Par exemple, un paquet gagnant 5, 3, 9 (dessus en premier) vaudrait 5 × 3 + 3 × 2 + 9 × 1 = 30.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

**Ce qui change.** Le crabe a perdu et propose une revanche, à une version « récursive » du jeu : certaines manches se décident en jouant une partie plus petite.

**La nouvelle règle.**
- Avant chaque manche : si la même configuration des deux paquets est déjà apparue **dans cette partie**, le joueur 1 gagne aussitôt la partie. Cela empêche une partie de durer indéfiniment.
- Sinon, chacun tire sa carte du dessus.
- Si chaque joueur a encore au moins autant de cartes que la valeur qu'il vient de tirer, le gagnant de la manche est celui d'une sous-partie, jouée avec les mêmes règles et des copies de ses n cartes suivantes (n = valeur qu'il a tirée). Par exemple, un joueur qui tire un 3 et a encore au moins 3 cartes entre dans la sous-partie avec une copie de ses 3 cartes du dessus.
- Sinon, la plus forte carte gagne, comme en partie 1.
- Le gagnant de la manche range les deux cartes sous son paquet comme avant : la sienne d'abord, même si elle est la plus faible.

**La réponse attendue.** Le score du gagnant de la partie principale, calculé comme en partie 1.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-04-defi-aoc-2020-22.zip](../../zips/terminale-04-defi-aoc-2020-22.zip).
