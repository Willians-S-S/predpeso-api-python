from pydantic import BaseModel
from datetime import datetime

class AnimalRequest(BaseModel):
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    healthCondition: str | None = None
    currentWeight: str | None = None
    createdAt: datetime | None = None
    updated_at: datetime | None = None
    farm_id: str 

class AnimalResponse(BaseModel):
    id: str 
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    healthCondition: str | None = None
    currentWeight: str | None = None
    createdAt: datetime | None = None
    updated_at: datetime | None = None
    farm_id: str 

class AnimalUpdate(BaseModel):
    id: str 
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    healthCondition: str | None = None
    currentWeight: str | None = None
    createdAt: datetime | None = None
    updated_at: datetime | None = None
    farm_id: str | None = None