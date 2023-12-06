# /app/schemas/delivery.py

from sqlalchemy import Column, String, DateTime, Enum, Float
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.base_schema import Base
from app.models.order import OrderStatuses


class Order(Base):
    __tablename__ = 'orders'

    id = Column(UUID(as_uuid=True), primary_key=True)
    items = Column(UUID(as_uuid=True), nullable=True)
    status = Column(Enum(OrderStatuses), nullable=True)
    discount = Column(Float, nullable=True)