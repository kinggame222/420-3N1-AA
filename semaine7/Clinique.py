from tkinter import *
from tkinter import ttk, messagebox

from tkcalendar import DateEntry

from semaine7 import hopital
import json


def lirefichier():
    valeur = []
    with open("employe.json", "r") as f:
        valeur = json.load(f)
    return valeur


base = 1


def choix(bouton):
    global base
    if bouton == "gauche":
        base = int(base - 1)

    elif bouton == "gauche2":
        base = 1
    elif bouton == "droite":
        base = int(base + 1)
    elif bouton == "droite2":
        base = list(lirefichier().keys())[-1]
    else:
        base = base
    return base


def valider():
    with open("usager.txt", "r") as f:
        valeur = f.readlines()

    if hopital.txtNom.get() == valeur[0].strip('\n') and hopital.txtMDP.get() == valeur[1]:
        hopital.window.destroy()
    else:
        messagebox.showerror("Erreur", "Nom d'usager ou mot de passe invalide")


def afficher(bouton):
    valeur = lirefichier()
    str_base = str(choix(bouton))  # Convertissez base en chaîne de caractères
    if str_base in valeur:
        txtNom.config(state="normal")
        txtAddre.config(state="normal")
        txtTel.config(state="normal")
        txtDate.config(state="normal")
        txtNum.config(state="normal")
        chk1.deselect()
        chk2.deselect()
        chk3.deselect()

        txtNom.delete(0, END)
        txtAddre.delete(0, END)
        txtTel.delete(0, END)
        txtDate.delete(0, END)
        txtNum.delete(0, END)

        txtNom.insert(0, valeur[str_base]["nom"])
        txtAddre.insert(0, valeur[str_base]["adresse"])
        txtTel.insert(0, valeur[str_base]["telephone"])
        txtDate.insert(0, valeur[str_base]["dateNaissance"])
        txtNum.insert(0, base)
        radiobtn.set(valeur[str_base]["salaire"])
        if valeur[str_base]["salaire"] == 0:
            opt_1.select()
        val = valeur[str_base]["dispo"]
        if val[0] == 1:
            chk1.select()
        if val[1] == 1:
            chk2.select()
        if val[2] == 1:
            chk3.select()

        txtNom.config(state="readonly")
        txtAddre.config(state="readonly")
        txtTel.config(state="readonly")
        txtDate.config(state="readonly")
        txtNum.config(state="readonly")


def ajouter():
    txtNom.config(state="normal")
    txtAddre.config(state="normal")
    txtTel.config(state="normal")
    txtDate.config(state="normal")
    txtNum.config(state="normal")

    txtNom.delete(0, END)
    txtAddre.delete(0, END)
    txtTel.delete(0, END)
    txtDate.delete(0, END)
    txtNum.delete(0, END)

    nnum = int(list(lirefichier().keys())[-1]) + 1
    txtNum.insert(0, nnum)
    txtNom.focus()
    btnDroite.configure(state="disabled")
    btnDroite2.configure(state="disabled")
    btnGauche.configure(state="disabled")
    btnGauchex2.configure(state="disabled")

    btnAjouter.configure(text="Sauvegarder", command=sauvegarder)

    pass


def sauvegarder():
    valeur = lirefichier()

    str_base = int(choix("droite2"))
    str_base += 1

    valeur[str_base] = {}
    valeur[str_base]["nom"] = txtNom.get()
    valeur[str_base]["adresse"] = txtAddre.get()
    valeur[str_base]["telephone"] = txtTel.get()
    valeur[str_base]["dateNaissance"] = txtDate.get()
    valeur[str_base]["salaire"] = radiobtn.get()
    val = [0, 0, 0]
    if var1.get() == 1:
        val[0] = True
    else:
        val[0] = False
    if var2.get() == 1:
        val[1] = True
    else:
        val[1] = False
    if var3.get() == 1:
        val[2] = True
    else:
        val[2] = False

    valeur[str_base]["dispo"] = val
    with open("employe.json", "w") as f:
        json.dump(valeur, f)
    btnDroite.configure(state="normal")
    btnDroite2.configure(state="normal")
    btnGauche.configure(state="normal")
    btnGauchex2.configure(state="normal")
    btnAjouter.configure(text="Ajouter", command=ajouter)

    pass


def sauvegarderModif():
    valeur = lirefichier()
    str_base = str(base)
    valeur[str_base]["nom"] = txtNom.get()
    valeur[str_base]["adresse"] = txtAddre.get()
    valeur[str_base]["telephone"] = txtTel.get()
    valeur[str_base]["dateNaissance"] = txtDate.get()
    valeur[str_base]["salaire"] = radiobtn.get()
    val = [0, 0, 0]
    if var1.get() == 1:
        val[0] = True
    else:
        val[0] = False
    if var2.get() == 1:
        val[1] = True
    else:
        val[1] = False
    if var3.get() == 1:
        val[2] = True
    else:
        val[2] = False

    valeur[str_base]["dispo"] = val
    with open("employe.json", "w") as f:
        json.dump(valeur, f)
    btnDroite.configure(state="normal")
    btnDroite2.configure(state="normal")
    btnGauche.configure(state="normal")
    btnGauchex2.configure(state="normal")
    btnAjouter.configure(text="Ajouter", command=ajouter)
    pass


def modifier():
    txtNom.config(state="normal")
    txtAddre.config(state="normal")
    txtTel.config(state="normal")
    txtDate.config(state="normal")
    txtNum.config(state="normal")
    btnDroite.configure(state="disabled")
    btnDroite2.configure(state="disabled")
    btnGauche.configure(state="disabled")
    btnGauchex2.configure(state="disabled")
    btnAjouter.configure(text="Sauvegarder", command=sauvegarderModif)


def supprimer():
    valeur = lirefichier()
    str_base = str(base)
    try:
        del valeur[str_base]
    except KeyError:
        print("Aucun employé n'est sélectionné")
    try:
        del valeur[base]
    except KeyError:
        print("Aucun employé n'est sélectionné")

    with open("employe.json", "w") as f:
        json.dump(valeur, f)
    btnDroite.configure(state="normal")
    btnDroite2.configure(state="normal")
    btnGauche.configure(state="normal")
    btnGauchex2.configure(state="normal")
    btnAjouter.configure(text="Ajouter", command=ajouter)
    afficher(1)


if __name__ == '__main__':
    window = Tk()

    window.title("Hopital d'Alma")
    window.geometry("800x400")
    window.resizable(False, False)
    photo = PhotoImage(file="amg.ico")
    window.iconphoto(False, photo)
    bg = "lightgray"
    window.config(background=bg)

    frmW = Frame(window)
    frmW.config(background=bg)

    lblTitre = LabelFrame(frmW, text="Employé", font=("Courrier", 20), background=bg)
    lblTitre.grid(row=0, column=0, padx=10, pady=0, sticky="nw", rowspan=2)

    lblNum = Label(lblTitre, text="Numéro :", font=("Courrier", 15), background=bg, justify="right")
    lblNum.grid(row=0, column=0, padx=0, pady=10, sticky="w")

    lblNom = Label(lblTitre, text="Nom :", font=("Courrier", 15), background=bg, justify="right")
    lblNom.grid(row=1, column=0, padx=0, pady=10, sticky="w")

    lblAddre = Label(lblTitre, text="Addresse :", font=("Courrier", 15), background=bg, justify="right")
    lblAddre.grid(row=2, column=0, padx=0, pady=10, sticky="w")

    lblTel = Label(lblTitre, text="Téléphone :", font=("Courrier", 15), background=bg, justify="right")
    lblTel.grid(row=3, column=0, padx=0, pady=10, sticky="w")

    lblTel = Label(lblTitre, text="Téléphone :", font=("Courrier", 15), background=bg, justify="right")
    lblTel.grid(row=3, column=0, padx=0, pady=10, sticky="w")

    lbtdate = Label(lblTitre, text="Date de naissance :", font=("Courrier", 15), background=bg, justify="right")
    lbtdate.grid(row=4, column=0, padx=0, pady=0, sticky="w")

    txtNum = Entry(lblTitre, font=("Courrier", 20), justify="center", background=bg, width=15)
    txtNum.grid(row=0, column=1, padx=0, pady=14)

    txtNom = Entry(lblTitre, font=("Courrier", 20), justify="center", background=bg, width=15)
    txtNom.grid(row=1, column=1, padx=0, pady=0)

    txtAddre = Entry(lblTitre, font=("Courrier", 20), justify="center", background=bg, width=15)
    txtAddre.grid(row=2, column=1, padx=0, pady=0)

    txtTel = Entry(lblTitre, font=("Courrier", 20), justify="center", background=bg, width=15)
    txtTel.grid(row=3, column=1, padx=0, pady=0)

    txtDate = DateEntry(lblTitre, font=("Courrier", 20), justify="center", background='black', width=10)
    txtDate.grid(row=4, column=1, padx=0, pady=13)

    lblTitre2 = LabelFrame(frmW, text="Échelle salarial", font=("Courrier", 20), background=bg)
    lblTitre2.grid(row=0, column=1, padx=5, pady=0, sticky="n")

    radiobtn = IntVar()
    opt_1 = Radiobutton(lblTitre2, text="moins de 10 000$", font=("Courrier", 12), value=1, justify="left",
                        variable=radiobtn, background=bg)
    opt_1.grid(row=0, column=0, sticky="w", pady=0)

    opt_2 = Radiobutton(lblTitre2, text="entre 10 000$ et 30 000$", font=("Courrier", 12), value=2, justify="left",
                        variable=radiobtn, background=bg)
    opt_2.select()
    opt_2.grid(row=1, column=0, sticky="w", pady=0)

    opt_3 = Radiobutton(lblTitre2, text="entre 30 001$ et 65 000$", font=("Courrier", 12), value=3, justify="left",
                        variable=radiobtn, background=bg)
    opt_3.grid(row=2, column=0, sticky="w", pady=0)

    opt_4 = Radiobutton(lblTitre2, text="plus de 65 000$", font=("Courrier", 12), value=4, justify="left",
                        variable=radiobtn, background=bg)
    opt_4.grid(row=3, column=0, sticky="w", pady=0)

    lblTitre3 = LabelFrame(frmW, text="Disponibilité", font=("Courrier", 20), background=bg, width=15)
    lblTitre3.grid(row=1, column=1, padx=0, pady=0, sticky="n")

    chkbtn2 = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    chk1 = Checkbutton(lblTitre3, text="8 h 00 à 16 h 00                ", font=("Courrier", 12), justify="center",
                       background=bg, variable=var1, onvalue=1, offvalue=0)
    chk1.grid(row=0, column=0, sticky="w", pady=5)

    chk2 = Checkbutton(lblTitre3, text="16 h 00 à 00 h 00", font=("Courrier", 12), justify="left",
                       background=bg, variable=var2, onvalue=1, offvalue=0)
    chk2.grid(row=1, column=0, sticky="w", pady=4)

    chk3 = Checkbutton(lblTitre3, text="00 h 00 à 8 h 00", font=("Courrier", 12), justify="left",
                       background=bg, variable=var3, onvalue=1, offvalue=0)
    chk3.grid(row=2, column=0, sticky="w", pady=0)

    btnframe = Frame(frmW)
    btnframe.config(background=bg)
    btnframe.grid(row=0, column=2, padx=5, pady=10, sticky="w")

    btnAjouter = Button(btnframe, text="Ajouter", font=("Courrier", 15), background=bg, width=10, command=ajouter)
    btnAjouter.grid(row=0, column=0, padx=0, pady=5, sticky="n")

    btnModifier = Button(btnframe, text="Modifier", font=("Courrier", 15), background=bg, width=10, command=modifier)
    btnModifier.grid(row=1, column=0, padx=0, pady=5, sticky="n")

    btnSupprimer = Button(btnframe, text="Supprimer", font=("Courrier", 15), background=bg, width=10, command=supprimer)
    btnSupprimer.grid(row=2, column=0, padx=0, pady=5, sticky="n")

    lblbtn = Frame(frmW)
    lblbtn.config(background=bg)
    lblbtn.grid(row=2, column=0, padx=10, pady=10, sticky='n', columnspan=4)

    btnGauchex2 = Button(lblbtn, text="<<", font=("Courrier", 15), background=bg, width=10,
                         command=lambda: afficher("gauche2"))
    btnGauchex2.grid(row=0, column=0, sticky='nesw', rowspan=2, padx=0)

    btnGauche = Button(lblbtn, text="<", font=("Courrier", 15), background=bg, width=10,
                       command=lambda: afficher("gauche"))
    btnGauche.grid(row=0, column=2, sticky='nesw', rowspan=2, padx=30)

    btnDroite = Button(lblbtn, text=">", font=("Courrier", 15), background=bg, width=10,
                       command=lambda: afficher("droite"))
    btnDroite.grid(row=0, column=4, sticky='nesw', rowspan=2, padx=25)

    btnDroite2 = Button(lblbtn, text=">>", font=("Courrier", 15), background=bg, width=10,
                        command=lambda: afficher("droite2"))
    btnDroite2.grid(row=0, column=6, sticky='nesw', rowspan=2, padx=30)

    btnQuitter = Button(lblbtn, text="Quitter", font=("Courrier", 15), background=bg, width=10, command=window.destroy)
    btnQuitter.grid(row=0, column=8, sticky='e', rowspan=2, padx=0)

    frmW.pack()
    afficher(1)

    window.mainloop()
