"""
auteur: William bouchard
date: 2023-11-20
But du programme: Gestion de base de données
"""

# ---> Docstring de votre module externe.

import decimal
from sqlite3 import Error

# ---> Importation de vos modules.
from moduleExterneConnexionBD import *

# ---> Fonction de connexion sur mySQL et docstring de votre fonction.
"""
def ConnexionMySQL(NomBD):
    connexion = mysql.connector.connect(host="alex.157-245-242-119.cprapid.com", user="alex_202130861",
        password="W=F~qof1(@==", database=NomBD)
    c = connexion.cursor()
    return c, connexion
"""

# ---> Fonction de connexion sur SQLite.
'''
def ConnexionSQLite(NomBD):
    conn = sqlite3.connect(NomBD)
    c = conn.cursor()
    return c, conn
'''

# ---> Fonction de déconnexion.

'''
def Deconnexion(c, conn):
    c.close()
    conn.close()
'''


# ---> Fonction qui permet la création des tables dans SQLite.


def CreationTablesSQLite():
    # Connexion a la bd sqlite
    c, conn = ConnexionSQLite("streaming.sqlite")
    c.execute("""CREATE TABLE IF NOT EXISTS plateformes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT,
        date_lancement DATE,
        tarif_mensuel NUMERIC(5, 2),
        nombre_utilisateurs INTEGER
    );""")

    c.execute("""CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        saison INTEGER,
        genre TEXT,
        plateforme_id INTEGER,
        date_sortie DATE,
        note NUMERIC(3, 1),
        FOREIGN KEY (plateforme_id) REFERENCES plateformes(id)
    );""")


# ---> Fonction qui permet la lecture des données dans mySQL.

def LectureDonneesMySQL():
    c, conn = ConnexionMySQL("alex_202130861")
    c.execute("""SELECT * FROM plateformes;""")
    for row in c.fetchall():
        print(row)
    c.execute("""SELECT * FROM series;""")
    for row in c.fetchall():
        print(row)
    Deconnexion(c, conn)


# ---> Fonction qui permet l'insertion des données dans SQLite en provenance de mySQL.


def InsertionDonneesMySQLtoSQLite():
    # connexion a la bd mysql
    c_mysql, conn_mysql = ConnexionMySQL("alex_202130861")
    c_mysql.execute("""SELECT * FROM plateformes;""")
    donne_mysql = c_mysql.fetchall()
    Deconnexion(c_mysql, conn_mysql)

    # Connexion à la bd sqlite
    c_sqlite, conn_sqlite = ConnexionSQLite("streaming.sqlite")

    # insertion des donnees dans sqlite
    for row in donne_mysql:
        # Convertir decimal.Decimal en float
        row = list(row)
        for i, item in enumerate(row):
            if isinstance(item, decimal.Decimal):
                row[i] = float(item)
        c_sqlite.execute(
            """INSERT INTO plateformes ( nom, description, date_lancement, tarif_mensuel, nombre_utilisateurs) VALUES ( ?, ?, ?, ?, ?);""",
            row)

    # Commit des donnees vers sqlite
    conn_sqlite.commit()
    Deconnexion(c_sqlite, conn_sqlite)


# ---> Fonction qui permet l'insertion des données dans SQLite en provenance du fichier CSV.

def InsertionDonneesCSVtoSQLite():
    # Connexion a la bd sqlite
    c_sqlite, conn_sqlite = ConnexionSQLite("streaming.sqlite")
    # insertion des donnees dans sqlite
    with open("series_data.csv", "r") as f:
        next(f)
        for line in f:
            row = line.split(",")
            c_sqlite.execute(
                """INSERT INTO series ( nom, saison, genre, plateforme_id, date_sortie, note) VALUES ( ?, ?, ?, ?, ?, ?);""",
                row)
    # Commit des donnees vers sqlite
    conn_sqlite.commit()
    Deconnexion(c_sqlite, conn_sqlite)


# ---> Fonction qui permet la modification d'une donnée dans SQLite.


def modificationDonneesSQLite():
    c, conn = None, None
    try:
        c, conn = ConnexionSQLite("streaming.sqlite")
        # Modification de la table series
        c.execute("""UPDATE series SET nom = '250000000' WHERE nom = 'Fleabag';""")
        conn.commit()
    except Error as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


# ---> Fonction qui permet la suppression d'une donnée dans SQLite.


def suppressionDonneesSQLite():
    c, conn = ConnexionSQLite("streaming.sqlite")
    # Suppression de la table series
    c.execute("""DELETE FROM series WHERE plateforme_id IN (SELECT id FROM plateformes WHERE nom = 'HBO');""")
    # Commit des donnees vers sqlite
    conn.commit()
    # Deconnexion de la bd sqlite
    Deconnexion(c, conn)
