# Используем базовый образ Python
FROM python:3.12

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем файлы проекта
COPY /src .
