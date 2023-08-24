# auteur: william Bouchard
# date: 2023-08-24
# exercise de la semaine 1

import math

# 01 – Géométrie d’un cercle

rayon = 1  # rayon du cercle
diametre = 2 * rayon  # diametre du cercle
circonference = 2 * math.pi * rayon  # circonference du cercle


# 02– Durée en seconde
# Affichez les heures, les minutes et les secondes selon une durée saisie en secondes.
# Exemple : 1230 secondes = 0 heure, 20 minutes et 30 secondes

def convertir_seconde(temps):
    heure = temps // 3600
    temps = temps % 3600
    minute = temps // 60
    temps = temps % 60
    seconde = temps
    print(heure, "heure,", minute, "minute et", seconde, "seconde")


# 03 – Calculateur de monnaie

# Écrire un programme qui invite l’utilisateur à saisir le nombre de pièces de 1 cent, 5 cents, 10 cents, 25 cents, 1 dollar et 2 dollars. Par la suite, vous devez indiquer le montant exact du total de votre monnaie.
def calculateur_monnaie():
    cent = int(input("nombre de pièces de 1 cent: "))
    cinq_cent = int(input("nombre de pièces de 5 cents: "))
    dix_cent = int(input("nombre de pièces de 10 cents: "))
    vingt_cinq_cent = int(input("nombre de pièces de 25 cents: "))
    un_dollar = int(input("nombre de pièces de 1 dollar: "))
    deux_dollar = int(input("nombre de pièces de 2 dollars: "))
    total = cent + cinq_cent * 5 + dix_cent * 10 + vingt_cinq_cent * 25 + un_dollar * 100 + deux_dollar * 200
    print("total de votre monnaie est: ", total / 100, "dollars")


# exemple
'''
nombre de pièces de 1 cent: 38
nombre de pièces de 5 cents: 23
nombre de pièces de 10 cents: 2
nombre de pièces de 25 cents: 345
nombre de pièces de 1 dollar: 23
nombre de pièces de 2 dollars: 3
total de votre monnaie est:  116.98 dollars
'''

# 04 – Facture de restaurant

'''
Concevoir l'algorithme qui produira la facture d'un repas dans un restaurant.

- On devra tenir compte des éléments suivants: Apéritif, Entrée, Plat principal, Dessert et Bouteille de vin.

- À partir de ces montants, il faut calculer le sous-total, y ajouter un pourboire de 15%, les taxes provinciale (9.975%) et fédérale de 5%.

- La facture doit avoir :

o L’adresse de l’entreprise

o La liste des articles avec leur prix

o Le sous-total, les taxes, le pourboire et le montant total
'''


def facture():
    print("Bienvenue au restaurant")
    aperitif = float(input("Apéritif: "))
    entree = float(input("Entrée: "))
    plat_principal = float(input("Plat principal: "))
    dessert = float(input("Dessert: "))
    bouteille_de_vin = float(input("Bouteille de vin: "))
    sous_total = aperitif + entree + plat_principal + dessert + bouteille_de_vin
    pourboire = sous_total * 0.15
    taxes_provinciale = sous_total * 0.09975
    taxes_federale = sous_total * 0.05
    total = sous_total + pourboire + taxes_provinciale + taxes_federale
    print("sous-total: ", sous_total)
    print("pourboire: ", pourboire)
    print("taxes provinciale: ", taxes_provinciale)
    print("taxes fédérale: ", taxes_federale)
    print("total: ", total)


if __name__ == "__main__":
    # convertir_seconde(1230)
    # calculateur_monnaie()
    facture()
