'''

Créez un programme de gestion de bibliothèque de livres avec des fonctions pour ajouter, emprunter, retourner et lister les livres.

	Faites une fonction main pour le menu qui permet d’appeler les 4 fonctions.
	Vous devez utiliser une liste (variable globale) pour stocker vos livres et un dictionnaire pour stocker le titre et l’auteur de chaque livre (variable locale).
	Lorsque vous ajoutez un livre :
o	Elle ne retourne aucune donnée
o	Demandez à l’utilisateur le titre et l’auteur du livre.
o	Ajouter une 3e valeur booléenne au livre dont la clé est la disponibilité.

	Lorsque vous listez un livre :
o	Elle retourne le nombre de livres.
o	Affichez chaque livre selon un des 2 formats suivants:
	TITRE par AUTEUR – Disponible
	TITRE par AUTEUR – Emprunté
o	De retour dans le main du programme, affichez le total de livres dans la bibliothèque.

	Lorsque vous empruntez un livre :
o	Elle retourne si le livre a été trouvé ou non.
o	Demandez le titre du livre à l’utilisateur.
o	De retour dans le main du programme, si le livre existe et qu’il est disponible, affichez un message que le livre est emprunté et identifiez le livre comme non disponible. Sinon, affichez un message qu’il ne soit pas trouvé ou pas disponible.

	Lorsque vous retournez un livre :
o	Elle retourne le texte en message
o	Demandez le titre du livre à l’utilisateur.
o	Si le livre existe et qu’il est non disponible, affichez un message que le livre est retourné et identifiez le livre comme disponible. Sinon, affichez un message qu’il ne soit pas trouvé ou pas emprunté.

'''


def ajouterLivre():
    titre = input("Entrez le titre du livre: ")
    auteur = input("Entrez l'auteur du livre: ")
    livre = [titre, auteur, True]
    livres.append(livre)


def emprunterLivre():
    titre = input("Entrez le titre du livre: ")
    for livre in livres:
        if livre[0] == titre:
            if livre[2]:
                livre[2] = False
                print("Le livre a été emprunté")
            else:
                print("Le livre n'est pas disponible")
            return
    print("Le livre n'existe pas")


def retournerLivre():
    titre = input("Entrez le titre du livre: ")
    for livre in livres:
        if livre[0] == titre:
            if not livre[2]:
                livre[2] = True
                print("Le livre a été retourné")
            else:
                print("Le livre est disponible")
            return
    print("Le livre n'existe pas")


def afficherLivres():
    print("Liste des livres")
    print("----------------")
    for livre in livres:
        if livre[2]:
            print(livre[0] + " par " + livre[1] + " - Disponible")
        else:
            print(livre[0] + " par " + livre[1] + " - Emprunté")
    print("Il y a " + str(len(livres)) + " livres dans la bibliothèque")


if __name__ == "__main__":
    livres = []
    choix = -1
    while choix != 0:
        print("\nGestionnaire de bibliothèque")
        print("-----------------------------")
        print("1. Ajouter un livre ")
        print("2. Emprunter un livre")
        print("3. Retourner un livre")
        print("4. Afficher les livres")
        print("0. Quitter")
        choix = int(input("\nChoisissez une option :"))
        if choix == 1:
            ajouterLivre()
        elif choix == 2:
            emprunterLivre()
        elif choix == 3:
            retournerLivre()
        elif choix == 4:
            afficherLivres()
        elif choix == 0:
            print("Au revoir!")
        else:
            print("Choix invalide")
