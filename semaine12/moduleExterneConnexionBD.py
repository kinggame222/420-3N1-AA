"""
auteur: William bouchard
date: 2023-11-20
but du programme: Gestion de base de données
"""

import sqlite3

import mysql.connector


def ConnexionSQLite(NomBD):
    conn = sqlite3.connect(NomBD)
    c = conn.cursor()
    return c, conn


def Deconnexion(c, conn):
    c.close()
    conn.close()


def ConnexionMySQL(NomBD):
    connexion = mysql.connector.connect(host="alex.157-245-242-119.cprapid.com", user="alex_202130861",
                                        password="W=F~qof1(@==", database=NomBD)

    c = connexion.cursor()
    return c, connexion
