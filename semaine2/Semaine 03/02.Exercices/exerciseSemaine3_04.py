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

def crerArborescence():
    # Créer l'arborescence de répertoire
    os.O_PATH("C:\\test")
    for i in range(1, 16):
        # Créer le répertoire de la semaine
        os.mkdir(f"Semaine {i:02d}")

        # Créer le répertoire des théories
        os.mkdir(f"Semaine {i:02d}/01.Théories")

        # Créer le répertoire des exercices
        os.mkdir(f"Semaine {i:02d}/02.Exercices")

        # Afficher un message à l'écran
        print(f"Semaine {i:02d} créée")

        # Créer le fichier de log
        with open(f"logs_{i:02d}.txt", "w") as fichier:
            fichier.write(f"Semaine {i:02d} créée")

if __name__ == "__main__":
    #crerArborescence()
    print(os.getcwd())



