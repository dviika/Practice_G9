class Human:
    def __init__(self, age): #initialize global variable of the class Human
        self.age = age
        self.favorite_drink = 'beer'

    def drink(self):
        if self.age < 18:
            self.favorite_drink = 'juice'
        print("Favorite drink: ", self.favorite_drink)
        print(f"{type(self).__name__} likes drink {self.favorite_drink}")


class Worker(Human):
    def __init__(self, age, salary):
        super().__init__(age) #classWorker doesn't have age we accesing age of Parent class by super().__init___(age)
        self.salary = salary
        if salary > 1000:
            self.favorite_drink = "whiskey"


Bob = Human(age=18)
Bob.drink()

Josh = Worker(age=35, salary=1200)
Josh.drink()
