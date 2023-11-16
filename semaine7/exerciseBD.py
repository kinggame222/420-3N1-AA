import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE if not exists employe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        adresse TEXT,
        ville TEXT,
        telephone TEXT,
        dateNaissance TEXT,
        salaire INTEGER,
        dispo TEXT
    )
''')

cursor.execute('''

        CREATE TABLE if not exists Emp (
                 Usager TEXT,
              MotDePasse TEXT
              
               )''')

cursor.execute('''
    INSERT INTO Emp (Usager, MotDePasse)
    VALUES ('etudiant','12345')
''')



def versBd(connexion, curseur):
    # Connexion à la base de données SQLite

    # Ouverture et chargement du fichier JSON
    with open('../Semaine 11/02.Exercices/Exercice 11.01 - employe.json', 'r') as fichier:
        donnees = json.load(fichier)

    # Insertion des données dans la table
    for cle, valeur in donnees.items():
        dispo = ','.join(map(str, valeur['dispo']))  # Conversion de la liste en chaîne de caractères
        curseur.execute('''
            INSERT INTO employe (nom, adresse, ville, telephone, dateNaissance, salaire, dispo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (valeur['nom'], valeur['adresse'], valeur['ville'], valeur['telephone'], valeur['dateNaissance'],
              valeur['salaire'], dispo))

    # Validation des modifications et fermeture de la connexion
    connexion.commit()
    connexion.close()


# Appel de la fonction
versBd(conn, cursor)

conn.close()
