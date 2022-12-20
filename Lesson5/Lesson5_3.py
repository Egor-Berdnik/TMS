tup = ("дама", "мадам", "ель", "шалаш")
res = filter(lambda x: x[0] == x[-1], tup)
print(tuple(res))
