from datetime import datetime, timedelta
from app.core.database import engine, Base
from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment, AppointmentStatus
from sqlalchemy.orm import Session
import bcrypt

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a session
    db = Session(bind=engine)
    
    try:
        # Create test users
        admin_user = User(
            email="admin@telehealth.com",
            hashed_password=bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            first_name="Admin",
            last_name="User",
            is_superuser=True
        )
        
        doctor_user = User(
            email="doctor@example.com",
            hashed_password=bcrypt.hashpw("doctor123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            first_name="John",
            last_name="Doe"
        )
        
        patient_user = User(
            email="patient@example.com",
            hashed_password=bcrypt.hashpw("patient123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            first_name="Jane",
            last_name="Smith"
        )
        
        # Create doctor
        doctor = Doctor(
            user=doctor_user,
            specialization="Cardiology",
            license_number="DOC123",
            years_of_experience=10
        )
        
        # Create patient
        patient = Patient(
            user=patient_user,
            medical_record_number="MRN123",
            date_of_birth=datetime(1990, 1, 1),
            emergency_contact_name="Emergency Contact",
            emergency_contact_phone="123-456-7890",
            has_insurance=True
        )
        
        # Create appointment
        appointment = Appointment(
            user=admin_user,
            doctor=doctor,
            patient=patient,
            scheduled_time=datetime.now() + timedelta(days=1),
            status=AppointmentStatus.PENDING,
            notes="Initial consultation"
        )
        
        # Add to session
        db.add(admin_user)
        db.add(doctor_user)
        db.add(patient_user)
        db.add(doctor)
        db.add(patient)
        db.add(appointment)
        
        # Commit changes
        db.commit()
        
        print("Database initialized with test data!")
        
    except Exception as e:
        db.rollback()
        print(f"Error initializing database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
