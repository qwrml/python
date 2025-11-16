import pytest
from database import engine, SessionLocal
from models.student import Base, Student

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_student_data():
    return {
        "name": "Test Student",
        "email": "test@example.com"
    }