class Student:
    def __init__(self, name, age, degree, year):
        self.name = name
        self.age = age
        self.degree = degree
        self.year = year

    def is_diss_year(self):
        if(self.year == 4):
            print("This student is required to do a disseration this year")
        else:
            print("This student does not have to do a dissertation this year")