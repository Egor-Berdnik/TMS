# def list_1(m1, m2, amount, l):
#     from random import randint
#     for i in range(amount):
#         l.append(randint(m1, m2))

list_1 = [1, 2, 3, 4, 5, 2, 4, 3, 4, 5, 4, 5]
def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
analysis()


# a = []
# b = {}
# analysis(a, b)
# for x in b:
#     print(analysis(x, b[x]))

# lst = []
# dct = {}

# mn = int(input('Минимум: '))
# mx = int(input('Максимум: '))
# qty = int(input('Количество элементов: '))

# list_1(mn, mx, qty, lst)
# analysis(lst, dct)
#
# for item in sorted(dct):
#     print("'%d':%d" % (item, dct[item]))