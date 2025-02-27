from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from predpeso.schemas.farm_schemas import FarmRequest, FarmResponse, FarmUpdate
from predpeso.services.farm_service import FarmService
from predpeso.db.connection import get_db



farm_router = APIRouter(prefix='/farm')

@farm_router.post("/", response_model=FarmResponse)
def creat_farm(farm: FarmRequest, db: Session = Depends(get_db) ):
    return FarmService(db_session=db).add(farm=farm)

@farm_router.get("/{id_farm}", response_model=FarmResponse)
def get_farm_id(id_farm: str, db: Session = Depends(get_db)):
    return FarmService(db_session=db).get(id_farm=id_farm)

@farm_router.get("/", response_model=list[FarmResponse])
def get_all(db: Session = Depends(get_db)):
    return FarmService(db_session=db).get_all()

@farm_router.put("/{id_farm}", response_model=FarmResponse)
def upadate_farm(farm: FarmUpdate, id_farm: str, db: Session = Depends(get_db) ):
    return FarmService(db_session=db).update(farm=farm, farm_id=id_farm)

@farm_router.delete("/{id_farm}")
def delete(id_farm: str, db: Session = Depends(get_db)):
    return FarmService(db_session=db).delete(farm_id=id_farm)