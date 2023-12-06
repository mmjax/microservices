from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body
from app.services.order_service import OrderService
from app.models.order import Order


order_router = APIRouter(prefix='/order', tags=['Order'])

@order_router.get('/')
def get_orders(order_service: OrderService = Depends(OrderService)) -> list[Order]:
    return order_service.get_orders()

@order_router.get('/test')
def root():
    return{'лаптев''лох'}

# @order_router.post('/{id}/finish')
# def finish_order(id: UUID, order_service: OrderService = Depends(OrderService)) -> Order:
#     try:
#         order = order_service.finish_order(id)
#         return order.dict()
#     except KeyError:
#         raise HTTPException(404, f'Order with id={id} not found')
#     except ValueError:
#         raise HTTPException(400, f'Order with id={id} can\'t be finished')

# @delivery_router.post('/{id}/cancel')
# def cancel_delivery(id: UUID, order_service: OrderService = Depends(OrderService)) -> Order:
#     try:
#         order = order_service.cancel_delivery(id)
#         return order.dict()
#     except KeyError:
#         raise HTTPException(404, f'Order with id={id} not found')
#     except ValueError:
#         raise HTTPException(400, f'Order with id={id} can\'t be canceled')

# @order_router.post('/{id}/discount')
# def set_discount(
#  id: UUID,
#  discount: float,
#  order_service: OrderService = Depends(OrderService)) -> Order:
#     try:
#         order = order_service.set_discount(id, discount)
#         return order.dict()
#     except KeyError:
#         raise HTTPException(404, f'Order with id={id} not found')
#     except ValueError:
#         raise HTTPException(400, f'Да пошел ты нахуй')