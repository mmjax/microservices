from fastapi import FastAPI
import asyncio
from app import rabbitmq
from starlette.middleware.sessions import SessionMiddleware
from app.endpoints.order_router import order_router, metrics_router
from app.endpoints.auth_router import auth_router


app = FastAPI(title='Order Service')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume_tasks(loop))

app.add_middleware(SessionMiddleware, secret_key='asas12334sadfdsf')
app.include_router(metrics_router)
app.include_router(order_router)
app.include_router(auth_router)
