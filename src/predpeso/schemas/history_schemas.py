from pydantic import BaseModel
from datetime import datetime

class HistoryResponse(BaseModel):
    id: str 
    weight: float 
    created_at: datetime
    image_url: str 
    animal_id: str

