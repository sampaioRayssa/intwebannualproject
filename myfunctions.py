import json
import random


def load_json(file_path):
    with open(file_path, 'r') as arquivo:
        return json.load(arquivo)

def save_json(file_path, data):
    with open(file_path, 'w') as arquivo:
        json.dump(data, arquivo, indent=4)

# Usuários
def load_users_general_list():
    return load_json('database/usuarios.json')

def save_users_general_list(update):
    save_json('database/usuarios.json', update)

# Administradores
def load_administrators_list():
    return load_json('database/administradores.json')

def save_administrators_list(update):
    save_json('database/administradores.json', update)

# Comuns
def load_commons_list():
    return load_json('database/comuns.json')

def save_commons_list(update):
    save_json('database/comuns.json', update)

# Entregadores
def load_deliverers_list():
    return load_json('database/entregadores.json')

def save_deliverers_list(update):
    save_json('database/entregadores.json', update)

# Entregas
def load_deliverys_list():
    return load_json('database/entregas.json')

def save_deliverys_list(update):
    save_json('database/entregas.json', update)


#cria uma entrega
def create_delivery(cliente,destinatario,descrição,valor):
    entregas = load_deliverys_list()
    entregadores = load_deliverers_list()
    entregador = random.choice(entregadores)
    id = (len(entregas) + 1)

    nova_entrega = {
        "status": "iniciada",
        "cliente":cliente,
        "destinatario":destinatario,
        "descrição": descrição,
        "valor":str(valor),
        "entregador": entregador,
        "id": id
    },

    entregas.append(nova_entrega)

    save_deliverers_list(entregas)

    return id
    
def deliver_delivery(id_entrega):
    entregas = load_deliverys_list()
    entregas[id_entrega]["status"] = "entregue"

    save_deliverers_list()

def confirm_delivery(id_entrega):
    entregas = load_deliverys_list()
    entregas[id_entrega]["status"] = "confirmada"

    save_deliverers_list()


'''
Ainda preciso fazer muitas coisas, mas entregas ja podem ser criadas pelo cliente, entregues pelo entregador e confirmadas pelo cliente

falta ainda o CRUD inteiro, essas são apenas algumas funções básicas
preciso de muita ajuda nisso, mas vão fazendo por conta
'''