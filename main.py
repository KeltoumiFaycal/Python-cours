import phonebook

c = phonebook.create_contact("Hugo", "12345678", True)
phonebook.add_contact(c)
print(phonebook.annuaire)

c = phonebook.create_contact("Marie", "35740743", False)
phonebook.add_contact(c)
print(phonebook.annuaire)

c = phonebook.create_contact("Max", "3976540743", False)
phonebook.add_contact(c)
print(phonebook.annuaire)

name = input("Nom contact ?")
print(name)

phone_number = input("Numero du contact ?")
print(phone_number)

is_favorite = input("contact en favoris ?")
print(is_favorite)

#  def display_all():