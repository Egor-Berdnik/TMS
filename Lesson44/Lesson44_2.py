n = int(input("Введите целое число: "))
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(fact(n))