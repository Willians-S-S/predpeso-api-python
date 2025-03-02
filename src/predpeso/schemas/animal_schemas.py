from pydantic import BaseModel
from datetime import datetime

from predpeso.schemas.history_schemas import HistoryResponse

class AnimalRequest(BaseModel):
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    health_condition: str | None = None
    farm_id: str 

class AnimalResponse(BaseModel):
    id: str 
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    image_url: str | None = None
    health_condition: str | None = None
    current_weight: float | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    farm_id: str 
    historys: list[HistoryResponse]

class AnimalUpdate(BaseModel):
    id: str 
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    health_condition: str | None = None
    current_weight: float | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    farm_id: str | None = None
