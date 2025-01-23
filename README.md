Aqui está a documentação simplificada do código que você forneceu:

---

# **Documentação Simplificada - Sistema de Entregas**

Este sistema gerencia informações de usuários, administradores, entregadores e entregas. Ele permite a criação, edição, remoção e consulta de dados de usuários e entregas, além de realizar a atribuição de status às entregas.

---

## **Funções Básicas de Save/Load (Armazenamento de Dados)**

1. **`load_json(file_path)`**: 
   - Carrega dados de um arquivo JSON.
   - Parâmetro: `file_path` (caminho do arquivo).
   - Retorna: dados carregados.

2. **`save_json(file_path, data)`**:
   - Salva dados em um arquivo JSON.
   - Parâmetros: `file_path` (caminho do arquivo) e `data` (dados a serem salvos).

---

## **Classes e Funções Principais**

### **1. Save**
- **Objetivo**: Salva dados em diferentes arquivos JSON.

#### Métodos:
- **`users_general_list(update)`**: Salva a lista geral de usuários.
- **`administrators_list(update)`**: Salva a lista de administradores.
- **`commons_list(update)`**: Salva a lista de usuários comuns.
- **`deliverers_list(update)`**: Salva a lista de entregadores.
- **`deliverys_list(update)`**: Salva a lista de entregas.

---

### **2. Load**
- **Objetivo**: Carrega dados de diferentes arquivos JSON.

#### Métodos:
- **`users_general_list()`**: Carrega a lista geral de usuários.
- **`administrators_list()`**: Carrega a lista de administradores.
- **`commons_list()`**: Carrega a lista de usuários comuns.
- **`deliverers_list()`**: Carrega a lista de entregadores.
- **`deliverys_list()`**: Carrega a lista de entregas.

---

### **3. Deliverys (Entregas)**
- **Objetivo**: Gerenciar entregas.

#### Métodos:
- **`create(cliente, destinatario, descrição, valor)`**: Cria uma nova entrega, atribuindo um entregador aleatório.
- **`update(id, entregador, status, cliente, destinatario, descrição, valor)`**: Atualiza os dados de uma entrega.
- **`delete(id)`**: Remove uma entrega.
  
#### Métodos de Consulta:
- **`get.by_client.all(user_cpf)`**: Retorna todas as entregas de um cliente.
- **`get.by_client.deliverying(user_cpf)`**: Retorna as entregas "em andamento" de um cliente.
- **`get.by_client.delivered(user_cpf)`**: Retorna as entregas "entregues" de um cliente.
- **`get.by_client.confirmed(user_cpf)`**: Retorna as entregas "confirmadas" de um cliente.
- **`get.by_deliverer.all(user_cpf)`**: Retorna todas as entregas de um entregador.
- **`get.by_deliverer.deliverying(user_cpf)`**: Retorna as entregas "em andamento" de um entregador.
- **`get.by_deliverer.delivered(user_cpf)`**: Retorna as entregas "entregues" de um entregador.
- **`get.by_deliverer.confirmed(user_cpf)`**: Retorna as entregas "confirmadas" de um entregador.
- **`get.all()`**: Retorna todas as entregas.

#### Métodos de Processamento:
- **`process.deliver(id)`**: Marca a entrega como "entregue".
- **`process.confirm(id)`**: Marca a entrega como "confirmada".

---

### **4. Users (Usuários)**
- **Objetivo**: Gerenciar usuários (clientes, entregadores e administradores).

#### Métodos:
- **`create(cpf, email, nome, telefone, senha)`**: Cria um novo usuário.
- **`edit(cpf, email, nome, telefone, senha)`**: Edita os dados de um usuário.
- **`delete(cpf)`**: Exclui um usuário.

#### Métodos de Consulta:
- **`get.all()`**: Retorna todos os usuários.
- **`get.deliverers()`**: Retorna todos os entregadores.
- **`get.administrators()`**: Retorna todos os administradores.
- **`get.by_cpf(cpf)`**: Retorna um usuário específico pelo CPF.

#### Métodos de Atribuição de Função:
- **`set_as.deliverer(cpf)`**: Adiciona um usuário como entregador.
- **`set_as.administrator(cpf)`**: Adiciona um usuário como administrador.

#### Métodos de Remoção de Função:
- **`unset_as.deliverer(cpf)`**: Remove um usuário da lista de entregadores.
- **`unset_as.administrator(cpf)`**: Remove um usuário da lista de administradores.

---

## **Fluxo de Funcionamento**

1. **Cadastro de Usuário**: 
   - O usuário se cadastra com informações como CPF, email, nome, telefone e senha.
   
2. **Gestão de Entregas**: 
   - O administrador ou entregador pode gerenciar as entregas, criando, atualizando, excluindo e alterando o status das entregas.

3. **Consultas de Entregas**: 
   - Usuários e entregadores podem consultar suas entregas em diferentes estados (em andamento, entregues, confirmadas).

4. **Gestão de Funções**: 
   - Administradores podem atribuir ou remover funções de entregador ou administrador para os usuários.

---

## **Exemplos de Uso**

- **Criar um usuário**:
  ```python
  users.create('12345678901', 'email@example.com', 'João Silva', '123456789', 'senha123')
  ```

- **Criar uma entrega**:
  ```python
  deliverys.create('12345678901', '98765432100', 'Entrega de comida', 50.00)
  ```

- **Alterar o status de uma entrega para 'entregue'**:
  ```python
  process.deliver(0)
  ```

- **Consultar todas as entregas de um cliente**:
  ```python
  get.by_client.all('12345678901')
  ```

---

### **Considerações Finais**

Este sistema é simples e direto, com a principal finalidade de gerenciar usuários e entregas de forma eficaz. A arquitetura foi organizada para permitir fácil acesso e manipulação dos dados de usuários e entregas, com persistência em arquivos JSON.

---

Essa documentação fornece uma visão geral do funcionamento do sistema. Se precisar de mais detalhes ou explicações sobre algum trecho específico, estou à disposição para ajudar!
