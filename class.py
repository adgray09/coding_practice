class Person(object):
    def __init__(self, person_name):
        self.name = person_name

    def say_hello(self):
        print("Hello my name is {}!".format(self.name))

Alex = Person("alex")
Alex.say_hello()

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

        self.courses = []

    def add_courses(self, course):
        self.courses.append(course)
    def get_courses(self):
        count = len(self.courses)
        print(f"I am taking {count} courses:")
        for course in self.courses:
            print(f" - {course}")

Richard = Student("richard")
Richard.say_hello()
Richard.add_courses("Linear Algebra")
Richard.add_courses("CS 1.1")
Richard.add_courses("BEW 1.1")
Richard.get_courses()

class Animal():
    def __init__ (self, species_name, animal_name):
        self.animal = species_name
        self.name = animal_name

    def say_species(self):
        print("My name is {} and I am a {}".format(self.name, self.animal))

terry = Animal("Tiger", "Terry")

terry.say_species()








