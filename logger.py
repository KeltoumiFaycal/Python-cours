from datetime import datetime


def save_log(text):
    # Ouverture du fichier en mode append
    f = open("phonebook.log", "a")