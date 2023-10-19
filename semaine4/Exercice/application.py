import tkinter as tk
from tkinter import ttk


from PIL import  Image


def couleur():
    if Option.get() == 0:
        fg1 = "red"
        lblTitre.config(fg=fg1)

    elif Option.get() == 1:
        fg1 = "blue"
        lblTitre.config(fg=fg1)
    elif Option.get() == 2:
        fg1 = "green"
        lblTitre.config(fg=fg1)


def Majuscule():
    lblTitre.config(text=lblTitre.cget("text").upper())


def Minuscule():
    lblTitre.config(text=lblTitre.cget("text").lower())


def messageSecret():
    lblTitre.config(text="You have been gnome'd")
    imgJB = tk.PhotoImage(file="C:/Users/202130861/420-3N1-AA/semaine4/Exercice/1.png")
    canvas.itemconfig(1, image=imgJB)
    window.after(5000)
    canvas.itemconfig(1, state="normal")
    lblTitre.config(text="Enfin les vacances sont terminées !")


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Fin des Vacances")
    window.geometry("800x600")
    window.resizable(False, False)

    frmW = tk.Frame(window)
    frmW.pack()

    lblTitre = tk.Label(frmW,
                        text="Enfin les vacances sont terminées !",
                        font=("Courrier", 20, "bold", "italic"),
                        fg='red')
    lblTitre.grid(row=0, column=0, sticky="w")

    largeur = 500 / 3
    imgJB = tk.PhotoImage(file="JeanBanlaire.png").zoom(15).subsample(80)
    canvas = tk.Canvas(frmW, width=largeur, height=largeur)
    canvas.create_image(largeur / 2, largeur / 2, image=imgJB)
    canvas.itemconfig(1, state="hidden")
    canvas.grid(row=1, column=0, sticky="n")

    fdsBoutonRadio = tk.LabelFrame(frmW, text="Couleur")
    fdsBoutonRadio.grid(row=2, column=0)

    Option = tk.IntVar()
    opt_1 = tk.Radiobutton(fdsBoutonRadio, text="Rouge", font=("Courrier", 20), value=0, variable=Option,
                           command=couleur)
    opt_1.grid(row=0, column=0)
    opt_1.select()
    opt_2 = tk.Radiobutton(fdsBoutonRadio, text="Bleu", font=("Courrier", 20), value=1, variable=Option,
                           command=couleur)
    opt_2.grid(row=0, column=1)
    opt_3 = tk.Radiobutton(fdsBoutonRadio, text="Vert", font=("Courrier", 20), value=2, variable=Option,
                           command=couleur)
    opt_3.grid(row=0, column=2)
    var = Option.get()
    fdsLabel = tk.LabelFrame(frmW)
    fdsLabel.grid(row=3, column=0, pady=20)
    label1 = tk.Label(fdsLabel, text="Bordure", font=("Courrier", 20), border=1)
    label1.grid(row=1, column=0, sticky="n")
    label2 = tk.Label(fdsLabel, text="Pas Bordure", font=("Courrier", 20), border=1, relief="groove")
    label2.grid(row=1, column=1, sticky="n")

    fdsLabel2 = tk.LabelFrame(frmW)
    fdsLabel2.grid(row=4, column=0, pady=20)
    label3 = tk.Button(fdsLabel2, text="Maj", font=("Courrier", 20), border=1, command=Majuscule)
    label3.grid(row=1, column=0, sticky="n")
    label4 = tk.Button(fdsLabel2, text="Min", font=("Courrier", 20), border=1, command=Minuscule)
    label4.grid(row=1, column=1, sticky="n")
    label5 = tk.Button(fdsLabel2, text="Sec", font=("Courrier", 20), border=1, command=messageSecret)
    label5.grid(row=1, column=2, sticky="n", padx=10)
    label6 = tk.Button(fdsLabel2, text="Img", font=("Courrier", 20), border=1)
    label6.grid(row=1, column=3, sticky="n")

    window.mainloop()
