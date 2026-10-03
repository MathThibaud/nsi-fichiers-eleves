# TP "L'annuaire et le devin" -- donnees (fichier fourni, ne pas modifier)
# Fabrique un annuaire FICTIF de 16 000 abonnes, trie par ordre alphabetique.
# Les numeros sont inventes (tires au hasard, toujours les memes).

import random

NOMS = """MARTIN BERNARD THOMAS PETIT ROBERT RICHARD DURAND DUBOIS MOREAU LAURENT
SIMON MICHEL LEFEBVRE LEROY ROUX DAVID BERTRAND MOREL FOURNIER GIRARD
BONNET DUPONT LAMBERT FONTAINE ROUSSEAU VINCENT MULLER LEFEVRE FAURE ANDRE
MERCIER BLANC GUERIN BOYER GARNIER CHEVALIER FRANCOIS LEGRAND GAUTHIER GARCIA
PERRIN ROBIN CLEMENT MORIN NICOLAS HENRY ROUSSEL MATHIEU GAUTIER MASSON
MARCHAND DUVAL DENIS DUMONT MARIE LEMAIRE NOEL MEYER DUFOUR MEUNIER
BRUN BLANCHARD GIRAUD JOLY RIVIERE LUCAS BRUNET GAILLARD BARBIER ARNAUD
MARTINEZ GERARD ROCHE RENARD SCHMITT ROY LEROUX COLIN VIDAL CARON
PICARD ROGER FABRE AUBERT LEMOINE RENAUD DUMAS LACROIX OLIVIER PHILIPPE
BOURGEOIS PIERRE BENOIT REY LECLERC PAYET ROLLAND LECLERCQ GUILLAUME LECOMTE
LOPEZ JEAN DUPUY GUILLOT HUBERT BERGER CARPENTIER SANCHEZ DUPUIS MOULIN
LOUIS DESCHAMPS HUET VASSEUR PEREZ BOUCHER FLEURY ROYER KLEIN JACQUET
ADAM PARIS POIRIER MARTY AUBRY GUYOT CARRE CHARLES RENAULT CHARPENTIER
MENARD MAILLARD BARON BERTIN BAILLY HERVE SCHNEIDER FERNANDEZ LE_GALL COLLET
LEGER BOUVIER JULIEN PREVOST MILLET PERROT DANIEL LE_ROUX COUSIN GERMAIN
BRETON BESSON LANGLOIS REMY LE_GOFF PELLETIER LEVEQUE PERRIER LEBLANC BARRE""".split()

PRENOMS = """Adam Agathe Alice Amir Anna Arthur Axel Camille Chloe Clara
Damien Eden Elena Elise Emma Enzo Ethan Eva Farah Gabriel
Hugo Ines Isaac Jade Jules Julia Kenza Leo Lea Lena
Liam Lina Lou Louis Louise Lucas Lucie Mael Manon Marius
Mathis Mila Nathan Noah Nora Oscar Paul Raphael Romy Rose
Sacha Sarah Theo Tom Victor Yanis Yasmine Zoe Malo Nina
Adele Alba Ambre Antoine Aya Baptiste Basile Celia Charlie Diane
Elias Emile Gaspard Ilyes Iris Jeanne Josephine Lana Leon Lisa
Lyna Margaux Martin Maya Mia Nael Noam Olivia Pablo Rayan
Robin Salome Samuel Simon Soline Tiago Timeo Valentin Victoire Ylan""".split()

def charger_annuaire():
    """Renvoie deux tableaux de meme longueur :
    noms    : les 'NOM Prenom' tries par ordre alphabetique (sans doublon) ;
    numeros : numeros[i] est le numero de telephone de noms[i]."""
    gen = random.Random(2026)
    noms = []
    for nom in NOMS:
        for prenom in PRENOMS:
            noms.append(nom.replace("_", " ") + " " + prenom)
    noms.sort()
    numeros = []
    for k in range(len(noms)):
        numero = "06"
        for j in range(4):
            numero = numero + " " + str(gen.randint(10, 99))
        numeros.append(numero)
    return noms, numeros

if __name__ == "__main__":
    noms, numeros = charger_annuaire()
    print(len(noms), "abonnés ;", noms[0], numeros[0], "...", noms[-1], numeros[-1])
