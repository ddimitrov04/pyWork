class Person:
    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.nationality)


class Student(Person):
    def __init__(self, first_name, last_name, age, nationality, university, yearOfStudy):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.yearOfStudy = yearOfStudy

    def print(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.nationality)
        print(self.university)
        print(self.yearOfStudy)

class Lecturer(Person):
    def __init__(self, first_name, last_name, age, nationality, university, experience):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        print(self.first_name)
        print(self.last_name)
        print(f"Age: {self.age}" )
        print(self.nationality)
        print(self.university)
        print("Years of experience: " + str(self.experience))


p1 = Person("John", "Wick", 32, "Bulgarian")
s1 = Student("John", "Wick", 32, "Bulgarian","UNSS",3)
l1 = Lecturer("Iliyan", "Georgiev", 24, "Turkish","UNSS",5)
p1.print()
s1.print()
l1.print()
