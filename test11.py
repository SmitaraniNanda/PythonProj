# 1. Match Statement – Day of the Week
day = int(input("Enter a number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# 2. For Loop – Multiplication Table
number = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# 3. While Loop – Number Guessing Game
import random
secret_number = random.randint(1, 100)
number = 1
attempts = 0
while number != secret_number:
    number = int(input("Guess the number (1-100): "))
    attempts += 1
    if number < secret_number:
        print("Too low!")
    elif number > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")

# 4. Function – Prime Number Checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 and 100:")
primes = [str(i) for i in range(1, 101) if is_prime(i)]
print(", ".join(primes))

# 5. Lambda – Sorting a List of Tuples
people = [("Smita", 30), ("Mamali", 25), ("Puspa", 35)]
people.sort(key=lambda x: x[1])
print("Sorted by age:", people)

# 6. Arrays – Reverse an Array
original_array = [1, 2, 3, 4, 5]
reversed_array = original_array[::-1]
print("Reversed array:", reversed_array)

# 7. Class and Object – Bank Account
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

account = BankAccount()
account.deposit(2000)
account.withdraw(500)
account.check_balance()

# 8. For Loop – Fibonacci Series
n = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
print("Fibonacci series:", end=" ")
for _ in range(n):
    print(a, end=", " if _ < n - 1 else "\n")
    a, b = b, a + b

# 9. While Loop – Factorial Calculation
number = int(input("Enter a number to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"Factorial of {number} is {factorial}")

# 10. Function – Palindrome Checker
def is_palindrome(s):
    return s == s[::-1]

strings_check = ["radar", "hello", "level", "world", "madam"]
for s in strings_check:
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
