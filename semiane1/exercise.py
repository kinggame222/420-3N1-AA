# auteur: william Bouchard
# date: 2023-08-24
# exercise de la semaine 1

import math

# 01 – Géométrie d’un cercle

rayon = 1  # rayon du cercle
diametre = 2 * rayon  # diametre du cercle
circonference = 2 * math.pi * rayon  # circonference du cercle
aire = math.pi * rayon * rayon  # aire du cercle


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


# 05 – Couvre plancher

'''
Votre voisin qui est propriétaire d’une entreprise de couvre plancher et il aimerait avoir 
une application pour calculer la quantité et le prix des tuiles de céramique à poser chez un client.
 Pour ce faire, le client vous donne la dimension de l’espace à couvrir (longueur et largeur),
  la dimension d’une tuile de céramique et le prix d’une boite ainsi que le nombre de tuiles compris dans une boite.
   N’oubliez pas d’inclure un pourcentage de perte de 5 %.

Ensuite, créer la soumission sous le même format que la facture du restaurant, sans le pourboire.
'''


def couvre_plancher():
    print("Bienvenue au couvre plancher")
    longueur = float(input("longueur: "))
    largeur = float(input("largeur: "))
    dimension_tuile = float(input("dimension d'une tuile: "))
    prix_boite = float(input("prix d'une boite: "))
    nombre_tuiles = float(input("nombre de tuiles compris dans une boite: "))
    espace = longueur * largeur
    nombre_tuiles_necessaires = espace / (dimension_tuile * dimension_tuile) * 1.05
    nombre_boites = math.ceil(nombre_tuiles_necessaires / nombre_tuiles)
    prix_total = nombre_boites * prix_boite
    print("espace à couvrir: ", espace)
    print("nombre de tuiles nécessaires: ", nombre_tuiles_necessaires)
    print("nombre de boites: ", nombre_boites)
    print("prix total: ", prix_total)


# 06 – Vérification de la note finale
'''Calculer et afficher la note finale d’un étudiant. L’étudiant a fait deux 
travaux notés sur 5 points qui compteront pour chacun 15% de la note finale.
 De plus, l’examen qui est noté sur 75 points correspond à 30% de la note finale.
 Et pour finir, l’épreuve terminale de cours sera notée sur 105 points et compte pour 40% de la note finale.'''


def note_final():
    note_travaux = float(input("note des deux travaux: "))
    note_examen = float(input("note de l'examen: "))
    note_epreuve = float(input("note de l'épreuve: "))
    note_final = note_travaux * 0.15 + note_examen * 0.3 + note_epreuve * 0.4
    print("note final: ", note_final)


# 07 – Conversion
'''Vous devez effectuer une conversion entre chacune de mesures suivantes 
selon le choix de l’utilisateur: pouce, pied, millimètre, centimètre, mètre et kilomètre'''


def conversion():
    print("Bienvenue au convertisseur")
    print("pouce: 1")
    print("pied: 2")
    print("millimètre: 3")
    print("centimètre: 4")
    print("mètre: 5")
    print("kilomètre: 6")
    choix = int(input("choix: "))
    choix2 = int(input("convertir vers: "))
    nombre = float(input("nombre: "))
    valeur_1 = 0  # en cm
    valeur_2 = 0  # en cm
    if choix == 1:
        valeur_1 = 2.54
        print("pouce")
    elif choix == 2:
        valeur_1 = 30.48
        print("pied")
    elif choix == 3:
        valeur_1 = 0.1
        print("millimètre")
    elif choix == 4:
        valeur_1 = 1
        print("centimètre")
    elif choix == 5:
        valeur_1 = 100
        print("mètre")
    elif choix == 6:
        valeur_1 = 100000
        print("kilomètre")
    else:
        print("erreur")

    if choix2 == 1:
        valeur_2 = 2.54
        print("pouce")
    elif choix2 == 2:
        valeur_2 = 30.48
        print("pied")
    elif choix2 == 3:
        valeur_2 = 0.1
        print("millimètre")
    elif choix2 == 4:
        valeur_2 = 1
        print("centimètre")
    elif choix2 == 5:
        valeur_2 = 100
        print("mètre")
    elif choix2 == 6:
        valeur_2 = 100000
        print("kilomètre")
    else:
        print("erreur")

    print(nombre * valeur_1 / valeur_2)


#
'''
La compagnie Gazon-Alma est une petite entreprise régionale qui fait l’entretien des gazons pour ces clients. Pour bien organiser son travail, l’entreprise aimerait avoir un outil (une application) qui lui permettrait d’estimer :

ü le temps nécessaire (en minute) pour tondre le gazon d’un cours rectangulaire;

ü le nombre de sacs d’engrais nécessaire pour recouvrir le gazon;

ü le prix total de l’engrais.

ü

Pour ce faire, chaque client fournit toujours la longueur et la largeur en pieds de son terrain. Il faut 25 secondes (en moyenne) pour tondre un m2 de superficie de gazon. Chaque sac d’engrais couvre 100 m2 et coûte 3.50$.

Ensuite, créer la facture sous le même format que la facture du restaurant, sans le pourboire.
'''

#08 – Gazon-Alma
def gazon_alma():
    print("Bienvenue au gazon alma")
    longueur = float(input("longueur: "))
    largeur = float(input("largeur: "))
    superficie = longueur * largeur
    temps = superficie * 25 / 60
    nombre_sacs = superficie / 100
    prix_total = nombre_sacs * 3.5
    print("superficie: ", superficie)
    print("temps nécessaire: ", temps)
    print("nombre de sacs d'engrais: ", nombre_sacs)
    print("prix total de l'engrais: ", prix_total)


if __name__ == "__main__":
    # convertir_seconde(1230)
    # calculateur_monnaie()
    # facture()
    # couvre_plancher()
    # note_final()
    # conversion()
    gazon_alma()
