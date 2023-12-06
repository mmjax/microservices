from uuid import UUID
from app.models.order import Order


order: list[Order] = []


class OrderRepo():
    def get_orders(self) -> list[Order]:
        return order

    def get_order_by_id(self, id: UUID) -> Order:
        for d in order:
            if d.id == id:
                return d
        raise KeyError

    def create_order(self, order: Order) -> Order:
        if len([d for d in order if d.id == order.id]) > 0:
            raise KeyError
        order.append(order)
        return order

    def set_status(self, order: Order) -> Order:
        for d in order:
            if d.id == order.id:
                d.status = order.status
                break
        return order

    def set_discount(self, order: Order) -> Order:
        for d in order:
            if d.id == order.id:
                d.discount = order.discount
                break
        return order

