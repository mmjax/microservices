FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /promo_app

# Установка зависимостей проекта
COPY ./promo_app/requirements.txt /promo_app/
RUN pip install --no-cache-dir --upgrade -r /promo_app/requirements.txt

# Перенос проекта в образ
COPY ./promo_app/app /promo_app/app

EXPOSE 81

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port 81"]