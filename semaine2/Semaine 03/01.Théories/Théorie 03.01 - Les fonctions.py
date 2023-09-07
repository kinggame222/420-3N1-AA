"""Ce cours est sur l'utilisation des fonctions en python"""
########################################################################################################################
# 03.01 - Définition et but des fonctions
########################################################################################################################
'''
En programmation, une fonction est un bloc de code réutilisable qui effectue une tâche spécifique. Les fonctions sont 
utilisées pour organiser le code en le subdivisant en tâches plus petites et plus gérables. Elles sont essentielles pour 
éviter la répétition de code et pour rendre le code plus lisible et plus modulaire.

    - Exemple : Fonction pour calculer la somme de deux nombres
'''


def additionner01(a, b):
    resultat = a + b
    return resultat


'''
-   'additionner' est le nom de la fonction.
-   'a' et 'b' sont des paramètres de la fonction, ce sont des valeurs que vous fournissez à la fonction pour effectuer 
    des calculs.
-   À l'intérieur de la fonction, `resultat` est calculé en additionnant `a` et `b`.
-   La commande `return` renvoie la valeur calculée comme résultat de la fonction.
'''

########################################################################################################################
# 03.02 - Avantages de l'utilisation de fonctions
########################################################################################################################
'''
Les fonctions permettent d'écrire du code une fois et de l'utiliser à plusieurs endroits dans votre programme. Cela 
évite la duplication de code.

    - Exemple : Utilisation de la fonction 'additionner'
'''


def additionner02():
    print("Résultat1 : 5 + 3 = " + str(additionner01(5, 3)))
    print("Résultat2 : 10 + 20 = " + str(additionner01(10, 20)))


''' 
-   Vous pouvez utiliser la fonction `additionner` pour effectuer des additions différentes sans réécrire le code à 
    chaque fois.

Les fonctions facilitent la division du code en petites parties gérables, donc la modulabilité. Vous pouvez développer, 
tester et déboguer des fonctions individuellement, ce qui simplifie la maintenance du code.

    - Exemple : Fonction pour calculer la moyenne de trois nombres
'''


def moyenne(a, b, c):
    resultat = (a + b + c) / 3
    return resultat


'''
-   Vous pouvez créer une nouvelle fonction pour calculer la moyenne sans affecter le code de la fonction `additionner`.

L'utilisation de fonctions permet de donner des noms significatifs aux blocs de code, ce qui rend le code plus lisible 
et compréhensible.

    - Exemple : Appel de fonction avec des noms de paramètres significatifs
'''


def additionner03():
    resultat = additionner01(a=5, b=3)
    print(str(resultat))


'''
- En utilisant des noms de paramètres explicites, il est clair quelles valeurs sont utilisées pour quelles opérations.

En résumé, les fonctions sont un élément clé de la programmation en Python. Elles permettent de structurer, d'organiser 
et de réutiliser du code de manière efficace, ce qui facilite le développement de logiciels complexes et maintenables.
'''

########################################################################################################################
# 03.03 - Déclaration de fonctions
########################################################################################################################
'''
En Python, une fonction est définie en utilisant le mot-clé def, suivi du nom de la fonction, une paire de parenthèses 
contenant des paramètres (si nécessaire), et un deux-points (:). Le code de la fonction est ensuite indenté sous la 
déclaration. Voici la syntaxe de base :

    def nom_de_la_fonction(parametres):
        # Code de la fonction indenté
        # ...
        return resultat  # Optionnel

    -   Exemple : Fonction qui multiplie deux nombres
'''


def multiplier(a, b):
    resultat = a * b
    return resultat


'''
Le mot-clé def est utilisé pour déclarer une nouvelle fonction. Il indique au compilateur Python que vous définissez une 
fonction nommée nom_de_la_fonction.

Les paramètres sont des valeurs que vous spécifiez dans la déclaration de la fonction, et les arguments sont les valeurs 
réelles que vous passez à la fonction lorsque vous l'appelez.

    -   Exemple : Fonction qui calcule la puissance
'''


def puissance(base, exposant):
    resultat = base ** exposant
    return resultat


'''
-   Dans cet exemple, base et exposant sont des paramètres de la fonction puissance. Lorsque vous appelez cette fonction 
    avec puissance(2, 3), 2 et 3 sont des arguments qui sont assignés aux paramètres base et exposant.

Une fonction peut retourner une valeur en utilisant le mot-clé return. Cela permet à la fonction de calculer un résultat 
ou de produire une sortie.

    -   Exemple : Fonction qui vérifie la parité
'''


def parite(nombre):
    if nombre % 2 == 0:
        return True
    else:
        return False


'''
Dans cette fonction, 'parite' vérifie si un nombre est pair en utilisant l'opération modulo (%). Si le résultat est 
zéro, la fonction retourne True, sinon elle retourne False.
'''

########################################################################################################################
# 03.04 - Appel de fonctions
########################################################################################################################
'''
Pour appeler une fonction en Python, utilisez simplement son nom suivi de parenthèses. Si la fonction prend des 
arguments, incluez-les entre les parenthèses. Voici un exemple simple :

    -   Définition de la fonction
'''


def dire_bonjour():
    print("Bonjour !")


def appel_bonjour():
    dire_bonjour()  # Appel de la fonction


'''
-   Dans cet exemple, la fonction dire_bonjour est définie pour afficher "Bonjour !". Pour l'appeler, nous utilisons 
    dire_bonjour().

Les arguments sont des valeurs que vous fournissez à une fonction pour qu'elle les utilise dans son code. Vous pouvez 
spécifier les arguments lors de l'appel de la fonction. Voici un exemple :
'''


# Définition de la fonction avec des arguments
def multiplier(a, b):
    resultat = a * b
    print(f"{a} multiplié par {b} égale {resultat}")


def appel_multiplier():
    multiplier(5, 3)  # Appel de la fonction avec des arguments


'''
-   Dans cet exemple, la fonction multiplier prend deux arguments, a et b, et les utilise pour calculer le produit. 
    Lorsque nous appelons la fonction avec multiplier(5, 3), nous passons les valeurs 5 et 3 comme arguments.

Une fonction peut renvoyer une valeur en utilisant le mot-clé return. Vous pouvez stocker cette valeur dans une variable 
lorsque vous appelez la fonction. Voici un exemple :
'''


# Définition de la fonction qui renvoie une valeur
def carre(x):
    resultat = x * x
    return resultat


def appel_carre():
    nombre = 4
    carre_de_nombre = carre(nombre)  # Appel de la fonction et gestion de la valeur de retour
    print(f"Le carré de {nombre} est {carre_de_nombre}")


'''
-   Dans cet exemple, la fonction carre calcule le carré de x et renvoie le résultat. Lorsque nous appelons la fonction 
    avec carre(nombre), nous stockons la valeur de retour dans carre_de_nombre.
'''

########################################################################################################################
# 03.05 - Variables locales et globales
########################################################################################################################
'''
La différence entre variables locales vs variables globales :
    -   Variables Locales : Les variables locales sont définies à l'intérieur d'une fonction et ne sont accessibles qu'à 
        l'intérieur de cette fonction. Elles ont une portée limitée à la fonction où elles sont déclarées.
'''


def locale_01():
    variable_locale = 42
    print(f"À l'intérieur de la fonction : {variable_locale}")


def appel_locale_01():
    locale_01()
    print(variable_locale)  # Cela générera une erreur car variable_locale est locale à ma_fonction


'''
-   Dans cet exemple, variable_locale est une variable locale à la fonction ma_fonction. Elle n'est pas accessible en 
    dehors de cette fonction.

    -   Variables plobales : Les variables globales sont définies en dehors de toutes les fonctions et sont accessibles 
        de n'importe où dans le programme. Elles ont une portée globale.
'''
variable_globale = 42


def global_01():
    print(f"À l'intérieur de la fonction : {variable_globale}")


def appel_global_01():
    global_01()
    print(f"En dehors de la fonction : {variable_globale}")


'''
-   Dans cet exemple, variable_globale est une variable globale car elle est définie en dehors de la fonction. Elle peut 
être utilisée à la fois à l'intérieur et à l'extérieur de la fonction.

La portée d'une variable détermine où elle peut être utilisée dans le code. Une variable locale a une portée limitée à 
la fonction dans laquelle elle est définie, tandis qu'une variable globale a une portée tout au long du programme.

Si une variable locale et une variable globale ont le même nom, la variable locale a la priorité à l'intérieur de la 
fonction. Cela signifie que la variable locale masque la variable globale avec le même nom à l'intérieur de la fonction.
'''
variable = "globale"


def portee():
    variable = "locale"  # Variable locale avec le même nom
    print(f"À l'intérieur de la fonction : {variable}")


def appel_portee():
    portee()
    print(f"En dehors de la fonction : {variable}")


'''
Dans cet exemple, la variable variable à l'intérieur de la fonction est locale et a la priorité sur la variable globale 
avec le même nom.

Comprendre la portée des variables est essentiel pour éviter les erreurs de nommage et assurer que les variables sont 
utilisées de manière cohérente dans un programme.
'''

########################################################################################################################
# 03.06 - Fonctions avec paramètres par défaut
########################################################################################################################
'''
En Python, vous pouvez définir des valeurs par défaut pour les paramètres d'une fonction. Cela signifie que si un 
argument n'est pas fourni lors de l'appel de la fonction, la valeur par défaut sera utilisée.
'''


def saluer(nom, message="Bonjour"):
    print(f"{message}, {nom}!")


def appel_saluer():
    saluer("Alice")  # Appel de la fonction avec un seul argument et utilise le message par défaut "Bonjour"
    saluer("Bob", "Salut")  # Appel de la fonction avec deux argumentsUtilise le message "Salut"


'''
-   Dans cet exemple, la fonction saluer a un paramètre nom et un paramètre message avec une valeur par défaut de 
    "Bonjour". Si message n'est pas spécifié lors de l'appel, la valeur par défaut est utilisée. Cela permet de rendre 
    la fonction plus flexible.

Vous pouvez appeler une fonction en omettant certains arguments, mais il est important de respecter l'ordre des
paramètres.
'''


def addition(a, b, c):
    resultat = a + b + c
    return resultat


def appel_addition():
    # Appel de la fonction avec des paramètres manquants
    somme = addition(5, 3)  # Cela générera une erreur car le paramètre 'c' est manquant


'''
-   Dans cet exemple, nous appelons la fonction addition avec seulement deux arguments au lieu de trois. Cela générera 
    une erreur car la fonction s'attend à recevoir trois arguments.

Cependant, si vous utilisez des paramètres par défaut comme expliqué précédemment, vous pouvez appeler la fonction sans 
spécifier tous les arguments, à condition de respecter l'ordre des paramètres.

    -   Exemple : Appel de Fonction avec Paramètres Manquants et Paramètres par Défaut
'''


def addition(a, b, c=0):
    resultat = a + b + c
    return resultat


def appel_addition2():
    somme = addition(5, 3)  # Appel de la fonction avec un paramètre manquant et utilise la valeur par défaut de
    # 'c' (0)


'''
Dans cet exemple, nous avons ajouté une valeur par défaut de 0 pour le paramètre c, ce qui permet d'appeler la fonction 
avec seulement deux arguments sans générer d'erreur.
'''

########################################################################################################################
# 03.07 - Fonctions variadiques
########################################################################################################################
'''
Utilisation de *args pour Accepter un Nombre Variable d'Arguments Positionnels :
*args permet à une fonction de recevoir un nombre variable d'arguments positionnels (sans nom). Les arguments sont 
passés sous forme de tuple.
'''


def somme(*args):
    total = 0
    for nombre in args:
        total += nombre
    return total


def appel_somme():
    resultat = somme(1, 2, 3, 4, 5)
    print(resultat)  # Affiche 15


'''
-   Dans cet exemple, la fonction somme accepte un nombre variable d'arguments positionnels (*args) et additionne tous 
    les nombres passés en arguments.

Utilisation de **kwargs pour Accepter un Nombre Variable d'Arguments Nommés :
**kwargs permet à une fonction de recevoir un nombre variable d'arguments nommés (avec des noms). Les arguments sont 
passés sous forme de dictionnaire.
'''


def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")


def appel_afficher_infos():
    afficher_infos(nom="Alice", age=30, ville="Paris")


'''
-   Dans cet exemple, la fonction afficher_infos accepte un nombre variable d'arguments nommés (**kwargs) et affiche 
    leurs noms et valeurs. Cela permet de passer des informations de manière flexible à la fonction.

Combinaison de *args et **kwargs :
Vous pouvez combiner *args et **kwargs dans une même fonction pour accepter à la fois des arguments positionnels et 
nommés.
'''


def afficher_infos(nom, age, *args, **kwargs):
    print(f"Nom: {nom}")
    print(f"Age: {age}")
    if args:
        print("Autres données non nommées :")
        for donnee in args:
            print(donnee)
    if kwargs:
        print("Autres données nommées :")
        for cle, valeur in kwargs.items():
            print(f"{cle}: {valeur}")


def appel_afficher_infos():
    afficher_infos("Bob", 30, "Alma", "Canada", langue="français", profession="ingénieur")


'''
-   Dans cet exemple, la fonction afficher_infos accepte des arguments nom et age obligatoires, ainsi qu'un nombre 
    variable d'arguments positionnels *args et d'arguments nommés **kwargs.
'''

########################################################################################################################
# 03.08 - Fonctions Lambda (Anonymes)
########################################################################################################################
'''
En Python, une fonction lambda (ou fonction anonyme) est une fonction sans nom. Elle est généralement utilisée pour des 
opérations simples et ponctuelles. La syntaxe de base est la suivante :

    lambda arguments: expression
    
    -   arguments : Les arguments de la fonction.
    -   expression : L'expression à évaluer et à retourner.

    -   Exemple : Fonction Lambda pour Calculer le Carré d'un Nombre
'''


def lambda_01():
    carre = lambda x: x ** 2
    resultat = carre(5)
    print(resultat)  # Affiche 25


'''
-   Dans cet exemple, nous avons créé une fonction lambda qui prend un argument x et renvoie le carré de x.

Les fonctions lambda sont couramment utilisées pour des opérations simples comme le tri, la filtration et les 
transformations de données.

    -   Exemple : Utilisation de Fonctions Lambda pour Trier une Liste de Tuples par le Deuxième Élément
'''


def lambda_02():
    points = [(3, 6), (1, 8), (4, 3)]
    points_tries = sorted(points, key=lambda point: point[1])
    print(points_tries)  # Affiche [(4, 3), (3, 6), (1, 8)]


'''
-   Dans cet exemple, nous utilisons une fonction lambda pour spécifier que nous voulons trier la liste points en 
    fonction du deuxième élément de chaque tuple.

    -   Exemple : Utilisation de fonctions Lambda pour filtrer une liste
'''


def lambda_03():
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nombres_pairs = list(filter(lambda x: x % 2 == 0, nombres))
    print(nombres_pairs)  # Affiche [2, 4, 6, 8]


'''
Ici, nous utilisons une fonction lambda pour filtrer les nombres pairs de la liste nombres.

Les fonctions lambda sont particulièrement utiles lorsque vous avez besoin de petites fonctions pour des tâches 
spécifiques et que vous ne voulez pas créer une fonction nommée distincte. Elles sont couramment utilisées dans des 
contextes où une fonction est passée en tant qu'argument à d'autres fonctions, comme sorted() et filter().

    -   Exemple: Trier une Liste de Dictionnaires par une Clé Spécifique

Supposons que vous ayez une liste de dictionnaires et que vous souhaitiez trier cette liste en fonction d'une clé 
spécifique dans les dictionnaires. Dans ce cas, vous pouvez utiliser une fonction lambda pour spécifier la clé de tri.
'''


def lambda_04():
    personnes = [
        {'nom': 'Alice', 'age': 30},
        {'nom': 'Bob', 'age': 25},
        {'nom': 'Eve', 'age': 35}
    ]

    # Trier la liste par âge
    personnes_triees = sorted(personnes, key=lambda x: x['age'])
    print(personnes_triees)


'''    
-   Dans cet exemple, la fonction lambda lambda x: x['age'] est utilisée comme clé de tri pour trier la liste de 
    dictionnaires par l'âge de chaque personne. Cela permet de personnaliser le tri en fonction d'une clé spécifique.
'''

########################################################################################################################
# 03.09 - Fonctions Récursives
########################################################################################################################
'''
Une fonction récursive est une fonction qui s'appelle elle-même pour résoudre un problème plus grand en le divisant en 
des problèmes plus petits du même type. En d'autres termes, c'est une fonction qui se répète elle-même pour arriver à 
une solution.

Le cas de base est la condition qui permet de mettre fin à la récursivité. C'est une condition qui spécifie quand la 
fonction doit s'arrêter et renvoyer une valeur ou effectuer une action spécifique. Sans un cas de base, la récursion 
serait infinie.

Le cas récursif est la partie de la fonction qui appelle elle-même avec des arguments différents pour résoudre un 
problème plus petit du même type. Cela se fait généralement après avoir effectué une action ou une opération.

    -   Exemple : Calcul de la Factorielle (Cas Réel de Récursivité)
'''


def factorielle(n):
    # Cas de base
    if n == 0:
        return 1
    # Cas récursif
    else:
        return n * factorielle(n - 1)


def appel_factorielle():
    resultat = factorielle(5)
    print(resultat)  # Affiche 120


'''
-   Dans cet exemple, la fonction factorielle calcule la factorielle d'un nombre en utilisant la récursivité. Le cas de 
base est lorsque n atteint 0, et la fonction renvoie 1. Sinon, la fonction se rappelle avec n - 1 pour résoudre un 
problème plus petit, puis multiplie le résultat par n.

!!! Attention aux Boucles Infinies !!!

Lors de la création de fonctions récursives, il est crucial de s'assurer qu'il existe un cas de base et que la récursion 
converge vers ce cas. Sinon, une boucle infinie se produira, ce qui entraînera un dépassement de la pile et le programme 
ne s'arrêtera jamais.

    -   Exemple : Boucle Infinie
'''


def boucle_infinie():
    print("Ceci est une boucle infinie")
    boucle_infinie()


def appel_boucle_infini():
    boucle_infinie()


'''
-   Dans cet exemple, la fonction boucle_infinie s'appelle elle-même sans condition de fin. Cela entraînera une boucle 
'''

########################################################################################################################
# 03.10 - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    appel_bonjour()
    appel_boucle_infini()
    appel_factorielle(8)
    appel_somme()
    appel_saluer()
    appel_addition()
    appel_addition2()
    appel_afficher_infos()
    appel_carre()
    appel_global_01()
    appel_locale_01()
    appel_multiplier()
    appel_portee()

########################################################################################################################
# 03.11 - Références
########################################################################################################################
'''
https://docs.python.org/fr/3.8/library/stdtypes.html
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming
https://python.sdv.univ-paris-diderot.fr/02_variables/
https://gayerie.dev/docs/python/index.html
https://python.doctor/
'''
