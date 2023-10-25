#Task create class Human in which define a method drink. During initializqation we accept age
#Create class vsriable favorite drink = 'beer'
#Create class Worket inherited from base Human and adding salary

#Tasks
#method drink -> should print name of the class and add
class Human:
    favorite_drink = 'beer'

    def __init__(self, age):  # initialize global variable of the class Human
        self.age = age
        if self.age < 18:
            self.favorite_drink = 'juice'

    def drink(self):
        print(f"{self.__class__.__name__} likes drink {self.favorite_drink}")


class Worker(Human):
    def __init__(self, age, salary):
        super().__init__(age)  # classWorker doesn't have age we accesing age of Parent class by super().__init___(age)
        self.salary = salary
        if salary > 1000:
            self.favorite_drink = "whiskey"


Bob = Human(age=18)
Bob.drink()

Josh = Worker(age=35, salary=1200)
Josh.drink()

print(Human.favorite_drink)
print(Human(18).favorite_drink)
