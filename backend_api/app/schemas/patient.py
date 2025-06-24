from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .user import User

class PatientBase(BaseModel):
    medical_record_number: str
    date_of_birth: datetime
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    has_insurance: Optional[bool] = False

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    medical_record_number: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    has_insurance: Optional[bool] = None

class Patient(PatientBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user: User

    class Config:
        from_attributes = True

class PatientList(BaseModel):
    patients: List[Patient]

    class Config:
        from_attributes = True
