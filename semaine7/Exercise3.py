import random
import time
import tkinter as tk
from tkinter import ttk, DISABLED


def calculer():
    total = 0
    option_value = Option.get()
    print(Option.get())
    if option_value == 1:
        lblTitreSymbole.config(text="+")
        total = int(entry.get()) + int(entry2.get())
        print(total)
        return total
    elif option_value == 2:
        total = int(entry.get()) - int(entry2.get())
        lblTitreSymbole.config(text="-")
        return total
    elif option_value == 3:
        total = int(entry.get()) * int(entry2.get())
        lblTitreSymbole.config(text="*")
        return total
    elif option_value == 4:
        total = int(entry.get()) / int(entry2.get())
        lblTitreSymbole.config(text="/")
        return total


def temps():
    temps_actuel = int(time.time() * 1000)
    Btn3.configure(state="disabled")
    Btn2.configure(state="normal")
    Btn1.configure(state="normal")
    Btn4.configure(state="normal")


def verif():
    total = calculer()
    print(total)
    tot = entryTotal.get()

    if total == (int)(tot):
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")


def generer_nombre():
    niveau = lsdNiveau.get()
    if niveau == "Niveau 1":
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry.insert(0, random.randint(1, 10))
        entry2.insert(0, random.randint(1, 10))
    elif niveau == "Niveau 2":
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry.insert(0, random.randint(1, 100))
        entry2.insert(0, random.randint(1, 100))
    elif niveau == "Niveau 3":
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry.insert(0, random.randint(1, 1000))
        entry2.insert(0, random.randint(1, 1000))
    else:
        raise ValueError("Niveau de difficulté invalide")


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Jeu de math")
    window.geometry("700x520")
    # window.resizable(False, False)

    frmW = tk.Frame(window)
    frmW.pack()
    mystr = tk.StringVar()
    mystr.set("0")
    frmW2 = tk.Frame(frmW)
    frmW2.pack()
    frmwv2 = tk.Frame(frmW2)
    frmwv2.grid(row=0, column=0)
    FrmRadioBTn = tk.LabelFrame(frmwv2, text="")
    FrmRadioBTn.grid(row=1, column=0, padx=10, pady=10, sticky="n")

    Option = tk.IntVar()
    opt_1 = tk.Radiobutton(FrmRadioBTn, text="Addition", font=("Courrier", 20), value=1, justify="left",
                           command=calculer, variable=Option)
    opt_1.select()
    opt_1.grid(row=0, column=0, sticky="w", pady=10)
    opt_1.select()
    opt_2 = tk.Radiobutton(FrmRadioBTn, text="Soustraction", font=("Courrier", 20), value=2, justify="left",
                           command=calculer, variable=Option)
    opt_2.grid(row=1, column=0, sticky="w", pady=10)
    opt_3 = tk.Radiobutton(FrmRadioBTn, text="Multiplication", font=("Courrier", 20), value=3, justify="left",
                           command=calculer, variable=Option)
    opt_3.grid(row=2, column=0, sticky="w", pady=10)
    opt_4 = tk.Radiobutton(FrmRadioBTn, text="Division", font=("Courrier", 20), value=4, justify="left",
                           command=calculer, variable=Option)
    opt_4.grid(row=3, column=0, sticky="w", pady=10)

    FrmCalcul = tk.LabelFrame(frmW2, text="A vous de jouer")
    FrmCalcul.grid(row=0, column=1, padx=10, pady=10)

    lblTitreSymbole = tk.Label(FrmCalcul, text="+", font=("Courrier", 50))
    lblTitreSymbole.grid(row=0, column=0)

    entry = tk.Entry(FrmCalcul, font=("Courrier", 20), width=7)
    entry.insert(0, '6')
    entry.grid(row=0, column=1)

    entry2 = tk.Entry(FrmCalcul, font=("Courrier", 20), width=7)
    entry2.focus_set()
    entry2.insert(0, '3')
    entry2.grid(row=1, column=1)

    lblTitre = tk.Label(FrmCalcul, text="____", font=("Courrier", 50))
    lblTitre.grid(row=2, column=1, pady=10)

    entryTotal = tk.Entry(FrmCalcul, font=("Courrier", 20), width=7)
    entryTotal.grid(row=3, column=1)

    Img = tk.PhotoImage(file="JeanBanlaire.png").zoom(14).subsample(50)
    canvas = tk.Canvas(FrmCalcul, width=200, height=200)
    canvas.create_image(50, 50, image=Img)
    canvas.grid(row=0, column=2, rowspan=4, columnspan=2, padx=10, pady=10)

    Btn1 = tk.Button(FrmCalcul, text="Ok", font=("Courrier", 15), width=10, command=verif)
    Btn1.grid(row=4, column=2)
    Btn2 = tk.Button(FrmCalcul, text="Passe", font=("Courrier", 15), width=10)
    Btn2.grid(row=4, column=3, padx=10, pady=10)

    liste = ("Niveau 1", "Niveau 2", "Niveau 3")
    lsdNiveau = ttk.Combobox(frmwv2, values=liste, font=("Courrier", 15), state="readonly", width=15,
                             postcommand=generer_nombre)
    lsdNiveau.current(0)
    lsdNiveau.grid(row=2, column=0)

    frmBtn = tk.Frame(frmW)
    frmBtn.pack()

    labfrm = tk.Frame(frmBtn)
    labfrm.grid(row=0, column=0)

    chk = tk.Checkbutton(labfrm, text="Voir les statistiques", font=("Courrier", 10), onvalue=1, offvalue=0, width=30)
    chk.grid(row=0, column=0)

    Btn3 = tk.Button(labfrm, text="Commencer", font=("Courrier", 15), width=10)
    Btn3.grid(row=0, column=3, padx=10, pady=10)
    Btn4 = tk.Button(labfrm, text="Effacer statistiques", font=("Courrier", 15), width=15)
    Btn4.grid(row=0, column=4, padx=10, pady=10)
    Btn5 = tk.Button(labfrm, text="Quitter", font=("Courrier", 15), width=5)
    Btn5.grid(row=0, column=5, padx=10, pady=10)

    frmBas = tk.Frame(frmW)
    frmBas.pack()

    FrmStat = tk.LabelFrame(frmBas, text="Réponse")
    FrmStat.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    lblnom = tk.Label(FrmStat, text="Bonne ", font=("Courrier", 10))
    lblnom.grid(row=0, column=0)
    lblmau = tk.Label(FrmStat, text="Mauvaise ", font=("Courrier", 10))
    lblmau.grid(row=0, column=1)
    lbltot = tk.Label(FrmStat, text="Total ", font=("Courrier", 10))
    lbltot.grid(row=0, column=2)

    entrynom = tk.Entry(FrmStat, font=("Courrier", 10), justify="center", textvariable=mystr, state=DISABLED, width=15)
    entrynom.insert(0, '0')
    entrynom.grid(row=1, column=0, padx=10, pady=10)

    entrymau = tk.Entry(FrmStat, font=("Courrier", 10), justify="center", textvariable=mystr, state=DISABLED, width=15)
    entrymau.insert(0, '0')
    entrymau.grid(row=1, column=1, padx=10, pady=10)
    entrytot = tk.Entry(FrmStat, font=("Courrier", 10), justify="center", textvariable=mystr, state=DISABLED, width=15)
    entrytot.insert(0, '0')
    entrytot.grid(row=1, column=2, padx=10, pady=10)

    Lbf = tk.LabelFrame(frmBas, text="Temps")
    Lbf.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tempm = tk.Label(Lbf, text="Temps moyen ", font=("Courrier", 10))

    tempm.grid(row=0, column=0)
    tempt = tk.Label(Lbf, text="Temps total ", font=("Courrier", 10))
    tempt.grid(row=0, column=1)

    entrynom = tk.Entry(Lbf, font=("Courrier", 10), justify="center", textvariable=mystr, state=DISABLED, width=15)

    entrynom.grid(row=1, column=0, padx=10, pady=10)
    entrymau = tk.Entry(Lbf, font=("Courrier", 10), justify="center", textvariable=mystr, state=DISABLED, width=15)
    entrymau.insert(0, '0')
    entrymau.grid(row=1, column=1, padx=10, pady=10)

    window.mainloop()
