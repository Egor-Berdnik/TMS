my_list = list(range(1, 51))
result = [my_list[-x-1] for x in range(len(my_list))]
print(result)