FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /order_app

# Установка зависимостей проекта
COPY ./requirements.txt /order_app/
RUN pip install --no-cache-dir --upgrade -r /order_app/requirements.txt

# Перенос проекта в образ
COPY ./app /order_app/app
COPY ./tests /order_app/tests

# Копирование файлов alembic
COPY ./alembic /order_app/alembic
COPY ./alembic.ini /order_app/alembic.ini


EXPOSE 80

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]