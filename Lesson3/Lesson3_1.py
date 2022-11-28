# # 1
# a, b = input("Введите предложение из 2 слов: ").split()
# print("!", b, " ! ", a, "!")
#
# a, b = input("Введите предложение из 2 слов: ").split()
# x = '! {}, ! {}, !'.format(b, a)
# print(x)
#
# a, b = input("Введите предложение из 2 слов: ").split()
# x = f'"!", {b}, " ! ", {a}, "!"'
# print(x)

from random import randint

# 2
# n = input("Введите Ваше имя: ")
# ag = int(input("Введите Ваш возраст: ")) #isdigit / exception
# if ag <= 0: # if not age.isdigit
#     print("Ошибка повторите ввод")
# elif 0 < ag < 10:
#     print("Привет, шкет", n)
# elif 10 < ag < 18:
#     print("Как жизнь, ", n)
# elif 18 < ag < 100:
#     print("Что желаете, ", n)
# else:
#     print(n, ", Вы лжете! В наше время столько не живут ...")

# 3
# n = input("Введите Ваше имя: ")
# ag = int(input("Введите Ваш возраст: "))
# while True:
#     if ag <= 0:
#         print("Ошибка повторите ввод !!")
#     elif ag > 0 and ag < 10:
#         print("Привет, шкет", n)
#     elif ag >= 10 and ag < 18:
#         print("Как жизнь, ", n)
#     elif ag >=18 and ag < 100:
#         print("Что желаете, ", n)
#     else:
#         print(n, ", Вы лжете! В наше время столько не живут ...")

# 4
# n = int(input("Введите число: "))
# i = 1
# res = 0
# while i <= n:
#     new += i ** 3
# print(new)
#
# t = sum([])
#
# n = int(input("Введите число: "))
# i = range(1, n+1)
# for x in i:
#     print(x ** 3)
# else:
#     print("Операция завершена.")

# 5
while True:                                         #x != i: print ввкдите число
    i = randint(1, 10)
    x = int(input("Введите число до 10: "))
    if x == i:
        print("Вы угадали!")
    else:
        print("Неудача, попробуйте еще раз.")