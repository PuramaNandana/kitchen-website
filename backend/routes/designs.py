from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(prefix="/designs", tags=["designs"])

@router.get("/", response_model=List[schemas.Design])
def get_designs(db: Session = Depends(database.get_db)):
    return db.query(models.Design).all()

@router.post("/", response_model=schemas.Design)
def create_design(design: schemas.DesignCreate, db: Session = Depends(database.get_db)):
    db_design = models.Design(**design.dict())
    db.add(db_design)
    db.commit()
    db.refresh(db_design)
    return db_design
