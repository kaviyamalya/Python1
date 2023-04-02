##swap two numbers without using temporary variable

a = 24
b = 60


print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b


print("a =", a)
print("b =", b)
