# Middleware Service

## Содержание


- [Описание](#описание)
- [Зависимости](#зависимости)
- [Установка](#установка)
- [Инструкция](#инструкция)



## Описание

Промежуточный сервис между клиентами и прочими внешними сервисами. Строит запросы
на основе шаблонных методов класса, производных от базового.


## Зависимости

- [Python](https://www.python.org/downloads/)

## Установка

Выполните гит клон на свою локальную/виртуальную машину - git clone https://github.com/Nekketsu4/Service-middleware.git


### Инструкция
```bash
#создайте виртуальное окружение
#Linux:
python3 -m venv env

#Windows:
python -m venv env


#активируйте виртуальное окружение
#Linux:
source venv/bin/activate

#Windows:
venv\Scripts\activate

#установите пакет с зависимостями 
pip install -r req.txt

#Запустите сервер
python3 manage.py runserver

#Перейдите по ссылке, чтобы протестировать API
http://127.0.0.1:8000/bots/
http://127.0.0.1:8000/bots/2/
http://127.0.0.1:8000/users/
http://127.0.0.1:8000/users/login
```
