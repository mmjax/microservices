from fastapi import FastAPI
from app.endpoints.order_router import order_router

app = FastAPI(title='Order Service')
app.include_router(order_router)

