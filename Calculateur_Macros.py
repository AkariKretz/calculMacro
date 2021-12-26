#!/usr/bin/python3

print("Calculateur de Macros")


fat = input("Pourcentage de masse grasse? ")
print("Pourcentage de masse grasse : " + fat + "%")
fat = float(fat)
poids = input("Poids? ")
print("poids : " + poids + "kg")
poids = float(poids)
MCM = float(poids - fat)
print("Taux de masse corporel maigre : " + str(MCM))

TMB = 370 + (21.6 * MCM)
print("TMB : " + str(TMB))

#Facteur d'activite
print("Facteur d'activite = 1.55 si pas d'activite physique")
print("Facteur d'activite = 1.72 si muscu 6 fois par semaine")
print("Facteur d'activite = 1.90 si sport 2 fois par jour")
fa = input("Facteur d'activite ")
print("Facteur d'activite  : " + fa)

## Calcule des calories ##
# Maintenance #
maintenance =  TMB * float(fa)
maintenance = int(maintenance)
print("calories pour une maintenance : " + str(maintenance))

# Perte de poids #
perte = maintenance - 500
print("calories pour une maintenance : " + str(perte))

# Prise de poids #
gain = maintenance + 500
print("calories pour une maintenance : " + str(gain))

## Calcul des macros ##
# De base #
glucide = (0.5 * maintenance) / 4
print("Glucides journaliers : "+ str(glucide) +"g")
proteine = (0.3 * maintenance) / 4
print("Proteines journalieres : "+ str(proteine) +"g")
lipide = (0.2 * maintenance) / 4
print("Lipides journaliers : "+ str(lipide) +"g")

# jouer jouer dessus pour la seche, principalement sur les glucides. si enleve des glucides les rajoueter au prot et lipide toujour garder 100%