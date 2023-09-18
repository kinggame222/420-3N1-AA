'''
Question 01 – Données sur des gens

Vous avez un fichier texte appelé donnees.txt qui contient des données tabulaires sous forme de colonnes, séparées par des tabulations. Chaque ligne représente un enregistrement. Les colonnes sont les suivantes : Nom, Age, Ville.

Votre tâche est d'écrire un programme Python qui lit ce fichier, analyse les données et effectue les opérations suivantes :
	Calcule l'âge moyen des personnes dans le fichier.
	Identifie la ville la plus fréquente dans le fichier.
	Identifie la personne la plus âgée et la personne la plus jeune.
'''


def lireFichier(nom_fichier):
    with open(nom_fichier, "r") as fichier:
        lignes = fichier.readlines()
    return lignes


def convertirLignesEnListe(lignes):
    liste = []
    for ligne in lignes:
        elements = ligne.split("\t")
        for item in elements:
            nouvelle_liste = ' '.join(item.split(' ')).split()
            liste.append(nouvelle_liste)
    return liste


def calculerAgeMoyen(liste):
    total = 0
    for item in liste:
        total += int(item[1])
    return (total / len(liste)).__floor__()


def villePlusFrequente(liste):
    villes = []
    for item in liste:
        villes.append(item[2])

    return max(set(villes), key=villes.count)


def personnePlusAgee(liste):
    max_val = 0
    tab = [0, 0]
    for i in liste:
        if max_val < int(i[1]):
            max_val = int(i[1])
            tab[0] = int(i[1])
            tab[1] = i[0]
    return tab


def personnePlusJeune(liste):
    min_val = 200
    tab = [0, 0]

    for i in liste:
        if min_val > int(i[1]):
            min_val = int(i[1])
            tab[0] = int(i[1])
            tab[1] = i[0]
    return tab


if __name__ == "__main__":
    nom_fichier = "donnees.txt"

    lignes = convertirLignesEnListe(lireFichier(nom_fichier))
    valJeune = personnePlusJeune(lignes)
    valvieux = personnePlusAgee(lignes)

    print("l'age moyen est : " + str(calculerAgeMoyen(lignes)))
    print("la ville la plus fréquenté est : " + villePlusFrequente(lignes))
    print("la personne la plus jeune est : " + str(valJeune[1]) + " " + str(valJeune[0]))
    print("la personne la plus agé est : " + str(valvieux[1]) + " " + str(valvieux[0]))
