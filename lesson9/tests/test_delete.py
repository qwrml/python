import pytest
from models.student import Student

class TestDeleteStudent:
    def test_soft_delete_student_success(self, db_session, sample_student_data):
        student = Student(**sample_student_data)
        db_session.add(student)
        db_session.commit()
        
        student_id = student.id
        student.is_active = False
        db_session.commit()
        
        deleted_student = db_session.get(Student, student_id)
        assert deleted_student.is_active == False