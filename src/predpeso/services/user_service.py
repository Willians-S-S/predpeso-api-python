from datetime import datetime
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
import uuid

from predpeso.models.models import UserModel
from predpeso.schemas.user_schemas import UserRequest, UserResponse, UserUpdate
class UserService:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
    
    def add(self, user: UserRequest) -> UserResponse:
        user_on_db = self.db_session.query(UserModel)\
            .filter_by(cpf = user.cpf, email = user.email)\
            .first()
        
        if(user_on_db):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuário já foi cadastrado.")
        
        date_created_and_updated = datetime.now()
        
        user_on_db = UserModel(**user.model_dump(), id=str(uuid.uuid4()), created_at=date_created_and_updated, updated_at=date_created_and_updated)

        self.db_session.add(user_on_db)
        self.db_session.commit()

        return user_on_db
    
    def get(self, user_id: str) -> UserResponse:
        user_on_db = self.db_session.query(UserModel).filter_by(id = user_id).first()

        if(not user_on_db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Usuário não encontrado."
                )
        
        return user_on_db
    
    def get_all(self) -> list[UserResponse]:
        users_on_db = self.db_session.query(UserModel).all()

        return users_on_db
    
    def update(self, user: UserUpdate, user_id: str):
        user_on_db = self.db_session.query(UserModel).filter_by(id = user_id).first()

        if(not user_on_db):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Usuário não encontrado.")

        
        for fild, value in user.model_dump().items():
            if value:
                print(fild, value)
                setattr(user_on_db, fild, value)

        self.db_session.commit()
        
        return user_on_db

    
    def delete(self, user_id: str) -> dict:
        user_on_db = self.db_session.query(UserModel).filter_by(id = user_id).first()

        if(not user_on_db):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Usuário não encontrado.")
        
        self.db_session.delete(user_on_db)
        self.db_session.commit()

        return {status.HTTP_204_NO_CONTENT: "Usuário deletado com sucesso."}

        
    