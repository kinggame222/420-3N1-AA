"""Ce cours est sur les variables et l'affichage à l'écran"""
########################################################################################################################
# 01.15 - Les variables
########################################################################################################################
'''
Une variable est une zone de la mémoire de l'ordinateur dans laquelle une valeur est stockée. Aux yeux du programmeur,
cette variable est définie par un nom, alors que pour l'ordinateur, il s'agit en fait d'une adresse, c'est-à-dire d'une
zone particulière de la mémoire.

En Python, la déclaration d'une variable et son initialisation (c'est-à-dire la première valeur que l'on va stocker
dedans) se font en même temps. Pour vous en convaincre, testez les instructions suivantes dans la console Python : 

    1.  Déclaration de la variable  :   x = 10
        Python détecte que la variable était un entier. On dit que Python est un langage au typage dynamique. Python a 
        alloué (réservé) l'espace en mémoire pour y accueillir un entier.
    
    2.  Affichage de la variable    :   x
        L'interpréteur nous a permis de connaître le contenu de la variable juste en tapant son nom. Retenez ceci car 
        c'est une spécificité de l'interpréteur Python, très pratique pour chasser (debugger) les erreurs dans un 
        programme. Par contre, la ligne d'un script Python qui contient seulement le nom d'une variable (sans aucune 
        autre indication) n'affichera pas la valeur de la variable à l'écran lors de l'exécution (pour autant, cette 
        instruction reste valide et ne générera pas d'erreur).
'''

########################################################################################################################
# 01.16 - Les types de variables
########################################################################################################################
'''
Allez voir la documentation officiel : https://docs.python.org/fr/3.8/library/stdtypes.html
'''

########################################################################################################################
# 01.17 - Les structures de données
########################################################################################################################
'''
En Python, il existe plusieurs structures de données intégrées qui sont utilisées pour stocker et organiser des 
collections d'objets. Ces structures de données intégrées offrent différentes fonctionnalités et sont utilisées dans 
divers contextes en fonction des besoins spécifiques du programme. Il existe également d'autres structures de données 
disponibles dans des modules ou bibliothèques externes, qui peuvent être importées et utilisées en fonction des 
exigences du projet. Voici quelques-unes des structures de données les plus couramment utilisées :

    1.  Listes (Lists) :
        Les listes sont des collections modifiables et ordonnées d'objets. Elles sont définies en utilisant des 
        crochets [] et les éléments sont séparés par des virgules. Les listes peuvent contenir des objets de différents 
        types et vous pouvez ajouter, supprimer ou modifier des éléments.

    2.  Tuples :
        Les tuples sont des collections qui reste identique(ne change pas) et ordonnées d'objets. Ils sont définis en 
        utilisant des parenthèses () et les éléments sont séparés par des virgules. Les tuples peuvent contenir des 
        objets de différents types, mais une fois créés, ils ne peuvent pas être modifiés.

    3.  Dictionnaires (Dictionaries) :
        Les dictionnaires sont des collections non ordonnées de paires clé-valeur. Chaque élément du dictionnaire est 
        constitué d'une clé unique et de sa valeur correspondante, et ils sont définis en utilisant des accolades {}. 
        Les dictionnaires sont utiles lorsque vous souhaitez accéder à des éléments par leur clé plutôt que par leur 
        position.

    4.  Ensembles (Sets) :
        Les ensembles sont des collections non ordonnées et non indexées d'objets uniques. Ils sont définis en utilisant 
        des accolades {}. Les ensembles éliminent les doublons, ce qui les rend utiles pour effectuer des opérations 
        d'union, d'intersection et de différence sur des collections.

    5.  Chaînes de caractères (Strings) :
        Les chaînes de caractères sont des séquences immuables de caractères. Elles sont définies en utilisant des 
        guillemets simples ('') ou doubles (""). Les chaînes de caractères sont utilisées pour représenter du texte et 
        offrent des opérations de manipulation spécifiques aux chaînes de caractères.
'''
def structure():
    ma_liste = [1, 2, "trois", 4.5]
    print(ma_liste)
    print(ma_liste[2] + '\n')

    mon_tuple = (1, 2, "trois", 4.5)
    print(mon_tuple)
    print(str(mon_tuple[3]) + '\n')

    mon_dictionnaire = {"nom": "John", "âge": 25, "ville": "Paris"}
    print(mon_dictionnaire)
    print(mon_dictionnaire['nom'] + '\n')

    mon_ensemble = {1, 2, 3, 4, 5}
    print(mon_ensemble)
    #print(str(mon_ensemble[0]))  # Erreur = TypeError: 'set' object is not subscriptable

    ma_chaine = "Bonjour, Python!"
    print(ma_chaine)
    print(ma_chaine[9:15])

########################################################################################################################
# 01.18 - Les conversion de types
########################################################################################################################
'''
En Python, vous pouvez convertir des valeurs d'un type à un autre en utilisant des fonctions de conversion intégrées. Il 
est important de noter que certaines conversions peuvent entraîner une perte de précision ou une modification de la 
valeur d'origine, il est donc recommandé d'utiliser les conversions de types de manière appropriée selon les besoins de 
votre programme. Voici quelques exemples de conversions de types couramment utilisées :

    1.  Conversion vers un entier (int) :
        Par exemple, si a = "10", la fonction int(a) convertit la chaîne de caractères "10" en un entier.

    2.  Conversion vers un flottant (float) :
        Par exemple, si b = "3.14", la fonction float(b) convertit la chaîne de caractères "3.14" en un flottant.

    3.  Conversion vers une chaîne de caractères (str) :
        Par exemple, si c = 42, la fonction str(c) convertit l'entier 42 en une chaîne de caractères.

    4.  Conversion vers une liste (list) :
        Par exemple, si d = (1, 2, 3), la fonction list(d) convertit un tuple (1, 2, 3) en une liste.

    5.  Conversion vers un tuple :
        Par exemple, si e = [1, 2, 3], la fonction tuple(e) convertit une liste [1, 2, 3] en un tuple.

    6.  Conversion vers un booléen (bool) :
        Par exemple, si f = 0, la fonction bool(f) convertit l'entier 0 en False.
'''
def conversion():
    a = "10"
    entier = int(a)
    print(entier)  # Affiche : 10

    b = "3.14"
    flottant = float(b)
    print(flottant)  # Affiche : 3.14

    c = 42
    chaine = str(c)
    print(chaine)  # Affiche : "42"

    d = (1, 2, 3)
    liste = list(d)
    print(liste)  # Affiche : [1, 2, 3]

    e = [1, 2, 3]
    tuple1 = tuple(e)
    print(tuple1)  # Affiche : (1, 2, 3)

    f = 0
    booleen = bool(f)
    print(booleen)  # Affiche : False

########################################################################################################################
# 01.19 - Les opérations
########################################################################################################################
'''
Les opérateurs en Python sont des symboles spéciaux qui effectuent des opérations sur des valeurs ou des variables. Ils 
permettent de réaliser des calculs, des comparaisons, des affectations et d'autres manipulations sur les données. 
Voici les principaux types d'opérateurs en Python :

    1.  Les opérateurs arithmétiques :
        +   : Addition
        -   : Soustraction
        *   : Multiplication
        /   : Division (division flottante)
        //  : Division entière (retourne la partie entière du quotient)
        %   : Modulo (reste de la division)
        **  : Exponentiation (élévation à la puissance)
'''
def operation_arithmetique():
    a = 5
    b = 3
    resultat = a + b
    #print('Opération d''addition : ' + resultat)        # Erreur = TypeError: can only concatenate str (not "int") to str
    print('Opération d\'addition : ' + str(resultat))   # Affiche: 8

    a = 5
    b = 3
    resultat = a - b
    print('Opération de soustraction : ' + str(resultat))   # Affiche: 2

    a = 5
    b = 3
    resultat = a * b
    print('Opérateur de multiplication : ' + str(resultat))  # Affiche: 15

    a = 10
    b = 3
    resultat = a / b
    print('Opérateur de division : ' + str(resultat))  # Affiche: 3.3333333333333335

    a = 10
    b = 3
    resultat = a // b
    print('Opérateur de division entière : ' + str(resultat))  # Affiche: 3

    a = 10
    b = 3
    resultat = a % b
    print('Opérateur de modulo : ' + str(resultat))  # Affiche: 1

    a = 2
    b = 3
    resultat = a ** b
    print('Opérateur d\'exponentiation : ' + str(resultat))  # Affiche: 8

'''
    2.  Les opérateurs de comparaison :
        ==  : Égal à
        !=  : Différent de
        <   : Inférieur à
        >   : Supérieur à
        <=  : Inférieur ou égal à
        >=  : Supérieur ou égal à
        
    3.  Les opérateurs logiques :
        and : ET logique
        or  : OU logique
        not : NON logique
        
    4.  Les opérateurs d'affectation :
        =   : Affectation simple
        +=  : Affectation avec addition
        -=  : Affectation avec soustraction
        *=  : Affectation avec multiplication
        /=  : Affectation avec division
        //= : Affectation avec division entière
        %=  : Affectation avec modulo
        **= : Affectation avec exponentiation

    5.  Autres opérateurs :
        ()      : Parenthèses pour grouper les expressions
        []      : Crochets pour accéder aux éléments d'une liste ou d'un tableau
        :       : Deux points utilisés dans les tranches (slicing)
        .       : Point utilisé pour accéder aux attributs d'un objet
        in      : Vérifie si une valeur fait partie d'une séquence
        is      : Vérifie si deux objets sont identiques
        not in  : Vérifie si une valeur ne fait pas partie d'une séquence
'''
########################################################################################################################
# 01.20 - Opérations sur les chaînes de caractères
########################################################################################################################
'''
En Python, les chaînes de caractères sont des séquences immuables de caractères encadrées par des guillemets simples 
('') ou doubles (""). Vous pouvez effectuer différentes opérations sur les chaînes de caractères pour les manipuler et 
les combiner. Voici quelques opérations couramment utilisées sur les chaînes de caractères en Python :

    1.  Concaténation de chaînes de caractères :
        Vous pouvez concaténer (joindre) des chaînes de caractères en utilisant l'opérateur de concaténation (+).
    
    2.  Répétition de chaînes de caractères :
        Vous pouvez répéter une chaîne de caractères en utilisant l'opérateur de multiplication (*).
    
    3.  Accès aux caractères individuels :
        Vous pouvez accéder aux caractères individuels d'une chaîne de caractères en utilisant l'index des caractères 
        (commençant par 0).
        
    4.  Tranches de chaînes de caractères :
        Vous pouvez extraire une partie d'une chaîne de caractères en utilisant les tranches (slicing).
        
    5.  Méthodes de manipulation de chaînes de caractères :
        Python fournit également de nombreuses méthodes intégrées pour manipuler les chaînes de caractères, telles que :
            - len() : retourne la longueur de la chaîne de caractères.
            - upper() : convertit la chaîne de caractères en majuscules.
            - lower() : convertit la chaîne de caractères en minuscules.
            - strip() : supprime les espaces vides au début et à la fin de la chaîne de caractères.
            - split() : divise la chaîne de caractères en une liste de sous-chaînes en utilisant un délimiteur.
            - et plusieurs autres...
'''
def operation_chaine():
    a = "Hello"
    b = "World"
    resultat = a + " " + b
    print('Concaténation de chaînes de caractères : ' + resultat)  # Affiche: "Hello World"

    a = "Hello "
    resultat = a * 3
    print('Répétition de chaînes de caractères : ' + resultat)  # Affiche: "Hello Hello Hello "

    a = "Hello"
    premier_caractere = a[0]
    print('Accès aux caractères individuels : ' + resultat)  # Affiche: "H"

    a = "Hello World"
    sous_chaine = a[6:11]
    print('Tranches de chaînes de caractères : ' + sous_chaine)  # Affiche: "World"

    a = "   Hello World   "
    longueur = len(a)
    en_majuscules = a.upper()
    en_minuscules = a.lower()
    sans_espaces = a.strip()
    mots = a.split()
    print('len()    : ' + str(longueur))  # 17
    print('upper()  : ' + en_majuscules)  # HELLO WORLD
    print('lower()  : ' + en_minuscules)  # hello world
    print('strip()  : ' + sans_espaces)   # Hello World
    print('split()  : ' + str(mots) + ' / ' + str(mots[0]) + ' / ' + str(mots[1]))  # ['Hello', 'World'] / Hello / World
    #print('split()  : ' + str(mots[2]))  # Erreur: IndexError: list index out of range

########################################################################################################################
# 01.21 - La fonction type()
########################################################################################################################
'''
En Python, la fonction type() est utilisée pour obtenir le type d'un objet ou d'une valeur. Elle retourne une référence 
vers le type de l'objet en question. Voici quelques exemples d'utilisation de la fonction type(). Cela peut être 
particulièrement utile lorsque vous travaillez avec des variables dont le type peut varier ou lors du débogage de code.
'''
def test_type():
    a = 42
    print('a = 42 : ' + str(type(a)))  # Affiche : <class 'int'>

    b = 3.14
    print('b = 3.14 : ' + str(type(b)))  # Affiche : <class 'float'>

    c = "Hello"
    print('c = "Hello" : ' + str(type(c)))  # Affiche : <class 'str'>

    d = [1, 2, 3]
    print('d = [1, 2, 3] : ' + str(type(d))) # Affiche : <class 'list'>

    e = {'a': 1, 'b': 2}
    print("e = {'a': 1, 'b': 2} : " + str(type(e)))  # Affiche : <class 'dict'>

########################################################################################################################
# 01.22 - La fonction print()
########################################################################################################################
'''
La fonction print() en Python est utilisée pour afficher du texte ou d'autres valeurs sur la sortie standard, 
généralement la console. Elle permet d'afficher des messages à l'utilisateur ou de vérifier les valeurs des variables 
pendant l'exécution d'un programme. Voici quelques exemples d'utilisation de la fonction print() :
'''
def fonction_print():
    print("Bonjour, Python!")  # Affichage simple.

    x = 42
    print(x)  # Afficher le contenu d'une variable.

    nom = "John"
    age = 25
    print("Nom:", nom, "Age:", age)  # Afficher plusieurs valeurs séparées par des virgules.

########################################################################################################################
# 01.23 - La fonction input()
########################################################################################################################
'''
La fonction print() en Python est utilisée pour demander à l'utilisateur d'entrer une données afin de la traiter dans
le programme python.
'''
def fonction_input():
    nom = input("Qu'elle est ton nom? ")  # Demande une saisie à l'écran.
    print(nom)  # Afficher le contenu de la variable saisie.

    age = input("Qu'elle est ton age? ")
    print(type(age))  # Vérification du type de la données

    age = int(age)  # Modification en type INTEGER
    print(type(age))  # Vérification du type de la données

    print(age)

########################################################################################################################
# 01.24 - La méthode .format()
########################################################################################################################
'''
La fonction format() permet de créer des chaînes formatées basées sur un gabarit. En utilisant les accolades dans une
chaine de caractères, il est possible par la suite de les remplacer par une valeur. Dans l'exemple ci-dessous:

    1.  Dans la chaîne de caractères, les accolades vides {} précisent l'endroit où le contenu de la variable doit être 
        inséré.
        
    2.  Juste après la chaîne de caractères, l'instruction .format(nom, x) fournit la liste des variables à insérer, 
        d'abord la variable nom puis la variable x.

    3.  On peut éventuellement préciser le formatage en mettant un caractère deux-points : puis par exemple ici .2f qui 
        signifie 2 chiffres après la virgule.

    4.  La méthode .format() agit sur la chaîne de caractères à laquelle elle est attachée par le point.
'''
def fonction_format():
    age = 34
    nom = "Alexandre"
    print("{} a {} ans".format(nom, age))

    nb_G = 4500
    nb_C = 2575
    prop_GC = (nb_G + nb_C) / 14800

    print("On a {} G et {} C -> prop GC = {:.2f}".format(nb_G, nb_C, prop_GC))

########################################################################################################################
# 01.25 - L'impression formaté (chaînes formatées)
########################################################################################################################
'''
Allez lire les articles suivants pour de la documentation :
    -   https://python.sdv.univ-paris-diderot.fr/03_affichage/#32-ecriture-formatee
    -   http://pascal.ortiz.free.fr/contents/python/chaines_formatees/index.html
'''

########################################################################################################################
# 01.26 - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    #structure()
    #conversion()
    #operation_arithmetique()
    #operation_chaine()
    #test_type()
    #fonction_print()
    #fonction_input()
    fonction_format()

########################################################################################################################
# 01.27 - Références
########################################################################################################################
'''
https://docs.python.org/fr/3.8/library/stdtypes.html
https://python.sdv.univ-paris-diderot.fr/02_variables/
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming
https://gayerie.dev/docs/python/index.html
'''