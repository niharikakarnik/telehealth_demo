import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import engine, Base
from app.models.user import User
from app.core.security import get_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import get_settings

settings = get_settings()

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

@pytest.fixture(scope="module")
def test_user(test_db):
    user = User(
        email="test@example.com",
        hashed_password=get_password_hash("test123"),
        first_name="Test",
        last_name="User"
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    return user

def test_create_token(test_client, test_user):
    response = test_client.post(
        "/token",
        json={"email": "test@example.com", "password": "test123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"

def test_invalid_login(test_client):
    response = test_client.post(
        "/token",
        json={"email": "invalid@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401

def test_read_users_me(test_client, test_user):
    # First get a token
    response = test_client.post(
        "/token",
        json={"email": "test@example.com", "password": "test123"}
    )
    token = response.json()["access_token"]
    
    # Use the token to access protected endpoint
    response = test_client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["first_name"] == "Test"
    assert data["last_name"] == "User"
