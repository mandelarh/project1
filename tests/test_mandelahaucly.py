import pytest

from cis301.project1.__main__ import main
from cis301.project1.student import Student
#import pytest
import sys




def test_student_args1():
    args = ['Mandela', 'CIS301', '3.8']
    gpa = args[2]

    s = Student(args[0],args[1], gpa)
    assert isinstance(s, Student)
    #assert isinstance(s.gpa, float)


def test_student_args2():
    with pytest.raises(ValueError) as exc_info:
        Student("Alice", 'CIS301',3.5)
    assert str(exc_info.value) == "GPA must be a string"

def test_student_args3():
    with pytest.raises(ValueError) as exc_info:
        Student("Bob", "CIS301", 4)
    assert str(exc_info.value) == "GPA must be a string"

def test_student_args4():
    with pytest.raises(ValueError) as exc_info:
        Student(None, "CIS301", '3.8')
    assert str(exc_info.value) == "Student name cannot be None"

def test_student_args5():
    # Test invalid classes (None)
    with pytest.raises(ValueError) as exc_info:
        Student("Bob", None, "3.5")  # Classes is None
    assert str(exc_info.value) == "Classes cannot be None"

def test_student_args6():
    # Test invalid classes (None)
    with pytest.raises(ValueError) as exc_info:
        Student("Bob",'CIS301', None)  # Classes is None
    assert str(exc_info.value) == "GPA cannot be None"

def test_student_args7():
    # Test invalid classes (None)
    with pytest.raises(ValueError) as exc_info:
        Student("Bob",'CIS301', '0')  # Classes is None
    assert str(exc_info.value) == "GPA cannot be 0"

def test_student_args8():
    student = Student("Bob", ["CIS301", "MATH101"], "3.5")
    #print(str(student))  # Debugging: Print the actual output
    expected_output = (
        "Bob has a GPA of 3.5 and is taking 2 classes: ['CIS301', 'MATH101'] Bob says This class is too much work"
    )
    assert str(student) == expected_output

def test_student_args9():
    # Create a Student object with no classes
    student = Student("Mandela", [], "4.0")

    # Verify the says() method output
    assert student.says() == "Mandela has no classes"

def test_says_with_classes():
    # Create a Student object with classes
    student = Student("Mandela", ["CIS301", "MATH101"], "3.5")

    # Verify the says() method output
    assert student.says() == "This class is too much work"