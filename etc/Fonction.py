import sqlite3
from tkinter import messagebox


def connexionBD():
    conn = sqlite3.connect('../etc/BDpool/pool.sqlite')
    cur = conn.cursor()
    return conn, cur


def deconnexionBD(conn, cur):
    cur.close()
    conn.close()


def verifier_connexion(courriel, mot_de_passe):
    conn, cur = connexionBD()
    cur.execute("SELECT * FROM PARTICIPANT WHERE courriel=? AND motDePasse=?",
                (courriel, mot_de_passe))
    participant = cur.fetchone()
    deconnexionBD(conn, cur)
    if participant is None:
        print("Connexion échouée")
    else:
        print("Connexion réussie")


def inscrire_participant(prenom, nom, courriel, mot_de_passe, reglement):
    if prenom == "" or mot_de_passe == "":
        affichererreur(0)

    elif reglement == 0:
        affichererreur(1)

    conn, cur = connexionBD()
    cur.execute("INSERT INTO PARTICIPANT (prenom, nom, courriel, motDePasse) VALUES (?, ?, ?, ?)",
                (prenom, nom, courriel, mot_de_passe))
    conn.commit()
    deconnexionBD(conn, cur)


def affichererreur(num):
    if num == 0:
        messagebox.showerror("Erreur", "Veuillez remplir les champs obligatoires")
    elif num == 1:
        messagebox.showerror("Erreur", "Veuillez accepter les conditions et règlements")


def afficherCalendierPartie(tree):
    # Création de la connexion et du curseur
    conn, cur = connexionBD()
    cur.execute("SELECT * FROM PARTIE ORDER BY datePartie ASC")
    parties = cur.fetchall()
    deconnexionBD(conn, cur)
    # Insertion des données dans le Treeview
    for partie in parties:
        tree.insert('', 'end', values=partie)


def afficherParticipants(tree):
    # Création de la connexion et du curseur
    conn, cur = connexionBD()
    cur.execute(
        "SELECT prenom,nom,courriel FROM PARTICIPANT ORDER BY id ASC")
    participants = cur.fetchall()
    deconnexionBD(conn, cur)
    # Insertion des données dans le Treeview
    for participant in participants:
        tree.insert('', 'end', values=participant)


def supprimerParticipant(tree):
    # Récupérer les ID des éléments cochés
    checked_items = tree.get_checked()

    # Vérifier s'il y a au moins une case cochée
    if not checked_items:
        messagebox.showinfo("Erreur", "Veuillez cocher au moins une case.")
        return

    # Demander une confirmation avant de supprimer
    confirmer = messagebox.askyesno("Confirmation",
                                    "Êtes-vous sûr de vouloir supprimer les participants sélectionnés ?")
    if not confirmer:
        return

    # Supprimer les enregistrements cochés de la base de données
    conn, cur = connexionBD()
    for item in checked_items:
        cur.execute("DELETE FROM PARTICIPANT WHERE id = ?", (item,))
    conn.commit()
    deconnexionBD(conn, cur)

    # Supprimer les éléments cochés du Treeview
    for item in checked_items:
        tree.delete(item)


def afficherJoueurs(tree):
    # Création de la connexion et du curseur
    conn, cur = connexionBD()
    cur.execute("SELECT id FROM JOUEUR ORDER BY nom ASC")
    joueur = cur.fetchone()
    joueurId = joueur[0]  # Extraire l'ID du tuple
    cur.execute("""
        WITH equipe AS (
        SELECT p.equipeReceveurId as equipeId FROM joueur j 
        JOIN partie_joueur pj ON j.id = pj.joueurId 
        JOIN partie p ON pj.partieId = p.id WHERE joueurId = ? 
        union all SELECT p.equipeVisiteurId as equipeId FROM joueur j 
        JOIN partie_joueur pj ON j.id = pj.joueurId 
        JOIN partie p ON pj.partieId = p.id 
        WHERE joueurId = ? ) SELECT * FROM equipe  """,
                (joueurId, joueurId))  # Utiliser joueurId pour les deux paramètres
    equipe = cur.fetchall()
    # Insertion des données dans le Treeview
    for joueur in equipe:
        tree.insert('', 'end', values=equipe)
