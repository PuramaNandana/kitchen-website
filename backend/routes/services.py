from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(prefix="/services", tags=["services"])

@router.get("/", response_model=List[schemas.Service])
def get_services(db: Session = Depends(database.get_db)):
    return db.query(models.Service).all()

@router.post("/", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(database.get_db)):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service
