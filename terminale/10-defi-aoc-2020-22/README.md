# Défi Advent of Code — Crab Combat (2020, jour 22)

Terminale NSI — Chapitre 10 — Processus et ordonnancement.

## Ce qu'il faut faire

Énoncé complet (en anglais) : <https://adventofcode.com/2020/day/22>. Ce résumé, écrit pour le manuel, ne remplace pas sa lecture.

**Contexte.** Sur le radeau, l'ennui guette ; heureusement, un petit crabe est monté à bord et accepte de jouer aux cartes avec vous, à un jeu proche de la bataille. Le fichier donne la main de départ de chaque joueur.

**Ce qu'il faut faire.**
- Le fichier contient deux blocs (joueur 1, puis joueur 2) : une carte par ligne, la carte du dessus en premier. Toutes les valeurs sont différentes.
- À chaque manche, chaque joueur retire sa carte du dessus ; la plus forte gagne. Le gagnant place les deux cartes sous son paquet : la sienne d'abord, puis celle de l'adversaire.
- La partie s'arrête quand un joueur a toutes les cartes.
- Score du gagnant : la carte du dessous est multipliée par 1, celle juste au-dessus par 2, etc., jusqu'à la carte du dessus multipliée par le nombre de cartes ; on additionne. Autrement dit, plus une carte est haut dans le paquet, plus elle compte. Réponse : ce score.

<details>
<summary><b>Partie 2</b> (à ouvrir après avoir réussi la partie 1)</summary>

Le crabe a perdu et propose une revanche à une version « récursive » du jeu.
- Avant chaque manche : si la même configuration des deux paquets est déjà apparue **dans cette partie**, le joueur 1 gagne aussitôt la partie.
- Sinon, chacun tire sa carte. Si chaque joueur a encore au moins autant de cartes que la valeur qu'il vient de tirer, le gagnant de la manche est celui d'une sous-partie jouée avec des copies de ses n cartes suivantes (n = valeur tirée). Sinon, la plus forte carte gagne. Le gagnant range les cartes comme avant.
- Réponse : le score du gagnant de la partie principale.

</details>

## Fichiers

Placer tous ces fichiers dans un même dossier de travail.

| Fichier | Rôle |
|---|---|
| `input.txt` | données maison (même format que sur adventofcode.com) |
| `verifier.py` | vérifie vos réponses (python3 verifier.py) |

Données fabriquées pour le manuel, au même format que celles du site adventofcode.com (l'énoncé se lit sur ce site, il n'est pas reproduit ici) ; les réponses diffèrent donc de celles que le site vous demanderait. Aucun corrigé n'est fourni : verifier.py dit seulement si une réponse est juste. Advent of Code est créé par Eric Wastl.

Tout télécharger d'un coup : [archive terminale-10-defi-aoc-2020-22.zip](../../zips/terminale-10-defi-aoc-2020-22.zip).
