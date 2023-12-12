from exceptions import input_error

contacts = {}

#додавання контакту
@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

# Функція для зміни контакту
@input_error
def change_contact(args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        raise KeyError

# Функція для отримання номера телефону
@input_error
def phone(args):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

# Функція для виведення всіх контактів
def all():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# Парсер введення
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args