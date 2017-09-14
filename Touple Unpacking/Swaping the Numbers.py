numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
print("+++++++++++++")
# This can be also used to swap variables by doing a, b = b, a ,
# since b, a on the right hand side forms the tuple (b, a) which is then unpacked.
a, b = b, a
print(a)
print(b)
print(c)