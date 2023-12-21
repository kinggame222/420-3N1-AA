'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *
from tkinter import messagebox

from Fonction import connexionBD, deconnexionBD, inscrire_participant
from menu import create_menu


def open_messagebox(event):
    messagebox.showinfo("Conditions et Règlements",
                        "- Le participant doit être employé du Collège d’Alma et doit avoir 18 ans lors de "
                        "l’inscription.\n\n"
                        "- Limite d’une inscription par courriel.\n\n"
                        "- Le prix de l’inscription est de 50$/équipe.\n\n"
                        "- Le pool commence le 19 septembre 2023 (12h00) et se termine le 18 avril 2024 (23h59) soit "
                        "le dernier jour de la saison régulière de la Ligue nationale de hockey 2023-2024.")


def reinitialiserLesChamps():
    txtNom.delete(0, END)
    txtPrenom.delete(0, END)
    txtMotDePasse.delete(0, END)
    txtCourriel.delete(0, END)
    varreglementchk.set(0)


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

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Inscription", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=3, pady=30)

    # Création et positionnement du labelframe
    labelframe = LabelFrame(frm, text="Info-participant", bg=bg, font=("Courrier", 10))
    labelframe.grid(row=1, column=0, sticky='nsew')

    # Création et positionnement du label prenom
    lblPrenom = Label(labelframe, text="Prénom :", bg=bg)
    lblPrenom.grid(row=0, column=0, sticky='e')

    # Création et positionnement de l'étoile rouge pour le champ prenom
    lblPrenomStar = Label(labelframe, text="*", fg="red", bg=bg)
    lblPrenomStar.grid(row=0, column=1, sticky='w')

    # Création et positionnement du champ prenom
    txtPrenom = Entry(labelframe, width=50)
    txtPrenom.grid(row=0, column=2)

    # Création et positionnement du label nom
    lblNom = Label(labelframe, text="Nom :", bg=bg)
    lblNom.grid(row=1, column=0, sticky='e')

    # Création et positionnement du champ nom
    txtNom = Entry(labelframe, width=50)
    txtNom.grid(row=1, column=2)

    # Création et positionnement du label mot de passe
    lblMotDePasse = Label(labelframe, text="Mot de passe :", bg=bg)
    lblMotDePasse.grid(row=2, column=0, sticky='e')

    # Création et positionnement du champ mot de passe
    txtMotDePasse = Entry(labelframe, width=50, show="*")
    txtMotDePasse.grid(row=2, column=2)

    # Création et positionnement du label courriel
    lblCourriel = Label(labelframe, text="Courriel :", bg=bg)
    lblCourriel.grid(row=3, column=0, sticky='e')

    # Création et positionnement de l'étoile rouge pour le champ courriel
    lblCourrielStar = Label(labelframe, text="*", fg="red", bg=bg)
    lblCourrielStar.grid(row=3, column=1, sticky='w')

    # Création et positionnement du champ courriel
    txtCourriel = Entry(labelframe, width=50)
    txtCourriel.grid(row=3, column=2)

    # Création et positionnement du label telephone
    lblTelephone = Label(labelframe, text="* Champs obligatoire", bg=bg, fg="red")
    lblTelephone.grid(row=4, column=0, sticky='e')
    # Création du Frame pour les boutons
    frmButtons = Frame(frm, bg=bg)
    frmButtons.grid(row=2, column=0, columnspan=3, pady=30)

    # Création du bouton sauvegarder
    btnSauvegarder = Button(frmButtons, text="Sauvegarder", font=("Courrier", 12), fg=fg, bg=bg, width=20,
                            command=lambda: inscrire_participant(txtPrenom.get(),
                                                                     txtNom.get(),
                                                                     txtMotDePasse.get(),
                                                                     txtCourriel.get(),
                                                                     varreglementchk.get()))
    btnSauvegarder.grid(row=0, column=0, padx=10)

    # Création du bouton réinitialiser
    btnReinitialiser = Button(frmButtons, text="Réinitialiser", font=("Courrier", 12), fg=fg, bg=bg, width=20,
                              command=reinitialiserLesChamps)
    btnReinitialiser.grid(row=0, column=1, padx=10)

    # Condition et reglement messagebox
    lblCondition = Label(frm, text="Conditions  et  règlements", bg=bg, fg="blue", cursor="hand2")
    lblCondition.grid(row=3, column=0, columnspan=3)
    lblCondition.bind("<Button-1>", open_messagebox)

    # checkbox
    varreglementchk = IntVar()
    chkreglement = Checkbutton(frm, text="J'accepte les conditions et règlements", variable=varreglementchk, bg=bg)
    chkreglement.grid(row=4, column=0, columnspan=3)

    # Boucle principale
    w.mainloop()
