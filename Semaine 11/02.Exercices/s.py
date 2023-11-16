import socket

def list_connections():
    # Obtenir le nom de l'hôte
    host_name = socket.gethostname()
    # Obtenir l'adresse IP
    ip_address = socket.gethostbyname(host_name)
    # Obtenir le dernier octet de l'adresse IP
    last_octet = ip_address.split('.')[-1]
    # Obtenir le préfixe de l'adresse IP
    prefix = '.'.join(ip_address.split('.')[:-1])
    # Parcourir toutes les adresses IP possibles dans le réseau local
    for i in range(1, 2):
        try:
            # Obtenir le nom de l'hôte pour l'adresse IP actuelle
            current_host_name = socket.gethostbyaddr(f"{prefix}.{i}")[0]
            print(f"Adresse IP : {prefix}.{i}, Nom d'hôte : {current_host_name}")
        except socket.herror:
            # Ignorer les erreurs (c'est-à-dire les adresses IP sans nom d'hôte)
            pass

list_connections()