from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base
from app.models.user import User


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    medical_record_number = Column(String, unique=True, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)
    has_insurance = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="patient", uselist=False)
    appointments = relationship("Appointment", back_populates="patient")

    def __repr__(self):
        return f"Patient(id={self.id}, medical_record_number={self.medical_record_number}, date_of_birth={self.date_of_birth})"
