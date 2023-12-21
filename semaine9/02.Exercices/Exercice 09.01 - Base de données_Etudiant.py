'''
Exercices sur les bases de données en python.
'''
import csv
import json

########################################################################################################################
# Importation des modules
########################################################################################################################

########################################################################################################################
# Question 01
########################################################################################################################
'''
Vous devez créer une fonction qui recevra un nom d’usager et qui affichera les résultats d’une requête :
-	Base de données : MySQL;
-	Manipulations :
o	Préparez la connexion;
o	Lisez la totalité de la table jeux_video;
o	Affichez la totalité de la table dans la console.

'''


def mysql_connexion():
    '''
    Fonction qui se connecte à la base de données MySQL et qui affiche les résultats d’une requête.
    '''
    # Préparez la connexion
    connexion = moduleExterne.conn()[0]
    curseur = moduleExterne.conn()[1]

    # Lisez la totalité de la table jeux_video
    curseur.execute("SELECT * FROM jeux_video")

    # Affichez la totalité de la table dans la console
    for ligne in curseur:
        print(ligne)

    # Fermeture de la connexion
    connexion.close()


########################################################################################################################
# Question 02
########################################################################################################################
'''
Pour chaque base de données, vous devez isoler la connexion et la déconnexion dans des fonctions.
-	Base de données : MySQL, PostgreSQL et SQLite;
-	Manipulations :
o	Les fonctions de connexion reçoivent le nom de la base de données ou du fichier en paramètre;
o	La fonction de déconnexion reçoit l’objet de connexion en paramètre;
o	Reproduisez la question 1 à l’aide d’une fonction pour chaque base de données et assurez-vous d’utiliser vos nouvelles fonctions de connexion et déconnexion.

'''


def postgresqlconn():
    connection_params = {'host': "localhost", 'user': "postgres", 'password': "postgres", 'database': "postgres", }

    with moduleExterne.mysqlconn(**connection_params) as db:
        # C'est ici que nous pouvons faire des manipulations avec la connexion.
        connexion, curseur = moduleExterne.conn()

        # Lisez la totalité de la table jeux_video
        curseur.execute("SELECT * FROM jeux_video")

        # Affichez la totalité de la table dans la console
        for ligne in curseur:
            print(ligne)

        pass
    moduleExterne.deconn(connexion)


########################################################################################################################
# Question 03
########################################################################################################################
import moduleExterne
from moduleExterne import *

########################################################################################################################
# Question 04
########################################################################################################################
'''
À partir du fichier hockey.csv, insérez les données dans une table.
-	Base de données : MySQL;
-	Manipulations :
o	Préparez votre base de données;
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour insérer les données dans votre nouvelle table;
o	Affichez les données que vous insérez à la console.

'''


def mysqlinsert():
    '''
    Fonction qui se connecte à la base de données MySQL et qui affiche les résultats d’une requête.
    '''
    # Préparez la connexion
    connexion = moduleExterne.mysqlconn()[0]
    curseur = moduleExterne.mysqlconn()[1]
    # insertion des données
    curseur.execute(
        "CREATE TABLE IF NOT EXISTS Hockey (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(50),equipe VARCHAR(50),"
        "Buts INT,Passe INT,Point INT)")

    with open('hockey.csv', 'r') as f:
        next(f)
        test = f.read().strip().split('\n')
        for i in test:
            i = i.split(',')
            curseur.execute("INSERT INTO Hockey (nom, equipe, Buts, Passe, Point) VALUES (%s, %s, %s, %s, %s)",
                            (i[0], i[1], i[2], i[3], i[4]))

    connexion.commit()

    # Affichez la totalité de la table dans la console

    curseur.execute("SELECT * FROM Hockey")
    for ligne in curseur:
        print(ligne)

    # Fermeture de la connexion
    connexion.close()


########################################################################################################################
# Question 05
########################################################################################################################
'''
À partir du fichier hockey.json, insérez les données dans une table.
-	Base de données : PostgreSQL;
-	Manipulations :
o	Préparez votre base de données;
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour insérer les données dans votre nouvelle table;
o	Affichez les données que vous insérez à la console.

'''


def insert_postgresql():
    # Préparez la connexion

    curseur = postgresql_connexion()[1]
    connexion = postgresql_connexion()[0]

    # insertion des données
    # curseur.execute(
    # "CREATE TABLE if not exists  Hockey (id SERIAL PRIMARY KEY,nom VARCHAR(50),equipe VARCHAR(50),Buts INT,Passe INT,Point INT)")
    d = []
    with open('hockey.json', 'r') as f:
        test = json.load(f)

        req = "INSERT INTO hockeyV3 (nom, equipe, buts, passes, points) VALUES (%s, %s, %s, %s, %s)"

        for i in test:
            d = (i['Nom'], i['Equipe'], i['Buts'], i['Passes'], i['Points'])
            print(d)
            curseur.execute(req, d)
            connexion.commit()
            curseur.execute("SELECT * FROM hockeyV3")
            c = curseur.fetchall()
            print(c)

        print(f"Nombre de lignes insérées : {curseur.rowcount}")


########################################################################################################################
# Question 06
########################################################################################################################
'''
À partir du fichier hockey.txt, insérez les données dans une table.
-	Base de données : SQLite;
-	Manipulations :
o	Préparez votre base de données;
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour insérer les données dans votre nouvelle table;
o	Affichez les données que vous insérez à la console.

'''


def insert_sqlite():
    # Prepare the connection
    connexion, curseur = sqlite_connexion()

    # Insert data from the CSV file
    with open('hockey.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            nom, equipe, Buts, Passe, Point = row
            curseur.execute("INSERT INTO Hockey (nom, equipe, Buts, Passe, Point) VALUES (?, ?, ?, ?, ?)",
                            (nom, equipe, Buts, Passe, Point))

    connexion.commit()
    connexion.close()


########################################################################################################################
# Question 07
########################################################################################################################
'''
À partir du fichier hockey_update.csv, modifiez les données dans une table.

- Base de données : MySQL;

- Manipulations :

o Réutilisez le module externe;

o Faites toutes les manipulations nécessaires pour modifier les données dans la bonne table;

o Affichez les données que vous modifiez à la console.
'''


def mysqlupdate():
    # Préparez la connexion
    connexion = moduleExterne.conn()[0]
    curseur = connexion.cursor()

    with open('hockey_update.csv', 'r') as f:
        next(f)
        test = f.read().strip().split('\n')
        for i in test:
            i = i.split(',')

            curseur.execute("UPDATE Hockey SET Point = %s WHERE nom = %s", (i[1], i[0]))

    connexion.commit()

    # Affichez la totalité de la table dans la console

    curseur.execute("SELECT * FROM Hockey")
    for ligne in curseur:
        print(ligne)

    # Fermeture de la connexion
    connexion.close()


########################################################################################################################
# Question 08
########################################################################################################################
'''
À partir du fichier hockey_update.json, modifiez les données dans une table.

- Base de données : PostgreSQL;

- Manipulations :

o Créez une fonction de type « one-shot » qui modifiera la structure de votre table PostgreSQL pour accepter un nouveau champ qui provient de votre fichier.

o Dans une autre fonction :

§ Réutilisez le module externe;

§ Faites toutes les manipulations nécessaires pour modifier les données dans la bonne table;

§ Affichez les données que vous modifiez à la console.
'''


def update_postgresql():
    connexion = postgresql_connexion()[0]
    curseur = connexion.cursor()
    # insertion des données
    try:
        curseur.execute("ALTER TABLE hockeyv3 ADD COLUMN position VARCHAR(50)")
    except:
        pass
    connexion.commit()
    with open('hockey_update.json', 'r') as f:
        test = json.load(f)

        for i in test:
            d = (i['Nom'], i['Position'])
            print(d)
            curseur.execute(
                "UPDATE hockeyv3 SET position = %s WHERE nom = %s",
                (i['Position'], i['Nom'])
            )
            print(f"Joueur {i['Nom']} mis à jour avec la position {i['Position']}")

        connexion.commit()

        curseur.execute("SELECT * FROM hockeyv3")


########################################################################################################################
# Question 09
########################################################################################################################
'''
À partir du fichier hockey_update.txt, modifiez les données dans une table.
-	Base de données : SQLite;
-	Manipulations :
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour modifier les données dans la bonne table;
o	Affichez les données que vous modifiez à la console.

'''


def update_sqlite():
    # Prepare the connection
    connexion, curseur = sqlite_connexion()

    curseur.execute("ALTER TABLE Hockey ADD COLUMN position VARCHAR(50)")

    with open('hockey_update.txt', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            nom, equipe, Buts, Passe, Point, position = row
            curseur.execute("INSERT INTO Hockey (nom, equipe, Buts, Passe, Point, position) VALUES (?, ?, ?, ?, ?, ?)",
                            (nom, equipe, Buts, Passe, Point, position))

    connexion.commit()

    connexion.close()


########################################################################################################################
# Question 10
########################################################################################################################
'''
Supprimez le joueur qui a 155 passes de la table.
-	Base de données : MySQL;
-	Manipulations :
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour modifier les données dans la bonne table;
o	Affichez les données que vous supprimez à la console.

'''


def mysqldelete():
    # Préparez la connexion
    connexion = moduleExterne.mysqlconn()[0]
    curseur = moduleExterne.mysqlconn()[1]

    dlt = "DELETE FROM Hockey WHERE Passe = 155"
    curseur.execute(dlt)
    connexion.commit()

    # Affichez la totalité de la table dans la console

    curseur.execute("SELECT * FROM Hockey")
    for ligne in curseur:
        print(ligne)

    # Fermeture de la connexion
    connexion.close()


########################################################################################################################
# Question 11
########################################################################################################################
'''
Supprimez les joueurs qui sont des défenseurs de la table.
-	Base de données : PostgreSQL;
-	Manipulations :
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour modifier les données dans la bonne table;
o	Affichez les données que vous supprimez à la console.

'''


def SuprimmerPost():
    # Préparez la connexion
    connexion = moduleExterne.postgresql_connexion()[0]
    curseur = moduleExterne.postgresql_connexion()[1]

    dlt = "DELETE FROM Hockey WHERE position = 'Defenseur'"
    curseur.execute(dlt)
    connexion.commit()

    curseur.execute("SELECT * FROM Hockey")
    for ligne in curseur:
        print(ligne)

    # Fermeture de la connexion
    connexion.close()


########################################################################################################################
# Question 12
########################################################################################################################
'''
Supprimez le joueur qui s’appelle « Paul Coffey » de la table.
-	Base de données : SQLite;
-	Manipulations :
o	Réutilisez le module externe;
o	Faites toutes les manipulations nécessaires pour modifier les données dans la bonne table;
o	Affichez les données que vous supprimez à la console.

'''


def SuprimmerSqlite():
    connexion, curseur = sqlite_connexion()

    det = "DELETE FROM Hockey WHERE nom = 'Ron Francis'"
    curseur.execute(det)

    curseur.execute("SELECT * FROM Hockey")
    deleted_data = curseur.fetchall()
    for ligne in deleted_data:
        print(ligne)

    connexion.commit()
    connexion.close()


########################################################################################################################
# Question 13
########################################################################################################################
'''
Vous devez refaire le gestionnaire de hockey que vous avez fait en Semaine 02.
-	Base de données : SQLite;
-	Manipulations :
o	Utilisation d'un nouveau fichier SQLITE pour la création de l'équipe :
	Créez un nouveau fichier de base de données : equipe.sqlite;
	Créez une fonction, de style « one-shot », pour créer la structure de la table pour recevoir les données.
o	La gestion des joueurs se fait maintenant avec la BD equipe.
o	Vous devez optimiser votre code en utilisation des fonctions:
	Utilisez les fonctions existantes dans votre module externe pour l'ouverture et fermeture de la BD;
	Une fonction pour chaque option du menu.
	Votre connexion et la déclaration de votre curseur se font dans le programme principal.
	Vous devez créer une fonction pour faire la vérification de l'existence d'un joueur dans la BD. Ajoutez cette fonction dans le module externe et utilisez-la pour les options : 3, 4 et 6.

'''


def verifier_existence_joueur(curseur, nom_joueur):
    curseur.execute("SELECT * FROM equipe WHERE nom = ?", (nom_joueur,))
    if curseur.fetchone() is None:
        return False
    return True


def ajouter_joueur(connexion, curseur):
    # Demander les détails du joueur à l'utilisateur
    nom = input("Nom du joueur : ")
    position = input("Position du joueur : ")
    equipe = input("Équipe du joueur : ")

    # Vérifier si le joueur existe déjà
    if verifier_existence_joueur(curseur, nom):
        print("Le joueur existe déjà.")
        return

    # Ajouter le joueur dans la BD equipe
    ajout_joueur = "INSERT INTO equipe (nom, position, equipe) VALUES (?, ?, ?)"
    curseur.execute(ajout_joueur, (nom, position, equipe))
    connexion.commit()

    print(f"Le joueur {nom} a été ajouté à l'équipe.")


def supprimer_joueur(connexion, curseur):
    # Demander le nom du joueur à supprimer
    nom_joueur = input("Nom du joueur à supprimer : ")

    # Vérifier si le joueur existe
    if not verifier_existence_joueur(curseur, nom_joueur):
        print("Le joueur n'existe pas.")
        return

    # Supprimer le joueur de la BD equipe
    suppression_joueur = "DELETE FROM equipe WHERE nom = ?"
    curseur.execute(suppression_joueur, (nom_joueur,))
    connexion.commit()

    print(f"Le joueur {nom_joueur} a été supprimé de l'équipe.")


def afficher_equipe(curseur):
    # Sélectionner tous les joueurs de la BD equipe
    selection_equipe = "SELECT * FROM equipe"
    curseur.execute(selection_equipe)
    equipe = curseur.fetchall()

    if not equipe:
        print("L'équipe est vide.")
    else:
        print("Liste des joueurs dans l'équipe :")
        for joueur in equipe:
            print(f"{joueur[0]} - {joueur[1]} - {joueur[2]}")


def getsionnaire():
    # Ouvrir la connexion et obtenir le curseur
    connexion, curseur = sqlite_connexionequipe()
    curseur.execute("CREATE TABLE IF NOT EXISTS equipe (nom TEXT, position TEXT, equipe TEXT)")

    while True:
        # Afficher le menu et obtenir le choix de l'utilisateur
        print("1. Ajouter un joueur")
        print("2. Supprimer un joueur")
        print("3. Afficher l'équipe")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_joueur(connexion, curseur)
            pass
        elif choix == "2":
            supprimer_joueur(connexion, curseur)
            pass
        elif choix == "3":
            afficher_equipe(curseur)
            pass
        elif choix == "4":

            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

    # Fermer la connexion à la fin du programme
    connexion.close()


if __name__ == '__main__':
    getsionnaire()
