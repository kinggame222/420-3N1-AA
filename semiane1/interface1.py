from tkinter import *
from tkcalendar import *







if __name__ == '__main__':
    window = Tk()

    window.title("Lire fichier")
    window.geometry("600x400")
    window.resizable(False, False)

    frmW = Frame(window)

    # mot de passe
    txtMotPasse = Entry(frmW, font=("Courrier", 25), justify="center", show="*")

    txtMotPasse.pack(padx=20, pady=20)

    # DATE
    DateNaissance = DateEntry(frmW, width=12, background='darkblue', foreground='white', borderwidth=2,
                              date_pattern='dd mm yyyy')
    DateNaissance.pack(padx=10, pady=10)

    txtNombre = Spinbox(frmW, font=("Courrier", 25), from_=0, to=100)
    txtNombre.pack(padx=20, pady=20)

    btnNouvelleEcran = Button(frmW, text="Nouvelle Ecran", font=("Courrier", 25), command=nouvelleecran)
    btnNouvelleEcran.pack(padx=20, pady=20)

    frmW.pack()

    window.mainloop()
