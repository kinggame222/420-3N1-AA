'''
Exercices sur la gestion des erreurs en python.
'''
import json
import logging
import sqlite3

import mysql
import psycopg2
from mysql.connector import OperationalError

########################################################################################################################
# Générale
########################################################################################################################
'''
Pour chaque question :
    -   Faites une recherche sur l'erreur pour en connaitre la définition.
    -   Pour chaque erreur ajouté un message personnalisé à l'écran pour informer l'utilisateur et affichez le code et 
        le nom/message de l'erreur renvoyé par le SGBD.
    -   Créez des cas de tests pour reproduire l'erreur et valider que votre exception est soulevée. Ensuite, dans le 
        fichier : Exercice 10.02 - Cas de tests.xlsx, ajouter les éléments nécessaires pour conserver des traces.
'''

########################################################################################################################
# Question 01 - Module de connexion et déconnexion
########################################################################################################################
'''
Faites une copie de votre module, créé à la semaine 09, pour vous connecter et déconnecter aux base de données. 
Ensuite, faites la gestion des erreurs des sous-classes suivantes :
    -   OperationalError
    -   ProgrammingError
    -   DatabaseError
'''

'''mysql'''


def conn():
    try:
        # Préparez la connexion
        connexion = mysql.connector.connect(host="alex.157-245-242-119.cprapid.com", user="alex_202130861",
                                            password="W=F~qof1(@==", database="alex_202130861")
        curseur = connexion.cursor()
    except mysql.connector.OperationalError as err:
        print("Erreur de connexion à la base de données MySQL : {0}".format(err))
        return None
    except mysql.connector.ProgrammingError as err:
        print("Erreur de programmation MySQL : {0}".format(err))
        return None
    except mysql.connector.DatabaseError as err:
        print("Erreur de base de données MySQL : {0}".format(err))
        return None

    return connexion, curseur


def deconn(connexion):
    try:
        # Fermeture de la connexion
        connexion.close()
    except mysql.connector.OperationalError as err:
        print("Erreur de connexion à la base de données MySQL : {0}".format(err))
        return None
    except mysql.connector.ProgrammingError as err:
        print("Erreur de programmation MySQL : {0}".format(err))
        return None
    except mysql.connector.DatabaseError as err:
        print("Erreur de base de données MySQL : {0}".format(err))
        return None


'''postgresql'''


def postgresql_connexion():
    try:
        '''
        Fonction qui se connecte à la base de données PostgreSQL et qui affiche les résultats d’une requête.
        '''
        connection_params = {'host': "localhost", 'user': "postgres", 'password': "postgres", 'database': "postgres",
                             'port': "5433"}

        connexion = psycopg2.connect(**connection_params)
        curseur = connexion.cursor()
    except psycopg2.OperationalError as err:
        print("Erreur de connexion à la base de données PostgreSQL : {0}".format(err))
        return None
    except psycopg2.ProgrammingError as err:
        print("Erreur de programmation PostgreSQL : {0}".format(err))
        return None
    except psycopg2.DatabaseError as err:
        print("Erreur de base de données PostgreSQL : {0}".format(err))
        return None

    return connexion, curseur


'''sqlite'''''


def sqlite_connexion():
    try:
        connexion = sqlite3.connect("../../semaine9/jeu_video.sqlite")
        curseur = connexion.cursor()
    except sqlite3.OperationalError as err:
        print("Erreur de connexion à la base de données SQLite : {0}".format(err))
        return None
    except sqlite3.ProgrammingError as err:
        print("Erreur de programmation SQLite : {0}".format(err))
        return None
    except sqlite3.DatabaseError as err:
        print("Erreur de base de données SQLite : {0}".format(err))
        return None
    return connexion, curseur


def sqlite_connexionequipe():
    try:
        connexion = sqlite3.connect("../../equipe.sqlite")
        curseur = connexion.cursor()

        return connexion, curseur
    except sqlite3.OperationalError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='w', level=logging.CRITICAL,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.error("Erreur de connexion à la base de données SQLite : {0}".format(err))
        return None

    except sqlite3.ProgrammingError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='w', level=logging.CRITICAL,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.error("Erreur de programmation SQLite : {0}".format(err))
        return None
    except sqlite3.DatabaseError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='w', level=logging.CRITICAL,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.error("Erreur de base de données SQLite : {0}".format(err))
    return None


########################################################################################################################
# Question 02 - La classe ERROR
########################################################################################################################
'''
À partir du code suivant :
    1.  Faites les modifications nécessaires pour l'adapter à votre environnement.
    2.  Faites la gestion des exceptions de la classe suivantes sur les 3 bases de données :
        -   Error
'''


def question_02():
    try:
        # Ouverture des connexions
        db_mysql = conn()
        connexionmysql = db_mysql[0]
        curmysql = db_mysql[1]
        db_sqlite = sqlite_connexion()
        connexionsqlite = db_sqlite[0]
        cursqlite = db_sqlite[1]
        db_postgresql = postgresql_connexion()
        connexionpostgresql = db_postgresql[0]
        curpostgresql = db_postgresql[1]

        #  Le requête sur les base de données
        request = "select * from jeux_video"

        # Traitement de mySQL
        print("---------- Affichage de mySQL ----------")
        with connexionmysql.cursor() as c:
            c.execute(request)
            resultats = c.fetchall()
            for jeu in resultats:
                print(str(jeu[0]) + ' ' + jeu[1] + ' ' + str(jeu[2]) + ' ' + jeu[3] + ' ' + jeu[4] + ' ' + str(jeu[5]))

        # Traitement de SQLite

        cursqlite.execute(request)
        resultats = cursqlite.fetchall()
        cursqlite.close()

        print("---------- Affichage de SQLite ----------")
        for jeu in resultats:
            print(str(jeu[0]) + ' ' + jeu[1] + ' ' + str(jeu[2]) + ' ' + jeu[3] + ' ' + jeu[4] + ' ' + str(jeu[5]))

        # Traitement de postgreSQL
        print("---------- Affichage de postgreSQL ----------")
        with curpostgresql as c:
            c.execute(request)
            resultats = c.fetchall()
            for jeu in resultats:
                print(str(jeu[0]) + ' ' + jeu[1] + ' ' + str(jeu[2]) + ' ' + jeu[3] + ' ' + jeu[4] + ' ' + str(jeu[5]))

        # Fermeture des connexions
        connexionmysql.close()
        connexionsqlite.close()
        connexionpostgresql.close()
    except mysql.connector.Error as err:
        print("Erreur de connexion à la base de données MySQL : {0}".format(err))
        return None
    except sqlite3.Error as err:
        print("Erreur de connexion à la base de données SQLite : {0}".format(err))
        return None
    except psycopg2.Error as err:
        print("Erreur de connexion à la base de données PostgreSQL : {0}".format(err))
        return None


########################################################################################################################
# Question 03 - SELECT, INSERT, UPDATE et DELETE avec SQLite
########################################################################################################################
'''
Documentation : https://docs.python.org/3/library/sqlite3.html#exceptions

Créez une requête pour chaque type et faites la gestion des erreurs des sous-classes suivantes :
    -   DataError
    -   IntegrityError
    -   ProgrammingError
'''


def reqsqlite():
    try:

        db_sqlite = sqlite_connexion()
        connexionsqlite = db_sqlite[0]
        cursqlite = db_sqlite[1]

        request = "select * from jeux_video"

        requast_insert = "INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) VALUES  ('bob', 2017, 'Action-RPG', 'Nintendo Switch', 9.5)"

        requast_update = "UPDATE jeux_video SET note = 10 WHERE titre= 'bob'"

        requast_delete = "DELETE FROM jeux_video WHERE titre = 'bob'"

        try:
            cursqlite.execute(requast_insert)
            connexionsqlite.commit()
        except sqlite3.DataError as err:
            print("Erreur dans les donné : {0}".format(err))
            return None
        except sqlite3.IntegrityError as err:
            print("Erreur d'intégrité : {0}".format(err))
            return None
        except sqlite3.ProgrammingError as err:
            print("Erreur de programmation SQLite : {0}".format(err))
            return None

        try:
            cursqlite.execute(requast_update)
            connexionsqlite.commit()
        except sqlite3.DataError as err:
            print("Erreur dans les donné : {0}".format(err))
            return None
        except sqlite3.IntegrityError as err:
            print("Erreur d'intégrité : {0}".format(err))
            return None
        except sqlite3.ProgrammingError as err:
            print("Erreur de programmation SQLite : {0}".format(err))
            return None

        try:
            cursqlite.execute(requast_delete)
            connexionsqlite.commit()
        except sqlite3.DataError as err:
            print("Erreur dans les donné : {0}".format(err))
            return None
        except sqlite3.IntegrityError as err:
            print("Erreur d'intégrité : {0}".format(err))
            return None
        except sqlite3.ProgrammingError as err:
            print("Erreur de programmation SQLite : {0}".format(err))
            return None
        try:
            cursqlite.execute(request)
            connexionsqlite.commit()

        except sqlite3.DataError as err:
            print("Erreur dans les donné : {0}".format(err))
            return None
        except sqlite3.IntegrityError as err:
            print("Erreur d'intégrité : {0}".format(err))
            return None
        except sqlite3.ProgrammingError as err:
            print("Erreur de programmation SQLite : {0}".format(err))
            return None
        resultats = cursqlite.fetchall()
        print("---------- Affichage de SQLite ----------")
        for jeu in resultats:
            print(str(jeu[0]) + ' ' + jeu[1] + ' ' + str(jeu[2]) + ' ' + jeu[3] + ' ' + jeu[4] + ' ' + str(jeu[5]))
    except sqlite3.OperationalError as err:
        print("Erreur de connexion à la base de données SQLite : {0}".format(err))
        return None
    except sqlite3.ProgrammingError as err:
        print("Erreur de programmation SQLite : {0}".format(err))
        return None
    except sqlite3.DatabaseError as err:
        print("Erreur de base de données SQLite : {0}".format(err))
        return None


########################################################################################################################
# Question 04 - SELECT, INSERT, UPDATE et DELETE avec MySQL
########################################################################################################################
'''
Documentation : https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors.html

Créez une requête pour chaque type et faites la gestion des erreurs des sous-classes suivantes :
    -   DataError
    -   IntegrityError
    -   ProgrammingError
'''


def reqMysql():
    try:
        db_mysql = conn()
        connexionmysql = db_mysql[0]
        curmysql = db_mysql[1]

        request = "select * from jeux_video"

        try:
            curmysql.execute(
                "INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) VALUES (%s, %s, %s, %s, %s)",
                ('bob', 2017, 'Action-RPG', 'Nintendo Switch', 9.5))
            connexionmysql.commit()
        except mysql.connector.DataError as err:
            print("Erreur dans les donné : {0}".format(err))
            return None
        except mysql.connector.IntegrityError as err:
            print("Erreur d'intégrité : {0}".format(err))
            return None
        except mysql.connector.ProgrammingError as err:

            print("Erreur de programmation MySQL : {0}".format(err))
            return None

        curmysql.execute("UPDATE jeux_video SET note = 10 WHERE titre= 'bob'")
        connexionmysql.commit()

        curmysql.execute("DELETE FROM jeux_video WHERE titre = 'bob1'")
        connexionmysql.commit()

        curmysql.execute(request)

        resultats = curmysql.fetchall()

        print("---------- Affichage de MySQL ----------")
        for jeu in resultats:
            print(str(jeu[0]) + ' ' + jeu[1] + ' ' + str(jeu[2]) + ' ' + jeu[3] + ' ' + jeu[4] + ' ' + str(jeu[5]))
    except mysql.connector.OperationalError as err:
        print("Erreur de connexion à la base de données MySQL : {0}".format(err))
        return None
    except mysql.connector.ProgrammingError as err:
        print("Erreur de programmation MySQL : {0}".format(err))
        return None
    except mysql.connector.DatabaseError as err:
        print("Erreur de base de données MySQL : {0}".format(err))
        return None


########################################################################################################################
# Question 05 - SELECT, INSERT, UPDATE et DELETE avec PostgreSQL
########################################################################################################################
'''
Documentation : https://www.psycopg.org/docs/errors.html

Créez une requête pour chaque type et faites la gestion des erreurs des sous-classes suivantes :     
    -   DataError
    -   IntegrityError
    -   ProgrammingError
'''


def reqpostgresql():
    try:
        db_postgresql = postgresql_connexion()
        connexionpostgresql = db_postgresql[0]
        curpostgresql = db_postgresql[1]

        request = "select * from jeux_video"

        try:
            curpostgresql.execute(
                "INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) VALUES (%s, %s, %s, %s, %s)",
                ('bob', 2017, 'Action-RPG', 'Nintendo Switch', 9.5))
            connexionpostgresql.commit()
        except psycopg2.DataError as err:
            print("Erreur dans les donné : {0}".format(err))
            return None
        except psycopg2.IntegrityError as err:
            print("Erreur d'intégrité : {0}".format(err))
            return None
        except psycopg2.ProgrammingError as err:

            print("Erreur de programmation PostgreSQL : {0}".format(err))
            return None

        curpostgresql.execute("UPDATE jeux_video SET note = 10 WHERE titre= 'bob'")
        connexionpostgresql.commit()

        curpostgresql.execute("DELETE FROM jeux_video WHERE titre = 'bob1'")
        connexionpostgresql.commit()

        curpostgresql.execute(request)

        resultats = curpostgresql.fetchall()

        print("---------- Affichage de PostgreSQL ----------")
        for jeu in resultats:
            print(str(jeu[0]) + ' ' + jeu[1] + ' ' + str(jeu[2]) + ' ' + jeu[3] + ' ' + jeu[4] + ' ' + str(jeu[5]))
    except psycopg2.OperationalError as err:
        print("Erreur de connexion à la base de données PostgreSQL : {0}".format(err))
        return None
    except psycopg2.ProgrammingError as err:
        print("Erreur de programmation PostgreSQL : {0}".format(err))
        return None
    except psycopg2.DatabaseError as err:
        print("Erreur de base de données PostgreSQL : {0}".format(err))
        return None


########################################################################################################################
# Question 06 - Fichier CSV
########################################################################################################################
'''
Documentation : https://docs.python.org/3/library/csv.html

Faites une copie de la question #04 de l'exercice 9.
Ensuite, pour la partie sur le fichier CSV, faites la gestion des erreurs des sous-classes suivantes :
    -   FileNotFoundError
    -   Error 
'''


def mysqlinsert():
    '''
    Fonction qui se connecte à la base de données MySQL et qui affiche les résultats d’une requête.
    '''
    try:
        # Préparez la connexion
        connexion = conn()[0]
        curseur = conn()[1]
        # insertion des données

        with open('hockey.csva', 'r') as f:
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
    except mysql.connector.Error as err:
        print("Erreur de connexion à la base de données MySQL : {0}".format(err))
        return None
    except FileNotFoundError as err:
        print("Erreur de fichier non trouvé : {0}".format(err))
        return None


########################################################################################################################
# Question 07 - Fichier JSON
########################################################################################################################
'''
Documentation : https://docs.python.org/3/library/json.html

Faites une copie de la question #05 de l'exercice 9.
Ensuite, pour la partie sur le fichier JSON, faites la gestion des erreurs des sous-classes suivantes :
    -   JSONDecodeError
    -   IndexError/KeyError
    -   ValueError
    -   TypeError
    -   AttributeError
'''


def fichierJson():
    try:
        # Préparez la connexion

        curseur = postgresql_connexion()[1]
        connexion = postgresql_connexion()[0]
        d = []
        with open('../semaine9/02.Exercices/hockey.json', 'r') as f:
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

    except psycopg2.Error as err:
        print("Erreur de connexion à la base de données PostgreSQL : {0}".format(err))
        return None
    except json.JSONDecodeError as err:
        print("Erreur de décodage JSON : {0}".format(err))
        return None
    except IndexError as err:
        print("Erreur d'index : {0}".format(err))
        return None
    except KeyError as err:
        print("Erreur de clé : {0}".format(err))
        return None
    except ValueError as err:
        print("Erreur de valeur : {0}".format(err))
        return None
    except TypeError as err:
        print("Erreur de type : {0}".format(err))
        return None
    except AttributeError as err:
        print("Erreur d'attribut : {0}".format(err))
        return None


########################################################################################################################
# Question 08 - Gestionnaire de hockey
########################################################################################################################
'''
Faites une copie du gestionnaire de hockey dont vous avez évolué le code à la semaine 09.
    1.  Ajoutez une gestion des exceptions aux endroits nécessaires.
    2.  Ajoutez une gestion de LOGGING selon les critères suivants:
        -   Sauvegardez les logs dans un fichier qui se nomme : Exercice 10.03 - logs.txt
        -   Formatez le message d'écriture sous le format : "asctime | levelname | name | message"
        -   Acceptez seulement les level à partir de Warning
        -   Voici la gestion des levels:
            -   Critical : Tout ce qui touche la connexion/déconnexion au BD. Affichez l'erreur reçue par le système.
            -   Error   : Toutes les autres manipulations avec la BD. Affichez l'erreur reçu par le système.
            -   Warning : Lorsqu'un utilisateur essaie d'ajouter un joueur déjà existant, modifier un joueur qui 
                          n'existe pas et supprimer un joueur qui n'existe pas.
'''


def verifier_existence_joueur(curseur, nom_joueur):
    try:
        # Vérifier si le joueur existe déjà
        curseur.execute("SELECT * FROM equipe WHERE nom = ?", (nom_joueur,))
        if curseur.fetchone() is None:
            return False
        return True
    except sqlite3.Error as err:
        print("Erreur dans la véfication : {0}".format(err))
        return None


def ajouter_joueur(connexion, curseur):
    try:
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

    except sqlite3.Error as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='w', level=logging.WARNING,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.warning("Erreur dans l'ajout d'un joueur : {0}".format(err))
        return None


def supprimer_joueur(connexion, curseur):
    try:
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

    except sqlite3.Error as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='w', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info("Erreur dans la suppression d'un joueur : {0}".format(err))

    return None


def afficher_equipe(curseur):
    try:
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

    except sqlite3.Error as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='w', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info("Erreur dans l'affichage de l'équipe : {0}".format(err))

        return None


def modifier_joueur(connexion, curseur):
    try:
        # Demander le nom du joueur à modifier
        nom_joueur = input("Nom du joueur à modifier : ")

        # Vérifier si le joueur existe
        if not verifier_existence_joueur(curseur, nom_joueur):
            print("Le joueur n'existe pas.")
            return

        # Demander les détails du joueur à l'utilisateur
        nom = input("Nom du joueur : ")
        position = input("Position du joueur : ")
        equipe = input("Équipe du joueur : ")

        # Modifier le joueur dans la BD equipe
        modification_joueur = "UPDATE equipe SET nom = ?, position = ?, equipe = ? WHERE nom = ?"
        curseur.execute(modification_joueur, (nom, position, equipe, nom_joueur))
        connexion.commit()

        print(f"Le joueur {nom_joueur} a été modifié.")

    except sqlite3.DatabaseError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='a', level=logging.CRITICAL,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.CRITICAL("Erreur dans la modification d'un joueur : {0}".format(err))

        return None

    except sqlite3.ProgrammingError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info("Erreur dans la modification d'un joueur : {0}".format(err))

        return None

    except sqlite3.IntegrityError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info("Erreur dans la modification d'un joueur : {0}".format(err))

        return None

    except sqlite3.DataError as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info("Erreur dans la modification d'un joueur : {0}".format(err))

        return None

    except sqlite3.Error as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='a', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info("Erreur dans la modification d'un joueur : {0}".format(err))

        return None
    except sqlite3.Warning as err:
        logging.basicConfig(filename='Exercice 10.03 - logs.txt', filemode='a', level=logging.WARNING,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.WARNING("Erreur dans la modification d'un joueur : {0}".format(err))

        return None


def getsionnaire():
    try:  # Ouvrir la connexion et obtenir le curseur
        connexion, curseur = sqlite_connexionequipe()
        curseur.execute("CREATE TABLE IF NOT EXISTS equipe (nom TEXT, position TEXT, equipe TEXT)")

        while True:
            # Afficher le menu et obtenir le choix de l'utilisateur
            print("1. Ajouter un joueur")
            print("2. Supprimer un joueur")
            print("3. Afficher l'équipe")
            print("4. Modifier un joueur")
            print("5. Quitter")
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

                modifier_joueur(connexion, curseur)
                pass

            elif choix == "5":
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

        # Fermer la connexion à la fin du programme
        connexion.close()
    except sqlite3.Error as err:
        print("Erreur dans la gestion de l'équipe : {0}".format(err))
        return None


########################################################################################################################
# Exécution du code
########################################################################################################################
if __name__ == "__main__":
    getsionnaire()
    print("X")
