'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *

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

    create_menu(w)

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, anchor='n')

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Gestion des Joueurs", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2, pady=40)

    # Création du label lblTexte
    texte = "<< EN CONSTRUCTION >>"
    lblTexte = Label(frm, text=texte, font=("Courrier", 30), fg='red', bg=bg)
    lblTexte.grid(row=1, column=0, columnspan=2)

    # Boucle principale
    w.mainloop()
