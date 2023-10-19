from tkinter import *

from tkcalendar import DateEntry
import Clinique

window = Tk()

window.title("Hopital Alma")
window.geometry("300x150")
window.resizable(False, False)
bg = "lightgray"
window.config(background=bg)
photo = PhotoImage(file="amg.ico")
window.iconphoto(False, photo)

frmW = Frame(window)
frmW.config(background=bg)

LblNom = Label(frmW, text="Nom d'usager :", font=("Courrier", 12), background=bg, justify="right")
LblNom.grid(row=0, column=0, padx=0, pady=0)

lblMDP = Label(frmW, text="Mot de passe :", font=("Courrier", 12), justify="right", background=bg)
lblMDP.grid(row=1, column=0, padx=0, pady=0)

txtNom = Entry(frmW, font=("Courrier", 12), justify="center")
txtNom.grid(row=0, column=1, padx=0, pady=0)

txtMDP = Entry(frmW, font=("Courrier", 12), justify="center", show="*")
txtMDP.grid(row=1, column=1, padx=0, pady=0)

btnConnexion = Button(frmW, text="Connexion", font=("Courrier", 12), background=bg, command=Clinique.valider)
btnConnexion.grid(row=2, column=0, padx=0, pady=10)

btnQuitter = Button(frmW, text="Quitter", font=("Courrier", 12), command=window.destroy, justify="left", background=bg)
btnQuitter.grid(row=2, column=1, padx=10, pady=10, sticky="w")

frmW.pack(padx=20, pady=20)

window.mainloop()
