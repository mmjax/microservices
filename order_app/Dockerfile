FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /order_app

# Установка зависимостей проекта
COPY ./order_app/requirements.txt /order_app/
RUN pip install --no-cache-dir --upgrade -r /order_app/requirements.txt

# Перенос проекта в образ
COPY ./order_app/app /order_app/app

# Копирование файлов alembic
COPY ./order_app/alembic /order_app/alembic
COPY ./order_app/alembic.ini /order_app/alembic.ini

EXPOSE 80

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port 80"]