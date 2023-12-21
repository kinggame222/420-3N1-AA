'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from etc.Fonction import verifier_connexion, connexionBD, deconnexionBD
from etc.menu import *


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
        affichermenu(w)


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

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, rely=0.5, anchor='center')

    # Création et positionnement du label lblTitre dans le Frame
    lblTitre = Label(frm, text="Connexion", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2, pady=30)

    # Création et positionnement du label lblNom dans le Frame
    lblNom = Label(frm, text="Courriel : ", font=("Courrier", 12), fg=fg, bg=bg)
    lblNom.grid(row=1, column=0, sticky='e')

    # Création et positionnement du champ txtNom dans le Frame
    txtNom = Entry(frm, width=30)
    txtNom.grid(row=1, column=1)

    # Création et positionnement du label lblMDP dans le Frame
    lblMDP = Label(frm, text="Mot de passe : ", font=("Courrier", 12), fg=fg, bg=bg)
    lblMDP.grid(row=2, column=0, sticky='e')

    # Création et positionnement du champ txtMDP dans le Frame
    txtMDP = Entry(frm, width=30, show="*")
    txtMDP.grid(row=2, column=1)

    # Création et positionnement du bouton btnConnexion dans le Frame
    btnConnexion = Button(frm, text="Connexion", font=("Courrier", 12), fg=fg, bg=bg, width=20,
                          command=lambda: verifier_connexion(txtNom.get(), txtMDP.get()))
    btnConnexion.grid(row=3, column=0, columnspan=2, pady=30)

    # Configure la grille pour que les widgets soient centrés
    frm.grid_columnconfigure(0, weight=1)
    frm.grid_columnconfigure(2, weight=1)

    # Boucle principale
    w.mainloop()
