import random
import json
from flask import *


'''
*** ME LEIA:
Este é apenas um código teste: aqui irei testar se o sistema de escolha de entregador aleatório funciona, 
além de testar se a estrutura do banco de dados vai funcionar bem.

agora estou apenas testando o versionamento git
'''

'''
Esta é a lista de usuarios, todos os usuarios comuns estão nela, onde estão armazenadas as informações básicas
do usuario. Percebam que pra simplificar o sistema, não coloquei nas informações do usuario se ele é um ADM ou Entregador,
isso por que as buscas por entregador e administrador seriam colossais e dificeis de fazer, ao invez disso, optei por fazer listas de 
privilégios: Uma lista de entregadores, uma lista de administradores, e uma lista de usuarios comuns, sendo assim, um usuario comum está
na lista comum, um entregador está na lista de entregadores e na lista de usuarios ao mesmo tempo.

Também há um dicionário onde estão armazenadas as informações, as listas apenas referenciam os usuarios
'''

ul = {
    #Cada usuario é referenciado por seu CPF, por ser unico e imutavel.
    "000.000.000-00":
    {
    "email": "test@mail",
    "nome": "user01",
    "tel": "(99) 99999-9999",
    "password": "teste"
    },

    "000.000.000-01":
    {
    "email": "test01@mail",
    "nome": "entregador01",
    "tel": "(99) 99999-9998",
    "password": "teste"
    },

    "000.000.000-02":
    {
    "email": "test02@mail",
    "nome": "entregador02",
    "tel": "(99) 99999-9997",
    "password": "teste"
    },

    "000.000.000-03":
    {
    "email": "test03@mail",
    "nome": "adm01",
    "tel": "(99) 99999-9996",
    "password": "admin"
    }


}

usuarios = [
    #aqui referencio os CPFs dos usuarios tratados como usuario comum.
    "000.000.000-00",
    "000.000.000-01",
    "000.000.000-02"
]

entregadores = [
    #Aqui referencio os CPFs dos entregadores. É possivel ser tanto usuario quanto entregador
    "000.000.000-01",
    "000.000.000-02",
    "pinto",
    "ereto",
]

administradores = [
    #Aqui referencio os CPFs dos Administradores, que terão permições extras e apenas poderão ser modificados por outros ADMs
    "000.000.000-03"
]

#Ao remover uma conta da lista de usuarios gerais, é possivel que erros aconteçam por seus CPFs estarem ainda listados como User, Entregador
#Ou ADM, esta função checa em todas as listas se há CPFs não vinculados listados, e os deleta. Função custosa, não usar sempre.
def check_lists_integrity():
    S = []
    for i in usuarios:
        if i not in ul:
            usuarios.remove(i)
            S.append(i)
    
    for i in entregadores:
        if i not in ul:
            entregadores.remove(i)
            S.append(i)
    
    for i in administradores:
        if i not in ul:
            administradores.remove(i)
            S.append(i)
    return f"{len(S)} erros corrigidos; CPFs {S} não estão listados"

#Uma função simples que escolhe um entregador aleatório para diversas finalidades
def get_random_entregador():
    return random.choice(entregadores)

#Uma função geral que retorna as informações de um usuario a recebendo seu CPF
def get_user_by_cpf(cpf):
    try:
        return ul[cpf]
    except:
        #isso significa que não hjá nenhuma conta vinculada a este cpf
        return "erro: não foi possível encontrar esta conta"

print(check_lists_integrity())