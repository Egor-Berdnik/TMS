a = b'r\xc3\xa9sum\xc3\xa9'
b = a.decode("utf-8")
print(b)
c = b.encode("Latin1")
print(c)
d = c.decode("utf-8")
print(d)