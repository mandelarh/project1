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
        self.name = name
        self.classes = classes
        self.gpa = gpa

    def says(self):
        """
            All students say "This class is too much work".
        Returns:
            a String statement that says "This class is too much work".
        """
        #raise NotImplementedError('not implemented yet')
        return "This class is too much work"

    def __str__(self):
        """
        Returns:
            a String that describes this Student.
        """
        #raise NotImplementedError('not implemented yet')
        return (f"{self.name} has a GPA of {self.gpa} and is taking {len(self.classes)} classes: {self.classes} {self.name}"
                f"says {self.says}")


class Studentdef:
    pass