'''
Question 05 – Lecture HTML

À l’aide de requests, conservez le code HTML de la page d’accueil du
site www.rds.ca dans un fichier html. Faites une vérification du code de statut,
 afin qu’il soit à 200 avant de faire l’écriture dans le fichier.

'''
import requests


def lireHtml(url, nom_fichier):
    reponse = requests.get(url)
    print(reponse.status_code)
    if reponse.status_code == 200:
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.write(reponse.text)
    else:
        print("Erreur lors de la lecture de la page.")


if __name__ == "__main__":
    lireHtml("https://www.rds.ca/", "rds.html")
    print("Lecture terminée.")