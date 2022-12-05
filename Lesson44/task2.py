def recursive_max(l):
    for i in l:
        if l[i] >= l[i+1]:
            return l[i]
        return l[i+1] >= l[i+1+1]

source = [2, 1, 0, 5, 7, 6, 4, 3]
print(recursive_max(source))
assert recursive_max(source) == 7