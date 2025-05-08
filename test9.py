# Arithmetic Operators
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
print(f"Area of rectangle: {area}")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average: {average}")

# Comparison Operators
a = float(input("Enter first number to compare: "))
b = float(input("Enter second number to compare: "))
if a > b:
    print("First number is greater.")
elif a < b:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Logical Operators
number = int(input("Enter a number to check if it's in range (10, 50): "))
if number > 10 and number < 50:
    print("Number is within range.")
else:
    print("Number is out of range.")

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid credentials.")

# Assignment Operators
x = 10
print(f"Initial value: {x}")
x += 5
print(f"After += 5: {x}")
x -= 3
print(f"After -= 3: {x}")
x *= 2
print(f"After *= 2: {x}")
x /= 4
print(f"After /= 4: {x}")

# Bitwise Operators
x = 5  # 0b0101
y = 3  # 0b0011
print(f"5 & 3 = {x & y}")
print(f"5 | 3 = {x | y}")
print(f"5 ^ 3 = {x ^ y}")



# Python Lists Tasks
# 1. List Creation & Access
movies = ["Inception", "Shutter Island", "Interstellar", "The Matrix", "Gladiator"]
print(f"First movie: {movies[0]}")
print(f"Last movie: {movies[-1]}")

# 2. List Modification
movies.append("The Dark Knight")
movies[2] = "The Prestige"
print(f"Modified list: {movies}")

# 3. List Methods
sample_list = ["banana", "apple", "cherry"]
sample_list.sort()
print(f"Sorted list: {sample_list}")
sample_list.append("date")
print(f"After append: {sample_list}")
sample_list.insert(1, "blueberry")
print(f"After insert: {sample_list}")
sample_list.remove("apple")
print(f"After remove: {sample_list}")
sample_list.pop()
print(f"After pop: {sample_list}")
sample_list.reverse()
print(f"After reverse: {sample_list}")

# 4. List Iteration
print("All movies:")
for movie in movies:
    print(movie)

print("Movies starting with 'S':")
for movie in movies:
    if movie.startswith("S"):
        print(movie)

# 5. List Comprehension
squares = [z**2 for z in range(1, 11)]
print(f"Squares from 1 to 10: {squares}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [z for z in numbers if z % 2 == 0]
print(f"Even numbers: {even_numbers}")
