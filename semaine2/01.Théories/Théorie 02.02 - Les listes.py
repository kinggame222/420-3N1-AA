"""Ce cours est sur l'utilisation des listes en python"""
########################################################################################################################
# 02.00 - Les listes
########################################################################################################################
'''
En Python, une liste est une structure de données qui permet de stocker et de gérer une collection ordonnée d'éléments. 
Une liste peut contenir différents types d'éléments tels que des nombres, des chaînes de caractères, d'autres listes, 
des tuples, des dictionnaires et plus encore. Les listes sont très flexibles et offrent des méthodes pour ajouter, 
supprimer, modifier et accéder aux éléments.

Syntaxe de base :
    ma_liste = [élément1, élément2, ..., élémentN]

Voici quelques points clés à retenir sur les listes en Python :

    - Collection Ordonnée : Les éléments dans une liste sont ordonnés, ce qui signifie qu'ils ont une position 
                            spécifique. Vous pouvez accéder à un élément en utilisant son index.

    - Mutabilité          : Les listes sont mutables, ce qui signifie que vous pouvez ajouter, supprimer et modifier des 
                            éléments à l'intérieur d'une liste après sa création.

    - Types d'Éléments    : Une liste peut contenir des éléments de différents types de données. Par exemple, une liste 
                            peut contenir des nombres, des chaînes de caractères, des booléens, etc.

    - Longueur Variable   : Vous pouvez ajouter ou supprimer des éléments de la liste à tout moment, ce qui signifie que
                            la longueur de la liste peut varier.

    - Indexation          : Les éléments dans une liste sont indexés à partir de zéro. Vous pouvez accéder à un élément 
                            en utilisant son index.

    - Méthodes Intégrées  : Python fournit de nombreuses méthodes intégrées pour travailler avec des listes, telles que 
                            append(), insert(), remove(), pop(), index(), sort(), len(), etc.

'''

########################################################################################################################
# 02.00 - La méthode append()
########################################################################################################################
'''
La méthode append() est une méthode intégrée dans Python qui permet d'ajouter un élément à la fin d'une liste existante. 
Cette méthode modifie directement la liste sur laquelle elle est appelée en ajoutant l'élément à la dernière position.

Voici la syntaxe générale de la méthode append() :
    ma_liste.append(élément)

    - ma_liste  : la liste à laquelle vous souhaitez ajouter l'élément.
    - élément   : l'élément que vous souhaitez ajouter à la liste.
'''


# Exemple : Ajout d'un élément à une liste vide
def append_01():
    nombres = []
    nombres.append(10)
    nombres.append(20)
    nombres.append(30)
    print(nombres)  # Résultat : [10, 20, 30]


'''
Dans cet exemple, nous avons créé une liste vide nombres et ajouté trois éléments à l'aide de la méthode append(). 
La liste nombres sera modifiée à chaque appel de append().
'''


# Exemple : Ajout de chaînes de caractères à une liste de mots
def append_02():
    mots = ["chat", "chien"]
    nouveau_mot = "oiseau"
    mots.append(nouveau_mot)
    print(mots)  # Résultat : ["chat", "chien", "oiseau"]


'''
Dans cet exemple, nous avons une liste mots contenant deux mots. 
Nous utilisons ensuite la méthode append() pour ajouter le mot "oiseau" à la fin de la liste.
'''

########################################################################################################################
# 02.00 - Concaténation de liste
########################################################################################################################
'''
Tout comme les chaînes de caractères, les listes supportent l'opérateur + de concaténation, ainsi que l'opérateur * pour 
la duplication. Il est conseillé d'utiliser la méthode .append() dont la syntaxe est plus élégante.
'''


# Exemple : Concaténation de chaine de caractères
def concatenation_01():
    ani1 = ["girafe", "tigre"]
    ani2 = ["singe", "souris"]
    print(ani1 + ani2)
    print(ani1 * 3)


# Exemple : Concaténation de numérique
def concatenation_02():
    a = []
    a += [15]
    print(a)
    a = a + [-5]
    print(a)


########################################################################################################################
# 02.00 - La méthode insert()
########################################################################################################################
'''
La méthode insert() est une méthode intégrée en Python qui permet d'insérer un élément à une position spécifique dans une 
liste existante. Cette méthode déplace les éléments existants vers la droite pour faire de la place à l'élément inséré.

Voici la syntaxe générale de la méthode insert() :
    ma_liste.insert(index, élément)

    - ma_liste  : la liste dans laquelle vous souhaitez insérer l'élément.
    - index     : l'index à laquelle vous souhaitez insérer l'élément.
    - élément   : l'élément que vous souhaitez insérer.
'''


# Exemple : Insérer un élément à un index spécifique
def insert_01():
    nombres = [1, 2, 3, 4, 5]
    nombres.insert(2, 10)
    print(nombres)  # Résultat : [1, 2, 10, 3, 4, 5]


'''
Dans cet exemple, nous avons une liste nombres et nous utilisons la méthode insert() pour ajouter le nombre 10 à 
l'index 2. Cela décale les éléments existants vers la droite.
'''


# Exemple : Insérer une chaîne de caractères dans une liste de mots
def insert_02():
    animaux = ["chien", "chat", "éléphant"]
    nouvel_animal = "tigre"
    animaux.insert(1, nouvel_animal)
    print(animaux)  # Résultat : ["chien", "tigre", "chat", "éléphant"]


'''
Dans cet exemple, nous avons une liste animaux et nous utilisons insert() pour insérer le mot "tigre" à l'index 1, ce 
qui déplace le mot "chat" vers la droite.
'''

########################################################################################################################
# 02.00 - La méthode remove()
########################################################################################################################
'''
La méthode remove() est une méthode intégrée en Python qui permet de supprimer la première occurrence d'une valeur 
spécifique dans une liste. Si la valeur n'est pas présente dans la liste, une erreur se produira. La méthode remove() 
modifie directement la liste en supprimant l'élément correspondant.

Voici la syntaxe générale de la méthode remove() :
    ma_liste.remove(valeur)

    - ma_liste  : la liste dans laquelle vous souhaitez supprimer la valeur.
    - valeur    : la valeur que vous souhaitez supprimer.
'''


# Exemple : Suppression d'une valeur spécifique
def remove_01():
    nombres = [10, 20, 30, 40, 20]
    nombres.remove(20)
    print(nombres)  # Résultat : [10, 30, 40, 20]


'''
Dans cet exemple, nous avons une liste nombres contenant plusieurs occurrences de la valeur 20. 
La méthode remove() supprime la première occurrence de 20 de la liste.
'''


# Exemple : Suppression d'une chaîne de caractères dans une liste de mots
def remove_02():
    fruits = ["pomme", "banane", "orange"]
    fruits.remove("banane")
    print(fruits)  # Résultat : ["pomme", "orange"]


'''
Dans cet exemple, nous avons une liste fruits contenant des noms de fruits. 
Nous utilisons la méthode remove() pour supprimer la chaîne "banane" de la liste.
'''

########################################################################################################################
# 02.00 - La méthode pop()
########################################################################################################################
'''
La méthode pop() est une méthode intégrée en Python qui permet de supprimer et de renvoyer l'élément à un index spécifié 
dans une liste. Si aucun index n'est spécifié, pop() supprime et renvoie le dernier élément de la liste. La méthode 
pop() modifie la liste en retirant l'élément à l'index spécifié.

Voici la syntaxe générale de la méthode pop() :
    élément_retiré = ma_liste.pop(index)

    - ma_liste  : la liste dans laquelle vous souhaitez retirer l'élément.
    - index     : l'index de l'élément que vous souhaitez retirer (facultatif).
'''


# Exemple : Retirer et récupérer l'élément à un index spécifique
def pop_01():
    nombres = [10, 20, 30, 40, 50]
    element_retire = nombres.pop(2)
    print("Élément retiré :", element_retire)  # Résultat : Élément retiré : 30
    print("Liste restante :", nombres)  # Résultat : Liste restante : [10, 20, 40, 50]


'''
Dans cet exemple, nous avons une liste nombres et nous utilisons pop(2) pour retirer et renvoyer l'élément à l'index 2, 
qui est 30. La liste résultante ne contient plus cet élément.
'''


# Exemple : Retirer et renvoyer le dernier élément de la liste
def pop_02():
    fruits = ["pomme", "banane", "orange"]
    dernier_fruit = fruits.pop()
    print("Dernier fruit retiré :", dernier_fruit)  # Résultat : Dernier fruit retiré : orange
    print("Liste restante :", fruits)  # Résultat : Liste restante : ["pomme", "banane"]


'''
Dans cet exemple, nous utilisons pop() sans argument pour retirer et renvoyer le dernier 
élément "orange" de la liste fruits.
'''

########################################################################################################################
# 02.00 - La méthode index()
########################################################################################################################
'''
La méthode index() est une méthode intégrée en Python qui permet de rechercher la première occurrence d'une valeur 
spécifique dans une liste et de renvoyer son index. Si la valeur n'est pas présente dans la liste, une erreur se 
produira. La méthode index() ne modifie pas la liste, elle renvoie simplement l'index de l'élément recherché.

Voici la syntaxe générale de la méthode index() :
    index = ma_liste.index(valeur)

    - ma_liste  : la liste dans laquelle vous souhaitez rechercher la valeur.
    - valeur    : la valeur que vous souhaitez rechercher.
'''


# Exemple : Recherche de l'index d'une valeur spécifique
def index_01():
    nombres = [10, 20, 30, 20, 40]
    index = nombres.index(20)
    print("Index de la première occurrence de 20 :", index)  # Résultat : Index de la première occurrence de 20 : 1


'''
Dans cet exemple, nous avons une liste nombres contenant plusieurs occurrences de la valeur 20. La méthode index() 
renvoie l'index de la première occurrence de 20 dans la liste, qui est 1.
'''


# Exemple : Recherche de l'index d'une chaîne de caractères dans une liste de mots
def index_02():
    animaux = ["chien", "chat", "chien", "oiseau"]
    index = animaux.index("chien")
    print("Index de la première occurrence de 'chien' :",
          index)  # Résultat : Index de la première occurrence de 'chien' : 0


'''
Dans cet exemple, nous avons une liste animaux contenant plusieurs occurrences du mot "chien". La méthode index() 
renvoie l'index de la première occurrence de "chien" dans la liste, qui est 0.

Il est important de noter que si la valeur que vous recherchez n'est pas présente dans la liste, une ValueError sera 
levée. Pour éviter cela, vous pouvez vérifier si la valeur existe dans la liste avant d'utiliser index().
'''


# Exemple : Vérification de l'existence d'une valeur dans une liste
def index_03():
    ma_liste = [1, 2, 3, 4, 5]
    valeur_recherchee = 3

    if valeur_recherchee in ma_liste:
        index = ma_liste.index(valeur_recherchee)  # Pour obtenir l'index
        print(f"La valeur existe dans la liste à l'index {index}.")
    else:
        print("La valeur n'existe pas dans la liste.")


########################################################################################################################
# 02.00 - L'indexage négative
########################################################################################################################
'''
L'indexage négatif est une fonctionnalité en Python qui vous permet d'accéder aux éléments d'une séquence 
(comme une liste) en comptant à partir de la fin de la séquence. L'indice -1 représente le dernier élément, -2 
représente l'avant-dernier élément, et ainsi de suite. L'indicage négatif fonctionne pour des séquences de toutes 
tailles, qu'elles soient petites ou grandes. Vous n'avez pas besoin de connaître la longueur totale de la séquence pour 
accéder aux éléments à partir de la fin.

    liste          : ["girafe", "tigre", "singe", "souris"]
    indice positif :        0        1        2         3
    indice négatif :       -4       -3       -2        -1
    
    liste          : ["A", "B", "C", "D", "E", "F"]
    indice positif :   0    1    2    3    4    5
    indice négatif :  -6   -5   -4   -3   -2   -1
'''


# Exemple : Accès aux éléments en utilisant l'indicage négatif
def index_04():
    ma_liste = [10, 20, 30, 40, 50]
    dernier_element = ma_liste[-1]  # Accès au dernier élément
    avant_dernier_element = ma_liste[-2]  # Accès à l'avant-dernier élément

    print("Dernier élément :", dernier_element)  # Résultat : Dernier élément : 50
    print("Avant-dernier élément :", avant_dernier_element)  # Résultat : Avant-dernier élément : 40


'''
Dans cet exemple, nous avons une liste ma_liste et nous utilisons l'indicage négatif pour accéder aux deux derniers 
éléments de la liste.
'''


# Exemple : Utilisation de l'indicage négatif pour extraire une sous-liste
def index_05():
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    derniers_trois_elements = nombres[-3:]  # Accès aux trois derniers éléments

    print("Derniers trois éléments :", derniers_trois_elements)  # Résultat : Derniers trois éléments : [8, 9, 10]


'''
Dans cet exemple, nous utilisons l'indicage négatif pour extraire les trois derniers éléments de la liste nombres.
'''

########################################################################################################################
# 02.00 - Accèder à l'aide des tranches
########################################################################################################################
'''
Un autre avantage des listes est la possibilité de sélectionner une partie d'une liste en utilisant un indiçage 
construit sur le modèle [m:n+1] pour récupérer tous les éléments, du émième au énième (de l'élément m inclus à 
l'élément n+1 exclu).

Donc, la syntaxe:
    liste[début:fin:pas]

'''


# Exemple : Afficher à l'aide de tranche.
def index_06():
    animaux = ["girafe", "tigre", "singe", "souris"]
    print(animaux[0:2])
    print(animaux[0:3])
    print(animaux[0:])
    print(animaux[:])
    print(animaux[1:])
    print(animaux[1:-1])


'''
Si aucun indice n'est indiqué à gauche ou à droite du symbole deux-points, Python prend par défaut tous les éléments 
depuis le début ou tous les éléments jusqu'à la fin respectivement.
On peut aussi préciser le pas en ajoutant un symbole deux-points supplémentaire et en indiquant le pas par un entier.
'''


# Exemple afficher avec les tranches
def index_07():
    animaux = ["girafe", "tigre", "singe", "souris"]
    print('["girafe", "tigre", "singe", "souris"]')
    print('animaux[0:3:2]')
    print(animaux[0:3:2])

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('x')
    print(x)
    print('x[::1]')
    print(x[::1])
    print('x[::2]')
    print(x[::2])
    print('x[::3]')
    print(x[::3])
    print('x[1:6:3]')
    print(x[1:6:3])


########################################################################################################################
# 02.00 - La méthode sort()
########################################################################################################################
'''
La méthode sort() est une méthode intégrée en Python qui permet de trier les éléments d'une liste dans l'ordre 
croissant. La méthode sort() modifie directement la liste en la réorganisant, sans renvoyer une nouvelle liste triée. 
Si vous souhaitez obtenir une nouvelle liste triée sans modifier l'originale, vous pouvez utiliser la fonction sorted().

Voici la syntaxe générale de la méthode sort() :
    ma_liste.sort()
'''


# Exemple : Trier une liste de nombres
def sort_01():
    nombres = [30, 10, 50, 20, 40]
    nombres.sort()
    print(nombres)  # Résultat : [10, 20, 30, 40, 50]


'''
Dans cet exemple, nous avons une liste nombres avec des valeurs désordonnées. 
En utilisant sort(), les éléments sont triés dans l'ordre croissant.
'''


# Exemple : Trier une liste de chaînes de caractères
def sort_02():
    mots = ["banane", "pomme", "orange", "fraise"]
    mots.sort()
    print(mots)  # Résultat : ["banane", "fraise", "orange", "pomme"]


'''
Dans cet exemple, nous avons une liste mots avec des chaînes de caractères non triées. 
En utilisant sort(), les mots sont triés alphabétiquement.
'''

########################################################################################################################
# 02.00 - La méthode sorted()
########################################################################################################################
'''
La fonction sorted() est une fonction intégrée en Python qui permet de trier les éléments d'une séquence (comme une 
liste, un tuple, etc.) dans l'ordre croissant et de renvoyer une nouvelle séquence triée. Contrairement à la méthode 
sort() qui modifie directement la liste, sorted() crée une nouvelle liste triée sans modifier la séquence d'origine.

Voici la syntaxe générale de la fonction sorted() :
    nouvelle_sequence = sorted(ma_sequence)
'''


# Exemple : Trier une liste de nombres
def sorted_01():
    nombres = [30, 10, 50, 20, 40]
    nombres_tries = sorted(nombres)
    print(nombres_tries)  # Résultat : [10, 20, 30, 40, 50]
    print(nombres)  # Résultat : [30, 10, 50, 20, 40] (la liste d'origine reste inchangée)


'''
Dans cet exemple, nous avons une liste nombres avec des valeurs désordonnées. En utilisant sorted(), une nouvelle liste 
triée nombres_tries est créée, laissant la liste d'origine nombres inchangée.
'''


# Exemple : Trier une liste de chaînes de caractères
def sorted_02():
    mots = ["banane", "pomme", "orange", "fraise"]
    mots_tries = sorted(mots)
    print(mots_tries)  # Résultat : ["banane", "fraise", "orange", "pomme"]
    print(mots)  # Résultat : ["banane", "pomme", "orange", "fraise"] (la liste d'origine reste inchangée)


'''
Dans cet exemple, nous avons une liste mots avec des chaînes de caractères non triées. En utilisant sorted(), une 
nouvelle liste triée mots_tries est créée, sans modifier la liste d'origine mots.
'''

########################################################################################################################
# 02.00 - La méthode reverse()
########################################################################################################################
'''
La méthode reverse() est une méthode intégrée en Python qui permet d'inverser l'ordre des éléments dans une liste. Après 
avoir utilisé la méthode reverse(), l'élément qui était à l'index 0 se retrouvera à l'index -1 (le dernier élément), 
l'élément à l'index 1 se retrouvera à l'index -2, et ainsi de suite.

Voici la syntaxe générale de la méthode reverse() :
    ma_liste.reverse()
'''


# Exemple : Inversion de l'ordre des nombres dans une liste
def reverse_01():
    nombres = [10, 20, 30, 40, 50]
    nombres.reverse()
    print(nombres)  # Résultat : [50, 40, 30, 20, 10]


'''
Dans cet exemple, la liste nombres est inversée en utilisant la méthode reverse(). Les éléments qui étaient à l'origine 
en début de liste sont maintenant à la fin.
'''


# Exemple : Inversion de l'ordre des mots dans une liste de chaînes de caractères
def reverse_02():
    mots = ["chat", "chien", "oiseau"]
    mots.reverse()
    print(mots)  # Résultat : ["oiseau", "chien", "chat"]


'''
Dans cet exemple, la liste mots contenant des chaînes de caractères est inversée en utilisant la méthode reverse(). Les 
mots qui étaient à l'origine en début de liste sont maintenant à la fin.
'''

########################################################################################################################
# 02.00 - La méthode len()
########################################################################################################################
'''
La fonction len() est une fonction intégrée en Python qui permet de renvoyer la longueur d'une séquence, comme une liste, 
un tuple, une chaîne de caractères, etc. Pour une liste, len() renvoie le nombre d'éléments présents dans la liste.
La fonction len() est utile lorsque vous avez besoin de connaître le nombre d'éléments dans une séquence, ce qui peut 
être particulièrement utile pour la programmation conditionnelle et la manipulation de données.

Voici la syntaxe générale de la fonction len() :
    longueur = len(ma_sequence)
'''


# Exemple : Calcul de la longueur d'une liste
def len_01():
    nombres = [10, 20, 30, 40, 50]
    longueur = len(nombres)
    print("Longueur de la liste :", longueur)  # Résultat : Longueur de la liste : 5


'''
'''


# Exemple : Vérification de la longueur d'une liste vide
def len_02():
    animaux = []
    longueur = len(animaux)
    if longueur == 0:
        print("La liste est vide.")
    else:
        print("La liste contient des éléments.")


'''
Dans cet exemple, nous avons une liste vide animaux. En utilisant len(), nous obtenons la longueur de la liste, qui 
est 0. Ensuite, nous vérifions si la longueur est égale à 0 pour déterminer si la liste est vide.
'''

########################################################################################################################
# 02.00 - La méthode count()
########################################################################################################################
'''
La méthode count() est une méthode intégrée en Python qui permet de compter le nombre d'occurrences d'un élément 
spécifique dans une liste.

Voici la syntaxe générale de la méthode count() :
    nombre_occurrences = ma_liste.count(element)

    - ma_liste  : la liste dans laquelle vous souhaitez compter les occurrences.
    - element   : l'élément que vous souhaitez compter.
'''


# Exemple : Compter le nombre d'occurrences d'un nombre dans une liste
def count_01():
    nombres = [10, 20, 30, 20, 40]
    nombre_occurrences = nombres.count(20)
    print("Nombre d'occurrences de 20 :", nombre_occurrences)  # Résultat : Nombre d'occurrences de 20 : 2


'''
Dans cet exemple, nous avons une liste nombres avec plusieurs occurrences de la valeur 20. La méthode count() renvoie le 
nombre d'occurrences de 20 dans la liste, qui est 2.
'''


# Exemple : Compter le nombre d'occurrences de chaînes de caractères dans une liste
def count_02():
    mots = ["chien", "chat", "chien", "chien", "oiseau"]
    nombre_occurrences = mots.count("chien")
    print("Nombre d'occurrences de 'chien' :", nombre_occurrences)  # Résultat : Nombre d'occurrences de 'chien' : 3


'''
Dans cet exemple, nous avons une liste mots contenant plusieurs occurrences du mot "chien". La méthode count() renvoie 
le nombre d'occurrences de "chien" dans la liste, qui est 3.
'''

########################################################################################################################
# 02.00 - La méthode clear()
########################################################################################################################
'''
La méthode clear() est une méthode intégrée en Python qui permet de supprimer tous les éléments d'une liste, la laissant 
vide. Après l'appel à clear(), la liste sera vide, ne contenant aucun élément. La méthode clear() est utile lorsque vous 
souhaitez réinitialiser ou nettoyer une liste en la vidant de son contenu existant.

Voici la syntaxe générale de la méthode clear() :
    ma_liste.clear()
'''


# Exemple : Vider une liste
def clear_01():
    nombres = [10, 20, 30, 40, 50]
    nombres.clear()
    print(nombres)  # Résultat : []


########################################################################################################################
# 02.00 - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    append_01()
    append_02()
    concatenation_01()
    concatenation_02()
    insert_01()
    insert_02()
    remove_01()
    remove_02()
    pop_01()
    pop_02()
    index_01()
    index_02()
    index_03()
    index_04()
    index_05()
    index_06()
    index_07()
    sort_01()
    sort_02()
    sorted_01()
    sorted_02()
    reverse_01()
    reverse_02()
    len_01()
    len_02()
    count_01()
    count_02()
    clear_01()

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
