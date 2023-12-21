"""Ce cours est sur l'utilisation des bases de données en python"""

########################################################################################################################
# 09.01 - Python et les base de données
########################################################################################################################
'''
L'utilisation de bases de données locales et distantes en développement d'application native en Python offre plusieurs 
avantages essentiels pour la conception et le déploiement de logiciels. Voici pourquoi il est pertinent d'utiliser ces 
deux types de bases de données :

    1.  Stockage des Données :  
            Bases de données locales (ou embarquées) : Ces bases de données sont stockées localement sur l'appareil de 
                l'utilisateur ou sur le serveur de l'application. Elles sont utilisées pour stocker des données 
                spécifiques à l'application, telles que les préférences de l'utilisateur, les données hors ligne, les 
                caches, etc. Les bases de données locales sont rapides et offrent une expérience utilisateur fluide.

            Bases de données distantes : Ces bases de données sont généralement situées sur des serveurs distants ou 
                dans le cloud. Elles permettent de stocker des données accessibles depuis n'importe quel appareil ou 
                emplacement, ce qui facilite le partage de données entre plusieurs utilisateurs et appareils.

    2.  Redondance et Sauvegarde :
            Bases de données locales : Elles peuvent servir de sauvegarde des données distantes en cas de déconnexion du 
                réseau ou de panne du serveur. Cela garantit la disponibilité des données, même en l'absence de 
                connectivité.

            Bases de données distantes : Les bases de données dans le cloud sont souvent sauvegardées automatiquement, 
                ce qui garantit que les données sont protégées contre la perte en cas de sinistre ou de panne.

    3.  Collaboration et Partage :
            Bases de données distantes : Elles permettent à plusieurs utilisateurs de collaborer sur les mêmes données 
                en temps réel, quelle que soit leur position géographique. Cela favorise la collaboration et la 
                productivité.
    
    4.  Évolutivité :
            Bases de données distantes : Dans le cloud, il est plus facile de faire évoluer la capacité de stockage ou 
                de traitement en fonction des besoins de l'application. Les bases de données locales ont des limites 
                physiques.
    
    5.  Sécurité :
            Bases de données distantes : Les fournisseurs de services cloud investissent massivement dans la sécurité 
                des données. Cela peut offrir une meilleure protection contre les attaques et les violations de données 
                par rapport à une base de données locale.
    
    6.  Maintenance et Mises à Jour :
            Bases de données distantes : Les mises à jour et la maintenance de la base de données sont gérées par le 
                fournisseur de services cloud, réduisant ainsi la charge de travail pour l'équipe de développement.

    7.  Économie de Ressources :
            Bases de données locales : Elles sont utiles pour économiser la bande passante réseau et réduire la charge 
                sur les serveurs distants en stockant des données fréquemment utilisées en local.

    8.  Prise en Charge Hors Ligne :
            Bases de données locales : Elles permettent aux applications de fonctionner hors ligne en stockant des 
                données localement. Cela améliore l'expérience utilisateur lorsque la connectivité réseau est limitée.

Donc, l'utilisation combinée de bases de données locales et distantes dans le développement d'applications natives en 
Python permet d'optimiser les performances, la disponibilité des données, la sécurité et la gestion des ressources. Le 
choix entre les deux dépend des besoins spécifiques de l'app, de la taille des l'utilisateurs et de la portée du projet.
'''

########################################################################################################################
# 09.02 - Préparation de PyCharm et des base de données
########################################################################################################################
'''
1.  MySQL - Base de données distante

    -   Présentation
    
    -   Donner les identifiants aux étudiants
    
    -   Ajout des fenêtres:
            View | Tool Windows | TODO
            View | Tool Windows | DATABASE
            
    -   Création de la table pour faire les tests de la théorie
            CREATE TABLE jeux_video (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titre VARCHAR(255) NOT NULL,
                annee_sortie INT,
                genre VARCHAR(50),
                plateforme VARCHAR(50),
                note DECIMAL(3, 1)
            );

2.  PostgreSQL - Base de données locale

    -   Création de la base de données.
            -- Création de la table des jeux vidéo
            CREATE TABLE jeux_video (
                id serial PRIMARY KEY,
                titre VARCHAR(255) NOT NULL,
                annee_sortie INT,
                genre VARCHAR(50),
                plateforme VARCHAR(50),
                note DECIMAL(3, 1)
            );

3.  SQLite - Base de données fichier et locale

    -   Préparation de SQLite (Voir le fichier)
    
    -   Création de la base de données et insertion des données dans la section sur sqlite.
            -- Création de la table des jeux vidéo
            CREATE TABLE jeux_video (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titre VARCHAR(255) NOT NULL,
                annee_sortie INT,
                genre VARCHAR(50),
                plateforme VARCHAR(50),
                note DECIMAL(3, 1)
            );

4.  Insertion des données pour les 3 différentes base de données.

    -- Insertion de données dans la table
    INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note)
    VALUES ('The Legend of Zelda: Breath of the Wild', 2017, 'Action-RPG', 'Nintendo Switch', 9.5),
           ('Grand Theft Auto V', 2013, 'Action-Aventure', 'PlayStation 4', 9.0),
           ('Minecraft', 2011, 'Sandbox', 'PC', 8.7),
           ('Fortnite', 2017, 'Battle Royale', 'Xbox One', 8.2),
           ('Red Dead Redemption 2', 2018, 'Action-Aventure', 'PlayStation 4', 9.6),
           ('Super Mario Odyssey', 2017, 'Plate-forme', 'Nintendo Switch', 9.4),
           ('FIFA 21', 2020, 'Sport', 'Xbox Series X', 8.0),
           ('The Witcher 3: Wild Hunt', 2015, 'Action-RPG', 'PC', 9.7),
           ('Overwatch', 2016, 'FPS', 'PlayStation 4', 8.9),
           ('Animal Crossing: New Horizons', 2020, 'Simulation de vie', 'Nintendo Switch', 9.3);
'''

########################################################################################################################
# 09.03 - MySQL - Base de données distante
########################################################################################################################
'''
1.  Installation du connecteur MySQL
    Pour vous connecter à une base de données MySQL, vous devez installer le connecteur MySQL qui est un paquet nommé 
    mysql-connector-python et qui est disponible sur PyPI.

    Voici la commande à faire dans le terminal : pip install mysql-connector-python

2.  Connexion à la base de données
    Le module mysql.connector fournit la méthode connect qui permet de retourner un objet qui représente la connexion 
    vers la base de données. Vous devez fournir les paramètres host, user et password pour donner l’adresse du SGBDR, 
    le login et le mot de passe de connexion. Vous pouvez également fournir le paramètre database pour indiquer quelle 
    base de données vous souhaitez utiliser.
    
    -   Exemple 1 : Connexion manuelle
'''
import mysql.connector


def mysql_connexion():
    # TODO : Mettre à jour les identifiants de connexion
    db = mysql.connector.connect(
        host="alex.157-245-242-119.cprapid.com",
        user="alex_202130861",
        password="W=F~qof1(@==",
        database="alex_202130861"
    )

    # C'est ici que nous pouvons faire des manipulations avec la connexion.
    db.close()


'''
    -   Exemple 2 : Connexion avec WITH pour nous assurer de fermer la connexion correctement (Comme les fichiers)
'''


def mysql_connexion2():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    with mysql.connector.connect(**connection_params) as db:
        # C'est ici que nous pouvons faire des manipulations avec la connexion.
        pass


'''
L'opérateur ** en Python est utilisé pour effectuer un "unpacking" de dictionnaire, ce qui signifie qu'il permet de 
passer les éléments clés-valeurs d'un dictionnaire comme arguments nommés à une fonction ou à un autre appel de fonction 
qui prend en charge cette syntaxe. Cela peut être particulièrement utile lorsque vous avez un dictionnaire contenant des 
valeurs que vous souhaitez utiliser comme arguments pour une fonction.

L’interaction avec la base de données se fera à travers un curseur. Cet objet permet à la fois d’envoyer des requêtes et 
de consulter les résultats quand il s’agit d’une requête de consultation de données. Pour créer un curseur, on appelle 
la méthode cursor() sur la connexion. Il est recommandé de fermer un curseur lorsqu’il n’est plus utilisé. Nous pouvons 
également employer la syntaxe with :

    -   Exemple 3 : Utilisation du curseur
'''


def mysql_cursor():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            pass


'''
3.  Sélection de données
    -   Exemple 4 : Récupérer des données et ensuite les afficher dans la console.
    
    Pour récupérer des données depuis la base de données, il suffit de passer un requête SQL de type select en 
    paramètre de la méthode execute du curseur et ensuite d’appeler la méthode fetchall() pour récupérer une liste 
    d'enregistrements (tuple) contenant les résultats.
'''


def mysql_select():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "select * from jeux_video"

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
            resultats = c.fetchall()
            for jeu in resultats:
                print(jeu)


'''
    -   Exemple 5 : Récupération des données directement sans passé par une liste. Donc, un à un.
    
    Parfois, on désire traiter directement la donnée retournée et il n’est pas nécessaire de la stocker dans une liste. 
    Nous pouvons améliorer notre code en optant pour l’appel à la méthode fetchone(). Cette méthode retourne un seul 
    résultat sous la forme d’un n-uplet. Lorsqu’il n’y a plus de résultat à lire, la méthode retourne None.
'''


def mysql_select2():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "select * from jeux_video"

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request)
            while True:
                jeu = c.fetchone()
                if jeu is None:
                    break
                print(jeu)


'''
Si vous fermez un curseur avant d’avoir extrait tous les résultats, vous obtiendrez une exception. N’utilisez pas la 
méthode fetchone() pour ne retourner que le premier résultat, elle n’a pas été conçue pour cela. Son rôle est de 
permettre de retourner tous les résultats d’une requête mais un à un.

Si vous voulez limiter le nombre de résultats retournés par une requête, utilisez l’instruction SQL limit:
    select * from jeux_video limit 1
    
    -   Exemple 6 : Récupération des données selon un nombre précis.
    
    La méthode fetchmany() prend en paramètre le nombre maximum de résultats qu’il faut aller chercher lors de cette 
    appel. Lorsqu’il n’y a plus de résultat, la méthode retourne une liste vide.
'''


def mysql_select3():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "select titre, genre, plateforme from jeux_video"

    with mysql.connector.connect(**connection_params) as db:
        #  Le 'buffered' permet de garder en mémoire les résultats. Seulement faire lors de l'utilisation de fetchmany()
        with db.cursor(buffered=True) as c:
            c.execute(request)
            resultats = c.fetchmany(4)
            for jeu in resultats:
                print(jeu)


'''
    -   Exemple 7 : Comment redéfinir tout le code dans une seule fonction
'''


def mysql_execution_requete(cursor, request):
    cursor.execute(request)
    resultats = cursor.fetchmany(3)
    for jeu in resultats:
        print(jeu)


def mysql_select4():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "select titre, genre, plateforme from jeux_video"

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor(buffered=True) as c:
            mysql_execution_requete(c, request)


'''
    -   Exemple 8 : Utilisation de paramètres dans les conditions where
'''


def mysql_select5():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = ("select titre, genre, plateforme, note from jeux_video \
                    where note > %s and note < %s")

    params = (9, 9.5)

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, params)

            # Autres options d'appel pour execute()
            # c.execute(request, (0, 9.5))
            # c.execute(request, [0, 9.5])
            # c.execute(request, (0,))
            # c.execute(request, [9.5])

            resultats = c.fetchall()
            for jeu in resultats:
                print(jeu)


'''
4.  Insertion de données
    -   Exemple 9 : Insertion de données standards avec commit
'''


def mysql_insert():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute("INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) \
                        VALUES ('Hollow Knight', 2017, 'Plateforme', 'Nintendo Switch', 9.1);")
            db.commit()


'''
l’appel à la méthode commit() de la connexion qui permet de valider les modifications. Si vous n’appelez pas cette 
méthode, la transaction avec la base de données ne sera pas terminée et aucune ligne ne sera insérée en base de données.

    -   Exemple 10 : Insertion de données avec paramètres
    
        Le connecteur MySQL fournit la propriété non standard autocommit sur la connexion. Si cette propriété vaut True 
        alors un commit est automatiquement fait après chaque exécution de requête.
'''


def mysql_insert2():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) VALUES (%s, %s, %s, %s, %s)"

    params = ('Kerbal Space Program', 2011, 'Simulation', 'PC', 9.0)

    with mysql.connector.connect(**connection_params) as db:
        db.autocommit = True  # Pour forcer la base de données un commit automatique
        with db.cursor() as c:
            c.execute(request, params)


'''
    -   Exemple 11 : Insertion de données multiples avec vérification du nombre d'insertion
'''


def mysql_insert3():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) VALUES (%s, %s, %s, %s, %s)"

    params = [
        ("The Elder Scrolls V: Skyrim", 2011, 'RPG', 'Xbox 360', 9.4),
        ('Half-Life 2', 2004, 'FPS', 'PC', 9.3),
        ('The Forest', 2014, 'Survie', 'PC', 8.5)
    ]

    with mysql.connector.connect(**connection_params) as db:
        db.autocommit = True  # Pour forcer la base de données un commit automatique
        with db.cursor() as c:
            c.executemany(request, params)
            print("Nombre de lignes insérées :", c.rowcount)


'''
5.  Modification de données

    -   Exemple 12 : Mise à jour selon la même méthode que les autres requêtes
'''


def mysql_update():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "alex.157-245-242-119.cprapid.com",
        'user': "alex_202130861",
        'password': "W=F~qof1(@==",
        'database': "alex_202130861",
    }

    request = "update jeux_video \
               set note = %s \
               where id = %s"

    params = (1.2, 1)

    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(request, params)
            db.commit()
            print("Nombre de lignes mises à jour :", c.rowcount)


########################################################################################################################
# 09.04 - PostgreSQL - Base de données locale
########################################################################################################################
'''
1.  Installation du connecteur MySQL
    Pour vous connecter à une base de données PostgreSQL, vous devez installer le connecteur qui est un paquet nommé 
    Psycopg2 et qui est disponible sur PyPI.

    Voici la commande à faire dans le terminal : pip install Psycopg2

2.  Exemple complets d'insertion, select et update

    Pour le connecteur Psycopg2, il est non nécessaire de préciser le paramètre autocommit=True, car depouis la version
    2.9, lorsque la connection est utilisé avec un with, le commit se fait automatiquement, si il n'a a pas d'erreur.
'''
import psycopg2


def postgresql_exemple():
    # TODO : Mettre à jour les identifiants de connexion
    connection_params = {
        'host': "localhost",
        'user': "postgres",
        'password': "postgres",
        'database': "postgres",
        'port': "5433"
    }

    request_s = "select * from jeux_video"

    request_i = "INSERT INTO jeux_video (titre, annee_sortie, genre, plateforme, note) VALUES (%s, %s, %s, %s, %s)"

    params_i = [
        ('The Elder Scrolls V: Skyrim', 2011, 'RPG', 'Xbox 360', 9.4),
        ('Half-Life 2', 2004, 'FPS', 'PC', 9.3),
        ('The Forest', 2014, 'Survie', 'PC', 8.5)
    ]

    request_u = "update jeux_video set note = %s where id = %s"

    params_u = (0, 1,)

    with psycopg2.connect(**connection_params) as db:
        with db.cursor() as c:
            # Insertion de données dans la table avec executemany()
            c.executemany(request_i, params_i)
            print("Nombre de lignes insérées :", c.rowcount)

            # Insertion de données dans la table executemany(), il faut placé la liste de paramètre entre crochet.
            c.executemany(request_u, [params_u])
            print("Nombre de lignes modifié :", c.rowcount)

            # Affichage de la totalité de la table
            c.execute(request_s)
            resultats = c.fetchall()
            for jeu in resultats:
                print(jeu)


########################################################################################################################
# 09.05 - SQLite - Base de données fichier et locale
########################################################################################################################
'''
1.  Installation du connecteur SQLite
    Pour vous connecter à une base de données SQLite, vous devez installer le connecteur qui est un paquet nommé 
    sqlite3 et qui est disponible sur PyPI.

    Voici la commande à faire dans le terminal : pip install sqlite3

2.  Exemple complets d'insertion, select et update
'''
import sqlite3


def sqlite_exemple():
    # Établir une connexion à la base de données
    conn = sqlite3.connect("jeux_video.sqlite")

    # Créer un curseur pour interagir avec la base de données
    cur = conn.cursor()

    # Créer une table dans la base de données
    cur.execute('''CREATE TABLE IF NOT EXISTS jeux_video (
                    id INTEGER PRIMARY KEY,
                    titre TEXT NOT NULL,
                    annee_sortie INT,
                    genre TEXT,
                    plateforme TEXT,
                    note DECIMAL(3, 1))''')

    # Insérer des données dans la table
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('The Legend of Zelda: Breath of the Wild', 2017, 'Action-RPG', 'Nintendo Switch', 9.5))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Grand Theft Auto V', 2013, 'Action-Aventure', 'PlayStation 4', 9.0))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Minecraft', 2011, 'Sandbox', 'PC', 8.7))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Fortnite', 2017, 'Battle Royale', 'Xbox One', 8.2))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Red Dead Redemption 2', 2018, 'Action-Aventure', 'PlayStation 4', 9.6))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Super Mario Odyssey', 2017, 'Plate-forme', 'Nintendo Switch', 9.4))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('FIFA 21', 2020, 'Sport', 'Xbox Series X', 8.0))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('The Witcher 3: Wild Hunt', 2015, 'Action-RPG', 'PC', 9.7))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Overwatch', 2016, 'FPS', 'PlayStation 4', 8.9))
    cur.execute("INSERT INTO jeux_video(titre, annee_sortie, genre, plateforme, note) VALUES (?, ?, ?, ?, ?)",
                ('Animal Crossing: New Horizons', 2020, 'Simulation de vie', 'Nintendo Switch', 9.3))

    # Valider (commit) les modifications dans la base de données
    conn.commit()

    # Interroger la base de données
    cur.execute("SELECT * FROM jeux_video")

    # Récupérer les résultats et les afficher
    jeux_video = cur.fetchall()
    for jeu in jeux_video:
        print(f"Titre : {jeu[1]}")

    # Fermer le curseur et la connexion à la base de données
    cur.close()
    conn.close()


########################################################################################################################
# 09.06 - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    print('test')
    sqlite_exemple()

########################################################################################################################
# 09.07 - Références
########################################################################################################################
'''
https://docs.python.org/fr/3.8/library/stdtypes.html
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming
https://python.sdv.univ-paris-diderot.fr/02_variables/
https://gayerie.dev/docs/python/index.html
https://python.doctor/
https://gayerie.dev/docs/python/python3/mysql.html#
'''
