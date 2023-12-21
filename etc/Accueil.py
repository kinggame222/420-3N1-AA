'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from menu import *

# Début du programme principal
if __name__ == '__main__':
    # Création de la fenêtre principale
    w = Tk()

    # Configuration de la fenêtre principale
    bg = "light grey"
    fg = "black"
    w.configure(bg=bg)
    w.title("Pool Hockey 2023-2024 - Collège d'alma")
    w.geometry("800x600")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    create_menu(w)

    # Création et positionnement du label lblTitre
    lblTitre = Label(w, text="Pool Hockey \n Collège d'Alma", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.place(relx=0.5, rely=0.3, anchor='center')

    # Création et positionnement du label lblTexte
    texte = "Bienvenue dans le pool de hockey du Collège d'Alma. \n" \
            "Vous etes invité a consulter le menu ci-haut pour vous inscrire, \n" \
            "Vous connecter, consulter votre classement, etc. \n\n" \
            "Bonne saison d'Hockey !"
    lblTexte = Label(w, text=texte, font=("Courrier", 15), fg=fg, bg=bg)
    lblTexte.place(relx=0.5, rely=0.5, anchor='n')

    # Boucle principale
    w.mainloop()
