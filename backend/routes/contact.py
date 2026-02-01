from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/contact", tags=["contact"])

@router.post("/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(database.get_db)):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact
