b_first = int(input('Введите первый элемент прогрессии: '))
n = int(input('Введите число элементов прогрессии: '))
print(b_first)
b_prev = b_first
for i in range(1, n):
    b_cur = b_prev * b_first
    print(b_cur)
    b_prev = b_cur
