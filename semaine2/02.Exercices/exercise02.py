# nom: William Bouchard
# date: 2023/08/31
# description: exercices semaine 2
#############################################################################################################
# Exercices 02 – Gestion d’équipe de hockey
#############################################################################################################
'''
Vous avez la charge de gérer une équipe de hockey.
Vous devez créer un programme Python pour effectuer des opérations
liées à la gestion des joueurs et des points. Assurez-vous d'appliquer les
bonnes pratiques de codage pour rendre votre code efficace et lisible.
Voici les fonctionnalités que votre programme doit inclure :
1. Ajouter un joueur :
Demandez à l'utilisateur d'entrer le nom d'un nouveau joueur et son nombre de points.
Ajoutez le nom et les points du joueur à la liste des joueurs de l'équipe.
i. Indice : Listes imbriquées
'''
import openpyxl
import pandas as pd



def ajouterJoueur(liste):
    nom = input("Entrez le nom du joueur: ")
    points = int(input("Entrez le nombre de points du joueur: "))
    wb = openpyxl.load_workbook("Exercice 02.03 - Canadiens de Montreal.xlsx")
    ws = wb.active
    ws.append([nom, points])
    wb.save("Exercice 02.03 - Canadiens de Montreal.xlsx")
    return liste


'''
Afficher les joueurs :
Affichez la liste complète des joueurs de l'équipe.
Chaque ligne contient le nom du joueur et son nombre de points.
'''


def afficherListe(liste):
    print(liste)


'''
Modifier le nom d’un joueur :
Demandez à l'utilisateur d'entrer le nom d'un joueur à modifier.
Demandez à l'utilisateur d'entrer le nouveau nom du joueur.
Si le nom du joueur est présent dans la liste, mettez-le à jour.
'''


def modifierNom(liste):
    nom = input("Entrez le nom du joueur à modifier: ")
    nouveauNom = input("Entrez le nouveau nom du joueur: ")
    wb = openpyxl.load_workbook("Exercice 02.03 - Canadiens de Montreal.xlsx")
    ws = wb.active
    for row in ws.iter_rows():
        for cell in row:
            if cell.value == nom:
                cell.value = nouveauNom

    wb.save("Exercice 02.03 - Canadiens de Montreal.xlsx")
    return liste


'''
Modifier les points :
Demandez à l'utilisateur d'entrer le nom d'un joueur pour modifier ses points.
Demandez à l'utilisateur d'entrée les nouveaux points du joueur.
Si le nom du joueur est présent dans la liste, mettez-les points à jour.
'''


def ModifierPoints(liste):
    nom = input("Entrez le nom du joueur à modifier: ")
    points = int(input("Entrez le nouveau nombre de points du joueur: "))
    wb = openpyxl.load_workbook("Exercice 02.03 - Canadiens de Montreal.xlsx")
    ws = wb.active
    sheet = wb["Feuil1"]
    for row in ws.iter_rows():
        for cell in row:
            if cell.value == nom:
                sheet.cell(row=cell.row, column=2).value = points

    wb.save("Exercice 02.03 - Canadiens de Montreal.xlsx")
    return liste


'''
Statistiques de l’équipe :
Affichez le nom du meilleur joueur et ses points.
i. Le nombre de joueurs dans l’équipe.
ii. Trouvez le joueur avec les points le plus élevé dans la liste.
iii. Trouvez le joueur avec les points le plus bas dans la liste.
iv. Trouvez la moyenne de points des joueurs.
'''


def Statistiques(liste):
    print("Le nombre de joueurs dans l'équipe est de: ", len(liste))
    if len(liste) > 0:
        print("Le joueur avec le plus de points est: ",
              liste['Nom du joueur'].values[liste['Points'].values.argmax()])
        print("Le joueur avec le moins de points est: ",
              liste['Nom du joueur'].values[liste['Points'].values.argmin()])
        print("La moyenne de points des joueurs est de: ", liste['Points'].mean())


'''
Supprimer un joueur :
Demandez à l'utilisateur d'entrer le nom d'un joueur à supprimer.
Si le joueur est présent dans la liste, supprimez-le.
'''


def supprimerJoueur(liste):
    nom = input("Entrez le nom du joueur à supprimer: ")
    wb = openpyxl.load_workbook("Exercice 02.03 - Canadiens de Montreal.xlsx")
    ws = wb.active

    sheet = wb["Feuil1"]
    for row in ws.iter_rows():
        for cell in row:
            if cell.value == nom:
                sheet.cell(row=cell.row, column=1).value = ""
                sheet.cell(row=cell.row, column=2).value = ""

    wb.save("Exercice 02.03 - Canadiens de Montreal.xlsx")


def AffichageJoueur():
    choix = -1
    print("\nGestionnaire équipe de hockey")
    print("-----------------------------")
    print("1. Ajouter un joueur ")
    print("2. Afficher les Joueurs")
    print("3. Modifier le nom d’un joueur ")
    print("4. Modifier les points ")
    print("5. Statistiques de l’équipe ")
    print("6. Supprimer un joueur ")
    print("7. Quitter")
    choix = input("\nChoisissez une option :")
    return choix


if __name__ == "__main__":

    choixOption = -1
    liste = pd.read_excel("Exercice 02.03 - Canadiens de Montreal.xlsx")
    while choixOption != "7":
        choixOption = AffichageJoueur()
        match choixOption:
            case "1":
                ajouterJoueur(liste)

            case "2":
                afficherListe(liste)

            case "3":
                modifierNom(liste)

            case "4":
                ModifierPoints(liste)

            case "5":
                Statistiques(liste)

            case "6":
                supprimerJoueur(liste)

            case "7":
                choix = "7"
                print("Au revoir!")
