# 1
a = 1
b = a
c = b

# 2
d = 2
e = str(2)

# 3
a = 1
b = float(a)
c = str(b)

# 4
t = input("Введите произвольную строку: ")
x = (t[::2])
y = (t[1::2])
print("Введена строка", t, "\n\n")
print(x, y, sep="     ")
print("\n", "!!!")