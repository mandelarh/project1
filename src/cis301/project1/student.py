from sysconfig import get_path_names
from tkinter.font import names


from cis301.examples.human import Human

class Student(Human):
    """
        This class is represents a Student
        Attributes:
            name:The student’s name.
            classes: The names of the classes the student is taking. A student may take zero or more classes.
            gpa:The student’s grade point average.
    """
    def __init__(self, name, classes, gpa):
        #raise NotImplementedError('not implemented yet')
        super().__init__(name)
        if self.name is None:
            raise ValueError("Student name cannot be None")
        self.name = name

        if classes is None:
            raise ValueError("Classes cannot be None")
        self.classes = classes

        if gpa is None:
            raise ValueError("GPA cannot be None")
        elif not isinstance(gpa, str):
            raise ValueError("GPA must be a string")
        elif gpa == '0':
            raise ValueError("GPA cannot be 0")

        self.gpa = gpa

    def says(self):
        """
            All students say "This class is too much work".
        Returns:
            a String statement that says "This class is too much work".
        """
        #raise NotImplementedError('not implemented yet')
        if not self.classes:
            return f"{self.name} has no classes"
        return "This class is too much work"

    def __str__(self):
        """
        Returns:
            a String that describes this Student.
        """
        #raise NotImplementedError('not implemented yet')
        return (f"{self.name} has a GPA of {self.gpa} and is taking {len(self.classes)} classes: {self.classes} {self.name} "
                f"says {self.says()}")


class Studentdef:
    pass

if __name__ == "__main__":
    # Create a Student object
    student = Student("Alice", ["CIS301", "MATH101"], "3.8")

    # Print the Student object (calls __str__ method)
    print(student)

    # Call the says() method
    print(student.says())