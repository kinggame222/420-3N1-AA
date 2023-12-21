'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''

from tkinter import *

from PIL import Image

# Début du programme principal
if __name__ == '__main__':
    # Création de la fenêtre principale
    w = Tk()

    # Configuration de la fenêtre principale
    bg = "light grey"
    fg = "black"
    w.configure(bg=bg)
    w.title("Pool Hockey 2023-2024 - Collège d'alma")
    w.geometry("800x505")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    # Création du Frame
    frm = Frame(w, bg=bg)
    frm.place(relx=0.5, anchor='n')

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Joueur : Cole Caufield", font=("Courrier", 20), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2, pady=40)

    # Création du labelframe
    labelframe = LabelFrame(frm, text="", labelanchor='n', width=400, height=400
                            , bg=bg, border=2,
                            highlightcolor='Black')  # Remplacer 'your_desired_color' par la couleur que vous voulez
    labelframe.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    # Frame pour l'image
    frmImage = Frame(labelframe, bg=bg)
    frmImage.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Ouvrir le fichier image
    img = Image.open("..\etc\image\cole-caufield-2024-45.png")

    # Obtenir les dimensions de l'image
    width, height = img.size

    # Créer l'objet PhotoImage
    image = PhotoImage(file="..\etc\image\cole-caufield-2024-45.png").subsample(2).zoom(1)

    # Créer le Canvas avec les dimensions de l'image
    canvas = Canvas(frmImage, width=width / 2, height=height / 2, bg=bg, bd=0, highlightthickness=0, relief='ridge',
                    borderwidth=0)

    # Ajouter l'image au Canvas
    canvas.create_image(width / 4, height / 4, image=image)  # L'image est centrée dans le Canvas

    # Ajouter le Canvas à la grille
    canvas.grid(row=0, column=0, padx=10, pady=10, rowspan=8, sticky='nsew')

    # Création du label lblEquipe
    lblEquipe = Label(frmImage, text="Équipe (no.Joueur): ", font=("Courrier", 15), fg=fg, bg=bg)
    lblEquipe.grid(row=0, column=1, sticky='e')

    # Création du label lblPosition
    lblPosition = Label(frmImage, text="Position: ", font=("Courrier", 15), fg=fg, bg=bg)
    lblPosition.grid(row=1, column=1, sticky='e')

    # Création du label lblDateNaissance
    lblDateNaissance = Label(frmImage, text="Date de naissance: ", font=("Courrier", 15), fg=fg, bg=bg)
    lblDateNaissance.grid(row=2, column=1, pady=10, sticky='e')

    # Création du label lbllieuNaissance
    lbllieuNaissance = Label(frmImage, text="Lieu de naissance: ", font=("Courrier", 15), fg=fg, bg=bg)
    lbllieuNaissance.grid(row=3, column=1, pady=10, sticky='e')

    # Création du label lblTaille
    lblTaille = Label(frmImage, text="Taille: ", font=("Courrier", 15), fg=fg, bg=bg)
    lblTaille.grid(row=4, column=1, pady=10, sticky='e')

    # Création du label lblPoids
    lblPoids = Label(frmImage, text="Poids: ", font=("Courrier", 15), fg=fg, bg=bg)
    lblPoids.grid(row=5, column=1, pady=10, sticky='e')

    # Création des champs texte
    lblNomequipe = Label(frmImage, text="Canadiens de Montréal (22)", font=("Courrier", 15), fg='blue', bg=bg)
    lblNomequipe.grid(row=0, column=2, sticky='w')

    lblPosition = Label(frmImage, text="Ailier gauche", font=("Courrier", 15), fg='blue', bg=bg)
    lblPosition.grid(row=1, column=2, sticky='w')

    lblDateNaissance = Label(frmImage, text="2 janvier 2001", font=("Courrier", 15), fg='blue', bg=bg)
    lblDateNaissance.grid(row=2, column=2, sticky='w')

    lbllieuNaissance = Label(frmImage, text="Stevens Point, Wisconsin, États-Unis", font=("Courrier", 15), fg='blue',
                             bg=bg)
    lbllieuNaissance.grid(row=3, column=2, sticky='w')

    lblTaille = Label(frmImage, text="172 cm (5 pieds 8 pouces)", font=("Courrier", 15), fg='blue', bg=bg)
    lblTaille.grid(row=4, column=2, sticky='w')

    lblPoids = Label(frmImage, text="79 kg (175 livres)", font=("Courrier", 15), fg='blue', bg=bg)
    lblPoids.grid(row=5, column=2, sticky='w')

    # Boucle principale
    w.mainloop()
