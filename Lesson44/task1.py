def recursive_reverse(l):
    if len(l) == 0:
        return
    for i in l:
        return l[-i-1] in l

source = [1, 2, 3, 4, 5]
print(recursive_reverse(source))