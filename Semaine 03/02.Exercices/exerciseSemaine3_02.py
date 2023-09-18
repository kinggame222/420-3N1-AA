'''

Question 02 – Fichiers employés

Vous avez deux fichiers CSV, employes1.csv et employes2.csv,
qui contiennent des informations sur des employé.
Votre tâche est de fusionner ces deux fichiers en un seul fichier CSV appelé employes_fusion.csv.
Assurez-vous d'ignorer les en-têtes de colonnes dans les fichiers sources.
'''


def fusionnerFichiers(nom_fichier1, nom_fichier2, nom_fichier_fusion):
    with (open(nom_fichier1, "r") as fichier1, open(nom_fichier2, "r")
    as fichier2, open(nom_fichier_fusion, "w") as fichier_fusion):
        # Ignorer les en-têtes
        #next(fichier1)
        next(fichier2)

        # Copier le contenu de fichier1 dans le fichier fusion
        for ligne in fichier1:
            fichier_fusion.write(ligne)

        # Copier le contenu de fichier2 dans le fichier fusion
        for ligne in fichier2:
            fichier_fusion.write(ligne)


def ecrireFichier(nom_fichier, lignes):
    with open(nom_fichier, "w") as fichier:
        for ligne in lignes:
            fichier.write(ligne)


if __name__ == "__main__":
    fusionnerFichiers("employes1.csv", "employes2.csv", "employes_fusion.csv")
    print("Fusion terminée.")
