from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(Text)

class Design(Base):
    __tablename__ = "designs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    image_url = Column(String)
    description = Column(String)

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    icon = Column(String)
    description = Column(String)
