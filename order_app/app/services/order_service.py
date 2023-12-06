from uuid import UUID
from datetime import datetime
from app.models.order import Order, OrderStatuses
from app.repositories.bd_order_repo import OrderRepo


class OrderService():
    order_repo: OrderRepo

    def __init__(self) -> None:
        self.order_repo = OrderRepo()

    def get_orders(self) -> list[Order]:
        return self.order_repo.get_orders()

    def create_order(self, order_id: UUID, items: dict) -> OrderRepo:
        order = OrderRepo(id=order_id, address=items, discount=None, status=OrderStatuses.CREATED)
        return self.order_repo.create_order(order)

    def paid_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != OrderStatuses.CREATED:
            raise ValueError
        order.status = OrderStatuses.PAID
        return self.order_repo.set_status(order)

    def set_discount(self, id: UUID, discount: float) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status == OrderStatuses.CREATED:
            order.discount = discount
            return self.order_repo.set_discount(order)
        raise ValueError

    def finish_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != OrderStatuses.CREATED:
            raise ValueError
        order.status = OrderStatuses.DONE
        return self.order_repo.set_status(order)
