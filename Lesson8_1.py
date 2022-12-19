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

auto = Auto("Chevrolet", 7, "Blue", "S7", 5.7)
print(auto.brand)
print(auto.age)

