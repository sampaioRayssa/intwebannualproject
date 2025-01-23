import json
import random

#funções básicas de save/load
def load_json(file_path):
    with open(file_path, 'r') as arquivo:
        return json.load(arquivo)

def save_json(file_path, data):
    with open(file_path, 'w') as arquivo:
        json.dump(data, arquivo, indent=4)

#classes, pra organizar melhor
class Save():
    def users_general_list(update):
        save_json('database/usuarios.json', update)

    def administrators_list(update):
        save_json('database/administradores.json', update)

    def commons_list(update):
        save_json('database/comuns.json', update)
    
    def deliverers_list(update):
        save_json('database/entregadores.json', update)

    def deliverys_list(update):
        save_json('database/entregas.json', update)

class Load():
    def users_general_list():
        return load_json('database/usuarios.json')
    
    def administrators_list():
        return load_json('database/administradores.json')

    def commons_list():
        return load_json('database/comuns.json')

    def deliverers_list():
        return load_json('database/entregadores.json')

    def deliverys_list():
        return load_json('database/entregas.json')


#cria uma entrega
  
def deliver_delivery(id_entrega):
    entregas = Load.deliverys_list()
    entregas[id_entrega]["status"] = "entregue"

    Save.deliverers_list()

def confirm_delivery(id_entrega):
    entregas = Load.deliverys_list()
    entregas[id_entrega]["status"] = "confirmada"

    Save.deliverers_list()



class delivery():
    def create(cliente,destinatario,descrição,valor):
        entregas = Load.deliverys_list()
        entregadores = Load.deliverers_list()
        entregador = random.choice(entregadores)
        id = len(entregas)

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

        Save.deliverers_list(entregas)

        return id
    
    def update(id,entregador = '', status = '', cliente='', destinatario='', descrição='', valor=''):
        entregas = delivery.get.all()

        if cliente:
            entregas[id]["cliente"] = cliente

        if destinatario:
            entregas[id]["destinatario"] = destinatario

        if descrição:
            entregas[id]["descricao"] = descrição

        if valor:
            entregas[id]["valor"] = valor

        if status:
            entregas[id]["status"] = status

        if entregador:
            entregas[id]["entregador"] = entregador

        Save.deliverys_list(entregas)

        return entregas[id]
    
    def delete(id):
        entregas = delivery.get.all()

        entregas.pop(id)

        Save.deliverys_list(entregas)
    
    class get():
        class by_client():
            def all(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if i["cliente"] == user_cpf:
                        S.append(i)
                return S

            def deliverying(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["cliente"] == user_cpf) and (i["status"] == "deliverying"):
                        S.append(i)
                return S
            
            def delivered(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["cliente"] == user_cpf) and (i["status"] == "delivered"):
                        S.append(i)
                return S
            
            def confirmed(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["cliente"] == user_cpf) and (i["status"] == "confirmed"):
                        S.append(i)
                return S

        class by_deliverer():
            def all(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if i["entregador"] == user_cpf:
                        S.append(i)
                return S

            def deliverying(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["entregador"] == user_cpf) and (i["status"] == "deliverying"):
                        S.append(i)
                return S
            
            def delivered(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["entregador"] == user_cpf) and (i["status"] == "delivered"):
                        S.append(i)
                return S
            
            def confirmed(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["entregador"] == user_cpf) and (i["status"] == "confirmed"):
                        S.append(i)
                return S

        def all():
            return Load.deliverys_list()

    class process():
        def deliver(id):
            entregas = delivery.get.all()

            entregas[id]['status'] = 'delivered'

            Save.deliverys_list(entregas)

            return entregas[id]
        
        def confirm(id):
            entregas = delivery.get.all()

            entregas[id]['status'] = 'confirmed'

            Save.deliverys_list(entregas)

            return entregas[id]
        