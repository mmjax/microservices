import traceback
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.schemas.order import Order as DBOrder


class OrderRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, order: DBOrder) -> Order:
        result = Order.from_orm(order)
        return result

    def _map_to_schema(self, order: Order) -> DBOrder:
        data = dict(order)
        result = DBOrder(**data)
        return result

    def get_orders(self) -> list[Order]:
        deliveries = []
        for d in self.db.query(DBOrder).all():
            deliveries.append(self._map_to_model(d))
        return deliveries

    def get_order_by_id(self, id: UUID) -> Order:
        order = self.db \
            .query(DBOrder) \
            .filter(DBOrder.id == id) \
            .first()
        if order is None:
            raise KeyError
        return self._map_to_model(order)

    def create_order(self, order: Order) -> Order:
        try:
            db_order = self._map_to_schema(order)
            self.db.add(db_order)
            self.db.commit()
            return self._map_to_model(db_order)
        except:
            traceback.print_exc()
            raise KeyError
