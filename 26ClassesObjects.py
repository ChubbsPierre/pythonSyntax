from student import Student

student1 = Student("Mark", 23, "Comp Sci", True)

print("Student 1 is " + student1.name)

student1.__setattr__("age", 25)

print("Student 1 is " + str(student1.age))