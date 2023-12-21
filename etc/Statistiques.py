'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *
from tkinter import ttk

from etc.Fonction import afficherJoueurs
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
    w.geometry("700x350")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    # Création du menu
    create_menu(w)

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, anchor='n')

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Statistiques - Joueur", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2)

    # Création du label lblTexte
    texte = "Vous pouvez cliquer sur le nom du participant pour visualiser ses caractéristiques"
    lblTexte = Label(frm, text=texte, font=("Courrier", 10), fg=fg, bg=bg)
    lblTexte.grid(row=1, column=0, columnspan=2)

    # Création du Treeview
    tree = ttk.Treeview(frm, columns=('#', 'Joueur', 'Date de naissance', 'Équipe', 'Position ', 'But', 'Passe'),
                        show='headings')
    tree.heading('#', text='#')
    tree.heading('Joueur', text=' Joueur')
    tree.heading('Date de naissance', text=' Date de naissance')
    tree.heading('Équipe', text=' Équipe')
    tree.heading('Position ', text=' Position ')
    tree.heading('But', text=' But')
    tree.heading('Passe', text=' Passe')
    tree.column('#', width=50)
    tree.column('Joueur', width=100)
    tree.column('Date de naissance', width=100)
    tree.column('Équipe', width=100)
    tree.column('Position ', width=100)
    tree.column('But', width=100)
    tree.column('Passe', width=100)
    tree.grid(row=2, column=0, columnspan=2)

    afficherJoueurs(tree)
    # Boucle principale
    w.mainloop()
