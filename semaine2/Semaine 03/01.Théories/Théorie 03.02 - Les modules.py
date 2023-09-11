"""Ce cours est sur l'utilisation des modules en python"""

########################################################################################################################
# 03.12 - La fonction 'open'
########################################################################################################################
'''
La fonction open() en Python est utilisée pour ouvrir des fichiers sur le système de fichiers de l'ordinateur. Elle est 
couramment utilisée pour effectuer des opérations de lecture ('r'), d'écriture ('w'), ou de lecture/écriture ('r+') sur 
des fichiers.

    -   La syntaxe de base de la fonction open() est la suivante :

            open(nom_du_fichier, mode)
            
            -   nom_du_fichier : C'est le chemin du fichier que vous souhaitez ouvrir. Il peut être absolu (complet) ou 
                relatif (par rapport au répertoire de travail actuel).
                
            -   mode : C'est une chaîne de caractères indiquant le mode d'ouverture du fichier. Les modes les plus 
                couramment utilisés sont :
                    -   'r' : Lecture (mode par défaut). Ouvre le fichier en lecture seulement.
                    -   'w' : Écriture. Crée un nouveau fichier vide s'il n'existe pas, ou tronque le contenu du fichier 
                              s'il existe.
                    -   'a' : Ajout (append). Ouvre le fichier en écriture, mais ajoute du contenu à la fin du fichier 
                              sans tronquer le contenu existant.
                    -   'x' : Création exclusive. Crée un nouveau fichier, mais génère une erreur si le fichier existe 
                              déjà.
                    -   'b' : Binaire. Ouvre le fichier en mode binaire (par exemple, 'rb' pour la lecture binaire).
                    -   't' : Texte (mode par défaut). Ouvre le fichier en mode texte.
                    
Voici quelques exemples d'utilisation de open() :

    1.  Ouvrir un fichier en mode lecture :
            fichier = open('mon_fichier.txt', 'r')

    2.  Ouvrir un fichier en mode écriture (crée un nouveau fichier ou tronque le contenu s'il existe) :
            fichier = open('nouveau_fichier.txt', 'w')

    3.  Ouvrir un fichier en mode ajout (append) :
            fichier = open('fichier_existant.txt', 'a')

    4.  Ouvrir un fichier binaire en mode lecture :
            fichier = open('image.jpg', 'rb')

Lorsque vous avez terminé de travailler avec le fichier, il est recommandé de le fermer en utilisant la méthode close() 
pour libérer les ressources système associées :
            fichier.close()
'''

########################################################################################################################
# 03.13 - L'instruction 'with'
########################################################################################################################
'''
L'instruction with en Python est utilisée pour créer un contexte géré, ce qui signifie qu'elle établit un contexte 
spécifique pour l'exécution d'un bloc de code. Le contexte géré est généralement associé à des opérations de ressources 
qui doivent être correctement gérées, telles que l'ouverture et la fermeture de fichiers, la gestion de la base de 
données, ou la gestion de ressources réseau.

L'une des principales utilisations de with est d'assurer que les ressources sont correctement nettoyées 
(c'est-à-dire fermées ou libérées) une fois que le bloc de code associé au contexte géré est sorti, même en cas 
d'exception ou d'erreur. Cela permet de garantir une gestion appropriée des ressources et d'éviter les fuites de 
ressources.

    -   La syntaxe générale de with ressemble à ceci :

            with contexte:
                # Code à l'intérieur du contexte
            # À ce stade, le contexte est nettoyé automatiquement
'''

########################################################################################################################
# 03.14 - Utilisation de fichier TXT
########################################################################################################################
'''
1.  Ouvrir un fichier TXT en mode lecture :
Pour ouvrir un fichier TXT en mode lecture (lecture seule), vous pouvez utiliser la fonction open() avec le mode 'r'.
'''


def texte_lecture():
    # Ouvrir le fichier en mode lecture
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_texte.txt', 'r') as fichier:
        contenu = fichier.read()  # Lire tout le contenu du fichier

    print(contenu)  # Afficher le contenu du fichier


'''
2.  Lire les lignes d'un fichier TXT en mode lecture :
Vous pouvez également lire les lignes d'un fichier TXT une par une à l'aide d'une boucle for.
'''


def texte_lecture_ligne():
    # Ouvrir le fichier en mode lecture
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_texte.txt', 'r') as fichier:
        lignes = fichier.readlines()  # Lire toutes les lignes du fichier

    # Parcourir les lignes du fichier et les afficher
    for ligne in lignes:
        print(ligne.strip())  # Utilisez strip() pour supprimer les caractères de nouvelle ligne ('\n')


'''
3.  Écrire dans un fichier TXT en mode écriture :
Pour écrire dans un fichier TXT, ouvrez-le en mode écriture ('w'). 
!!! Attention!!! , cela écrasera le contenu existant du fichier.
'''


def texte_ecriture_ecrase():
    # Ouvrir le fichier en mode écriture
    with open('fichier_texte_w.txt', 'w') as fichier:
        fichier.write("Ceci est une ligne.\n")
        fichier.write("Ceci est une autre ligne.\n")


'''
4.  Ajouter du contenu à un fichier TXT en mode ajout :
Si vous souhaitez ajouter du contenu à un fichier TXT sans effacer le contenu existant, ouvrez-le en mode ajout ('a').
'''


def texte_ecriture_suite():
    # Ouvrir le fichier en mode ajout
    with open('fichier_texte_w.txt', 'a') as fichier:
        fichier.write("Ceci est une nouvelle ligne ajoutée.\n")


'''
En résumé, nous avons utilisé les méthodes suivantes :
    -   read()      : https://www.w3schools.com/python/ref_file_read.asp
    -   readlines() : https://www.w3schools.com/python/ref_file_readlines.asp
    -   strip()     : https://www.w3schools.com/python/ref_string_strip.asp
    -   write()     : https://www.w3schools.com/python/ref_file_write.asp

'''
########################################################################################################################
# 03.15 - Utilisation de fichier CSV
########################################################################################################################
'''
Un module couramment utilisé pour lire des fichiers CSV (Comma-Separated Values) en Python est le module csv. Ce module 
est inclus dans la bibliothèque standard de Python, ce qui signifie qu'il est disponible sans avoir besoin 
d'installation supplémentaire.

Voici comment vous pouvez utiliser le module csv pour lire des fichiers CSV en Python :
'''
# Étape 01 : Importer le module CSV
import csv


def lecture_csv():
    # Étape 02 : Ouvrir le fichier CSV
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_csv.csv', mode='r') as fichier_csv:
        # Étape 03 : Utilisation du lecteur CSV
        lecteur = csv.reader(fichier_csv)
        for ligne in lecteur:
            # Étape 04 : Écriture du fichier CSV
            print(ligne)


'''
1. Exemple plus complet d'utilisation des données.
'''


def utilisation_csv():
    # Ouvrir le fichier CSV en mode lecture
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_csv.csv', 'r', encoding='utf-8') as fichier_csv:
        lecteur = csv.reader(fichier_csv)  # Utilisation de reader pour lire les données en tant que listes

        # Ignorer la première ligne d'en-tête
        next(lecteur)

        # Initialiser une liste pour stocker les jeux vidéo à prix réduit
        jeux_a_prix_reduit = []

        # Parcourir les lignes du fichier CSV
        for ligne in lecteur:
            nom_jeu = ligne[0]  # La première colonne (index 0) contient le nom du jeu
            # La cinquième colonne (index 4) contient le prix en tant que chaîne, nous la convertissons en float
            prix_jeu = float(ligne[4])

            # Vérifier si le prix est inférieur à 50 dollars
            if prix_jeu < 50.0:
                jeux_a_prix_reduit.append(nom_jeu)

    # Afficher les jeux vidéo à prix réduit
    print("Jeux vidéo à moins de 50$ :")
    for jeu in jeux_a_prix_reduit:
        print(jeu)


'''
2.  Exemple d'écriture dans un fichier CSV
'''


def ecriture_csv():
    # Nouvelle données à écrire dans le fichier CSV
    jeux = [
        ['Cyberpunk 2077', 'Action-RPG', '2020', 'PC', '39.99'],
        ['Red Dead Redemption 2', 'Action-Aventure', '2018', 'PlayStation 4', '49.99'],
        ['Fortnite', 'Battle Royale', '2017', 'PC', '5.00'],
        ['Minecraft Dungeons', 'Action-Aventure', '2020', 'Xbox One', '29.99'],
    ]

    # Ouvrir le fichier CSV en mode écriture
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_csv.csv', 'a', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)

        # Tout dépendant du fichier d'écriture, il est possible de devoir ajouter une ligne vide
        writer.writerow([])

        # Écrire les données dans le fichier CSV
        for ligne in jeux:
            writer.writerow(ligne)

    print("Données écrites dans le fichier CSV avec succès.")


'''
En résumé, nous avons utilisé les méthodes/fonctions suivantes :
    -   reader()        :   https://docs.python.org/3/library/csv.html#reader-objects
    -   next()          :   https://www.w3schools.com/python/ref_func_next.asp
    -   csv.writer()    :   https://docs.python.org/3/library/csv.html#writer-objects
    -   writerow()      :   https://docs.python.org/3/library/csv.html#writer-objects
'''

########################################################################################################################
# 03.16 - Utilisation de fichier JSON
########################################################################################################################
'''
Un fichier JSON (JavaScript Object Notation) est un format de données léger et lisible par l'homme utilisé pour stocker 
et échanger des informations structurées. Il est basé sur une notation d'objet en JavaScript, mais il est largement 
utilisé dans divers langages de programmation, y compris Python. Voici quelques caractéristiques importantes des 
fichiers JSON :

    1.  Structure de Données Hiérarchique : Les fichiers JSON permettent de représenter des données structurées sous 
        forme de paires clé-valeur. Ils peuvent contenir des objets JSON imbriqués, ce qui permet de créer des 
        structures de données hiérarchiques complexes.

    2.  Types de Données Pris en Charge : JSON prend en charge plusieurs types de données, notamment les objets, les 
        tableaux, les chaînes de caractères, les nombres, les booléens et les valeurs nulles. Cela le rend adapté à une 
        variété de scénarios de données.

    3.  Facile à Lire et à Écrire : La syntaxe JSON est simple et lisible par l'homme. Les données sont généralement 
        formatées de manière à être facilement compréhensibles. Cela le rend idéal pour les fichiers de configuration, 
        les échanges de données entre serveurs et clients, etc.

    4.  Léger : Les fichiers JSON sont relativement légers en termes de taille de fichier, ce qui les rend efficaces 
        pour le stockage et la transmission de données sur le réseau.

    5.  Compatibilité : JSON est pris en charge par de nombreux langages de programmation, y compris Python, JavaScript, 
        Java, C#, etc. Cela le rend interopérable et largement utilisé dans le développement logiciel.

Un exemple de structure JSON basique ressemble à ceci :

    {
        "nom": "John Doe",
        "age": 30,
        "adresse": {
            "rue": "123 Main Street",
            "ville": "Anytown",
            "pays": "États-Unis"
        },
        "amis": ["Alice", "Bob", "Charlie"]
    }
    
    -   Dans cet exemple, nous avons un objet JSON principal avec des paires clé-valeur. La clé "adresse" contient un 
        objet JSON imbriqué, et la clé "amis" contient un tableau de chaînes de caractères.

Les fichiers JSON sont couramment utilisés pour stocker des données de configuration, des données d'API, des données de 
base de données NoSQL, des journaux de données, et bien plus encore. Leur simplicité et leur polyvalence en font un 
format de données populaire dans le développement de logiciels.

    1.  Exemple pour lire un fichier JSON
'''
import json


def lecture_json():
    # Ouvrir le fichier JSON en mode lecture
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_json.json', 'r') as fichier_json:
        donnees = json.load(fichier_json)

    # Accéder aux données
    print("Nom :", donnees['nom'])
    print("Âge :", donnees['age'])
    print("Ville :", donnees['ville'])


'''
    2.  Exemple pour écrire un fichier JSON
'''


def ecriture_json():
    # Données à écrire
    donnees = {
        "nom": "Bob",
        "age": 32,
        "ville": "New York"
    }

    # Ouvrir le fichier JSON en mode écriture
    with open('fichier_json2.json', 'w') as fichier_json:
        json.dump(donnees, fichier_json)

    # Ouvrir le fichier JSON en mode écriture à la suite
    with open('fichier_json2.json', 'a') as fichier_json:
        json.dump(donnees, fichier_json)

    print("Données écrites dans le fichier JSON.")


'''
    3.  Exemple pour lire et écrire à l'aide d'un fichier JSON complexe.
'''


def lecture_json_complexe():
    # Ouvrir le fichier JSON en mode lecture
    with open('../../../../Downloads/01.Théories (1)/01.Théories/fichier_json_complexe.json', 'r') as fichier_json:
        donnees = json.load(fichier_json)

    # Accès aux données
    personnes = donnees['personnes']
    projets = donnees['projets']

    # Afficher des informations spécifiques
    for personne in personnes:
        print(f"Nom : {personne['nom']}")
        print(f"Âge : {personne['age']}")
        print(f"Ville : {personne['ville']}")
        print()

    for projet, details in projets.items():
        print(f"Projet : {projet}")
        print(f"Nom : {details['nom']}")
        print(f"Technologies : {', '.join(details['technologies'])}")
        print()


def ecriture_json_complexe():
    # Données à écrire dans le fichier JSON
    donnees = {
        "personnes": [
            {
                "nom": "Eva",
                "age": 24,
                "ville": "Berlin"
            },
            {
                "nom": "Charlie",
                "age": 29,
                "ville": "Londres"
            }
        ],
        "projets": {
            "projet3": {
                "nom": "Application de bureau",
                "technologies": ["Python", "Qt"]
            },
            "projet4": {
                "nom": "Application IoT",
                "technologies": ["Arduino", "Python"]
            }
        }
    }

    # Ouvrir le fichier JSON en mode écriture
    # Le paramètre 'indent' définit le nombre d'espaces d'indentation pour formater la sortie
    with open('fichier_json_complexe2.json', 'w') as fichier_json:
        json.dump(donnees, fichier_json, indent=4)

    print("Données écrites dans le fichier JSON complexe.")


'''
En résumé, nous avons utilisé les méthodes/fonctions suivantes :
    -   load()  :   https://www.geeksforgeeks.org/json-load-in-python/
    -   dump()  :   https://www.geeksforgeeks.org/json-dump-in-python/
'''

########################################################################################################################
# 03.00 -
########################################################################################################################
'''
'''

########################################################################################################################
# 03.17 - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    texte_lecture()
    #texte_lecture_ligne()
    #texte_ecriture_ecrase()
    #texte_ecriture_suite()
    #lecture_csv()
    #utilisation_csv()
    #ecriture_csv()
    #lecture_json()
    #ecriture_json()
    #lecture_json_complexe()
    #ecriture_json_complexe()

########################################################################################################################
# 03.18 - Références
########################################################################################################################
'''
https://docs.python.org/fr/3.8/library/stdtypes.html
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming
https://python.sdv.univ-paris-diderot.fr/02_variables/
https://gayerie.dev/docs/python/index.html
'''
