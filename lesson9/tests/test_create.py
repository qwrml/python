import pytest
from models.student import Student

class TestCreateStudent:
    def test_create_student_success(self, db_session, sample_student_data):
        student = Student(**sample_student_data)
        db_session.add(student)
        db_session.commit()
        
        assert student.id is not None
        assert student.name == "Test Student"
        assert student.email == "test@example.com"
        assert student.is_active == True