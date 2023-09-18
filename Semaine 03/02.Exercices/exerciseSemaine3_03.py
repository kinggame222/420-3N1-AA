'''

Question 03 – Cornhole bags

Vous avez un fichier qui se nomme bag-data.json et qui contient de l’information sur des poches pour le jeu de Cornhole. Vous devez lire se fichier, analyser les données et sortir quelques statistiques. À l’aide de la bibliothèque Pandas, effectuer les tâches suivantes :

ü Afficher chacun des Series Name pour chaque Bag Manufacturer.

ü Afficher le top 10 des bags selon le Speed Friction Fastest Side.

ü Afficher le top 10 des bags selon le Speed Friction Other Side.

ü Selon le choix de Bag Manufacturer de l’utilisateur, créez un fichier JSON qui contient seulement l’information de ses Series Name et les 2 Speed Fiction.
'''
import json
import pandas as pd


def lirejson(nom_fichier):
    fichier = open(nom_fichier, "r")
    donne = json.load(fichier)
    return donne


def afficherSeriesName(donne):
    data = lirejson(donne)
    bag_data = data['data']['data']

    df = pd.DataFrame(bag_data)

    TEST = df['Bag Manufacturer / Series Name'].str.split(' ', n=1, expand=True)

    return df.groupby(TEST[0])['Bag Manufacturer / Series Name'].apply(list)


def top10BagsSelonSpeedFriction(donne, colonne):
    # Créer un DataFrame à partir des données des sacs
    data = lirejson(donne)
    bag_data = data['data']['data']
    df = pd.DataFrame(bag_data)

    # Convertir la colonne en float pour trier correctement
    df[colonne] = df[colonne].astype(float)

    # Trier les sacs par la colonne donnée et obtenir le top 10
    top_10_bags = df.sort_values(by=colonne, ascending=False).head(10)

    return top_10_bags


def crerJsonSelonBagManufacturer(donne, bag_manufacturer):
    # Créer un DataFrame à partir des données des sacs
    data = lirejson(donne)
    bag_data = data['data']['data']
    df = pd.DataFrame(bag_data)

    # Filtrer les sacs selon le bag_manufacturer
    df = df[df['Bag Manufacturer / Series Name'].str.contains(bag_manufacturer)]

    # Créer un nouveau DataFrame avec les colonnes demandées
    new_df = pd.DataFrame({
        'Series Name': df['Bag Manufacturer / Series Name'],
        'Speed Friction Fastest Side': df['Speed Friction Fastest Side'],
        'Speed Friction Other Side': df['Speed Friction Other Side']
    })

    # Créer un fichier JSON à partir du nouveau DataFrame
    new_df.to_json('bag-manufacturer.json', orient='records')
    print("Le fichier bag-manufacturer.json a été créé.")


if __name__ == "__main__":
    print("serie")
    print("--------------------")

    print(afficherSeriesName('bag-data.json'))
    print("--------------------")
    print("top 10 bags selon speed friction fastest side")
    print(top10BagsSelonSpeedFriction('bag-data.json', 'Speed Friction Fastest Side'))
    print("--------------------")
    print("top 10 bags selon speed friction other side")
    print(top10BagsSelonSpeedFriction('bag-data.json', 'Speed Friction Other Side'))

    choix = input("Entrez le nom du bag manufacturer: ")
    crerJsonSelonBagManufacturer('bag-data.json', choix)
