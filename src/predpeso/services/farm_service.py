from datetime import datetime
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
import uuid

from predpeso.models.models import FarmModel, UserModel
from predpeso.schemas.farm_schemas import FarmRequest, FarmResponse, FarmUpdate
class FarmService:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
    
    def add(self, farm: FarmRequest) -> FarmResponse:

        user_on_db = self.db_session.query(UserModel).filter_by(id = farm.user_id).first()

        if not user_on_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Usuário não encontrado.")
        
        date_created_and_updated = datetime.now()
        
        farm_on_db = FarmModel(**farm.model_dump(), id=str(uuid.uuid4()), created_at=date_created_and_updated, updated_at=date_created_and_updated)

        self.db_session.add(farm_on_db)
        self.db_session.commit()

        return farm_on_db
    
    def get(self, farm_id: str) -> FarmResponse:
        farm_on_db = self.db_session.query(FarmModel).filter_by(id = farm_id).first()

        if(not farm_on_db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Fazenda não encontrado."
                )
        
        return farm_on_db
    
    def get_all(self) -> list[FarmResponse]:
        farms_on_db = self.db_session.query(FarmModel).all()

        return farms_on_db
    
    def update(self, farm: FarmUpdate, farm_id: str):
        farm_on_db = self.db_session.query(FarmModel).filter_by(id = farm_id).first()

        if(not farm_on_db):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Fazenda não encontrado.")

        for fild, value in farm.model_dump().items():
            if value:
                print(fild, value)
                setattr(farm_on_db, fild, value)

        self.db_session.commit()
        
        return farm_on_db

    
    def delete(self, farm_id: str) -> dict:
        farm_on_db = self.db_session.query(FarmModel).filter_by(id = farm_id).first()

        if(not farm_on_db):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Fazenda não encontrado.")
        
        self.db_session.delete(farm_on_db)
        self.db_session.commit()

        return {status.HTTP_204_NO_CONTENT: "Fazenda deletado com sucesso."}

        
    