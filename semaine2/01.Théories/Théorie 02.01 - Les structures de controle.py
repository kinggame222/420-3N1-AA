"""Ce cours est sur les boucles et les comparaisons en python"""

########################################################################################################################
# 02.00 - Les conditionnelles
########################################################################################################################
'''
Les structures conditionnelles if, elif et else en Python permettent de prendre des décisions dans le code en fonction 
de certaines conditions. Elles permettent d'exécuter différents blocs de code en fonction de la vérité ou de la fausseté 
de différentes expressions.

    - if    :   La structure if est utilisée pour exécuter un bloc de code si une condition est évaluée comme vraie.
                Si la condition est fausse, le bloc de code sous l'instruction if ne sera pas exécuté.
                    if condition:
                        # Bloc de code à exécuter si la condition est vraie
                        # ...
                        
    - elif  :   L'instruction elif (abréviation de "else if") est utilisée pour ajouter une condition alternative à 
                tester si la condition de l'instruction if est fausse. Vous pouvez avoir plusieurs clauses elif pour 
                tester plusieurs conditions alternatives.
                    if condition:
                        # Bloc de code à exécuter si la condition est vraie
                        # ...
                    elif autre_condition:
                        # Bloc de code à exécuter si la première condition est fausse et cette condition est vraie
                        # ...

    - else  :   L'instruction else est utilisée pour exécuter un bloc de code si aucune des conditions précédentes 
                (if ou elif) n'est vraie. Il peut y avoir au plus une instruction else dans une structure conditionnelle
                    if condition:
                        # Bloc de code à exécuter si la condition est vraie
                        # ...
                    elif autre_condition:
                        # Bloc de code à exécuter si la première condition est fausse et cette condition est vraie
                        # ...
                    else:
                        # Bloc de code à exécuter si aucune des conditions précédentes n'est vraie
                        # ...
'''


# Exemple : Vérification de la parité
def condition1():
    nombre = 7
    if nombre % 2 == 0:
        print(nombre, "est pair")
    else:
        print(nombre, "est impair")


# Exemple : Comparaison de nombres
def condition2():
    a = 5
    b = 10
    if a > b:
        print("a est plus grand que b")
    elif a < b:
        print("a est plus petit que b")
    else:
        print("a et b sont égaux")


# Exemple : Vérification de la présence d'un élément dans une liste
def condition3():
    ma_liste = [1, 2, 3, 4, 5]
    element = 3
    if element in ma_liste:
        print(element, "est dans la liste")
    else:
        print(element, "n'est pas dans la liste")


# Exemple : Catégorisation d'une note
def condition4():
    note = 85
    if note >= 90:
        print("A")
    elif note >= 80:
        print("B")
    elif note >= 70:
        print("C")
    else:
        print("D")


# Exemple : Vérification de la validité d'un mot de passe
def condition5():
    mot_de_passe = "motdepasse"
    saisie = input("Entrez le mot de passe : ")
    if saisie == mot_de_passe:
        print("Mot de passe correct !")
    else:
        print("Mot de passe incorrect.")


########################################################################################################################
# 02.00 - Les boucles FOR
########################################################################################################################
'''
La boucle `for` en Python est une structure de contrôle utilisée pour itérer à travers une séquence d'éléments tels que 
des listes, des tuples, des chaînes de caractères, des ensembles, etc. Elle permet d'exécuter un bloc de code plusieurs 
fois, chaque itération correspondant à un élément de la séquence. Voici une description de la boucle `for` en Python :

Syntaxe de base:
    for element in sequence:
        # Bloc de code (ou bloc d'instructions) à exécuter pour chaque élément de la séquence
        # ...

    - `element`  :  C'est une variable d'itération qui prend la valeur de chaque élément de la séquence à chaque 
                    itération. Vous pouvez choisir n'importe quel nom pour cette variable. Elle prend n'importe 
                    lequel type.
                    
                    Normalement, le nom i est choisi pour la variable d'itération. Ceci est une habitude en informatique 
                    et indique en général qu'il s'agit d'un entier (le nom i vient sans doute du mot indice ou index en 
                    anglais). Nous vous conseillons de suivre cette convention afin d'éviter les confusions, si vous 
                    itérez sur les indices vous pouvez appeler la variable d'itération i.
                    Si, par contre, vous itérez sur une liste comportant des chaînes de caractères, utilisez un nom 
                    explicite pour la variable d'itération. Par exemple :
                        for prenom in ["Joe", "Bill", "John"]:
                            ou
                        for proportion in [0.12, 0.53, 0.07, 0.28]:
                    
    - `sequence` :  C'est la séquence d'éléments à travers laquelle vous itérez. Cela peut être une liste, un tuple, 
                    une chaîne de caractères, un ensemble ou même un objet itérable défini par l'utilisateur.

    - ':'        :  Le caractère deux-points à la fin de la ligne débutant par for. Cela signifie que la boucle for 
                    attend un bloc d'instructions, en l’occurrence toutes les instructions que Python répétera à chaque 
                    itération de la boucle. On appelle ce bloc d'instructions le corps de la boucle. Comment 
                    indique-t-on à Python où ce bloc commence et se termine ? Cela est signalé uniquement par 
                    l'indentation, c'est-à-dire le décalage vers la droite de la (ou des) lignes du bloc d'instructions.

La boucle `for` itère à travers la séquence, exécute le bloc de code à l'intérieur du `for` pour chaque élément, puis 
passe au suivant jusqu'à ce que tous les éléments de la séquence aient été traités.

Exemple d'utilisation de la boucle `for` :
'''


def boucle_exemple1():
    nombres = [1, 2, 3, 4, 5]
    for nombre in nombres:
        carre = nombre ** 2
        print(f"Le carré de {nombre} est {carre}")


'''
Dans cet exemple, la boucle `for` itère à travers la liste `nombres`, assigne chaque élément à la variable `nombre`, 
calcule le carré de chaque nombre, et affiche le résultat.

La boucle `for` est très utile pour effectuer des opérations répétées sur des collections de données ou pour itérer à 
travers des séquences de manière ordonnée.
'''


# Exemple : Itérer à travers une liste qui contient des caractères
def boucle_exemple2():
    fruits = ["pomme", "banane", "orange", "raisin"]
    for fruit in fruits:
        print(fruit)


# Exemple : Itérer à travers une chaîne de caractères
def boucle_exemple3():
    message = "Bonjour"
    for lettre in message:
        print(lettre)


# Exemple : Itérer à travers un dictionnaire
def boucle_exemple4():
    personne = {"nom": "John", "âge": 30, "ville": "New York"}
    for cle, valeur in personne.items():
        print(f"{cle}: {valeur}")


# Exemple : Utilisation d'une boucle for imbriquée pour créer un motif
def boucle_exemple5():
    for i in range(5):
        for j in range(i + 1):
            print("*", end=" ")
        print()


########################################################################################################################
# 02.00 - Les boucles WHILE
########################################################################################################################
'''
La boucle while en Python est une structure de contrôle qui permet d'exécuter un bloc de code tant qu'une condition 
donnée est vraie. La condition est évaluée avant chaque itération, et si elle est vraie, le bloc de code est exécuté. La 
boucle continue jusqu'à ce que la condition devienne fausse. 

Voici la syntaxe de la boucle while :
    while condition:
        # Bloc de code à exécuter tant que la condition est vraie
        # ...

Une boucle while nécessite généralement trois éléments pour fonctionner correctement :
    - Initialisation de la variable d'itération avant la boucle.
    - Test de la variable d'itération associée à l'instruction while.
    - Mise à jour de la variable d'itération dans le corps de la boucle.

Exemple d'utilisation de la boucle while :
'''


def boucle_exemple6():
    compteur = 0
    while compteur < 5:
        print(compteur)
        compteur += 1


'''
Dans cet exemple, la boucle while s'exécute tant que la valeur de compteur est inférieure à 5. À chaque itération, le 
compteur est incrémenté de 1 et la valeur actuelle du compteur est affichée.
'''


# Exemple : Affichage des puissances de 2 jusqu'à un certain seuil
def boucle_exemple7():
    puissance = 1
    limite = 100
    while puissance <= limite:
        print(puissance)
        puissance *= 2


# Exemple : Saisie utilisateur contrôlée par une boucle
def boucle_exemple8():
    mot_de_passe = "motdepasse"
    tentative = input("Entrez le mot de passe : ")
    while tentative != mot_de_passe:
        print("Mot de passe incorrect")
        tentative = input("Entrez le mot de passe : ")
    print("Mot de passe correct !")


# Exemple : Calcul de la somme des entiers jusqu'à un certain nombre
def boucle_exemple9():
    limite = 10
    somme = 0
    nombre = 1
    while nombre <= limite:
        somme += nombre
        nombre += 1
    print("La somme des entiers jusqu'à", limite, "est", somme)


# Exemple : Simulation d'un jeu de devinette
def boucle_exemple10():
    import random

    nombre_secret = random.randint(1, 100)
    essais = 0
    devinette = 0

    while devinette != nombre_secret:
        devinette = int(input("Devinez le nombre : "))
        essais += 1

    print(f"Bravo ! Vous avez trouvé en {essais} essais.")


# Exemple : Calcul de la factorielle d'un nombre
def boucle_exemple11():
    n = 5
    factorielle = 1
    i = 1
    while i <= n:
        factorielle *= i
        i += 1
    print(f"La factorielle de {n} est {factorielle}")


'''
Faites bien attention aux tests et à l'incrémentation que vous utilisez car une erreur mène souvent à des « boucles 
infinies » qui ne s'arrêtent jamais. Vous pouvez néanmoins toujours stopper l'exécution d'un script Python à l'aide de 
la combinaison de touches Ctrl-F2 ou le bouton STOP (carré rouge) dans la fenêtre d'exécution.
'''


def boucle_infini():
    i = 0
    while i < 10:
        print("J'aime le python")


'''
La boucle while combinée à la fonction input() peut s'avérer commode lorsqu'on souhaite demander à l'utilisateur une 
valeur numérique. La fonction input() prend en argument un message (sous la forme d'une chaîne de caractères), demande à 
l'utilisateur d'entrer une valeur et renvoie celle-ci sous forme d'une chaîne de caractères. Il faut ensuite convertir 
cette dernière en entier.
'''


def boucle_input():
    i = 0
    while i <= 10:
        reponse = input("Entrez un entier supérieur à 10 : ")
        i = int(reponse)


########################################################################################################################
# 02.00 - La fonction range()
########################################################################################################################
'''
La fonction range() en Python est une fonction intégrée qui génère une séquence de nombres entiers. Elle est souvent 
utilisée avec les boucles for pour générer une séquence d'indices à travers laquelle itérer. 

Syntaxe de base :
    range(début, fin, pas)
    
    - 'début'   : C'est le premier nombre de la séquence (inclus).
    - 'fin'     : C'est le dernier nombre de la séquence (exclu).
    - 'pas'     : C'est l'incrément entre les nombres de la séquence (par défaut, pas est de 1).
    
La fonction range() est principalement utilisée pour générer des séquences numériques dans le contexte des boucles for, 
mais elle peut également être utilisée pour générer des séquences de nombres dans d'autres situations.
'''


# Exemple : Générer une séquence de nombres de 0 à 4
def range1():
    for i in range(5):
        print(i)  # Affiche : 0, 1, 2, 3, 4


# Exemple : Générer une séquence de nombres de 2 à 8 (par incréments de 2)
def range2():
    for j in range(2, 9, 2):
        print(j)  # Affiche : 2, 4, 6, 8


# Exemple : Utilisation de range() pour créer une liste de nombres
def range3():
    liste = list(range(1, 6))
    print(liste)  # Affiche : [1, 2, 3, 4, 5]


########################################################################################################################
# 02. - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    condition1()
    # condition2()
    # condition3()
    # condition4()
    # condition5()
    # boucle_exemple1()
    # boucle_exemple2()
    # boucle_exemple3()
    # boucle_exemple4()
    # boucle_exemple5()
    # boucle_exemple6()
    # boucle_exemple7()
    # boucle_exemple8()
    # boucle_exemple9()
    # boucle_exemple10()
    # boucle_exemple11()
    # boucle_infini()
    # boucle_input()
    # range1()
    # range2()
    # range3()

########################################################################################################################
# 02.00 - Références
########################################################################################################################
'''
https://docs.python.org/fr/3.8/library/stdtypes.html
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming
https://python.sdv.univ-paris-diderot.fr/02_variables/
https://gayerie.dev/docs/python/index.html
'''
