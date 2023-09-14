'''
Question 04 – Préparation de cours

Vous êtes engagé par votre enseignant afin de lui préparer un script python pour la création de son environnement d’enseignement. À l’aide de OS, votre script doit faire les tâches suivantes :

ü À la racine de votre OneDrive personnel, créer une arborescence de répertoire sous ce format jusqu’à un total de 15 semaines :

o Sigle et titre du cours -> Semaine 01 -> 01.Théories

-> 02.Exercices

Semaine 02 -> 01.Théories

-> 02.Exercices

…

ü Ajoutez un répertoire du nom de _Correction à la racine de votre arborescence. Dans ce répertoire, ajoutez un nouveau répertoire selon les #DA des étudiants qui se trouve dans le fichier DA.txt

ü Pour chaque répertoire créé, afficher un message à l’écran afin de vérifier l’état d’avancement. Affichez aussi ce même message dans un fichier en y ajoutant un timestamp dans le nom du fichier : logs_TIMESTAMP.txt
'''

import os
from datetime import datetime


def crerArborescence():
    # je lai fait dans mon dossier test pour ne pas risquer de tout effacer
    os.chdir("C:\\test")
    temp = datetime.now().strftime("%Y%m%d%H%M%S")
    for i in range(1, 16):
        if not os.path.exists(f"Semaine {i:02d}"):
            os.mkdir(f"Semaine {i:02d}")
            os.mkdir(f"Semaine {i:02d}/01.Théories")
            os.mkdir(f"Semaine {i:02d}/02.Exercices")
            print(f"Semaine {i:02d} créée")
            with open(f"logs_{temp}.txt", "a") as fichier:
                fichier.write(f"Semaine {i:02d} créée + {temp}\n")

    if not os.path.exists("_Correction"):
        os.mkdir("_Correction")
    with open("/Semaine 03/02.Exercices/DA.txt", "r") as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            if not os.path.exists(f"_Correction/{ligne}"):
                os.mkdir(f"_Correction/{ligne}")
                print(f"{ligne} créé")
            with open(f"logs_{temp}.txt", "a") as fichier_c:
                fichier_c.write(f"{ligne} créé + {temp}\n")


if __name__ == "__main__":
    crerArborescence()
    # print(os.getcwd())
