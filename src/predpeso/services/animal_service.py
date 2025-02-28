from datetime import datetime
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
import uuid

from predpeso.models.models import AnimalModel, FarmModel
from predpeso.schemas.animal_schemas import AnimalRequest, AnimalResponse, AnimalUpdate

ENTENY = "Animal"

class AnimalService:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
    
    def add(self, animal: AnimalRequest) -> AnimalResponse:

        farm_on_db = self.db_session.query(FarmModel).filter_by(id = animal.farm_id).first()

        if not farm_on_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Fazenda não encontrado.")
        
        date_created_and_updated = datetime.now()
        
        animal_on_db = AnimalModel(**animal.model_dump(), id=str(uuid.uuid4()), created_at=date_created_and_updated, updated_at=date_created_and_updated)

        self.db_session.add(animal_on_db)
        self.db_session.commit()

        return animal_on_db
    
    def get(self, animal_id: str) -> AnimalResponse:
        animal_on_db = self.db_session.query(AnimalModel).filter_by(id = animal_id).first()

        if(not animal_on_db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"{ENTENY} não encontrado."
                )
        
        return animal_on_db
    
    def get_all(self) -> list[AnimalResponse]:
        animals_on_db = self.db_session.query(AnimalModel).all()

        return animals_on_db
    
    def update(self, animal: AnimalUpdate, animal_id: str):
        animal_on_db = self.db_session.query(AnimalModel).filter_by(id = animal_id).first()

        if(not animal_on_db):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"{ENTENY} não encontrado.")

        for fild, value in animal.model_dump().items():
            if value:
                print(fild, value)
                setattr(animal_on_db, fild, value)

        self.db_session.commit()
        
        return animal_on_db

    
    def delete(self, animal_id: str) -> dict:
        animal_on_db = self.db_session.query(AnimalModel).filter_by(id = animal_id).first()

        if(not animal_on_db):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"{ENTENY} não encontrado.")
        
        self.db_session.delete(animal_on_db)
        self.db_session.commit()

        return {status.HTTP_204_NO_CONTENT: f"{ENTENY} deletado com sucesso."}

        
    