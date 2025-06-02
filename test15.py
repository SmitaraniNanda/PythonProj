# 1. Variables and Data Types
name = "Alice"
age = 25
height = 5.4
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# 2. Input and Output
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 3. Conditional Statements
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 4. Loops
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

n = int(input("Enter a number to print even numbers up to: "))
i = 2
while i <= n:
    print(i)
    i += 2

# 5. Functions
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Factorial of 5:", factorial(5))
print("Is 7 prime?", is_prime(7))

# 6. Lists and Loops
numbers = [1, 2, 3, 4, 5]
print("Squares of numbers:")
for num in numbers:
    print(num ** 2)

print("Max:", max(numbers))
print("Min:", min(numbers))

# 7. Strings
s = "madam"
reversed_s = s[::-1]
print("Reversed string:", reversed_s)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in s if char in vowels)
print("Vowel count:", vowel_count)

print("Is palindrome:", s == reversed_s)

# 8. Dictionaries
students = {"Alice": 90, "Bob": 85}
print("Students:", students)

# Add
students["Charlie"] = 88
# Update
students["Bob"] = 92
# Delete
del students["Alice"]

print("Updated students:", students)

# 9. List Comprehension
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

# 1: Calculator
print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", a + b)
elif operation == "-":
    print("Result:", a - b)
elif operation == "*":
    print("Result:", a * b)
elif operation == "/":
    print("Result:", a / b)
else:
    print("Invalid operation")

# 2: Number Guessing Game
import random
secret_number = random.randint(1, 100)
guess = -1
while guess != secret_number:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")

# 3: To-Do List CLI App
todo_list = []
while True:
    action = input("Choose: add/view/remove/exit: ").strip().lower()
    if action == "add":
        task = input("Enter task: ")
        todo_list.append(task)
    elif action == "view":
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    elif action == "remove":
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list.pop(index)
        else:
            print("Invalid index")
    elif action == "exit":
        break
    else:
        print("Unknown command")

# 4: Basic Contact Book
contacts = {}
while True:
    action = input("Choose: add/view/exit: ").strip().lower()
    if action == "add":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif action == "view":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif action == "exit":
        break
    else:
        print("Unknown command")
