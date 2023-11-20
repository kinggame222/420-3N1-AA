"""
auteur: William bouchard
date: 2023-11-20
but du programme: Gestion de base de données
"""

# ---> Commandes pour la création de votre base de données : streaming.sqlite
# cd C:\Users\202130861\420-3N1-AA\semaine12
# sqlite3 streaming.sqlite
# databases = pour vériier que la base de données a été créée.


from e202130861_bd import *

if __name__ == "__main__":
    # Création des tables dans SQLite.
    CreationTablesSQLite()
    try:
        InsertionDonneesMySQLtoSQLite()
        InsertionDonneesCSVtoSQLite()
    except Exception as e:
        print(f"Une erreur s'est produite dans l'insertion des données : {e}")
    finally:
        modificationDonneesSQLite()
        suppressionDonneesSQLite()

    print('Sommatif 3')
