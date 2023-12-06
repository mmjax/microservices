import enum
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class OrderStatuses(enum.Enum):
    CREATED = 'created'
    PAID = 'paid'
    DONE = 'done'


class Order(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    items: UUID
    status: OrderStatuses
    discount: float | None
