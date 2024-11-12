# RESTful API справочника

## Установка
1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение:
```python/python3 -m venv venv```
3. Из корневой папки установите зависимости из requirements.txt:
```pip install -r requirements.txt```
4. Переименуйте .env.example в .env и отредактируйте переменные.
5. Создайте базу данных в PostgreSQL с указанным именем в ```.env``` .
6. Из папки srс/ примените миграции:
```python/python3 manage.py migrate```
7. Запустите приложение:
```python/python3 manage.py runserver```


## Импорт данных о материалах в БД из .xlsx файла.
- Необходимо отправить POST запрос с файлом на endpoint ```api/v1/import-materials/```.
- Формат файла в примере ```example.xlsx```. Также необходимо указать id категории.

