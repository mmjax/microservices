from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body
import asyncio

from app.services.promocode_service import PromocodeService
from app.models.promocode import Promocode
from app.rabbitmq import send_discount
import logging

promocode_router = APIRouter(prefix='/promocode', tags=['Promocode'])
logging.basicConfig()

@promocode_router.get('/{code}')
def get_promocode(code: str, promocode_service: PromocodeService = Depends(PromocodeService)) -> Promocode:
    return promocode_service.get_promocode(code)

@promocode_router.get('/')
def get_promocode(promocode_service: PromocodeService = Depends(PromocodeService)) -> list[Promocode]:
    return promocode_service.get_promocodes()

@promocode_router.post('/')
def create_promocode(code: str, discount: float, promocode_service: PromocodeService = Depends(PromocodeService)) -> Promocode:
    try:
        promocode = promocode_service.create_promocode(code, discount)
        return promocode.dict()
    except KeyError:
        raise HTTPException(404, f'Cant create promocode')
    
@promocode_router.post('/discount')
def set_discount(code: str, id: UUID, promocode_service: PromocodeService = Depends(PromocodeService)):
    try:
        logging.info('я здесь')
        discount = promocode_service.get_promocode(code)
        logging.info(discount)
        asyncio.run(send_discount(discount, id))
        return {'status': 200}
    except KeyError:
        raise HTTPException(404, f'Order with id={id} not found')
    except ValueError:
        raise HTTPException(400, f'Такого промокода нет')