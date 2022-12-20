<<<<<<< HEAD
from datetime import time
from time import sleep

class Auto:

    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

class Truck(Auto):

    def max_load(self):
        print("Attention!")
        super().move()

    def load(self):
        sleep(1)
        print("load")
        sleep(1)

class Car(Auto):
    def max_speed(self, max_speed):
        self.max_speed = max_speed
        print(f"max_speed is {max_speed}")
        super().move()

truck1 = Truck("Volvo", 12, "red", "New", 14)
car1 = Car("Chevrolet", 7, "Blue", "S7", 5)
print(truck1.color)
print(truck1.max_load())
print(truck1.load())
print(car1.max_speed(180))
=======
from datetime import time
from time import sleep

class Auto:

    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

class Truck(Auto):

    def max_load(self):
        print("Attention!")
        super().move()

    def load(self):
        sleep(1)
        print("load")
        sleep(1)

class Car(Auto):
    def max_speed(self, max_speed):
        self.max_speed = max_speed
        print(f"max_speed is {max_speed}")
        super().move()

truck1 = Truck("Volvo", 12, "red", "New", 14)
car1 = Car("Chevrolet", 7, "Blue", "S7", 5)
print(truck1.color)
print(truck1.max_load())
print(truck1.load())
print(car1.max_speed(180))
>>>>>>> fe4f1a3b7f0868cb0bf7fbcf3c3a018c06fa18a0
