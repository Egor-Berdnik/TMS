my_list = list(range(1, 101))
result = [x for x in my_list if x % 10 == 0]
result1 = [x*10 if x % 4 != 0 else x*2 for x in result]
print(result1)