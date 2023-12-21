'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

import sqlite3


# Connexion à la base de données
def connexionBD():
    """
    Cette fonction établit une connexion à la base de données SQLite et renvoie l'objet de connexion et le curseur.
    """
    conn = sqlite3.connect('../etc/BDpool/pool.sqlite')
    cur = conn.cursor()
    return conn, cur


# Déconnexion de la base de données
def deconnexionBD(conn, cur):
    """
    Cette fonction ferme la connexion à la base de données SQLite et le curseur.
    """
    cur.close()
    conn.close()


# Insertion d'un participant dans la base de données
def insertionParticipant(prenom, nom, courriel, mot_de_passe):
    """
    Cette fonction insère un nouveau participant dans la table PARTICIPANT de la base de données.
    Elle prend en paramètres le prénom, le nom, le courriel et le mot de passe du participant.
    """
    conn, cur = connexionBD()
    cur.execute("INSERT INTO PARTICIPANT (prenom, nom, courriel, motDePasse) VALUES (?, ?, ?, ?)",
                (prenom, nom, courriel, mot_de_passe))
    conn.commit()
    deconnexionBD(conn, cur)


# Insertion d'un participant dans le pool
def insertParticipantPool():
    """
    Cette fonction insère un participant dans la table PARTICIPANT_POOL de la base de données.
    Elle utilise l'ID du dernier participant inséré et une liste prédéfinie d'IDs de joueurs.
    """
    conn, cur = connexionBD()
    cur.execute("SELECT MAX(id) FROM PARTICIPANT ")
    idParticipant = cur.fetchone()[0]
    joueurIds = [8477934, 8477956, 8480012, 8478864, 8476454, 8477942, 8480801, 8477946, 8479339, 8484144, 8477409,
                 8475913, 8481557, 8481528, 8475692, 8480069, 8479323, 8479325, 8474590, 8477447, 8476883, 8477970,
                 8478024, 8474593]
    for i, joueurId in enumerate(joueurIds, start=1):
        cur.execute("INSERT INTO PARTICIPANT_POOL (participantId, ronde,joueurId) VALUES (?, ?, ?)",
                    (idParticipant, i, joueurId))
        conn.commit()
    deconnexionBD(conn, cur)


# Insertion d'un participant et de son pool dans la base de données
insertionParticipant("william", "bouchard", "williambou588@gmail.com", "123")
insertParticipantPool()
