from datetime import datetime
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session
import uuid

from predpeso.models.models import UserModel
from predpeso.schemas.user_schemas import UserRequest, UserResponse, UserUpdate
from predpeso.security.password_hash import get_password_hash, verify_password
from predpeso.security.jwt_token import create_acess_token

class UserService:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
    
    def add(self, user: UserRequest) -> UserResponse:
        user_on_db = self.db_session.query(UserModel)\
            .filter_by(cpf = user.cpf, email = user.email)\
            .first()
        
        if(user_on_db):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já foi cadastrado.")

        del user_on_db

        user_on_db = self.db_session.query(UserModel)\
            .filter_by(cpf = user.cpf)\
            .first()
        
        if(user_on_db):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CPF já foi cadastrado.")
        
        date_created_and_updated = datetime.now()

        user.password = get_password_hash(user.password)
        
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
                if fild == "password":
                    value = get_password_hash(value)
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

    def login(self, form_data: OAuth2PasswordRequestForm):
        user_on_db = self.db_session.query(UserModel).filter_by(username = form_data.username).first()

        if not user_on_db or not verify_password(form_data.password, user_on_db.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username ou senha incorretos.")
        
        access_token = create_acess_token(data={"sub": user_on_db.username})    

        return {"access_token": access_token, "token_type": "bearer"}
    