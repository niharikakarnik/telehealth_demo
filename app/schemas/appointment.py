from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum
from .user import User
from .doctor import Doctor
from .patient import Patient

class AppointmentStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class AppointmentBase(BaseModel):
    scheduled_time: datetime
    status: AppointmentStatus
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user: User
    doctor: Doctor
    patient: Patient

    class Config:
        from_attributes = True

class AppointmentList(BaseModel):
    appointments: List[Appointment]

    class Config:
        from_attributes = True
