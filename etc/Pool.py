'''
Nom william bouchard
Date 2023-11-30
Description Pool hockey
'''
from etc.Fonction import connexionBD, deconnexionBD
from menu import *


# Récupération du nom du joueur
def get_nom_joueur(gp, joueurId, cur, partie, Id):
    """
    Cette fonction récupère le nom du joueur en fonction de son ID.
    Elle prend en paramètres le joueurId, le curseur de la base de données, le nom de la partie et l'ID.
    """
    cur.execute(
        f"WITH equipe AS ( SELECT p.equipeReceveurId as equipeId  FROM joueur j  JOIN {partie} pj ON j.id = pj.{Id}  "
        f"JOIN partie p ON pj.partieId = p.id WHERE {gp} = ?  "
        f"union all  SELECT p.equipeVisiteurId as equipeId  FROM joueur j  JOIN {partie} pj ON j.id = pj.{Id}  "
        f"JOIN partie p ON pj.partieId = p.id  WHERE {gp} = ?)  SELECT equipeId, COUNT(equipeId) FROM equipe  GROUP BY equipeId  ORDER BY 2 DESC limit 1",
        (joueurId, joueurId))
    result = cur.fetchone()

    cur.execute("SELECT prenom,nom FROM JOUEUR WHERE id = ?", (joueurId,))
    resultNom = cur.fetchone()

    if result is not None:
        cur.execute("SELECT abreviation FROM EQUIPE WHERE id = ?", (result[0],))
        resultEquipe = cur.fetchone()

        nomJoueur = str(resultNom[0]) + " " + str(resultNom[1] + " (" + str(resultEquipe[0]) + ")")
    else:
        nomJoueur = "Unknown"
    return nomJoueur


# Affichage du pool
def affichagePool():
    """
    Cette fonction affiche le pool de joueurs.
    Elle récupère les IDs des joueurs et les affiche dans un ordre spécifique.
    """
    conn, cur = connexionBD()
    cur.execute("SELECT joueurId FROM choix ORDER BY ronde")
    joueurIds = [row[0] for row in cur.fetchall()]

    nu = 1
    num = 1
    joueurIndex = 0

    for i in range(0, 4):
        for j in range(0, 6):
            labelframe = LabelFrame(frmbouton, text="Round " + str(nu), font=("Courrier", 10), fg=fg, bg=bg)
            labelframe.grid(row=i, column=j)
            nu += 1

            for k in range(0, 5):
                if nu < 22:
                    nomJoueur = get_nom_joueur("joueurId", joueurIds[joueurIndex], cur, "partie_joueur", "joueurId")
                    joueurIndex += 1
                    lbl = Label(labelframe, text=nomJoueur, font=("Courrier", 10), fg=fg, bg=bg)
                    lbl.grid(row=k, column=0, sticky='w')
                    num += 1

                else:
                    nomJoueur = get_nom_joueur("gardienId", joueurIds[joueurIndex], cur, "partie_gardien", "gardienId")
                    joueurIndex += 1
                    lbl = Label(labelframe, text=nomJoueur, font=("Courrier", 10), fg=fg, bg=bg)
                    lbl.grid(row=k, column=0, sticky='w')
                    num += 1

    deconnexionBD(conn, cur)


# Début du programme principal
if __name__ == '__main__':

    # Création de la fenêtre principale
    w = Tk()

    # Configuration de la fenêtre principale
    bg = "light grey"
    fg = "black"
    w.configure(bg=bg)
    w.title("Pool Hockey 2023-2024 - Collège d'alma")
    w.geometry("1000x800")
    w.iconbitmap("..\etc\image\Image1.ico")
    w.resizable(False, False)

    create_menu(w)

    # frame
    frm = Frame(w, bg=bg)
    frm.grid(row=0, column=0, sticky='ew')
    w.grid_rowconfigure(0, weight=1)
    w.grid_columnconfigure(0, weight=1)

    # Création et positionnement du label lblTitre
    lblTitre = Label(frm, text="Participant: William ", font=("Courrier", 30), fg=fg, bg=bg)
    lblTitre.grid(row=0, column=0, columnspan=2, pady=10)

    # Création et positionnement du label lblTexte
    texte = "(Choisir 24 joueurs en cochants la case a gauche de leur nom)"
    lblTexte = Label(frm, text=texte, font=("Courrier", 10), fg=fg, bg=bg)
    lblTexte.grid(row=1, column=0, columnspan=2)

    # Création du Canvas
    canvas = Canvas(frm, width=800, height=2, bg=bg, bd=0, highlightthickness=0)
    canvas.grid(row=2, column=0, columnspan=2, pady=10)

    # Création de la ligne
    canvas.create_line(0, 0, w.winfo_screenwidth(), 0, fill="black")

    # frame
    frmbouton = Frame(frm, bg=bg)
    frmbouton.grid(row=3, column=0, columnspan=2)

    # Création du Canvas
    canvas = Canvas(frm, width=800, height=2, bg=bg, bd=0, highlightthickness=0)
    canvas.grid(row=4, column=0, columnspan=2, pady=10)
    canvas.create_line(0, 0, w.winfo_screenwidth(), 0, fill="black")

    # frame pour bouton
    frm1 = Frame(frm, bg=bg)
    frm1.grid(row=5, column=0, columnspan=2, pady=10)

    # Création et positionnement du bouton sauvegarder, modifier, réinitialiser dans le Frame
    btnSauvegarder = Button(frm1, text="Sauvegarder", font=("Courrier", 12), fg=fg, bg=bg, width=20)
    btnSauvegarder.grid(row=0, column=0, pady=10, padx=10)

    btnModifier = Button(frm1, text="Modifier", font=("Courrier", 12), fg=fg, bg=bg, width=20)
    btnModifier.grid(row=0, column=1, pady=10, padx=10)

    btnReinitialiser = Button(frm1, text="Réinitialiser", font=("Courrier", 12), fg=fg, bg=bg, width=20)
    btnReinitialiser.grid(row=0, column=2, pady=10, padx=10)
    affichagePool()
    # Boucle principale
    w.mainloop()
