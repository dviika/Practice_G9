from abc import ABC, abstractclassmethod, abstractmethod

class Human:
    sex = 'man'
    age = 18
    name = 'Body'

    def print_age(self):
        print(self.age)



class Student(Human):
    age = 21
    faculty = 'IT'

human0 = Human()
student0 = Student() #item of class
student0.age = 19
student1 = Student() #item of class

# print(human0.age)
human0.print_age()
print(student0.faculty)
print(student1.age)

class AbstractHuman(ABC):
    @abstractmethod
    def walk(self):
        print('I am walking')

    @abstractmethod
    def speech(self):
        print('I am speaking')

class RealHuman(AbstractHuman):
    def walk(self):
        print('I am walking')

    def speech(self):
        print('I am speaking')

real_human_1 = RealHuman()
real_human_1.walk()
real_human_1.speech()

    # human2 = AbstractHuman()
    # human2.func()
