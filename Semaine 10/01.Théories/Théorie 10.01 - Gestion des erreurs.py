"""Ce cours est sur la gestion des erreurs"""

########################################################################################################################
# 10.00 - Explication
########################################################################################################################
'''
La gestion des erreurs en Python est un aspect crucial de la programmation, car elle permet de gérer des situations 
imprévues ou incorrectes qui pourraient survenir pendant l'exécution d'un programme. Python propose un mécanisme de 
gestion des exceptions qui vous permet de gérer ces erreurs de manière élégante et structurée. 

Une exception est une erreur qui se produit pendant l'exécution d'un programme. Elle interrompt le flux normal du 
programme et peut être déclenchée par de nombreuses raisons. En Python, une exception est un objet qui représente une 
erreur ou une situation anormale qui s'est produite pendant l'exécution d'un programme. Les exceptions sont utilisées 
pour gérer les erreurs, les avertissements et d'autres conditions exceptionnelles. 

Structure d'une exception en Python :
-------------------------------------
    1.  Type d'exception : Chaque exception est associée à un type d'exception spécifique, qui est une classe Python. 
        Par exemple, ZeroDivisionError, FileNotFoundError, ValueError, etc. Ces classes d'exception sont préalablement 
        définies dans Python, mais vous pouvez également créer vos propres exceptions personnalisées en définissant des 
        classes dérivées de la classe Exception.

    2.  Message d'erreur (facultatif) : Lorsque vous déclenchez ou interceptez une exception, vous pouvez fournir un 
        message d'erreur personnalisé. Ce message est généralement une chaîne de caractères qui décrit la nature de 
        l'erreur. Le message d'erreur est facultatif, mais il est très utile pour décrire l'erreur en termes 
        compréhensibles par l'utilisateur ou le développeur.

    3.  Empilement des appels : Lorsqu'une exception est déclenchée, Python conserve la trace de la pile d'appels 
        (stack trace), ce qui signifie qu'il enregistre la séquence d'appels de fonctions qui a conduit à l'exception. 
        Cette trace de la pile est incluse dans le message d'erreur lorsque l'exception est affichée. Elle est utile 
        pour le débogage, car elle montre où l'exception a été générée.
'''


def exemple_division1():
    1 / 0


def exemple_division2():
    exemple_division1()


'''

Comment Python gère les exceptions :
------------------------------------
    1.  Déclenchement d'une exception : Une exception est déclenchée (levée) lorsqu'une erreur se produit dans le code. 
        Par exemple, une division par zéro déclenche une ZeroDivisionError, et l'exception est levée.

    2.  Interception d'une exception : Vous pouvez intercepter (capturer) une exception en utilisant la structure 
        try...except. Cette structure permet de gérer des exceptions en spécifiant comment le programme doit réagir 
        lorsque l'erreur se produit.
            try:
                # Code susceptible de générer une exception
            except ExceptionType as e:
                # Code pour gérer l'exception

    3.  Propagation des exceptions : Si une exception n'est pas gérée dans la fonction où elle est levée, elle se 
        propage vers les fonctions appelantes jusqu'à ce qu'elle soit capturée par un bloc try...except approprié. Si 
        elle n'est jamais interceptée, le programme s'arrête et affiche un message d'erreur.

    4.  Nettoyage avec finally : Un bloc finally peut être utilisé pour exécuter du code de nettoyage, quel que soit le 
        résultat (exception ou non) du bloc try.

    5.  Création d'exceptions personnalisées : Vous pouvez créer vos propres exceptions en définissant des classes 
        dérivées de Exception ou de ses sous-classes. Cela vous permet de gérer des erreurs spécifiques à votre 
        application.

    6.  Affichage des exceptions : Lorsqu'une exception est déclenchée, Python affiche l'erreur en indiquant le type de 
        l'exception, le message d'erreur (le cas échéant) et la trace de la pile (stack trace). Cela vous aide à 
        identifier l'origine de l'erreur.
'''

########################################################################################################################
# 10.00 - try...except
########################################################################################################################
'''
Parfois un programme est capable de traiter le problème à l’origine de l’exception. Par exemple si le programme demande 
à l’utilisateur de saisir un nombre et que l’utilisateur saisit une valeur erronée, le programme peut simplement 
demander à l’utilisateur de saisir une autre valeur. Plutôt que de faire échouer le programme, il est possible d’essayer 
de réaliser un traitement et, s’il échoue de proposer un traitement adapté.

Voici quelques exemples avec des types d'exceptions:
----------------------------------------------------
    1.  ValueError : Cette exception survient lorsqu'une fonction reçoit un argument du bon type mais d'une valeur 
        inappropriée.
'''


def exemple_ValueError():
    nombre = input("Entrez un nombre : ")
    try:
        nombre = int(nombre)
    except ValueError:
        print("Désolé la valeur saisie n'est pas un nombre.")


'''
    2.  ZeroDivisionError : Cette exception est levée lorsqu'une division par zéro est tentée.
'''


def exemple_ZeroDivisionError():
    try:
        numerateur = int(input("Entrez un numérateur : "))
        denominateur = int(input("Entrez un dénominateur : "))
        resultat = numerateur / denominateur
        print("Le resultat de la division est", resultat)
    except ValueError:
        print("Désolé, les valeurs saisies ne sont pas des nombres.")
    except ZeroDivisionError:
        print("Désolé, la division par zéro n'est pas permise.")

    # Si le traitement est similaire, on peut utiliser un tuple d'exceptions
    #   except (ValueError, ZeroDivisionError):
    #       print("Désolé, quelque chose ne s'est pas bien passé.")


'''
    3.  TypeError : Elle est levée lorsque l'opération ou la fonction est appliquée à un objet d'un type inapproprié.
'''


def exemple_TypeError():
    try:
        # Tentative d'exécution d'une opération incorrecte
        resultat = 10 + "20"
    except TypeError as e:
        # Gestion de l'exception TypeError
        print(f"Une exception de type TypeError s'est produite : {e}")


'''
    4.  IndexError : Cette exception est générée lorsqu'une séquence (liste, chaîne, etc.) est indexée en dehors de sa 
        plage valide.
'''


def exemple_IndexError():
    try:
        liste = [1, 2, 3]
        element = liste[4]  # Tentative d'accéder à un élément en dehors de la plage valide
    except IndexError as e:
        print(f"Une exception de type IndexError s'est produite : {e}")


'''
    5.  KeyError : Cette exception se produit lorsqu'un dictionnaire tente d'accéder à une clé qui n'existe pas.
'''


def exemple_KeyError():
    try:
        mon_dictionnaire = {"nom": "Alice", "age": 30}
        valeur = mon_dictionnaire["prénom"]  # Tentative d'accéder à une clé inexistante
    except KeyError as e:
        print(f"Une exception de type KeyError s'est produite : {e}")


'''
    6.  IOError : Générée pour des erreurs d'E/S générales.
'''


def exemple_IOError():
    try:
        # Tentative d'ouverture d'un fichier qui n'existe pas
        with open("fichier_inexistant.txt", "r") as fichier:
            contenu = fichier.read()
    except IOError as e:
        print(f"Une exception de type FileNotFoundError s'est produite : {e}")


'''
    7.  Récupération du message de l'exception : Les exceptions possèdent une représentation sous forme de chaîne de 
        caractères pour fournir un message.
'''


def exemple_Message():
    nombre = input("Entrez nombre : ")
    try:
        nombre = int(nombre)
    except ValueError as e:
        print(e)


########################################################################################################################
# 10.00 - La clause else
########################################################################################################################
'''
La clause else dans un bloc try...except en Python est utilisée pour spécifier un ensemble d'instructions à exécuter si 
aucune exception n'est levée pendant l'exécution du bloc try.
'''


def exemple_else():
    try:
        numerateur = int(input("Entrez un numérateur : "))
        denominateur = int(input("Entrez un dénominateur : "))
        resultat = numerateur / denominateur
    except (ValueError, ZeroDivisionError):
        print("Désolé, quelque chose ne s'est pas bien passé.")
    else:
        print("Le resultat de la division est", resultat)


########################################################################################################################
# 10.00 - La clause finally
########################################################################################################################
'''
La clause finally dans un bloc try...except en Python est utilisée pour spécifier un ensemble d'instructions qui seront 
exécutées qu'une exception soit levée ou non. Cela signifie que le code dans la clause finally sera toujours exécuté, 
quelle que soit la situation. La clause finally est couramment utilisée pour effectuer des opérations de nettoyage, 
telles que la fermeture de fichiers ou de connexions réseau, après l'exécution du bloc try, qu'une exception soit 
survenue ou non.
'''


def exemple_finaly():
    try:
        # Tentative d'ouvrir un fichier
        fichier = open("mon_fichier.txt", "r")
        contenu = fichier.read()
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    else:
        print(f"Contenu du fichier : {contenu}")
    finally:
        # Fermeture du fichier, même si une exception est levée
        fichier.close()


########################################################################################################################
# 10.00 - Déclencher des exceptions (raise)
########################################################################################################################
'''
En Python, vous pouvez déclencher des exceptions à l'aide de l'instruction raise. Cela vous permet de signaler des 
erreurs ou des conditions exceptionnelles dans votre code.

    1.  Déclencher une exception personnalisée : Vous pouvez créer vos propres exceptions personnalisées en définissant 
        une classe héritée de la classe Exception de base.

    2.  Déclencher des exceptions intégrées : Python dispose d'un grand nombre d'exceptions intégrées pour des 
        situations courantes.

        Exemple 1 : ValueError - Déclenchée lorsque le type de données d'un argument est correct, mais la valeur de 
                    l'argument n'est pas appropriée.
'''


def exemple_ValueError2(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")


def exemple_ValueError1():
    try:
        exemple_ValueError2(-5)
    except ValueError as e:
        print(f"Erreur : {e}")


'''
        Exemple 2 : TypeError: Déclenchée lorsque le type de données d'un argument est incorrect.
'''


def exemple_TypeError2(age):
    if not isinstance(age, int):
        raise TypeError("L'âge doit être de type entier (int).")


def exemple_TypeError1():
    try:
        exemple_TypeError2("cent")
    except TypeError as e:
        print(f"Erreur : {e}")


'''
        Exemple 3 : Le mot-clé raise est également utilisé pour relancer une exception dans un bloc mot-clé except.
'''


def exemple_raise():
    try:
        numerateur = int(input("Entrez un numérateur : "))
        denominateur = int(input("Entrez un dénominateur : "))
        resultat = numerateur / denominateur
        print("Le resultat de la division est", resultat)
    except (ValueError, ZeroDivisionError):
        print("Désolé, quelque chose ne s'est pas bien passé.")
        raise


########################################################################################################################
# 10.00 - Logging des erreurs
########################################################################################################################
import logging

'''
Si besoin, commencez par faire l'installation du module dans votre environnement: pip install logging

La bibliothèque logging en Python est un module intégré qui permet de gérer les journaux (logs) dans une application. 
Elle offre une manière souple et puissante de contrôler les informations de journalisation, de les formater et de les 
stocker dans diverses sorties (fichiers, console, etc.). Les journaux sont utiles pour le suivi, le débogage et la 
maintenance des applications.

    1.  Il est possible d'utiliser les 5 niveaux d'erreurs pour l'affichage de nos message. Seul les message à partir de
        warning() sont affiché dans la console.
'''


def exemple_logging1():
    logging.debug('Ceci est un message de débogage')
    logging.info('Ceci est une information')
    logging.warning('Ceci est un avertissement')
    logging.error('Ceci est une erreur')
    logging.critical('Ceci est une erreur critique')


'''
    2.  La fonction logging.basicConfig() est utilisée pour configurer le système de journalisation (logging) de Python. 
        Elle doit être appelée au début de votre programme pour spécifier comment vous souhaitez gérer les journaux, 
        notamment les niveaux de journalisation, le format du journal et la destination du journal. 
        Voici quelques paramètres:
        
        -   filename (facultatif) : Si vous souhaitez enregistrer les journaux dans un fichier, vous pouvez spécifier le 
            nom du fichier. Par exemple, filename='mon_journal.log' enregistrera les journaux dans un fichier appelé 
            'mon_journal.log'. Si vous ne spécifiez pas filename, les journaux seront envoyés vers la console.
            
        -   filemode (facultatif) : Si vous souhaitez spécifié le mode d'ouverture du fichier. Par défaut, sa valeur 
            est 'a' pour append.

        -   level (facultatif) : Ce paramètre définit le niveau minimal de journalisation. Seuls les messages de 
            journalisation de ce niveau et supérieurs seront enregistrés. Les niveaux de journalisation courants, du 
            plus bas au plus élevé, sont DEBUG, INFO, WARNING, ERROR, et CRITICAL. Par exemple, level=logging.DEBUG 
            enregistrera tous les messages de journalisation, tandis que level=logging.WARNING enregistrera uniquement 
            les messages de niveau avertissement (warning) et supérieurs.

        -   format (facultatif) : Ce paramètre vous permet de définir un format personnalisé pour vos messages de 
            journalisation. Vous pouvez inclure des informations telles que la date, le nom du logger, le niveau de 
            journalisation et le message. Par exemple, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' 
            affichera la date, le nom du logger, le niveau de journalisation et le message dans chaque entrée de 
            journal. Si vous ne spécifiez pas format, un format par défaut sera utilisé.
'''


def exemple_logging2():
    logging.basicConfig(filename='mon_journal.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logging.debug('Ceci est un message de débogage')
    logging.info('Ceci est une information')
    logging.warning('Ceci est un avertissement')
    logging.error('Ceci est une erreur')
    logging.critical('Ceci est une erreur critique')


def exemple_logging3():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('Utilisateur connecté')


'''
    3.  Il est possible d'utiliser des variables pour stocké de l'infromation et l'afficher dans le log.
'''


def exemple_logging4():
    name = 'Alex'

    logging.error('%s a soulevé une erreur', name)


'''
    4.  C'est possible de récupérer les exceptions soulevé par l'execution de notre programme.
'''


def exemple_logging5():
    logging.basicConfig(filename='mon_journal.log', filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    a = 5
    b = 0

    try:
        c = a / b
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


'''
    5.  Le principe des gestionnaires (handlers) dans le module logging de Python est de spécifier où et comment les 
        messages de journalisation doivent être gérés. En d'autres termes, les gestionnaires déterminent le flux de 
        sortie des messages de journalisation, ce qui peut inclure l'enregistrement dans un fichier, l'affichage à la 
        console, l'envoi par e-mail, etc. Voici un aperçu des principaux concepts relatifs aux gestionnaires :

        -   Flux de sortie (Stream) : Les gestionnaires déterminent le flux de sortie des messages de journalisation. 
            Vous pouvez spécifier le flux cible, tel qu'un fichier, la console (sys.stdout), un socket réseau, etc.

        -   Niveaux de journalisation (Levels) : Vous pouvez associer des gestionnaires à des niveaux de journalisation 
            spécifiques. Par exemple, vous pouvez avoir un gestionnaire qui ne traite que les messages d'erreur (ERROR) 
            ou un autre qui gère les messages de débogage (DEBUG). Cela permet de contrôler précisément quelles 
            informations sont envoyées à chaque gestionnaire.

        -   Formatage (Formatting) : Les gestionnaires vous permettent de spécifier le format des messages de 
            journalisation. Vous pouvez inclure des informations telles que la date, le nom du journal (logger name), 
            le niveau de journalisation, le message, etc., dans le format des journaux.

        -   Personnalisation (Customization) : Vous pouvez créer des gestionnaires personnalisés pour répondre à vos 
            besoins spécifiques. Par exemple, vous pourriez créer un gestionnaire qui envoie des journaux par e-mail ou 
            stocke des journaux dans une base de données.

        -   Hiérarchie de Gestionnaires (Handler Hierarchy) : Vous pouvez utiliser plusieurs gestionnaires, organisés en 
            une hiérarchie, pour gérer les journaux de manière sélective. Par exemple, un gestionnaire de niveau 
            supérieur pourrait traiter tous les messages d'avertissement (WARNING) et supérieurs, tandis qu'un 
            gestionnaire de niveau inférieur pourrait traiter uniquement les messages de débogage (DEBUG).
'''


def exemple_logging6():
    # Crée un logger (journal) nommé "mon_logger"
    logger = logging.getLogger("mon_logger")
    logger.setLevel(logging.DEBUG)  # Niveau de journalisation le plus bas (DEBUG)

    # Crée un gestionnaire pour la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Gère les messages de niveau INFO et supérieur
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Crée un gestionnaire de fichier
    file_handler = logging.FileHandler('mon_journal.log')
    file_handler.setLevel(logging.ERROR)  # Gère les messages de niveau ERROR et supérieur
    file_handler.setFormatter(formatter)

    # Ajoute les gestionnaires au logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Exemples de messages de journalisation
    logger.debug("Ceci est un message de débogage (DEBUG).")
    logger.info("Ceci est un message d'information (INFO).")
    logger.warning("Ceci est un avertissement (WARNING).")
    logger.error("Ceci est une erreur (ERROR).")

    # Ferme le gestionnaire de fichier pour libérer les ressources
    file_handler.close()


########################################################################################################################
# 10.00 - Exécution du code
########################################################################################################################
if __name__ == "__main__":
    print('test')
    exemple_logging6()

########################################################################################################################
# 10.00 - Références
########################################################################################################################
'''
https://docs.python.org/fr/3.8/library/stdtypes.html
https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf
https://www.programiz.com/python-programming
https://python.sdv.univ-paris-diderot.fr/02_variables/
https://gayerie.dev/docs/python/index.html
https://python.doctor/
https://gayerie.dev/docs/python/python3/mysql.html#
https://www.pierre-giraud.com/python-apprendre-programmer-cours/introduction-gestion-erreur-exception/
https://docs.python.org/fr/3/tutorial/errors.html
https://gayerie.dev/docs/python/python3/exception.html
'''
