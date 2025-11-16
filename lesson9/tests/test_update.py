import pytest
from models.student import Student

class TestUpdateStudent:
    def test_update_student_success(self, db_session, sample_student_data):
        student = Student(**sample_student_data)
        db_session.add(student)
        db_session.commit()
        
        student.name = "Updated Student"
        student.email = "updated@example.com"
        db_session.commit()
        
        updated_student = db_session.get(Student, student.id)
        assert updated_student.name == "Updated Student"
        assert updated_student.email == "updated@example.com"