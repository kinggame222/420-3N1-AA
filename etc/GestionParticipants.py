'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *

import ttkwidgets

from etc import Fonction
from etc.Fonction import afficherParticipants, supprimerParticipant
from menu import create_menu

# Début du programme principal
if __name__ == '__main__':
    # Création de la fenêtre principale
    w = Tk()

    # Configuration de la fenêtre principale
    bg = "light grey"
    fg = "black"
    w.configure(bg=bg)
    w.title("Pool Hockey 2023-2024 - Collège d'alma")
    w.geometry("580x430")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    create_menu(w)  # Crée le menu de la fenêtre

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, anchor='n')

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Gestion des Participants", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=3, pady=40)

    # Création du Treeview
    tree = ttkwidgets.CheckboxTreeview(frm, columns=(
        'Prénom', 'Nom', 'Courriel'))

    # Configuration du Treeview
    tree.heading('Prénom', text='Prénom')
    tree.heading('Nom', text='Nom')
    tree.heading('Courriel', text='Courriel')
    tree.column('#0', width=50)
    tree.column('Prénom', width=100)
    tree.column('Nom', width=100)
    tree.column('Courriel', width=300)
    tree.grid(row=1, column=0, columnspan=3)

    # Création du bouton btnAjouter
    btnAjouter = Button(frm, text="Ajouter", font=("Courrier", 10), fg=fg, bg=bg)
    btnAjouter.grid(row=2, column=0, pady=10, sticky='ew')

    # Création du bouton btnModifier
    btnModifier = Button(frm, text="Modifier", font=("Courrier", 10), fg=fg, bg=bg)
    btnModifier.grid(row=2, column=1, pady=10, sticky='ew', padx=10)

    # Création du bouton btnSupprimer
    btnSupprimer = Button(frm, text="Supprimer", font=("Courrier", 10), fg=fg, bg=bg,
                          command=lambda: supprimerParticipant(tree))
    btnSupprimer.grid(row=2, column=2, pady=10, sticky='ew')

    afficherParticipants(tree)

    # Boucle principale
    w.mainloop()
