a = list(range(1, 21))
print(a)
b = int(input("Введите число от 1 до 20: "))
print(b)
mid = len(a) // 2
low = 0
high = len(a) - 1
while a[mid] != b and low <= high:
    if b > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)
