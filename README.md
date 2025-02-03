# **Documentação Simplificada - Sistema de Entregas**

Esta documentação foi gerada com o auxílio de uma IA de linguagem natural, com o único intuito de fornecer uma visão geral e simplificada das funcionalidades e estruturas do sistema de entregas, para facilitar o entendimento e a integração entre os desenvolvedores back-end e front-end.


## **Geração da Documentação**

A documentação foi gerada com o auxílio de uma ferramenta de Inteligência Artificial (IA), especificamente o modelo GPT-3 da OpenAI (ChatGPT), que analisou o código fornecido e extraiu os principais componentes e suas funcionalidades. O principal objetivo é fornecer uma explicação concisa e acessível sobre a estrutura e as funções do código, visando principalmente os desenvolvedores front-end.

Este documento não substitui uma documentação técnica detalhada, mas oferece uma visão geral útil para facilitar o entendimento do fluxo e da utilização das funções principais do sistema.

---

## **Funções Básicas de Save/Load (Armazenamento de Dados)**

Essas funções são responsáveis por carregar e salvar dados em arquivos JSON, garantindo persistência das informações.

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
- **Objetivo**: Salvar dados em diferentes arquivos JSON para persistência.

#### Métodos:
- **`users_general_list(update)`**: Salva a lista geral de usuários.
- **`administrators_list(update)`**: Salva a lista de administradores.
- **`commons_list(update)`**: Salva a lista de usuários comuns.
- **`deliverers_list(update)`**: Salva a lista de entregadores.
- **`deliverys_list(update)`**: Salva a lista de entregas.

---

### **2. Load**
- **Objetivo**: Carregar dados de diferentes arquivos JSON para acesso e manipulação.

#### Métodos:
- **`users_general_list()`**: Carrega a lista geral de usuários.
- **`administrators_list()`**: Carrega a lista de administradores.
- **`commons_list()`**: Carrega a lista de usuários comuns.
- **`deliverers_list()`**: Carrega a lista de entregadores.
- **`deliverys_list()`**: Carrega a lista de entregas.

---

### **3. Deliverys (Entregas)**
- **Objetivo**: Gerenciar as entregas, incluindo criação, atualização, remoção e alteração de status.

#### Métodos:
- **`create(cliente, destinatario, descrição, valor)`**: Cria uma nova entrega, atribuindo um entregador aleatório.
- **`update(id, entregador, status, cliente, destinatario, descrição, valor)`**: Atualiza os dados de uma entrega existente.
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
- **`get.all()`**: Retorna todas as entregas no sistema.

#### Métodos de Processamento:
- **`process.deliver(id)`**: Marca a entrega como "entregue".
- **`process.confirm(id)`**: Marca a entrega como "confirmada".

---

### **4. Users (Usuários)**
- **Objetivo**: Gerenciar usuários (clientes, entregadores e administradores), incluindo a criação, edição, remoção e consulta de dados.

#### Métodos:
- **`create(cpf, email, nome, telefone, senha)`**: Cria um novo usuário com informações fornecidas.
- **`edit(cpf, email, nome, telefone, senha)`**: Edita os dados de um usuário existente.
- **`delete(cpf)`**: Exclui um usuário.

#### Métodos de Consulta:
- **`get.all()`**: Retorna todos os usuários cadastrados.
- **`get.deliverers()`**: Retorna todos os entregadores cadastrados.
- **`get.administrators()`**: Retorna todos os administradores cadastrados.
- **`get.by_cpf(cpf)`**: Retorna um usuário específico pelo CPF.

#### Métodos de Atribuição de Função:
- **`set_as.deliverer(cpf)`**: Adiciona um usuário à lista de entregadores.
- **`set_as.administrator(cpf)`**: Adiciona um usuário à lista de administradores.

#### Métodos de Remoção de Função:
- **`unset_as.deliverer(cpf)`**: Remove um usuário da lista de entregadores.
- **`unset_as.administrator(cpf)`**: Remove um usuário da lista de administradores.

---

## **Fluxo de Funcionamento**

1. **Cadastro de Usuário**: 
   - O usuário se cadastra fornecendo informações como CPF, email, nome, telefone e senha.
   
2. **Gestão de Entregas**: 
   - Administradores ou entregadores podem gerenciar as entregas, criando, atualizando, excluindo e alterando o status das entregas.

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

Esta documentação foi criada para fornecer uma visão geral clara e direta das principais funcionalidades do sistema de entregas. O objetivo principal é facilitar a comunicação entre os desenvolvedores front-end e back-end, permitindo uma melhor compreensão das funcionalidades e integração do sistema. Caso precise de mais detalhes sobre algum aspecto do código, entre em contato e estaremos à disposição para fornecer mais explicações.

---

Esta versão da documentação deve ser mais transparente quanto à sua origem e objetivo. Se precisar de mais ajustes, fique à vontade para pedir!
