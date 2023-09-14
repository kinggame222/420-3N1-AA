'''
Créez une version simplifiée du jeu du pendu. Écrivez des fonctions pour choisir un mot aléatoire, afficher les lettres devinées et vérifier si le mot a été deviné.

	Faites une fonction main pour l’exécution du jeu et l’appel des fonctions.
	Créez une liste de mot (Variable globale) entrée à la main.
	À l’aide d’une fonction, utilisez le module ‘random’ pour déterminer un mot aléatoire à faire trouver.
	Créez une fonction qui permet de faire afficher les lettres devinées et les lettres qui restent à trouver (avec le caractère ‘_’)
	Créez une fonction qui permet de vérifier si le mot a été trouvé.
	Votre jeu doit rouler jusqu’à tant que le mot soit complètement trouvé, peu importe le nombre d’essais.

'''

import math
import random


def choisir_mot(liste):
    return math.floor(random.random() * len(liste))


def afficher_lettres(mot):
    for i in mot:
        print("_", end=" ")


def verifier_mot(mot):
    mot_devine = False
    mot_partiel = "_" * len(mot)

    while not mot_devine:
        lettre = input("Entrez une lettre: ")
        if lettre in mot:
            print(mot)
            for i in range(len(mot)):
                if mot[i] == lettre:
                    mot_partiel = mot_partiel[:i] + lettre + mot_partiel[i + 1:]
            print("La lettre est dans le mot")
        else:
            print("La lettre n'est pas dans le mot")

        print(mot_partiel)
        if mot_partiel == mot:
            mot_devine = True
            print("Félicitations, vous avez deviné le mot!")


if __name__ == "__main__":
    liste = ['bonjour', 'salut', 'aurevoir', 'hello', 'bye', 'ciao', 'hola', 'guten tag', 'namaste', 'ni hao']
    mot_choisi = choisir_mot(liste)
    mot_a_deviner = liste[mot_choisi]
    print("Bienvenue au jeu du pendu!")
    afficher_lettres(mot_a_deviner)
    verifier_mot(mot_a_deviner)