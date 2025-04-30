a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # (same object)
print(a is c)  # (same content, different object)
print(a == c)  # (same values)
