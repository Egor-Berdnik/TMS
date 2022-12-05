list_1 = [1, 2, 3, 4, 5, 2, 4, 3, 4, 5, 4, 5]
def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
            return
        else:
            your_dict[i] = 1
            return
print(analysis(list_1))