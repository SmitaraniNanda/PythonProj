#1)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


s = "Python Programming"
substring = s[7:]  # Start from index 7 to the end
print(substring)


s = "Equilar"
upper = s.upper()
lower = s.lower()
print(upper)
print(lower)


s1 = "1234"
s2 = "12a3"

print(s1.isdigit())
print(s2.isdigit())

#2)
a = 10
b = 5
add = a + b
subtract = a - b
multiply = a * b
divide = a / b
print(add, subtract, multiply, divide)


n = 4
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


radius = 5
pi = 3.14
area = pi * radius ** 2
print("Area =", area)


value = 3.14159
rounded = round(value, 2)
print(rounded)



# Convert "123" to int
s = "123"
num = int(s)
print(num)  # Output: 123


# Convert 45 to string
n = 45
s = str(n)
print(s)  # Output: "45"


# Convert "3.14" to float
s = "3.14"
f = float(s)
print(f)  # Output: 3.14


#3)
num = 5
str_num = "10"
# Convert string to integer
result = num + int(str_num)
print(result)


str1 = "4"
str2 = "5"
# Convert both to integers
product = int(str1) * int(str2)
print(product)  


num = 9.81
converted = int(num)
print(converted)  # O/p: 9 (decimal part is truncated)


# Booleans to Integers
print(int(True))   # O/p: 1
print(int(False))  # O/p: 0

# Integers to Booleans
print(bool(1))     # O/p: True
print(bool(0))     # O/p: False
























































