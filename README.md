# Digital Performance

Sistema web para gestores de agência de Marketing Digital.

## Funcionalidades

- Login por email e senha (usuários definidos em `data/users.csv`)
- Visualização de métricas em tabela
- Filtros por data
- Ordenação por qualquer coluna
- Coluna `cost_micros` visível apenas para usuários com papel `admin`
- API REST para autenticação e consulta de métricas

## Estrutura do Projeto

```
digital-performance/
├── app.py
├── controllers/
│   ├── api_controller.py
│   └── web_controller.py
├── models/
│   ├── user_model.py
│   └── metric_model.py
├── data/
│   ├── users.csv
│   └── metrics.csv
├── frontend/
│   └── templates/
│       ├── index.html
│       └── dados.html
├── static/
│   └── style.css
└── README.md
```

## Como executar:

1. **Instale as dependências:**
   ```
   pip install flask pandas
   ```

2. **Garanta que os arquivos `users.csv` e `metrics.csv` estejam na pasta `data/`.**

3. **Execute o servidor:**
   ```
   python app.py
   ```

4. **Acesse o sistema:**
   - Frontend: http://localhost:5000
   - API: http://localhost:5000/api

## Testando a API via Postman:

- **Login**
  - Endpoint: `POST /api/login`
  - Body (JSON):
    
  ```
  {
  "email": "admin@gmail.com",
  "password": "oeiruhn56146"
  }
  ```
  ``` 
    {
      "email": "user@gmail.com",
      "password": "908ijofff"
    }
  ```

- **Métricas**
  - Endpoint: `GET /api/metrics`
  - Parâmetros: `role`, `date_from`, `date_to`, `sort_by`, `order`
  - Exemplo:
    ```
    http://localhost:5000/api/metrics?role=admin&date_from=2024-01-01&date_to=2024-01-31&sort_by=score&order=desc
    ```
    ```
    http://localhost:5000/api/metrics?role=user&date_from=2024-01-01&date_to=2024-01-31&sort_by=score&order=desc
    ```

## Observações:

- Não é possível cadastrar novos usuários pelo sistema.
- Login apenas com os dados do users.csv

```Login

  email: admin@gmail.com
  user1
  password: oeiruhn56146
  admin

  ////

  email: user@gmail.com
  user2
  password: 908ijofff
  user
