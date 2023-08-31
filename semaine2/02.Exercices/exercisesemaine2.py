# nom: William Bouchard
# date: 2023/08/28
# description: exercices semaine 2
#############################################################################################################
# 01 – Boucles de base
#############################################################################################################
import time

'''
Soit la liste : vache, souris, levure, bactérie. Affichez l'ensemble des éléments de cette 
liste (un élément par ligne) de trois façons différentes (deux méthodes avec for et une avec while).
'''


def afficherListe(liste):
    for i in liste:
        print(i)


def afficherListe2(liste):
    for i in range(len(liste)):
        print(liste[i])


def afficherListe3(liste):
    i = 0
    while i < len(liste):
        print(liste[i])
        i += 1


#############################################################################################################
# 02 – Boucle et jours de la semaine
#############################################################################################################

'''
Constituez une liste semaine contenant les 7 jours de la semaine.
Écrivez une série d'instructions affichant les jours de la semaine
(en utilisant une boucle for), ainsi qu'une autre série d'instructions affichant les
jours du week-end (en utilisant une boucle while).

'''


def afficherJoursSemaine(liste):
    for i in liste:
        print(i)


def afficherJoursWeekend(liste):
    i = 5
    while i < len(liste):
        print(liste[i])
        i += 1


#############################################################################################################
# 03 – Nombres de 1 à 10 sur une ligne
#############################################################################################################
'''
Avec une boucle, affichez les nombres de 1 à 10 sur une seule ligne.
'''


def afficherNombres():
    for i in range(1, 11):
        print(i, end=' ')


#############################################################################################################
# 04 – Nombres pairs et impairs
#############################################################################################################
'''
Soit impaire la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. Écrivez un programme qui, 
à partir de la liste impaire, construit une liste paire dans laquelle tous les éléments d’impair 
sont incrémentés de 1.
'''


def afficherNombrePair():
    impaire = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    paire = []
    for i in impaire:
        paire.append(i + 1)
    print(paire)


#############################################################################################################
# 05 – Produit de nombres consécutifs
#############################################################################################################
'''
Avez les fonctions list() et range(), créez la liste entiers contenant les nombres entiers pairs
de 2 à 20 inclus. Calculez ensuite le produit des nombres consécutifs deux à deux d’entiers en utilisant une boucle.
'''


def afficherProduit():
    entiers = list(range(2, 21, 2))
    produit = 1
    for i in entiers:
        produit *= i
    print(produit)


#############################################################################################################
# 06 – Triangle
#############################################################################################################
'''
Créez un script qui dessine un triangle comme celui-ci :
*
**
***
****
*****
******
*******
********
*********
**********
'''


def triangle():
    for i in range(1, 11):
        print('*' * i)


#############################################################################################################
# 07 – Triangle inversé
#############################################################################################################
'''
Créez un script qui dessine un triangle comme celui-ci :
**********
*********
********
*******
******
*****
****
***
**
*
'''


def triangleInversé():
    for i in range(10, 0, -1):
        print('*' * i)


#############################################################################################################
# 08 – Triangle gauche
#############################################################################################################
'''
Créez un script qui dessine un triangle comme celui-ci :
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
'''


def triangleGauche():
    for i in range(1, 11):
        print(' ' * (10 - i) + '*' * i)


#############################################################################################################
# 09 – Pyramide
#############################################################################################################
'''
Créez un script qui dessine une pyramide dessinée à partir d'un nombre arbitraire de lignes N.
 Vous pourrez demander à l'utilisateur le nombre de lignes de la pyramide avec la fonction input().
'''


def Pyramide():
    Nombre = int(input('Entrez un nombre pour la grandeur de la pyramide : '))
    for i in range(1, Nombre):
        print(
            ' ' * (Nombre - i) +
            '§' * (i - 1) + '|' +
            '§' * (i - 1)
        )


#############################################################################################################
# 10 – Table de multiplication
#############################################################################################################
'''
Lire un nombre entier positif et afficher la table de multiplication de ce nombre.
Exemple : la table de multiplication du nombre 5 est 
5 x 1 = 5		5 x 6 = 30		5 x 11 = 55
5 x 2 = 10		5 x 7 = 35		5 x 12 = 60
5 x 3 = 15		5 x 8 = 40		5 x 13 = 65
5 x 4 = 20		5 x 9 = 45		5 x 14 = 70
5 x 5 = 25		5 x 10 = 50		5 x 15 = 75
'''


def TableDeMultiplication():
    Nombre = int(input('Entrez un nombre pour la table de multiplication : '))
    for i in range(1, 16):
        print(Nombre, 'x', i, '=', Nombre * i)


#############################################################################################################
# 11 – Jours de la semaine
#############################################################################################################
'''
Constituez une liste semaine contenant les 7 jours de la semaine.
1.	À partir de cette liste, comment récupérez-vous seulement les 5 premiers jours de la semaine d'une part, et ceux du week-end d'autre part ? Utilisez pour cela l'indexage.
2.	Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indexage).
3.	Trouvez deux manières pour accéder au dernier jour de la semaine.
4.	Inversez les jours de la semaine en une commande.
'''


def JoursDeLaSemaine(semaine):
    print(semaine[:5])
    print(semaine[5:])
    print(semaine[-1])
    print(semaine[6])
    print(semaine[::-1])


#############################################################################################################
# 12 – Saisons
#############################################################################################################
'''
Créez 4 listes hiver, printemps, été et automne contenant les mois correspondants à ces saisons. Créez ensuite une liste saisons contenant les listes hiver, printemps, été et automne. Prévoyez ce que renvoient les instructions suivantes, puis vérifiez-le dans l'interpréteur :
1.	saisons[2]
2.	saisons[1][0]
3.	saisons[1:2]
4.	saisons[:][1]. Comment expliquez-vous ce dernier résultat ?
'''


def Saisons():
    # devrais lister de facons correct
    hiver = ['décembre', 'janvier', 'février']
    printemps = ['mars', 'avril', 'mai']
    ete = ['juin', 'juillet', 'août']
    automne = ['septembre', 'octobre', 'novembre']
    saisons = [hiver, printemps, ete, automne]
    print(saisons[2])
    print(saisons[1][0])
    print(saisons[1:2])
    print(saisons[:][1])


#############################################################################################################
# 13 – Table de multiplication par 8
#############################################################################################################
'''
Affichez la table de multiplication par 8 en une seule commande avec les instructions range() et list().
'''


def tableDeMultiplicationPar8():
    # multiplie par 8 ... 8 fois ?
    print(list(range(8, 81, 8)))


#############################################################################################################
# 14 – Nombres pairs
#############################################################################################################
'''
Répondez à la question suivante en une seule commande.
Combien y a-t-il de nombres pairs dans l'intervalle [2, 10000] inclus ?
'''


def nombresPairs():
    # print la longueur de la liste
    print(len(list(range(2, 10000, 2))))


#############################################################################################################
# 15 – Gestionnaire de tâches
#############################################################################################################
'''
Écrivez un programme qui simule un gestionnaire de tâches. 
L'utilisateur peut ajouter des tâches, les afficher et les marquer comme terminées.
'''


def gestionnaireDeTaches():
    taches = []
    while True:
        print('1. Ajouter une tâche')
        print('2. Afficher les tâches')
        print('3. Marquer une tâche comme terminée')
        print('4. Quitter')
        choix = int(input('Entrez votre choix : '))

        if choix == 1:
            # ajoute une tache a la liste
            taches.append(input('Entrez une tâche : '))

        elif choix == 2:
            # affiche les taches
            for i in range(len(taches)):
                print(i + 1, taches[i])

        elif choix == 3:
            # supprime une tache
            for i in range(len(taches)):
                print(i + 1, taches[i])
            tache = int(input('Entrez le numéro de la tâche terminée : '))
            taches.pop(tache - 1)

        elif choix == 4:
            # quitte le programme
            print('fermeture du programme')
            # je me suis amusé à faire ça
            time.sleep(2)
            break
        else:
            # si c'est invalide
            print('Choix invalide')

semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
liste = ['vache', 'souris', 'levure', 'bactérie']

if __name__ == "__main__":
    # afficherListe(liste)
    # afficherListe2(liste)
    # afficherListe3(liste)
    # afficherJoursSemaine(semaine)
    # afficherJoursWeekend(semaine)
    # afficherNombres()
    # afficherProduit()
    # triangle()
    # triangleInversé()
    Pyramide()
    # TableDeMultiplication()
    # JoursDeLaSemaine(semaine)
    # Saisons()
    # tableDeMultiplicationPar8()
    # nombresPairs()
    # gestionnaireDeTaches()
