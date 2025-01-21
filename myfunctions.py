import json

def load_users_general_list():
    with open('database/usuarios.json', 'r') as arquivo:
        return json.load(arquivo)

def save_users_general_list(update):
    with open('database/usuarios.json', 'w') as arquivo:
        json.dump(update, arquivo)
