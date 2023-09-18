# Auteur : william bouchard
# Date : 2023-09-18
# But : programme qui permet de faire la gestion de motoneiges

import motoneige


def menu():
    print("\nGestion motoneiges\n------------------")
    print("1. Afficher les motoneiges")
    print("2. Total par marque")
    print("3. Envoyer dans un fichier TXT")
    print("4. Quitter")


def lecture_csv(nom_fichier):
    # Lire le fichier CSV et retourner une liste
    with open(nom_fichier, "r") as fichier:
        next(fichier)
        lignes = fichier.readlines()
        # Convertir les lignes en liste
        liste = [f'{i} {val}' for i, val in enumerate(lignes, 1)]
        return liste


def afficherMotoneiges(lignes):
    # Afficher les motoneiges avec les informations
    ligne_aficher = ""
    for ligne in lignes:
        elements = ligne.split(",")
        elements[3] = motoneige.pieds_en_metres(float(elements[3]))
        for item in elements:
            ligne_aficher += " " + format(item)
    # affiche les motoneiges
    print(ligne_aficher)
    choix_motoneige = int(input("Entrez le numéro de la motoneige: "))
    elements = lignes[choix_motoneige - 1].split(",")
    choix_url = elements[0].split(" ")
    url = choix_url[1]
    nom = motoneige.enlever_annee(elements[1])
    motoneige.affichage_image(url, nom)
    print("L'image a été enregistrée sous le nom " + nom + ".jpg")


def total_marque(lignes):
    # Afficher le total par marque
    compteur = []
    nombreDeFoisMotoneige = []
    for ligne in lignes:
        elements = ligne.split(",")
        if elements[5] not in compteur:
            compteur.append(elements[5])
        nombreDeFoisMotoneige.append(elements[5])
    nbdefois = set(nombreDeFoisMotoneige)
    for i in nbdefois:
        print(i, ":", nombreDeFoisMotoneige.count(i))
    print("Total par marque")


def ecrire_fichier(lignes):
    # Créer un fichier texte avec les motoneiges
    choix_fichier = input("Entrez le nom du modele: ")

    for ligne in lignes:
        elements = ligne.split(",")
        if elements[5] == choix_fichier:
            ligneAEcrire = elements[6].replace('\n', '') + " " + motoneige.enlever_annee(
                elements[1] + "\n")

            with open(f"{choix_fichier}.txt", "a") as fichier:
                fichier.write(ligneAEcrire)


if __name__ == '__main__':
    choix = -1
    ligne = lecture_csv("motoneiges.csv")
    while choix != 4:
        menu()
        choix = int(input("Entrez votre choix: "))
        if choix == 1:
            afficherMotoneiges(ligne)
        elif choix == 2:
            total_marque(ligne)
        elif choix == 3:
            ecrire_fichier(ligne)
        elif choix == 4:
            print("Bye")
        else:
            print("Choix invalide.")
