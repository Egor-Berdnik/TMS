a, b, c, d = input("Введите 4 строки: 1. "), input("2: "), input("3: "), input("4: ")
print(a, b, c, d)
f.write(a + "\n")
f.write(b + "\n")
f.close()
f = open("Homework.txt.", "a")
f.write(c + "\n")
f.write(d + "\n")

a, b, c, d = input("Введите 4 строки: 1. "), input("2: "), input("3: "), input("4: ")
with open("Homework.txt.", "w") as f:
    print(a, b, c, d)
    f.write(a + "\n")
    f.write(b + "\n")
    f.close()
with open("Homework.txt.", "a") as f:
    f.write(c + "\n")
    f.write(d + "\n")