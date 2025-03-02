from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from predpeso.db.connection import get_db
from predpeso.models.models import UserModel
from predpeso.schemas.user_schemas import UserRequest, UserResponse, UserUpdate
from predpeso.schemas.token_schemas import Token
from predpeso.security.jwt_token import get_current_user
from predpeso.services.user_service import UserService



user_router = APIRouter(prefix='/user')

@user_router.post("/", response_model=UserResponse)
def creat_user(user: UserRequest, db: Session = Depends(get_db) ):
    return UserService(db_session=db).add(user=user)

@user_router.get("/{id_user}", response_model=UserResponse)
def get_user_id(
                id_user: str,  
                db: Session = Depends(get_db),
                current_user=Depends(get_current_user)):
    
    return UserService(db_session=db).get(user_id=id_user)

@user_router.get("/", response_model=list[UserResponse])
def get_all(db: Session = Depends(get_db)):
    return UserService(db_session=db).get_all()

@user_router.put("/{id_user}", response_model=UserResponse)
def upadate_user(user: UserUpdate, 
                 id_user: str, 
                 db: Session = Depends(get_db),
                 current_user: UserModel = Depends(get_current_user)):
    print(type(current_user))
    return UserService(db_session=db).update(user=user, user_id=id_user, current_user=current_user)

@user_router.delete("/{id_user}")
def delete(id_user: str, 
           db: Session = Depends(get_db),
           current_user=Depends(get_current_user)):
    return UserService(db_session=db).delete(user_id=id_user)

@user_router.post("/token", response_model=Token)
def longin_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return UserService(db_session=db).login(form_data=form_data)