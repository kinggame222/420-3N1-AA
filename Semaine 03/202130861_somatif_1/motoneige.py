# Auteur : william bouchard
# Date : 2023-09-18
# But : programme qui permet de faire la gestion de motoneiges

import io
import requests
from PIL import Image


def pieds_en_metres(pieds):
    return float(pieds) * 0.3048


def enlever_annee(modele):
    Modele_couper = modele[5:]
    return Modele_couper


def affichage_image(url, nom):
    # Créer le nom du fichier
    filepath = nom + ".jpg"

    # Télécharge l'image
    r = requests.get(url, stream=True)
    # Vérifier le code de statut
    if r.status_code == 200:
        # Enregistre l'image avec le nom du fichier
        img = Image.open(io.BytesIO(r.content))
        img.save(filepath)
        # Affiche l'image
        img.show()
