'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

import subprocess
from tkinter import *
from tkinter import messagebox


def ouvrir_page(w, page):
    # Ouvrir la page demandée
    if page == "etc.Quitter":
        # Si la page demandée est "etc.Quitter", on quitte l'application
        w.destroy()
        pass
    # Sinon, on ouvre la page demandée
    w.destroy()

    subprocess.call(["python", "-m", page])


def afficher_info_sur():
    # afficher une boîte de dialogue avec les informations sur l'application
    nom_application = "Application de gestion de pool de hockey"
    votre_nom = "William Bouchard"
    date_creation = "2023-11-30"
    messagebox.showinfo("À propos de …", f"{nom_application}\n{votre_nom}\n{date_creation}")


def affichermenu(w):
    # Création de la barre de menu
    menuBar = Menu(w)

    # Création du menu "Pool"
    pool_menu = Menu(menuBar, tearoff=0)
    pool_menu.add_command(label="Accueil", command=lambda: ouvrir_page(w, "etc.Accueil"))
    pool_menu.add_command(label="Connexion", command=lambda: ouvrir_page(w, "etc.Connexion"))
    pool_menu.add_command(label="Pool", command=lambda: ouvrir_page(w, "etc.Pool"))
    pool_menu.add_command(label="Quitter", command=lambda: ouvrir_page(w, "etc.Quitter"))
    menuBar.add_cascade(label="Pool", menu=pool_menu, state=NORMAL)

    # Création du menu "Participant"
    participant_menu = Menu(menuBar, tearoff=0)
    participant_menu.add_command(label="Inscription", command=lambda: ouvrir_page(w, "etc.Inscription"))
    participant_menu.add_command(label="Connexion", command=lambda: ouvrir_page(w, "etc.Connexion"))
    participant_menu.add_separator()
    participant_menu.add_command(label="Classement", command=lambda: ouvrir_page(w, "etc.Classement"))
    menuBar.add_cascade(label="Participant", menu=participant_menu, state=NORMAL)

    # Création du menu "Statistiques"
    stats_menu = Menu(menuBar, tearoff=0)
    stats_menu.add_command(label="Joueur", command=lambda: ouvrir_page(w, "etc.GestionJoueurs"))
    stats_menu.add_separator()
    stats_menu.add_command(label="Équipe", command=lambda: ouvrir_page(w, "etc.GestionEquipe"))
    stats_menu.add_separator()
    stats_menu.add_command(label="Calendrier des parties", command=lambda: ouvrir_page(w, "etc.CalendrierParties"))
    menuBar.add_cascade(label="Statistiques", menu=stats_menu, state=NORMAL)

    # Création du menu "Administration"
    admin_menu = Menu(menuBar, tearoff=0)
    admin_menu.add_command(label="Gestion des participants", command=lambda: ouvrir_page(w, "etc.GestionParticipants"))
    admin_menu.add_command(label="Gestion des Équipes", command=lambda: ouvrir_page(w, "etc.GestionEquipe"))
    admin_menu.add_command(label="Gestion des Joueurs", command=lambda: ouvrir_page(w, "etc.GestionJoueurs"))
    menuBar.add_cascade(label="Administration", menu=admin_menu, state=NORMAL)

    # Création du menu "À propos"
    about_menu = Menu(menuBar, tearoff=0)
    about_menu.add_command(label="À propos de …", command=afficher_info_sur)
    menuBar.add_cascade(label="À propos", menu=about_menu, state=NORMAL)

    # Ajout de la barre de menu à la fenêtre principale
    w.config(menu=menuBar)


def create_menu(w):
    # Création de la barre de menu
    menuBar = Menu(w)

    # Création du menu "Pool"
    pool_menu = Menu(menuBar, tearoff=0)
    pool_menu.add_command(label="Accueil", command=lambda: ouvrir_page(w, "etc.Accueil"))
    pool_menu.add_command(label="Connexion", command=lambda: ouvrir_page(w, "etc.Connexion"))
    pool_menu.add_command(label="Pool", command=lambda: ouvrir_page(w, "etc.Pool"))
    pool_menu.add_command(label="Quitter", command=lambda: ouvrir_page(w, "etc.Quitter"))
    menuBar.add_cascade(label="Pool", menu=pool_menu, state=DISABLED)

    # Création du menu "Participant"
    participant_menu = Menu(menuBar, tearoff=0)
    participant_menu.add_command(label="Inscription", command=lambda: ouvrir_page(w, "etc.Inscription"))
    participant_menu.add_command(label="Connexion", command=lambda: ouvrir_page(w, "etc.Connexion"))
    participant_menu.add_separator()
    participant_menu.add_command(label="Classement", command=lambda: ouvrir_page(w, "etc.Classement"))
    menuBar.add_cascade(label="Participant", menu=participant_menu, state=DISABLED)

    # Création du menu "Statistiques"
    stats_menu = Menu(menuBar, tearoff=0)
    stats_menu.add_command(label="Joueur", command=lambda: ouvrir_page(w, "etc.GestionJoueurs"))
    stats_menu.add_separator()
    stats_menu.add_command(label="Équipe", command=lambda: ouvrir_page(w, "etc.GestionEquipe"))
    stats_menu.add_separator()
    stats_menu.add_command(label="Calendrier des parties", command=lambda: ouvrir_page(w, "etc.CalendrierParties"))
    menuBar.add_cascade(label="Statistiques", menu=stats_menu, state=DISABLED)

    # Création du menu "Administration"
    admin_menu = Menu(menuBar, tearoff=0)
    admin_menu.add_command(label="Gestion des participants", command=lambda: ouvrir_page(w, "etc.GestionParticipants"))
    admin_menu.add_command(label="Gestion des Équipes", command=lambda: ouvrir_page(w, "etc.GestionEquipe"))
    admin_menu.add_command(label="Gestion des Joueurs", command=lambda: ouvrir_page(w, "etc.GestionJoueurs"))
    menuBar.add_cascade(label="Administration", menu=admin_menu, state=DISABLED)

    # Création du menu "À propos"
    about_menu = Menu(menuBar, tearoff=0)
    about_menu.add_command(label="À propos de …", command=afficher_info_sur)
    menuBar.add_cascade(label="À propos", menu=about_menu, state=DISABLED)

    # Ajout de la barre de menu à la fenêtre principale
    w.config(menu=menuBar)
