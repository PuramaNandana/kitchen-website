from pydantic import BaseModel
from typing import Optional

class ContactBase(BaseModel):
    name: str
    email: str
    message: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        from_attributes = True

class DesignBase(BaseModel):
    title: str
    image_url: str
    description: str

class DesignCreate(DesignBase):
    pass

class Design(DesignBase):
    id: int

    class Config:
        from_attributes = True

class ServiceBase(BaseModel):
    title: str
    icon: str
    description: str

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int

    class Config:
        from_attributes = True
