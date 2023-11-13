'''
Vous devez isoler les fonctions de connexion et déconnexion dans un module externe et en faire son utilisation.
-	Base de données : MySQL, PostgreSQL et SQLite;
-	Manipulations :
o	Les 4 fonctions doivent se retrouver dans un seul module;
o	Ajoutez le Docstring à votre nouveau module;
o	Inscrivez, dans votre fichier de réponse, comment accéder à la documentation du Docstring de votre nouveau module;
o	Vous devez importer ce module dans votre fichier de réponse de l’exercice.
o	Dans une seule fonction, à l’aide de votre nouveau module, connectez-vous aux bases de données, affichez la totalité des jeux et déconnectez-vous aux bases de données.

'''
import sqlite3
import mysql.connector

import psycopg2


def conn():
    # Préparez la connexion
    connexion = mysql.connector.connect(
        host="alex.157-245-242-119.cprapid.com",
        user="alex_202130861",
        password="W=F~qof1(@==",
        database="alex_202130861")
    curseur = connexion.cursor()

    return connexion, curseur


def deconn(connexion):
    # Fermeture de la connexion
    connexion.close()





def postgresql_connexion():
    '''
    Fonction qui se connecte à la base de données PostgreSQL et qui affiche les résultats d’une requête.
    '''
    connection_params = {
        'host': "localhost",
        'user': "postgres",
        'password': "postgres",
        'database': "postgres",
        'port': "5433"
    }

    connexion = psycopg2.connect(**connection_params)
    curseur = connexion.cursor()

    return connexion, curseur


def sqlite_connexion():
    connexion = sqlite3.connect("hockey.sqlite")
    curseur = connexion.cursor()

    return connexion, curseur

def sqlite_connexionequipe():
    connexion = sqlite3.connect("../../equipe.sqlite")
    curseur = connexion.cursor()

    return connexion, curseur
