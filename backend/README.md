# Backend

Backend da aplicação desenvolvido em **Flask**, com **SQLAlchemy**, **Flask-Migrate**, **JWT** e banco **MySQL**.

## Tecnologias

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Flask-Migrate
* PyMySQL
* Alembic

## Estrutura

```bash
backend/
├── app/
│   ├── extensions/     # Configuração de banco, JWT e migrations
│   ├── models/         # Modelos ORM
│   └── routes/         # Rotas da API
├── migrations/         # Arquivos de migrations do Alembic
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto
└── .gitignore
```

## Como executar

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

No arquivo `app/__init__.py`, a aplicação usa a seguinte URI de conexão:

```python
mysql+pymysql://<YOUR USERNAME>:<YOUR_PASSWORD>@localhost/sigac
```

Substitua os valores pelas credenciais do seu ambiente local. Se preferir, essa configuração pode ser movida para variáveis de ambiente depois.

### 5. Rodar a aplicação

```bash
python main.py
```

A aplicação será iniciada em modo debug.

## Migrations

As migrations ficam na pasta `migrations/`.

Para criar uma nova migration:

```bash
flask db migrate -m "sua mensagem"
```

Para aplicar as alterações no banco:

```bash
flask db upgrade
```

## Variáveis e arquivos ignorados

O projeto já ignora:

* `venv/`
* `__pycache__/`
* `*.pyc`