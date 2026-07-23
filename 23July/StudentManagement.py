import logging

logger = logging.getLogger("GROOT")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("Student.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Student:
    school_name = "ABC higher secondary school"
    student_count = 0

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        Student.student_count += 1

        # log student creation
        logger.info(
            f"Student Created -> Name:{self.name},Age:{self.age},Marks:{self.marks}"
        )

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            old_marks = getattr(self, "_marks", None)
            self._marks = value

            # log mark updates
            if old_marks is not None:
                logger.info(f"Marks Updated for {self.name}:{old_marks} to {value}")

        else:
            raise ValueError("Marks should be between 0 and 100")

    def display(self):
        return f"Name:{self.name} | Age:{self.age} | Marks:{self.marks}"

    @classmethod
    def change_school_name(cls, school_name):
        old_name = cls.school_name
        cls.school_name = school_name

        # log school name changes
        logger.info(f"School name Changed:{old_name} to {cls.school_name}")

    @staticmethod
    def pass_or_fail(marks):
        return "Pass" if marks >= 35 else "Fail"


# Testing Output:

s1 = Student("Madhavan", 22, 85)

print(s1.display())
# Name:Madhavan | Age:22 | Marks:85

print(Student.student_count)
# 1

print(Student.school_name)
# ABC higher secondary school

Student.change_school_name("XYZ School")
print(Student.school_name)
# XYZ School

print(Student.pass_or_fail(s1.marks))
