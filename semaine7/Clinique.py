from datetime import datetime
from tkinter import *
from tkinter import messagebox

from tkcalendar import DateEntry

from semaine7 import hopital

base = 2


# Fonction pour gérer le choix de l'utilisateur
def choix(bouton):
    global base

    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    curseur.execute("SELECT COUNT(*) FROM employe")
    nombre_enregistrements = curseur.fetchone()[0]
    if nombre_enregistrements <= 1:
        btnDroite.config(state="disabled")
        btnDroite2.config(state="disabled")
    else:
        btnDroite.config(state="normal")
        btnDroite2.config(state="normal")

    if bouton == "gauche":
        base = int(base - 1)

    elif bouton == "gauche2":
        curseur.execute("SELECT * FROM employe limit 1")
        base = curseur.fetchone()[0]
    elif bouton == "droite":
        base = int(base + 1)
    elif bouton == "droite2":
        curseur.execute("SELECT MAX(id) FROM employe")
        base = curseur.fetchone()[0]
    else:
        base = base
    return base

# Fonction pour valider les informations de l'utilisateur
def valider():
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    # Récupération du nom d'utilisateur et du mot de passe saisis
    nom_utilisateur_saisi = hopital.txtNom.get()
    mot_de_passe_saisi = hopital.txtMDP.get()

    # Requête SQL pour récupérer les informations de l'utilisateur à partir de la base de données
    curseur.execute("SELECT Usager, MotDePasse FROM Emp WHERE Usager = ?", (nom_utilisateur_saisi,))
    resultat = curseur.fetchone()

    # Fermeture de la connexion à la base de données
    connexion.close()

    # Vérification que l'utilisateur existe dans la base de données et que le mot de passe est correct
    if resultat is not None and resultat[0] == nom_utilisateur_saisi and resultat[1] == mot_de_passe_saisi:
        hopital.window.destroy()
    else:
        messagebox.showerror("Erreur", "Nom d'usager ou mot de passe invalide")


import sqlite3

# Fonction pour créer une connexion à la base de données SQLite

def creer_connexion():
    # Créer une connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    # Créer un objet curseur
    curseur = connexion.cursor()
    # Retourner la connexion et le curseur
    return connexion, curseur

# Fonction pour mettre l'application en mode consultation

def mode_consultation():
    # Désactiver tous les champs du formulaire
    txtNom.config(state="disabled")
    txtAddre.config(state="disabled")
    txtTel.config(state="disabled")
    txtDate.config(state="disabled")
    txtNum.config(state="disabled")
    opt_1.config(state="disabled")
    opt_2.config(state="disabled")
    opt_3.config(state="disabled")
    opt_4.config(state="disabled")
    chk1.config(state="disabled")
    chk2.config(state="disabled")
    chk3.config(state="disabled")

    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    # Lire le premier enregistrement de la table employe
    curseur.execute("SELECT * FROM employe ORDER BY id LIMIT 1")
    enregistrement = curseur.fetchone()
    if enregistrement is not None:
        # Afficher l'enregistrement dans le formulaire
        txtNum.insert(0, enregistrement[0])
        txtNom.insert(0, enregistrement[1])
        txtAddre.insert(0, enregistrement[2])
        txtTel.insert(0, enregistrement[3])
        txtDate.set_date(enregistrement[4])
        radiobtn.set(enregistrement[5])
        dispo = list(map(bool, map(int, enregistrement[6].split(','))))
        if dispo[0]: chk1.select()
        if dispo[1]: chk2.select()
        if dispo[2]: chk3.select()

    # Gérer l'activation/désactivation des boutons
    btnAjouter.config(state="normal")
    btnModifier.config(state="normal")
    btnSupprimer.config(state="normal")
    btnQuitter.config(state="normal")
    btnGauchex2.config(state="disabled")
    btnGauche.config(state="disabled")
    curseur.execute("SELECT COUNT(*) FROM employe")
    nombre_enregistrements = curseur.fetchone()[0]
    if nombre_enregistrements <= 1:
        btnDroite.config(state="disabled")
        btnDroite2.config(state="disabled")
    else:
        btnDroite.config(state="normal")
        btnDroite2.config(state="normal")

# Fonction pour ajouter un nouvel enregistrement

def ajouter():
    # Effacer tous les champs du formulaire
    txtNom.delete(0, END)
    txtAddre.delete(0, END)
    txtTel.delete(0, END)
    txtDate.delete(0, END)
    txtNum.delete(0, END)

    # Activer tous les champs du formulaire (sauf le numéro d'employé)
    txtNom.config(state="normal")
    txtAddre.config(state="normal")
    txtTel.config(state="normal")
    txtDate.config(state="normal")
    opt_1.config(state="normal")
    opt_2.config(state="normal")
    opt_3.config(state="normal")
    opt_4.config(state="normal")
    chk1.config(state="normal")
    chk2.config(state="normal")
    chk3.config(state="normal")

    # Mettre le focus sur le champ Nom
    txtNom.focus()

    # Désactiver les boutons de navigation
    btnGauchex2.config(state="disabled")
    btnGauche.config(state="disabled")
    btnDroite.config(state="disabled")
    btnDroite2.config(state="disabled")

    # Modifier le texte des boutons AJOUTER et MODIFIER
    btnAjouter.config(text="ENREGISTRER", command=enregistrer)
    btnModifier.config(text="ANNULER", command=mode_consultation)


def enregistrer():
    # Ajouter les données du formulaire à la table employe
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()
    nom = txtNom.get()
    adresse = txtAddre.get()
    telephone = txtTel.get()
    dateNaissance = txtDate.get()
    salaire = radiobtn.get()
    dispo = [var1.get(), var2.get(), var3.get()]
    # ville = txtVille.get()  # Assuming txtVille is a field in your form
    curseur.execute('''
        INSERT INTO employe (nom, adresse, telephone, dateNaissance, salaire, dispo)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nom, adresse, telephone, dateNaissance, salaire, ','.join(map(str, dispo))))
    connexion.commit()

    # Revenir en mode consultation
    mode_consultation()


def afficher(bouton):
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    base = choix(bouton)

    # Exécution d'une requête SQL pour récupérer l'enregistrement correspondant à base
    curseur.execute("SELECT * FROM employe WHERE id = ?", (base,))
    enregistrement = curseur.fetchone()

    # Fermeture de la connexion à la base de données
    connexion.close()

    if enregistrement is not None:
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

        txtNom.insert(0, enregistrement[1])
        txtAddre.insert(0, enregistrement[2])
        txtTel.insert(0, enregistrement[4])
        # Convert the date to 'd/m/y' format before inserting it into txtDate
        txtNum.insert(0, enregistrement[0])  # Insert the id into txtNum
        radiobtn.set(enregistrement[5])
        if enregistrement[5] == 0:
            opt_1.select()
        if isinstance(enregistrement[6], int):
            dispo = [bool(enregistrement[6])]
        else:
            dispo = list(map(bool, map(int, enregistrement[6].split(','))))
        # Ensure dispo has at least three elements
        while len(dispo) < 3:
            dispo.append(False)
        if dispo[0]: chk1.select()
        if dispo[1]: chk2.select()
        if dispo[2]: chk3.select()
        # Convert the date string to a datetime.date object before formatting it
        dateNaissance = datetime.strptime(enregistrement[5], '%Y-%m-%d').date()
        txtDate.insert(0, dateNaissance.strftime('%d/%m/%Y'))

        txtNom.config(state="readonly")
        txtAddre.config(state="readonly")
        txtTel.config(state="readonly")
        txtDate.config(state="readonly")
        txtNum.config(state="readonly")


def ajouter():
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

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

    # Exécution d'une requête SQL pour récupérer le dernier id de la table employe
    curseur.execute("SELECT MAX(id) FROM employe")
    dernier_id = curseur.fetchone()[0]
    if dernier_id is None:
        dernier_id = 0  # Si la table est vide, on commence à 1
    nnum = dernier_id + 1
    txtNum.insert(0, nnum)
    txtNom.focus()
    btnDroite.configure(state="disabled")
    btnDroite2.configure(state="disabled")
    btnGauche.configure(state="disabled")
    btnGauchex2.configure(state="disabled")

    btnAjouter.configure(text="Sauvegarder", command=enregistrer)

    # Fermeture de la connexion à la base de données
    connexion.close()


def mode_consultation():
    # Désactiver tous les champs du formulaire
    txtNom.config(state="disabled")
    txtAddre.config(state="disabled")
    txtTel.config(state="disabled")
    txtDate.config(state="disabled")
    txtNum.config(state="disabled")
    opt_1.config(state="disabled")
    opt_2.config(state="disabled")
    opt_3.config(state="disabled")
    opt_4.config(state="disabled")
    chk1.config(state="disabled")
    chk2.config(state="disabled")
    chk3.config(state="disabled")

    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    # Lire le premier enregistrement de la table employe
    curseur.execute("SELECT * FROM employe ORDER BY id LIMIT 1")
    enregistrement = curseur.fetchone()
    if enregistrement is not None:
        # Afficher l'enregistrement dans le formulaire
        txtNum.insert(0, enregistrement[0])
        txtNom.insert(0, enregistrement[1])
        txtAddre.insert(0, enregistrement[2])
        txtTel.insert(0, enregistrement[3])
        txtDate.set_date(enregistrement[4])
        radiobtn.set(enregistrement[5])
        dispo = list(map(bool, map(int, enregistrement[6].split(','))))
        if dispo[0]: chk1.select()
        if dispo[1]: chk2.select()
        if dispo[2]: chk3.select()

    # Gérer l'activation/désactivation des boutons
    btnAjouter.config(state="normal")
    btnModifier.config(state="normal")
    btnSupprimer.config(state="normal")
    btnQuitter.config(state="normal")
    btnGauchex2.config(state="disabled")
    btnGauche.config(state="disabled")
    curseur.execute("SELECT COUNT(*) FROM employe")
    nombre_enregistrements = curseur.fetchone()[0]
    if nombre_enregistrements <= 1:
        btnDroite.config(state="disabled")
        btnDroite2.config(state="disabled")
    else:
        btnDroite.config(state="normal")
        btnDroite2.config(state="normal")


def sauvegarderModif():
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    # Récupération des valeurs du formulaire
    nom = txtNom.get()
    adresse = txtAddre.get()
    telephone = txtTel.get()
    dateNaissance = txtDate.get()
    salaire = radiobtn.get()
    dispo = [var1.get(), var2.get(), var3.get()]
    # ville = txtVille.get()  # Assuming txtVille is a field in your form
    curseur.execute('''
        UPDATE employe SET nom = ?, adresse = ?, telephone = ?, dateNaissance = ?, salaire = ?, dispo = ? WHERE id = ?
    ''', (nom, adresse, telephone, dateNaissance, salaire, ','.join(map(str, dispo)), base))

    # Validation des modifications
    connexion.commit()

    # Fermeture de la connexion à la base de données
    connexion.close()

    btnDroite.configure(state="normal")
    btnDroite2.configure(state="normal")
    btnGauche.configure(state="normal")
    btnGauchex2.configure(state="normal")
    btnAjouter.configure(text="Ajouter", command=ajouter)


def modifier():
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    # Récupération des valeurs du formulaire
    nom = txtNom.get()
    adresse = txtAddre.get()
    telephone = txtTel.get()
    dateNaissance = txtDate.get_date()  # Assuming txtDate is a DateEntry widget
    salaire = radiobtn.get()
    dispo = [var1.get(), var2.get(), var3.get()]

    # Conversion de la liste dispo en chaîne de caractères
    dispo_str = ','.join(map(str, dispo))

    # Exécution d'une requête SQL pour mettre à jour l'enregistrement correspondant à base
    curseur.execute('''
        UPDATE employe SET nom = ?, adresse = ?, telephone = ?, dateNaissance = ?, salaire = ?, dispo = ? WHERE id = ?
    ''', (nom, adresse, telephone, dateNaissance, salaire, dispo_str, base))

    # Validation des modifications
    connexion.commit()

    # Fermeture de la connexion à la base de données
    connexion.close()

    btnDroite.configure(state="normal")
    btnDroite2.configure(state="normal")
    btnGauche.configure(state="normal")
    btnGauchex2.configure(state="normal")
    btnAjouter.configure(text="Ajouter", command=ajouter)


def supprimer():
    # Connexion à la base de données SQLite
    connexion = sqlite3.connect('../Semaine 11/02.Exercices/bd.sqlite')
    curseur = connexion.cursor()

    # Exécution d'une requête SQL pour supprimer l'enregistrement correspondant à base
    curseur.execute("DELETE FROM employe WHERE id = ?", (base,))

    # Validation des modifications
    connexion.commit()

    # Fermeture de la connexion à la base de données
    connexion.close()

    btnDroite.configure(state="normal")
    btnDroite2.configure(state="normal")
    btnGauche.configure(state="normal")
    btnGauchex2.configure(state="normal")
    btnAjouter.configure(text="Ajouter", command=ajouter)
    afficher(1)


if __name__ == '__main__':
    window = Tk()
    radiobtn = IntVar()

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

    txtDate = DateEntry(lblTitre, font=("Courrier", 20), justify="center", background='black', width=10,
                        date_pattern='d/m/y')
    txtDate.grid(row=4, column=1, padx=0, pady=13)

    lblTitre2 = LabelFrame(frmW, text="Échelle salarial", font=("Courrier", 20), background=bg)
    lblTitre2.grid(row=0, column=1, padx=5, pady=0, sticky="n")


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

    chk2 = Checkbutton(lblTitre3, text="16 h 00 à 00 h 00", font=("Courrier", 12), justify="left", background=bg,
                       variable=var2, onvalue=1, offvalue=0)
    chk2.grid(row=1, column=0, sticky="w", pady=4)

    chk3 = Checkbutton(lblTitre3, text="00 h 00 à 8 h 00", font=("Courrier", 12), justify="left", background=bg,
                       variable=var3, onvalue=1, offvalue=0)
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
