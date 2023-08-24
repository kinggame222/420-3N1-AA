"""Ce cours est sur les bonnes pratiques de la programmation Python"""
########################################################################################################################
# 01.01 - Les bonnes pratiques : https://peps.python.org/pep-0008/
########################################################################################################################
'''
PEP 8 est un guide de style officiel pour écrire du code Python. PEP signifie "Python Enhancement Proposal" (proposition 
d'amélioration Python) et le numéro 8 est celui spécifique à la recommandation de style de code.

Le PEP 8 fournit des directives sur la façon de formater le code Python pour le rendre plus lisible et cohérent. Il vise 
à améliorer la lisibilité du code et à faciliter la collaboration entre les développeurs. 
'''

########################################################################################################################
# 01.02 - Les commentaires
########################################################################################################################
# Ceci est un commentaire sur une ligne

'''
    1.  Les commentaires sont sur le même niveau d'indentation que le code qu'ils commentent. Les commentaires sont 
        constitués de phrases complètes, avec une majuscule au début (sauf si le premier mot est une variable qui 
        s'écrit sans majuscule) et un point à la fin.

    2.  Les commentaires qui suivent le code sur la même ligne sont à éviter le plus possible et doivent être séparés du 
        code par au moins deux espaces.
'''
print("Hello, World!")  # Ceci est aussi un commentaire sur une ligne

"""
    3.  La PEP 8 recommande très fortement d'écrire les commentaires en anglais, sauf si vous êtes à 120% sûr que votre 
        code ne sera lu que par des francophones.
"""

########################################################################################################################
# 01.03 Les docstrings
########################################################################################################################
'''
Il est important de créer de la documentation pour expliquer ce que fait le module et comment utiliser chaque fonction. 
Les chaînes de caractères entre triple guillemets situées en début du module et de chaque fonction sont là pour cela, 
on les appelle docstrings (« chaînes de documentation » en français). Ces docstrings permettent notamment de fournir de 
l'aide lorsqu'on invoque la commande help().

    1.  De manière générale, écrivez des docstrings pour les modules, les fonctions, les classes et les méthodes. 
        Lorsque l'explication est courte et compacte comme dans certaines fonctions ou méthodes simples, utilisez des 
        docstrings d'une ligne.
    
    2.  Lorsque vous avez besoin de décrire plus en détail un module, une fonction, une classe ou une méthode, utilisez 
        une docstring sur plusieurs lignes.
        
    3.  Les éléments essentiels sont: 
        -   ce que fait la fonction ou la méthode,
        -   ce qu'elle prend en argument,
        -   ce qu'elle renvoie.

    4.  Il existe des solutions pour bien organiser les docstrings:
        -   Google  =   https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        -   Numpy   =   https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

Exemples d'utilisation: 
    -   Commencez par importer vos script dans votre 'Python Console': import message
    -   Faites un test dans votre 'Python Console' en appellant: help(message)
    -   Encore dans la console Python, importez le fichier du cours et faite l'appelle de la fonction help()
    -   Vous pouvez aussi appeller une fonction précise prevenant d'un module: help(message.bonjour)
    -   En résumé, les docstrings sont destinés aux utilisateurs du module. Leur but est différent des commentaires qui, 
        eux, sont destinés à celui qui lit le code
'''

########################################################################################################################
# 01.04 - L'indentation
########################################################################################################################
'''
En Python, l'indentation est une caractéristique syntaxique fondamentale qui détermine la structure et la logique du 
code. Contrairement à certains autres langages de programmation qui utilisent des accolades ou des mots-clés pour 
délimiter les blocs de code, Python utilise l'indentation pour indiquer la structure hiérarchique du code.

L'indentation consiste à ajouter des espaces ou des tabulations en début de ligne pour définir les blocs de code. Voici 
quelques points importants à connaître sur l'indentation en Python :

    1.  Niveau d'indentation : Les blocs de code sont définis par des niveaux d'indentation. Les lignes de code qui font 
        partie d'un même bloc doivent avoir la même indentation (même nombre d'espaces ou de tabulations en début de 
        ligne). Par convention, il est recommandé d'utiliser 4 espaces pour chaque niveau d'indentation.
        
    2.  Cohérence de l'indentation : L'indentation doit être cohérente dans tout le code. Si vous utilisez des espaces 
        pour l'indentation dans un bloc, vous devez continuer à utiliser des espaces pour l'indentation dans tout le 
        code. De même, si vous utilisez des tabulations, vous devez maintenir la même convention d'indentation avec des 
        tabulations dans tout le code.

    3.  Signification de l'indentation : L'indentation détermine la structure et la portée des blocs de code. Un bloc de 
        code avec une indentation supérieure est considéré comme étant à l'intérieur d'un bloc de code avec une 
        indentation inférieure. Par exemple, les instructions à l'intérieur d'une boucle `for` ou d'une condition `if` 
        sont indentées à un niveau supérieur par rapport à l'instruction de contrôle elle-même.

Exemple :
'''


def indentation_01():
    if 1 == 1:  # Peu importe la condition
        # Instructions indentées à l'intérieur du bloc if
        print("Condition est vraie")
        print("Autre instruction")
    # Fin du bloc if, retour à l'indentation précédente
    print("Fin du programme")


'''
    4.  Structure conditionnelle et boucles : Les structures conditionnelles telles que `if`, `else`, `elif`, ainsi que 
        les boucles telles que `for` et `while`, utilisent l'indentation pour délimiter les blocs de code associés. Le 
        contenu de ces blocs est exécuté en fonction de la condition ou de l'itération.
Exemple :
'''


def indentation_02():
    for i in range(5):
        # Instructions indentées à l'intérieur de la boucle for
        print(i)
    # Fin de la boucle for, retour à l'indentation précédente
    print("Fin du programme")


'''
L'indentation correcte est essentielle en Python pour garantir que le code soit correctement structuré et fonctionne 
comme prévu. Une indentation incorrecte peut entraîner des erreurs de syntaxe ou modifier la logique du code. Par 
conséquent, il est important de veiller à maintenir une indentation cohérente et correcte tout au long de votre code 
Python.
'''

########################################################################################################################
# 01.05 - Les règles de nommage
########################################################################################################################
'''
1.  Python est sensible à la casse, ce qui signifie que les variables AleX, alex ou ALEX sont différentes.

2.  Le nom des variables en Python peut être constitué de lettres minuscules (a à z), de lettres majuscules (A à Z), de 
    nombres (0 à 9) ou du caractère souligné (_). Vous ne pouvez pas utiliser d'espace dans un nom de variable. Aussi, 
    un nom de variable ne doit pas débuter par un chiffre.

3.  Les noms de variables, de fonctions et de modules doivent être de la forme suivante. En minuscules avec un caractère 
    « souligné » (« tiret du bas » ou underscore en anglais) pour séparer les différents « mots » dans le nom.
        ma_variable
        fonction_test_27()
        mon_module

4.  Les constantes sont écrites en majuscules
        MA_CONSTANTE
        VITESSE_LUMIERE
        
5.  Les noms des classes et des exceptions sont de la forme: 
        MaClasse
        MyException
        
6.  Pensez à donner à vos variables des noms qui ont du sens. Évitez autant que possible les a1, a2, i, truc, toto... 
    Les noms de variables à un caractère sont néanmoins autorisés pour les boucles et les indices :
'''


def nommage_01():
    ma_liste = [1, 3, 5, 7, 9, 11]
    for i in range(len(ma_liste)):
        print(ma_liste[i])


'''
    Bien sûr, une écriture plus simplifié de l'exemple précédent permet de se débarrasser de l'indice i :
'''


def nommage_02():
    ma_liste = [1, 3, 5, 7, 9, 11]
    for entier in ma_liste:
        print(entier)


'''
    Enfin, des noms de variable à une lettre peuvent être utilisés lorsque cela a un sens mathématique (par exemple, 
    les noms x, y et z évoquent des coordonnées cartésiennes).
'''

########################################################################################################################
# 01.06 - Gestion des espaces
########################################################################################################################
'''
1.  La PEP 8 recommande d'entourer les opérateurs (+, -, /, *, ==, !=, >=, not, in, and, or...) d'un espace avant et 
    d'un espace après.
'''


def espace_01():
    # code recommandé :
    ma_variable = 3 + 7
    mon_texte = "souris"
    mon_texte == ma_variable

    # code non recommandé :
    ma_variable = 3 + 7
    mon_texte = "souris"
    mon_texte == ma_variable


'''
2.  Pas d'espace à l'intérieur de crochets, d'accolades et de parenthèse.
'''


def espace_02():
    # code recommandé :
    ma_liste[1]
    mon_dico
    {"clé"}
    ma_fonction(argument)
    # code non recommandé :
    ma_liste[1]
    mon_dico
    {"clé"}
    ma_fonction(argument)


'''
3.  Pas d'espace avant la parenthèse ouvrante d'une fonction ou le crochet ouvrant d'une liste ou d'un dictionnaire.
'''


def espace_03():
    # code recommandé :
    ma_liste[1]
    mon_dico
    {"clé"}
    ma_fonction(argument)
    # code non recommandé :
    ma_liste[1]
    mon_dico
    {"clé"}
    ma_fonction(argument)


'''
4.  On met un espace après les caractères ':' et ',' (mais pas avant) ':'.
'''


def espace_04():
    # code recommandé :
    ma_liste = [1, 2, 3]
    mon_dico = {"clé1": "valeur1", "clé2": "valeur2"}
    ma_fonction(argument1, argument2)
    # code non recommandé :
    ma_liste = [1, 2, 3]
    mon_dico = {"clé1": "valeur1", "clé2": "valeur2"}
    ma_fonction(argument1, argument2)


'''
5.  Par contre, pour les tranches de listes, on ne met pas d'espace autour du ':'.
'''


def espace_05():
    ma_liste = [1, 3, 5, 7, 9, 1]
    # code recommandé :
    ma_liste[1:3]
    ma_liste[1:4:2]
    ma_liste[::2]
    # code non recommandé :
    ma_liste[1: 3]
    ma_liste[1: 4:2]
    ma_liste[::2]


'''
6.  On n'ajoute pas plusieurs espaces autour du '=' ou des autres opérateurs.
'''


def espace_06():
    # code recommandé :
    x1 = 1
    x2 = 3
    x_old = 5
    # code non recommandé :
    x1 = 1
    x2 = 3
    x_old = 5


########################################################################################################################
# 01.07 - Longeur de ligne
########################################################################################################################
'''
Pour des raison historique et de lisibilité, une ligne de code ne doit pas dépasser 79 caractère.
    1.  Pour écrire une ligne de code sur plusieurs lignes de votre éditeurs, pn peut utiliser le backslash: \
'''


def longueur_01():
    ma_variable = 3
    if ma_variable > 1 and ma_variable < 10 \
            and ma_variable % 2 == 1 and ma_variable % 3 == 0:
        print(f"Fonction longueur_01() : ma variable vaut {ma_variable}")


'''
    2.  À l'intérieur d'une parenthèse, on peut revenir à la ligne sans utiliser le caractère \ . C'est aussi pratiques 
        pour répartir sur plusieurs lignes une chaîne de caractères qui sera affichée sur une seule ligne. Même chose 
        pour évaluer une expression trop longue.
'''


def longueur_02(argument_1, argument_2,
                argument_3, argument_4):
    return argument_1 + argument_2
    print("ATGCGTACAGTATCGATAAC"
          "ATGACTGCTACGATCGGATA"
          "CGGGTAACGCCATGTACATT")

    if (ma_variable > 1 and ma_variable < 10
            and ma_variable % 2 == 1 and ma_variable % 3 == 0):
        print(f"Fonction longueur_02() : ma variable vaut {ma_variable}")


def longueur_03():
    longueur_02("texte très long", "tigre",
                "singe", "souris")


########################################################################################################################
# 01.08 - Lignes vides
########################################################################################################################
'''
Dans un script, les lignes vides sont utiles pour séparer visuellement les différentes parties du code.

Il est recommandé de laisser deux lignes vides avant la définition d'une fonction ou d'une classe et de laisser une 
seule ligne vide avant la définition d'une méthode (dans une classe).

On peut aussi laisser une ligne vide dans le corps d'une fonction pour séparer les sections logiques de la fonction
'''

########################################################################################################################
# 01.09 - Les mots réservés
########################################################################################################################
'''
Les mots réservés en Python sont des mots clés qui ont une signification spéciale dans le langage et qui ne peuvent pas 
être utilisés comme identificateurs (noms de variables, de fonctions, de classes, etc.). Ils sont utilisés pour définir 
la syntaxe et la structure du langage Python. Voici la liste des mots réservés en Python :
'''
import keyword


def mots_reserve():
    print(keyword.kwlist)


'''
Ces mots réservés sont utilisés pour des constructions spécifiques dans le code Python, tels que les déclarations de 
classes (class), les déclarations de fonctions (def), les instructions conditionnelles (if, elif, else), les boucles 
(for, while), les exceptions (try, except, finally), les déclarations d'importation (import), et bien d'autres encore.

Il est important de noter que vous ne devez pas utiliser ces mots réservés comme noms pour vos variables, fonctions, 
classes ou autres identificateurs, car cela entraînerait une erreur de syntaxe.
'''

########################################################################################################################
# 01.10 - Les séquences d’échappement
########################################################################################################################
'''
En Python, les séquences d'échappement sont des combinaisons spéciales de caractères qui sont utilisées pour représenter 
des caractères spéciaux ou des codes non imprimables dans les chaînes de caractères. Les séquences d'échappement 
commencent par un antislash (\) suivi d'un ou plusieurs caractères.

Voici quelques exemples courants de séquences d'échappement en Python : COLLER LES CARACTÈRES !!
    1.  `\ n` : Nouvelle ligne
        Cette séquence d'échappement est utilisée pour insérer une nouvelle ligne. Lorsqu'elle est rencontrée dans une 
        chaîne de caractères, elle génère une nouvelle ligne.

    2.  `\ t` : Tabulation horizontale
        Cette séquence d'échappement insère une tabulation horizontale dans une chaîne de caractères.

    3.  `\ \` : Antislash
        Utilisé pour insérer un antislash dans une chaîne de caractères.

    4.  `\ '` : Guillemet simple
        Utilisé pour insérer un guillemet simple dans une chaîne de caractères délimitée par des guillemets simples.

    5.  `\ "` : Guillemet double
        Utilisé pour insérer un guillemet double dans une chaîne de caractères délimitée par des guillemets doubles.

    6.  `\ xhh` : Caractère ASCII en hexadécimal
        Cette séquence d'échappement est utilisée pour insérer un caractère ASCII spécifique en utilisant sa valeur 
        hexadécimale.

Il existe d'autres séquences d'échappement disponibles en Python pour représenter des caractères spéciaux, des codes de 
contrôle et des caractères non imprimables. Vous pouvez vous référer à la documentation officielle de Python pour 
obtenir une liste complète des séquences d'échappement disponibles.
'''

########################################################################################################################
# 01.11 - Exécution d'un nouveau programme principal
########################################################################################################################
'''En Python, la variable spéciale `__name__` est une variable prédéfinie qui contient le nom du module courant. Son
utilisation est courante pour déterminer si un script Python est exécuté en tant que programme principal ou s'il est
importé en tant que module dans un autre script.

Lorsque vous exécutez un script Python directement, c'est-à-dire en le lançant comme un programme principal, la valeur
de `__name__` est définie sur `"__main__"`. Cela indique que le script est exécuté en tant que point d'entrée principal
du programme.

Par exemple, considérons le code suivant dans un fichier nommé `example.py` :
'''


def main():
    print("Ceci est le programme principal.")


if __name__ == "__main__":
    main()
    # affiche_message()
    # espace_01()
    # espace_02()
    # espace_03()
    # espace_04()
    # espace_05()
    # espace_06()
    # indentation_01()
    # indentation_02()
    # longueur_01()
    # longueur_03()
    # mots_reserve()
    # nommage_01()
    # nommage_02()

'''
Lorsque vous exécutez `Cours01.py`, la fonction `main()` sera appelée et affichera "Ceci est le programme principal.". 
Cela se produit car la condition `__name__ == "__main__"` est évaluée comme vraie lorsque le script est exécuté 
directement.

Cependant, si vous importez le module `example` dans un autre script Python, la condition `__name__ == "__main__"` sera 
évaluée comme fausse, car `__name__` sera le nom réel du module (`"example"` dans ce cas) et non `"__main__"`. Cela 
permet d'éviter l'exécution du code destiné uniquement au programme principal lorsque le module est importé.

L'utilisation de `__name__` est courante pour encapsuler le code exécutable dans une fonction `main()` ou dans un bloc 
conditionnel `if __name__ == "__main__":`, ce qui permet de tester le script en tant que programme principal, mais 
également de l'importer et d'utiliser ses fonctions et classes dans d'autres modules sans que le code du programme 
principal ne soit exécuté.

En résumé, `__name__` est une variable spéciale en Python qui indique le nom du module courant. Lorsqu'il est égal à 
`"__main__"`, cela signifie que le script est exécuté en tant que programme principal. Cela permet de différencier le 
comportement du script lorsque vous l'exécutez directement ou lorsque vous l'importez en tant que module.
'''

########################################################################################################################
# 01.12 - Conseils sur la conception d'un script
########################################################################################################################
'''
Voici quelques conseils pour vous aider à concevoir un script Python.

    1.  Réfléchissez avec un papier, un crayon... et un cerveau (voire même plusieurs) ! Reformulez avec des mots en 
        français (ou en anglais) les consignes qui vous ont été données ou le cahier des charges qui vous a été 
        communiqué. Dessinez ou construisez des schémas si cela vous aide.
    
    2.  Découpez en fonctions chaque élément de votre programme. Vous pourrez ainsi tester chaque élément indépendamment 
        du reste. Pensez à écrire les docstrings en même temps que vous écrivez vos fonctions.
    
    3.  Quand l'algorithme est complexe, commentez votre code pour expliquer votre raisonnement. Utiliser des fonctions 
        (ou méthodes) encore plus petites peut aussi être une solution.
        
    4.  Documentez-vous. L'algorithme dont vous avez besoin existe-t-il déjà dans un autre module ? Existe-t-il sous la 
        forme de pseudo-code ? De quels outils mathématiques avez-vous besoin dans votre algorithme ?
        
    5.  Si vous créez ou manipulez une entité cohérente avec des propriétés propres, essayez de construire une classe. 
        
    6.  Utilisez des noms de variables explicites, qui signifient quelque chose. En lisant votre code, on doit 
        comprendre ce que vous faites. Choisir des noms de variables pertinents permet aussi de réduire les commentaires.
    
    7.  Quand vous construisez une structure de données complexe (par exemple une liste de dictionnaires contenant 
        d'autres objets), documentez et illustrez l'organisation de cette structure de données sur un exemple simple.
    
    8.  Testez toujours votre code sur un jeu de données simple pour pouvoir comprendre rapidement ce qui se passe. Par 
        exemple, une séquence de 1000 bases est plus facile à gérer que le génome humain ! Cela vous permettra également 
        de retrouver plus facilement une erreur lorsque votre programme ne fait pas ce que vous souhaitez.
    
    9.  Lorsque votre programme « plante », lisez le message d'erreur. Python tente de vous expliquer ce qui ne va pas. 
        Le numéro de la ligne qui pose problème est aussi indiqué.
    
    10. Discutez avec des gens. Faites tester votre programme par d'autres. Les instructions d'utilisation sont-elles 
        claires ?
    
    11. Si vous distribuez votre code :
        -   Rédigez une documentation claire.
        -   Testez votre programme (jetez un œil aux tests unitaires).
        -   Précisez une licence d'utilisation. Voir par exemple le site Choose an open source license.
'''

########################################################################################################################
# 01.13 - Organisation du code
########################################################################################################################
'''
"""Docstring d'une ligne décrivant brièvement ce que fait le programme.

Usage:
======
    python nom_de_ce_super_script.py argument1 argument2

    argument1: un entier signifiant un truc
    argument2: une chaîne de caractères décrivant un bidule
"""

__authors__ = ("Johny B Good", "Hubert de la Pâte Feuilletée")
__contact__ = ("johny@bgood.us", "hub@pate.feuilletee.fr")
__copyright__ = "MIT"
__date__ = "2030-01-01"
__version__= "1.2.3"

import module_interne
import module_interne_2

import module_externe

UNE_CONSTANTE = valeur
UNE_AUTRE_CONSTANTE = une_autre_valeur


class UneSuperClasse():
    """Résumé de la docstring décrivant la classe.

    Description détaillée ligne 1
    Description détaillée ligne 2
    Description détaillée ligne 3
    """

    def __init__(self):
        """Résumé de la docstring décrivant le constructeur.

        Description détaillée ligne 1
        Description détaillée ligne 2
        Description détaillée ligne 3
        """
        [...]

    def une_méthode_simple(self):
        """Docstring d'une ligne décrivant la méthode."""
        [...]

    def une_méthode_complexe(self, arg1):
        """Résumé de la docstring décrivant la méthode.

        Description détaillée ligne 1
        Description détaillée ligne 2
        Description détaillée ligne 3
        """
        [...]
        return un_truc


def une_fonction_complexe(arg1, arg2, arg3):
    """Résumé de la docstring décrivant la fonction.

    Description détaillée ligne 1
    Description détaillée ligne 2
    Description détaillée ligne 3
    """
    [...]
    return une_chose


def une_fonction_simple(arg1, arg2):
    """Docstring d'une ligne décrivant la fonction."""
    [...]
    return autre_chose


if __name__ == "__main__":
    # ici débute le programme principal
'''

########################################################################################################################
# 01.14 - Références
########################################################################################################################
'''
https://peps.python.org/pep-0008/
https://python.sdv.univ-paris-diderot.fr/15_bonnes_pratiques/
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming/docstrings
'''
