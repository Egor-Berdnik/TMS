dict_1 = {
  "k1": 1,
  "k2": 2,
  "k3": 3,
  "k4": 4,
  "k5": 5
}
dict_2 = {a: b for b, a in dict_1.items()}
print(dict_2)