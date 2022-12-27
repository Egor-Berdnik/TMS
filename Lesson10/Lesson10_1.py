import traceback

x = float(input("x = "))
y = float(input("y = "))
what = input("Выберите операцию: ")

if what == "+":
    res = x + y
    print(f'Сумма равна {res}')

if what == "/":
    try:
        res = x / y
        print(f'Разность равна {res}')
    except ZeroDivisionError as err:
        traceback.print_exception(err)