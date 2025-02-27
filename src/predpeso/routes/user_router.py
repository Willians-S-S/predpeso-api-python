from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from predpeso.schemas.user_schemas import UserRequest, UserResponse, UserUpdate
from predpeso.services.user_service import UserService
from predpeso.db.connection import get_db



user_router = APIRouter(prefix='/user')

@user_router.post("/", response_model=UserResponse)
def creat_user(user: UserRequest, db: Session = Depends(get_db) ):
    return UserService(db_session=db).add(user=user)

@user_router.get("/{id_user}", response_model=UserResponse)
def get_user_id(id_user: str, db: Session = Depends(get_db)):
    return UserService(db_session=db).get(id_user=id_user)

@user_router.get("/", response_model=list[UserResponse])
def get_all(db: Session = Depends(get_db)):
    return UserService(db_session=db).get_all()

@user_router.put("/{id_user}", response_model=UserResponse)
def upadate_user(user: UserUpdate, id_user: str, db: Session = Depends(get_db) ):
    return UserService(db_session=db).update(user=user, user_id=id_user)

@user_router.delete("/{id_user}")
def delete(id_user: str, db: Session = Depends(get_db)):
    return UserService(db_session=db).delete(user_id=id_user)