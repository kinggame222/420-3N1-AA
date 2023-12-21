'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *
from tkinter import ttk

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
    w.geometry("650x400")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    create_menu(w)

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, anchor='n')

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Classement", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2)

    # Création du label lblTexte
    texte = "Vous pouvez cliquer sur le nom du participant pour visualiser les joueurs sélectionnés \n \n Voici comment sont attribués les points "
    lblTexte = Label(frm, text=texte, font=("Courrier", 10), fg=fg, bg=bg)
    lblTexte.grid(row=1, column=0, columnspan=2)

    # Création du Treeview
    tree = ttk.Treeview(frm, columns=('Position', 'Nom', 'Points'), show='headings')
    tree.heading('Position', text='Position')
    tree.heading('Nom', text='Nom')
    tree.heading('Points', text='Points')
    tree.column('Position', width=200)
    tree.column('Nom', width=200)
    tree.column('Points', width=200)
    tree.grid(row=2, column=0, columnspan=2)

    tree.insert('', 'end', values=(1, 'Nancy', 100))
    tree.insert('', 'end', values=(2, 'Alexandre', 94))

    # Boucle principale
    w.mainloop()
