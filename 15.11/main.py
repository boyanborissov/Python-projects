#1
class Person:
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def print_name(self):
        self.fullname = self.first_name + " " + self.last_name
        print("My name is " + self.fullname)

    def print_nationality(self):
        print("My nationality is " + self.nationality + "\n")

#2
class Student(Person):
    def __init__(self, first_name, last_name, age, nationality, university, yearsofstudy):
        super().__init__(first_name, last_name, age, nationality)
        self.university = university
        self.yearsofstudy = yearsofstudy

    def goodmorning (self):
        self.fullname = self.first_name + " " + self.last_name
        print("My name is " + self.fullname)

    def print_nationality(self):
        print("My nationality is " + self.nationality)

    def print_university(self):
        print("My university is " + self.university + "")

    def print_yearsofstudy(self):
        print("My years of study are " + str(self.yearsofstudy) + "\n")
#3
class Lecturer(Student):
    def __init__(self, first_name, last_name, age, nationality, university, yearsofstudy, experience):
        super().__init__(first_name, last_name, age, nationality, university, yearsofstudy)
        self.experience = experience

    def goodmorning (self):
        self.fullname = self.first_name + " " + self.last_name
        print("My name is " + self.fullname)

    def print_nationality(self):
        print("My nationality is " + self.nationality)

    def print_university(self):
        print("My university is " + self.university + "")

    def print_yearsofstudy(self):
        print("My years of study are " + str(self.yearsofstudy))

    def print_experience(self):
        print("My experience are " + str(self.experience) + "\n")

YourPerson = Lecturer("Dimiie", "Dimitrov", 18, "bulgarian", "TU SOFIA", 1, 12)
YourPerson2 = Lecturer("Vesko", "Atanasov", 17, "evrein", "Nov Bulgarski", 1, 10)
YourPerson3 = Lecturer("Milko", "Kotlarov", 18, "bulgarian", "TU SOFIA", 2, 9)

YourPerson.goodmorning()
YourPerson.print_nationality()
YourPerson.print_university()
YourPerson.print_yearsofstudy()
YourPerson.print_experience()

YourPerson2.print_name()
YourPerson2.print_nationality()
YourPerson2.print_university()
YourPerson2.print_yearsofstudy()
YourPerson2.print_experience()

YourPerson3.print_name()
YourPerson3.print_nationality()
YourPerson3.print_university()
YourPerson3.print_yearsofstudy()
YourPerson3.print_experience()
