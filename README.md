# PredPeso API

## Descrição

O **PredPeso API** é um sistema de gerenciamento para registro e controle de fazendas, animais e históricos de pesos, desenvolvido em **FastAPI** e utilizando o banco de dados **SQLAlchemy** com **Alembic** para migrações.

Este projeto visa fornecer funcionalidades como:

* Cadastro, visualização, atualização e exclusão de usuários, fazendas e animais.
* Armazenamento de imagens relacionadas aos animais.
* Previsão de peso de animais usando inferência com redes neurais.
* Histórico de pesos dos animais.

## Tecnologias

* **FastAPI**: Framework moderno e rápido para construir APIs.
* **SQLAlchemy**: ORM para interação com banco de dados.
* **Alembic**: Ferramenta para gerenciamento de migrações de banco de dados.
* **Pydantic**: Validação de dados.
* **TensorFlow**: Modelo de rede neural para predição de peso.
* **PostgreSQL**: Banco de dados relacional utilizado.
* **JWT**: Autenticação baseada em token para proteger endpoints.

## Como rodar

### 1. Instalar as dependências

Certifique-se de ter o **Python 3.9+** instalado e, em seguida, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 2. Configuração do Banco de Dados

Crie um arquivo `.env` na raiz do projeto com a seguinte variável de ambiente:

```
DB_URL=postgresql://<usuario>:<senha>@localhost:5432/<nome_do_banco>
```

Exemplo:

```
DB_URL=postgresql://user:password@localhost:5432/predpeso
```

### 3. Rodar as migrações

Execute o comando abaixo para aplicar as migrações e criar as tabelas no banco de dados:

```bash
alembic upgrade head
```

### 4. Rodar a API

Após configurar o banco de dados e as migrações, você pode rodar a API com o comando abaixo:

```bash
uvicorn predpeso.app:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

### 5. Testar a API

Você pode acessar a documentação interativa da API através do **Swagger UI** em:

```
http://127.0.0.1:8000/docs
```

Ou utilizar a **ReDoc**:

```
http://127.0.0.1:8000/redoc
```

## Estrutura de Diretórios

```
/src
    /predpeso
        /app.py                # Inicia a aplicação FastAPI
        /routes
            /animal_router.py  # Endpoints para gerenciamento de animais
            /farm_router.py    # Endpoints para gerenciamento de fazendas
            /user_router.py    # Endpoints para gerenciamento de usuários
        /services
            /animal_service.py # Lógica de negócios para animais
            /farm_service.py   # Lógica de negócios para fazendas
            /user_service.py   # Lógica de negócios para usuários
        /models
            /models.py         # Definição dos modelos do banco de dados
        /db
            /connection.py     # Conexão com o banco de dados
            /base.py           # Base para os modelos do banco de dados
        /schemas
            /animal_schemas.py # Esquemas de dados para animais
            /farm_schemas.py   # Esquemas de dados para fazendas
            /user_schemas.py   # Esquemas de dados para usuários
        /commons
            /inference.py      # Lógica de inferência para predição de peso
            /image.py           # Lógica de manipulação de imagens
        /security
            /password_hash.py  # Funções para manipulação de senhas
            /jwt_token.py      # Lógica para autenticação JWT
```

## Endpoints

### `/user`

* `POST /user/`: Cria um novo usuário.
* `GET /user/{id_user}`: Obtém detalhes de um usuário específico.
* `GET /user/`: Obtém todos os usuários.
* `PUT /user/{id_user}`: Atualiza informações de um usuário.
* `DELETE /user/{id_user}`: Deleta um usuário.
* `POST /user/token`: Realiza login e retorna um token JWT.

### `/farm`

* `POST /farm/`: Cria uma nova fazenda.
* `GET /farm/{id_farm}`: Obtém detalhes de uma fazenda.
* `GET /farm/`: Obtém todas as fazendas.
* `PUT /farm/{id_farm}`: Atualiza informações de uma fazenda.
* `DELETE /farm/{id_farm}`: Deleta uma fazenda.

### `/animal`

* `POST /animal/`: Cria um novo animal.
* `GET /animal/{id_animal}`: Obtém detalhes de um animal.
* `GET /animal/`: Obtém todos os animais.
* `PUT /animal/{id_animal}`: Atualiza informações de um animal.
* `DELETE /animal/{id_animal}`: Deleta um animal.
* `PUT /animal/inference`: Realiza a predição do peso de um animal com base em uma imagem.

