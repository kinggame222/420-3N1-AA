'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *
from tkinter import ttk

from Fonction import connexionBD, deconnexionBD, afficherJoueurs, afficherParticipants
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
    w.geometry("625x310")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    create_menu(w)

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, anchor='n')

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Calendrier des parties", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2)

    # Création du Treeview
    tree = ttk.Treeview(frm, columns=('Date', 'Équipe\nVisiteur', 'Pointage', 'Équipe\nDomicile', 'Pointage ', ' '),
                        show='headings')
    tree.heading('Date', text='Date')
    tree.heading('Équipe\nVisiteur', text='Équipe\nVisiteur')
    tree.heading('Pointage', text='Pointage')
    tree.heading('Équipe\nDomicile', text='Équipe\nDomicile')
    tree.heading('Pointage ', text='Pointage ')
    tree.heading(' ', text=' ')
    tree.column('Date', width=100)
    tree.column('Équipe\nVisiteur', width=100)
    tree.column('Pointage', width=100)
    tree.column('Équipe\nDomicile', width=100)
    tree.column('Pointage ', width=100)
    tree.column(' ', width=100)
    tree.grid(row=2, column=0, columnspan=2)

    afficherParticipants(tree)

    # Boucle principale
    w.mainloop()
