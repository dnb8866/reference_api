# RESTful API справочника материалов с категориями и возможностью отображения в виде дерева.

## Установка без Docker
1. Клонируйте репозиторий.
2. Создайте виртуальное окружение:
```python/python3 -m venv venv```
3. Активируйте виртуальное окружение:
* Для Linux/MacOS ```source venv/bin/activate```
* Для Windows ```venv\Scripts\activate.bat```
4. Из корневой папки установите зависимости из requirements.txt:
```pip install -r requirements.txt```
5. Переименуйте .env.example в .env и отредактируйте переменные.
6. Создайте базу данных в PostgreSQL с указанным именем в ```.env``` .
7. Из папки srс/ примените миграции:
```python/python3 manage.py migrate```
8. Запустите приложение:
```python/python3 manage.py runserver```

## Установка c Docker
1. Клонируйте репозиторий.
2. Запустите из корня проекта
```docker compose up --build```.
3. Сервис доступен по адресу ```localhost:8000.```


## Импорт данных о материалах в БД из .xlsx файла.
- Необходимо отправить POST запрос с файлом на endpoint ```api/v1/import-materials/```.
- Формат файла в примере ```example.xlsx```. Также необходимо указать id категории.

## Динамическая документация
- Endpoint `localhost:8000/redoc/` - документация Redoc.
- Endpoint `localhost:8000/swagger/` - документация Swagger.