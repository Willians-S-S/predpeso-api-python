from pydantic import BaseModel
from datetime import datetime

class animalRequest(BaseModel):
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    healthCondition: str | None = None
    currentWeight: str | None = None
    createdAt: datetime | None = None
    updated_at: datetime | None = None
    farm_id: str 

class animalResponse(BaseModel):
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

class animalUpdate(BaseModel):
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