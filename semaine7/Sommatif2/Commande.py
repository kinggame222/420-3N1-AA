'''
Nom: william bouchard
Date: 2023-10-23
description: la page commande
'''

import tkinter
from tkinter import *
import datetime
from tkinter import ttk
import json

from IPython.terminal.pt_inputhooks import tk


def date():
    now = datetime.datetime.now()
    lblDate.config(text=now.strftime("%d-%m-%Y"))


def lirefichier():
    valeur = []
    with open("commandePizza.json", "r") as f:
        valeur = json.load(f)
    return valeur


def Sauvegarderjson():
    if txtNom.get() == "" or txtTel.get() == "":
        lblNom.config(text="Nom : *", font=("Courrier", 12), fg="red")
        txtNom.focus()
    else:
        lblNom.config(text="Nom : *", font=("Courrier", 12), fg="black")

    if txtTel.get() == "":
        lblTel.config(text="Téléphone : *", font=("Courrier", 12), fg="red")
        txtTel.focus()
    else:
        lblTel.config(text="Téléphone : *", font=("Courrier", 12), fg="black")
        save()


def save():
    try:
        calculerfacture()
        commandePizza = lirefichier()
        nfacture = f"facture-{len(commandePizza) + 1}"

        commandePizza[nfacture] = {}
        commandePizza[nfacture]["Nom"] = txtNom.get()
        commandePizza[nfacture]["Adresse"] = txtAdresse.get()
        commandePizza[nfacture]["Courriel"] = txtCourriel.get()
        commandePizza[nfacture]["Telephone"] = txtTel.get()
        commandePizza[nfacture]["Quantite"] = lblPizza.get()
        commandePizza[nfacture]["Dimension"] = Option.get()
        commandePizza[nfacture]["Assaisonnement"] = [var1.get(), var2.get(), var3.get(), var4.get()]
        commandePizza[nfacture]["Temps"] = lsd.get()
        commandePizza[nfacture]["Total"] = txtTotal.get()

        with open("commandePizza.json", "w") as f:
            json.dump(commandePizza, f, indent=4)

        annuler()
    except:
        print("erreur dans la sauvegarde")


def annuler():
    txtNom.delete(0, END)
    txtAdresse.delete(0, END)
    txtCourriel.delete(0, END)
    txtTel.delete(0, END)
    lblPizza.delete(0, END)
    txtTotal.delete(0, END)
    txtNom.focus()

    lblPizza.delete(0, END)
    lblPizza.insert(0, 1)

    lblTotal.config(text="Total: ", font=("Courrier", 12))
    txtTotal.config(state="normal")
    txtTotal.delete(0, END)
    txtTotal.config(state="readonly")

    chkAnchois.deselect()
    chkChamp.deselect()
    chkOgnion.deselect()
    chkPV.deselect()
    opt_1.select()


def calculerfacture():
    total = 0
    option_value = Option.get()

    if option_value == 1:
        total = 6.99
        if var1.get() == 1:
            total += 0.75

        if var2.get() == 1:
            total += 0.75

        if var3.get() == 1:
            total += 0.75

        if var4.get() == 1:
            total += 0.75

    elif option_value == 2:
        total = 9.99
        if var1.get() == 1:
            total += 1

        if var2.get() == 1:
            total += 1

        if var3.get() == 1:
            total += 1

        if var4.get() == 1:
            total += 1

    elif option_value == 3:
        total = 11.99
        if var1.get() == 1:
            total += 1.25

        if var2.get() == 1:
            total += 1.25

        if var3.get() == 1:
            total += 1.25

        if var4.get() == 1:
            total += 1.25

    elif option_value == 4:
        total = 14.99
        if var1.get() == 1:
            total += 1.50

        if var2.get() == 1:
            total += 1.50

        if var3.get() == 1:
            total += 1.50

        if var4.get() == 1:
            total += 1.50

    total = total * int(lblPizza.get())
    total = total * 1.14975
    total = round(total, 2)
    txtTotal.config(state="normal")
    txtTotal.delete(0, END)
    txtTotal.insert(0, total)
    txtTotal.config(state="readonly")


if __name__ == '__main__':
    window = Tk()

    window.title("Pizza en Folie - Commande")
    window.geometry("612x750")
    window.resizable(False, False)
    window.iconbitmap("pizza.ico")

    frmW = Frame(window)

    frmHaut = Frame(frmW)

    imgPizzaG = tkinter.PhotoImage(file="pizza.png").zoom(7).subsample(80)
    canvas = Canvas(frmHaut, width=195, height=195)
    canvas.create_image(100, 100, image=imgPizzaG)
    canvas.grid(row=0, column=0)

    FrmDate = Frame(frmHaut)

    lblTitre = Label(FrmDate, text="PIZZA en FOLIE", font=("Courrier", 20, "bold"))
    lblTitre.grid(row=0, column=0)

    lblDate = Label(FrmDate, text="1", font=("Courrier", 20, "bold"))
    lblDate.grid(row=1, column=0)

    FrmDate.grid(row=0, column=1)

    imgPizzaD = tkinter.PhotoImage(file="pizza.png").zoom(7).subsample(80)
    canvas = Canvas(frmHaut, width=195, height=195)
    canvas.create_image(100, 100, image=imgPizzaD)

    canvas.grid(row=0, column=2)

    frmCommande = Frame(frmW)

    lblPizza = Label(frmCommande, text="Inscrire la commande", font=("Courrier", 20, "bold"))
    lblPizza.grid(row=0, column=0, sticky="ewn", columnspan=2)

    LblfrmCommande = LabelFrame(frmCommande, text="Info-Client", font=("Courrier", 12))

    lblNom = Label(LblfrmCommande, text="Nom :  *", font=("Courrier", 12))
    lblNom.grid(row=0, column=0, sticky="e")

    txtNom = Entry(LblfrmCommande, font=("Courrier", 12), width=50)
    txtNom.grid(row=0, column=1)

    lblAdresse = Label(LblfrmCommande, text="Adresse :    ", font=("Courrier", 12))
    lblAdresse.grid(row=1, column=0, sticky="e")

    txtAdresse = Entry(LblfrmCommande, font=("Courrier", 12), width=50)
    txtAdresse.grid(row=1, column=1)

    lblCourriel = Label(LblfrmCommande, text="Courriel :    ", font=("Courrier", 12))
    lblCourriel.grid(row=2, column=0, sticky="e")

    txtCourriel = Entry(LblfrmCommande, font=("Courrier", 12), width=50)
    txtCourriel.grid(row=2, column=1, sticky="e")

    lblTel = Label(LblfrmCommande, text="Téléphone : *", font=("Courrier", 12))
    lblTel.grid(row=3, column=0, sticky="e")

    txtTel = Entry(LblfrmCommande, font=("Courrier", 12), width=50)
    txtTel.grid(row=3, column=1, sticky="e")

    lblPizza = Label(LblfrmCommande, text="* Champs obligatoire", font=("Courrier", 12))
    lblPizza.grid(row=4, column=0, sticky="w", columnspan=2)

    LblfrmCommande.grid(row=1, column=0, sticky="ewn", padx=10, pady=10)

    frmch = Frame(frmCommande)

    LblfrmCommande2 = LabelFrame(frmch, text="Quantité", font=("Courrier", 12))

    lblPizza = Spinbox(LblfrmCommande2, from_=1, to=25, font=("Courrier", 12), width=5)
    lblPizza.grid(row=0, column=0, sticky="w", padx=40, pady=10)

    LblfrmCommande3 = LabelFrame(frmch, text="Dimension", font=("Courrier", 12))

    Option = IntVar()

    opt_1 = Radiobutton(LblfrmCommande3, text="Petite", font=("Courrier", 12), value=1, variable=Option)
    opt_1.grid(row=0, column=0, sticky="w", padx=40)
    opt_1.select()
    opt_2 = Radiobutton(LblfrmCommande3, text="Moyenne", font=("Courrier", 12), value=2, variable=Option)
    opt_2.grid(row=1, column=0, sticky="w", padx=40)
    opt_3 = Radiobutton(LblfrmCommande3, text="Grande", font=("Courrier", 12), value=3, variable=Option)
    opt_3.grid(row=2, column=0, sticky="w", padx=40)
    opt_4 = Radiobutton(LblfrmCommande3, text="Extra-Grande", font=("Courrier", 12), value=4, variable=Option)
    opt_4.grid(row=3, column=0, sticky="w", padx=40)

    LblfrmCommande4 = LabelFrame(frmch, text="Assaisonnements", font=("Courrier", 12))

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    chkChamp = Checkbutton(LblfrmCommande4, text="Champignons", font=("Courrier", 12), onvalue=1, offvalue=0,
                           variable=var1)
    chkChamp.grid(row=0, column=0, sticky="w")

    chkAnchois = Checkbutton(LblfrmCommande4, text="Anchois", font=("Courrier", 12), onvalue=1, offvalue=0,
                             variable=var2)
    chkAnchois.grid(row=1, column=0, sticky="w")

    chkPV = Checkbutton(LblfrmCommande4, text="Poivrons vert", font=("Courrier", 12), onvalue=1, offvalue=0,
                        variable=var3)
    chkPV.grid(row=2, column=0, sticky="w")

    chkOgnion = Checkbutton(LblfrmCommande4, text="oignion", font=("Courrier", 12), onvalue=1, offvalue=0,
                            variable=var4)
    chkOgnion.grid(row=3, column=0, sticky="w")

    frmTempDePrep = Frame(frmCommande)

    lblTemps = Label(frmTempDePrep, text="La commande sera prete dans", font=("Courrier", 12))
    lblTemps.grid(row=0, column=0, sticky="we", padx=10, pady=10)

    liste = ("15 minutes", "30 minutes", "45 minutes", "1 heure", "2 heures", "3 heures", "4 heures", "5 heures")
    lsd = ttk.Combobox(frmTempDePrep, values=liste, font=("Courrier", 15), state="readonly")
    lsd.current(0)
    lsd.grid(row=0, column=1)

    LblfrmCommande5 = LabelFrame(frmCommande, text="Facture", font=("Courrier", 12))

    lblTotal = Label(LblfrmCommande5, text="Total: ", font=("Courrier", 12))
    lblTotal.grid(row=0, column=0, sticky="w", padx=0)

    txtTotal = Entry(LblfrmCommande5, font=("Courrier", 12), width=10, state="readonly")

    txtTotal.grid(row=0, column=1, sticky="w", padx=0, pady=10)

    btnCalculer = Button(LblfrmCommande5, text="Calculer facture", font=("Courrier", 12), width=20,
                         command=calculerfacture)
    btnCalculer.grid(row=0, column=2, sticky="w", padx=10, pady=10)

    btnQuitter = Button(LblfrmCommande5, text="Annuler", font=("Courrier", 12), width=10, command=annuler)

    btnQuitter.grid(row=0, column=3, sticky="we", padx=10, pady=10)

    bntEnvoyer = Button(frmCommande, text="Envoyer", font=("Courrier", 12), width=10, command=Sauvegarderjson)
    bntEnvoyer.grid(row=5, column=0, sticky="we", padx=10)

    bntQuitter = Button(frmCommande, text="Quitter", font=("Courrier", 12), width=10, command=window.destroy)
    bntQuitter.grid(row=6, column=0, sticky="we", padx=10)

    LblfrmCommande2.grid(row=0, column=0, padx=0, sticky="nsew")
    LblfrmCommande3.grid(row=0, column=1, padx=50, sticky="nsew")
    LblfrmCommande4.grid(row=0, column=2, padx=0, sticky="nsew")
    LblfrmCommande5.grid(row=4, column=0, padx=10, sticky="nsew")

    frmTempDePrep.grid(row=3, column=0, sticky="ew", pady=10)

    frmch.grid(row=2, column=0, sticky="ew", padx=10)
    frmCommande.grid(row=2, column=0, sticky="ewn")
    frmHaut.grid(row=0, column=0, sticky="ew")
    frmW.grid(row=0, column=0, sticky="ew")

    date()
    window.mainloop()
