# Déclaration d'une fonction create_contact
def create_contact(name, number, is_favorite):
    contact = {
        'name': name,
        'phone_number': number,
        'is_favorite': is_favorite,
    }
# retour a contact
    return contact

#annuaire qui prend en parametre {}
annuaire = {}

# Déclaration d'une fonction add_contact qui prend en parametre (c) = contact /fonction = correspond a un ensemble d'action
def add_contact(c):

# recuper number qui est assoocier a la cle phone_number que l'on stock dans une nouvelle variable number
    number = c['phone_number']

# contact = annuaire qui est associer number
    annuaire[number] = c

# Déclaration d'une fonction get_name
def get_names():

# names qui prend en parametre []
    names = []

# Déclaration d'une boucle phone_number qui prend en parametre annuaire
    for phone_number in annuaire:

# annuaire qui a pour parametre phone_number
        contact = annuaire(phone_number)

# contacte qui est associer a la cle name
        names.append(contact['name'])

# Parcours de l'annuaire pour recuperer le nom de chaque contact
# trier les noms par ordre alphabetique

#retour a names
    return names
