from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    # Création de la fenêtre principale (main window)
    w = Tk()

    bg = "DarkOrchid4"
    fg = "white"
    w.title("Mon deuxième programme")
    w.geometry("800x600")
    w.iconbitmap("jeuxAlma.ico")

    frmW = Frame(w, bg="red", bd=1, border=2)
    frmW.pack()

    fdsBoutonRadio = LabelFrame(frmW, text="Radio bouton")
    fdsBoutonRadio.grid(row=0, column=0)
    fdsBoutonRadio.pack(expand="no", side=TOP)

    lblTitre = Label(frmW, text="Nom a insérer", font=("Courrier", 40), fg=fg, bg=bg)
    lblTitre.pack(padx=20, pady=20)

    txtNom = Entry(frmW, font=("Courrier", 25), bg='Red1', fg=fg, justify="center")
    txtNom.insert(0, 'Nom')
    txtNom.pack(padx=20, pady=20)

    btn = Button(frmW, text="Cliquez ici", font=("Courrier", 25), bg='RoyalBlue3', fg=fg)
    btn.pack(padx=20, pady=20)

    largeur = 500 / 3
    imgImage = PhotoImage(file="Exercice/1.png").zoom(15).subsample(80)
    canvas = Canvas(frmW, width=largeur, height=largeur)
    canvas.create_image(largeur / 2, largeur / 2, image=imgImage)
    canvas.pack()
    chkTPS = Checkbutton(frmW, text="TPS", font=("Courrier", 25), onvalue=1, offvalue=0)
    chkTPS.select()
    chkTPS.pack(padx=20, pady=20)
    chkTVQ = Checkbutton(frmW, text="TVQ", font=("Courrier", 25), onvalue=1, offvalue=0)
    chkTVQ.pack(padx=20, pady=20)

    Option = IntVar()
    opt_1 = Radiobutton(fdsBoutonRadio, text="oui", font=("Courrier", 20), value=1, variable=Option)
    opt_1.grid(row=0, column=0)
    opt_1.select()
    opt_2 = Radiobutton(fdsBoutonRadio, text="non", font=("Courrier", 20), value=2, variable=Option)
    opt_2.grid(row=1, column=1)
    opt_3 = Radiobutton(fdsBoutonRadio, text="wtf", font=("Courrier", 20), value=3, variable=Option)
    opt_3.grid(row=2, column=2)

    liste = ("Python", "C++", "Java", "PHP", "HTML", "CSS", "JavaScript", "C#")
    lsd = ttk.Combobox(frmW, values=liste, font=("Courrier", 20), state="readonly")
    lsd.current(0)
    lsd.pack()

    menuBar = Menu(w)

    filemenu = Menu(menuBar, tearoff=0)

    filemenu.add_command(label="Fichier")

    menuBar.add_separator()

    editmenu = Menu(menuBar, tearoff=0)

    menuBar.add_separator()
    editmenu.add_command(label="Undo")
    editmenu.add_command(label="Cut")
    editmenu.add_command(label="Copy")
    editmenu.add_command(label="Paste")
    editmenu.add_command(label="Delete")
    editmenu.add_command(label="Select All")
    w.config(menu=menuBar)

    w.mainloop()
