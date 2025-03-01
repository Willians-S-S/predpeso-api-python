from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from predpeso.schemas.animal_schemas import AnimalRequest, AnimalResponse, AnimalUpdate
from predpeso.services.animal_service import AnimalService
from predpeso.db.connection import get_db



animal_router = APIRouter(prefix='/animal')

@animal_router.post("/", response_model=AnimalResponse)
def creat_animal(animal: AnimalRequest, db: Session = Depends(get_db) ):
    return AnimalService(db_session=db).add(animal=animal)

@animal_router.get("/{id_animal}", response_model=AnimalResponse)
def get_animal_id(id_animal: str, db: Session = Depends(get_db)):
    return AnimalService(db_session=db).get(animal_id=id_animal)

@animal_router.get("/", response_model=list[AnimalResponse])
def get_all(db: Session = Depends(get_db)):
    return AnimalService(db_session=db).get_all()

@animal_router.put("/inference/{id_animal}", response_model=AnimalResponse)
def upadate_animal(image_url: str, id_animal: str, db: Session = Depends(get_db)):
    return AnimalService(db_session=db).inference(animal_id=id_animal, image_url=image_url)

@animal_router.put("/{id_animal}", response_model=AnimalResponse)
def upadate_animal(animal: AnimalUpdate, id_animal: str, db: Session = Depends(get_db) ):
    return AnimalService(db_session=db).update(animal=animal, animal_id=id_animal)

@animal_router.delete("/{id_animal}")
def delete(id_animal: str, db: Session = Depends(get_db)):
    return AnimalService(db_session=db).delete(animal_id=id_animal)