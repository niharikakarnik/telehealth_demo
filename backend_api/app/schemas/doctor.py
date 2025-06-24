from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .user import User

class DoctorBase(BaseModel):
    specialization: str
    license_number: str
    years_of_experience: int

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(DoctorBase):
    specialization: Optional[str] = None
    license_number: Optional[str] = None
    years_of_experience: Optional[int] = None

class Doctor(DoctorBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user: User

    class Config:
        from_attributes = True

class DoctorList(BaseModel):
    doctors: List[Doctor]

    class Config:
        from_attributes = True
