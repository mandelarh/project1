from cis301.project1.__main__ import main
from cis301.project1.student import Student
from cis301.project1.__main__ import main
import sys



def test_student():
    s= Student("Alex", '"Operating Systems", "Database Systems", "Data Structures"', '3.5')
    assert isinstance(s, Student)

def test_student_says():
    s= Student("Alex", '"Operating Systems", "Database Systems", "Data Structures"', "3.5")

    assert s.says() == "This class is too much work"  # Use == for comparison
def test_student_args1():
    args = ['Mandela', 'CIS301', '3.8']
    gpa = float(args[2])

    s = Student(args[0],args[1],args[2], gpa)
    assert isinstance(s, Student)
    assert isinstance(s.gpa, float)