from cis301.project1.student import Student
from cis301.project1.__main__ import main
import sys

def test_student():
    s= Student("Alex", '"Operating Systems", "Database Systems", "Data Structures"', '3.5')
    assert isinstance(s, Student)

def test_student_says():
    s= Student("Alex", '"Operating Systems", "Database Systems", "Data Structures"', "3.5")
    assert isinstance(s.says(), "This class is too much work")
