https://github.com/codingwithroby/fastapi-the-complete-course

```
python3 -m venv fastapienv
source fastapienv/bin/activate
pip install fastapi
pip install "uvicorn[standard]"
pip list
deactivate
```
=====
```
uvicorn books:app --reload

uvicorn fastapienv.books:app --reload

uvicorn TodosApp.main:app --reload
pip install "fastapi[standard]"
fastapi run books.py           
```
====
```
1xx: Information Response: Request Processing.
2xx: Success: Request Successfully complete
     200: Successful, 201: created - Post request, 204: No content - successful with PUT
3xx: Redirection: Further action must be complete
4xx: Client Errors: An error was caused by the client.
    400: Bad request, 401: Unauthorized, 404:Not found, 422, Unprocessable entity- semantic error in client request.
5xx: Server Errors: An error occurred on the server.

    500: Internal server error.
```
====
```
pip install sqlalchemy
```
====
```
Pip install passlib

Pip install bcrypt==4.0.1
```
====
```
pip install python-multipart
```
====
```
Pip install "python-jose[cryptography]"

Openssl rand -hex 32
```
====
```
pip install pytest
pytest --disable-warnings
```
====
```
pip install httpx
pip install pytest-asyncio
```
====
```
pip install aiofiles

pip install jinja2
```
====
```
pip3 freeze > requirements.tsx
pip install -r requirements.tsx
uvicorn Project5.TodoApp.main:app --host 0.0.0.0 --port 10000
```
====
```
productions deploy of PostgreSQL:
elephantsql.com
```
====
```
sqlite3 todos.db //to create database
.schema
.mod table //to get results in table form

select * from todos;
insert into todos (title, description, priority, complete) values ( 'Go to tesco', 'description of go to store', 3, 0);
```
====
```
SQLALCHEMY_DATABSE_URL = 'postgresql://postgres:test1234@localhost/todoappdb
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) //its used only for Sqlite
```
====
```
pip install alembic
alembic init <folder name>
alembic revision -m < message>
alembic upgrade <revision #>
alembic downgrade -1
```
