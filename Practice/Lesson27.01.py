# ООП
# абстрактный метод
# теория граф
# подходы к вычислению сложности алгоритвов - по времени, памяти, операций
# - линейная, квадратичная, факториальная, логарифмическая
# граф - фигура с точками и линиями
# - индекс в БД
# индексы хранятся в оперативной памяти
# индексы реализуются в хеш таблице или деревьях(В tree)


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector coords: x={self.x} y={self.y} z={self.z}"

    def __add__(self, other):
        res = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return res

    def __sub__(self, other):
        res = Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return res

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

        return Vector(int(self.x / other), int(self.y / other), int(self.z / other))

    def __matmul__(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def norm(self):
        return (self.x **2 + self.y **2 + self.z ** 2) **0.5

v1 = Vector(6, 4, 2)
v2 = Vector(1, 2, 3)
print(v1.norm())
