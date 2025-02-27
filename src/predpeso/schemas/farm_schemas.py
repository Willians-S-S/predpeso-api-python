from pydantic import BaseModel
from datetime import datetime

class FarmRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    animal_quantity: int | None = None
    user_id: str | None = None

class FarmResponse(BaseModel):
    id: str | None = None
    name: str | None = None
    description: str | None = None
    animal_quantity: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    user_id: str | None = None

class FarmUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    animal_quantity: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    user_id: str | None = None