from uuid import UUID
from pydantic import BaseModel, ConfigDict


class Promocode(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    code: str
    discount: float
