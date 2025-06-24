from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Enum as SQLAlchemyEnum, Text
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime
from enum import Enum

class AppointmentStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(SQLAlchemyEnum(AppointmentStatus), default=AppointmentStatus.PENDING, nullable=False)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

    def __repr__(self):
        return f"Appointment(id={self.id}, scheduled_time={self.scheduled_time}, status={self.status})"
