def my_gen(some_list):
    for i in some_list:
        res = i * i
        yield res

my_list = [1, 2, 3, 4, 5]
my_iterator = my_gen(my_list)

for i in my_iterator:
    print(i)

