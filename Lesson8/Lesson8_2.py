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
        return "move"

    def stop(self):
        return "stop"

    def birthday(self):
        return self.age + 1

class Truck(Auto):

    def max_load(self):
        return "Attention!"
        super().move()

    def load(self):
        sleep(1)
        return "load"
        sleep(1)

class Car(Auto):
    def max_speed(self, max_speed):
        self.max_speed = max_speed
        return f"max_speed is {max_speed}"
        super().move()

truck1 = Truck("Volvo", 12, "red", "New", 14)
car1 = Car("Chevrolet", 7, "Blue", "S7", 5)
print(truck1.color)
print(truck1.max_load())
print(truck1.load)
print(car1.max_speed(180))