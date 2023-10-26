'''
Nom: william bouchard
Date: 2023-10-23
Description: page de connection
'''

import datetime
import subprocess
import tkinter
from tkinter import *
import Commande


def date():
    now = datetime.datetime.now()
    lblDate.config(text=now.strftime("%d-%m-%Y"))


def connexion():
    with open("login.txt", "r") as f:
        mdp = f.read()
    if txtMDP.get() == mdp:
        window.destroy()
        subprocess.call(["python", "-m", "semaine7.Sommatif2.Commande"])
    else:
        lblMDP.config(text="Mot de passe : ", font=("Courrier", 12), fg="red")


if __name__ == '__main__':
    window = Tk()

    window.title("Pizza en Folie - Connexion")
    window.geometry("620x320")
    window.resizable(False, False)
    window.iconbitmap("pizza.ico")

    frmW = Frame(window)

    imgPizzaG = tkinter.PhotoImage(file="pizza.png").zoom(5).subsample(80)
    canvas = Canvas(frmW, width=200, height=200)
    canvas.create_image(100, 100, image=imgPizzaG)
    canvas.grid(row=0, column=0)

    FrmDate = Frame(frmW)

    lblTitre = Label(FrmDate, text="PIZZA en FOLIE", font=("Courrier", 20, "bold"))
    lblTitre.grid(row=0, column=0)

    lblDate = Label(FrmDate, text="1", font=("Courrier", 20, "bold"))
    lblDate.grid(row=1, column=0)

    FrmDate.grid(row=0, column=1)

    imgPizzaD = tkinter.PhotoImage(file="pizza.png").zoom(5).subsample(80)
    canvas = Canvas(frmW, width=200, height=200)
    canvas.create_image(100, 100, image=imgPizzaD)

    ligne = Canvas(frmW)
    ligne.create_line(0, 0, 618, 0, width=10)
    ligne.grid(row=2, column=0, columnspan=3, sticky="we")

    canvas.grid(row=0, column=2)

    FrmMDP = Frame(frmW)

    lblMDP = Label(FrmMDP, text="Mot de passe : ", font=("Courrier", 12))
    lblMDP.grid(row=0, column=0, sticky="n")

    txtMDP = Entry(FrmMDP, font=("Courrier", 12), show="*", width=10)
    txtMDP.grid(row=0, column=1, sticky="n")

    FrmMDP.grid(row=2, column=1, sticky="new", pady=20)

    BtnConnexion = Button(FrmMDP, text="Connexion", font=("Courrier", 12), width=10, command=connexion)
    BtnConnexion.grid(row=1, columnspan=2, sticky="ew", pady=10)

    frmW.grid(row=0, column=0, sticky="ew")

    date()
    window.mainloop()
