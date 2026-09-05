"""A small example of classes, objects, and instance methods."""

class Student:
    """Store a student's details and calculate their average marks."""

    school_name = "Green Valley High School"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, "
              f"Average: {self.average_marks():.1f}, School: {self.school_name}")


student1 = Student("Aarav", 20, [85, 90, 78])
student2 = Student("Isha", 21, [55, 60, 40])

student1.display_info()
student2.display_info()

print("\nBoth students belong to:", student1.school_name, "and", student2.school_name)

# Changing one object does not change the other.
student1.age = 22
print(f"\n{student1.name}'s new age: {student1.age}")
print(f"{student2.name}'s age is unchanged: {student2.age}")

print("\nType of student1:", type(student1))
print("Is student1 a Student?", isinstance(student1, Student))
