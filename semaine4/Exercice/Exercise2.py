import tkinter as tk
from tkinter import ttk, messagebox
import time


def heure():
    print(time.strftime("%H:%M:%S:%p"))
    after_id = window.after(1, heure)


def calculer():
    hectare = entryHec.get()
    if isinstance(hectare, int):
        messagebox.showerror("Erreur", "Veuillez entrer un nombre")
        return
    TPS = chkTPS_var.get()
    TPV = chkTPV_var.get()
    liste = lsd.get()
    cout = 0
    print(lsd.current())


    rabais = 0
    if liste == "Mauvaises Herbes (1$/hectare)":
        cout = float(hectare) * 1
    elif liste == "Sauterelles (2$/hectare)":
        cout = float(hectare) * 2
    elif liste == "Vers (3$/hectare)":
        cout = float(hectare) * 3
    elif liste == "Combiné (5$/hectare)":
        cout = float(hectare) * 5

    if TPS == 1:
        tps = cout * 0.05
    else:
        tps = 0
    if TPV == 1:
        tvq = round(cout * 0.09975, 5)

    else:
        tvq = 0
    if float(hectare) > 500:
        rabais = (cout - 500) * 0.15
    else:
        if liste == "Combiné (5$/hectare)":
            rabais = (cout - 500) * 0.25
        elif cout > 1250:
            rabais = (cout - 1250) * 0.40

    if cout > 1000:
        rabais = rabais + (cout - 1000) * 0.05

    print(rabais)
    total = cout + float(tps) + float(tvq)
    entryCout.config(state="normal")
    entryCout.delete(0, tk.END)
    entryCout.insert(0, total)
    entryCout.config(state="readonly")
    entryTps.config(state="normal")
    entryTps.delete(0, tk.END)
    entryTps.insert(0, tps)
    entryTps.config(state="readonly")
    entryTvq.config(state="normal")
    entryTvq.delete(0, tk.END)
    entryTvq.insert(0, tvq)
    entryTvq.config(state="readonly")
    entryRabais.config(state="normal")
    entryRabais.delete(0, tk.END)
    entryRabais.insert(0, rabais)
    entryRabais.config(state="readonly")


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Compagnie Aérienne 2023")
    window.geometry("400x200")
    window.resizable(False, False)

    frmW = tk.Frame(window)
    frmW.pack()

    menuBar = tk.Menu(window)
    fichier = tk.Menu(menuBar, tearoff=0)
    fichier.add_cascade(label="Imprimer")
    fichier.add_cascade(label="Quitter")
    menuBar.add_cascade(label="Fichier", menu=fichier)

    Soumission = tk.Menu(menuBar, tearoff=0)
    Soumission.add_cascade(label="Calculer")
    Soumission.add_cascade(label="Initialiser")
    menuBar.add_cascade(label="Soumission", menu=Soumission)
    menuBar.add_command(label="a propos", command=heure)

    window.config(menu=menuBar)

    Frm1 = tk.Frame(frmW)
    liste = ("Mauvaises Herbes (1$/hectare)", "Sauterelles (2$/hectare)", "Vers (3$/hectare)", "Combiné (5$/hectare)")
    lsd = ttk.Combobox(Frm1, values=liste, font=("Courrier", 10), state="readonly", width=32)
    lsd.current(0)
    lsd.grid(row=0, column=0, columnspan=2, pady=10)

    Frm1.grid(row=1, column=0)
    lblTitreH = tk.Label(Frm1, text="Nombre d'hectare:", font=("Courrier", 10))
    lblTitreH.grid(row=1, column=0)
    entryHec = tk.Entry(Frm1, font=("Courrier", 10), width=19, justify="center")
    entryHec.insert(0, '100')
    entryHec.grid(row=1, column=1)

    FrmFacture = tk.LabelFrame(frmW, text="Facture")
    FrmFacture.grid(row=2, column=0)
    lblTitre = tk.Label(FrmFacture, text="Cout Total:", font=("Courrier", 10), justify="center")
    lblTitre.grid(row=0, column=0)
    lblTotal = tk.Label(FrmFacture, text="Total des rabais:", font=("Courrier", 10), justify="center")
    lblTotal.grid(row=1, column=0)
    Tps = tk.Label(FrmFacture, text="TPS:", font=("Courrier", 10), justify="center")
    Tps.grid(row=2, column=0)
    Tvq = tk.Label(FrmFacture, text="TVQ:", font=("Courrier", 10), justify="center")
    Tvq.grid(row=3, column=0)

    entryCout = tk.Entry(FrmFacture, font=("Courrier", 10), justify="center", state="readonly")
    entryCout.grid(row=0, column=1)
    entryRabais = tk.Entry(FrmFacture, font=("Courrier", 10), justify="center", state="readonly")
    entryRabais.grid(row=1, column=1)
    entryTps = tk.Entry(FrmFacture, font=("Courrier", 10), justify="center", state="readonly")
    entryTps.grid(row=2, column=1)
    entryTvq = tk.Entry(FrmFacture, font=("Courrier", 10), justify="center", state="readonly")
    entryTvq.grid(row=3, column=1)

    chkTPS_var = tk.IntVar()
    chkTPV_var = tk.IntVar()

    FrmTaxe = tk.LabelFrame(frmW, text="taxe")
    FrmTaxe.grid(row=1, column=2, padx=10, pady=10)
    chkTPS = tk.Checkbutton(FrmTaxe, text="TPS", font=("Courrier", 2), variable=chkTPS_var, onvalue=1, offvalue=0,
                            command=calculer)
    chkTPS.grid(row=0, column=0)
    lblTitre = tk.Label(FrmTaxe, text="TPS:", font=("Courrier", 10), justify="center")
    lblTitre.grid(row=0, column=1)
    chkTPv = tk.Checkbutton(FrmTaxe, text="TPS", font=("Courrier", 2), variable=chkTPV_var, onvalue=1, offvalue=0,
                            command=calculer)
    chkTPv.grid(row=1, column=0)
    lblTitre2 = tk.Label(FrmTaxe, text="TVQ:", font=("Courrier", 10))
    lblTitre2.grid(row=1, column=1)

    BtnFrm = tk.Frame(frmW)
    BtnFrm.grid(row=2, column=2)
    Btn = tk.Button(BtnFrm, text="Calculer", font=("Courrier", 10), bg='RoyalBlue3', fg="white", width=8,
                    command=calculer)
    Btn.grid(row=0, column=0)
    btn2 = tk.Button(BtnFrm, text="Initialiser", font=("Courrier", 10), bg='RoyalBlue3', fg="white", width=8,
                     command=heure)
    btn2.grid(row=1, column=0, pady=10)
    btn3 = tk.Button(BtnFrm, text="Quitter", font=("Courrier", 10), bg='RoyalBlue3', fg="white", width=8,
                     command=window.destroy)
    btn3.grid(row=2, column=0)

    tk.mainloop()
