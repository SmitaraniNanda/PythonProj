# 1. Operators + Lists + Functions
def element_wise_sum(list1, list2):
    max_len = max(len(list1), len(list2))
    list1 += [0] * (max_len - len(list1))
    list2 += [0] * (max_len - len(list2))
    return [list1[i] + list2[i] for i in range(max_len)]

print("1:", element_wise_sum([1, 2, 3], [4, 5]))


# 2. Tuples + Dictionaries + If-Else
def scores_above_threshold(data, threshold):
    score_dict = {name: score for name, score in data}
    print("2: Students above threshold:")
    for name, score in score_dict.items():
        if score > threshold:
            print(name)

scores_above_threshold([("Smita", 85), ("Mamali", 60), ("Puspa", 95)], 70)


# 3. Sets + For Loop + Lambda
def unique_sorted_squares(nums):
    unique_nums = set(nums)
    return sorted([x**2 for x in unique_nums], key=lambda x: x)

print("3:", unique_sorted_squares([1, 2, 2, 3, 4, 4]))


# 4. While Loop + Match
def command_line_interface():
    items = []
    while True:
        command = input("Enter a command (add, remove, print, exit): ")
        match command:
            case "add":
                item = input("Enter item to add: ")
                items.append(item)
            case "remove":
                item = input("Enter item to remove: ")
                if item in items:
                    items.remove(item)
            case "print":
                print(items)
            case "exit":
                break
            case _:
                print("Unknown command.")

print("4: To run the interactive interface, call command_line_interface()")


# 5. Class + Object + Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display(self):
        super().display()
        print(f"Number of doors: {self.num_doors}")

print("5:")
v = Vehicle("Toyota", "Corolla")
v.display()
c = Car("Honda", "Civic", 4)
c.display()


# 6. Polymorphism + Functions
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    print(animal.sound())

print("6:")
animal_sound(Dog())
animal_sound(Cat())


# 7. Iterators + For Loop
class EvenIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current

print("7: Even numbers up to 10:")
for num in EvenIterator(10):
    print(num, end=' ')
print()


# 8. Modules + Scope
# factorial function (can be assumed from a module)
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("8: Factorial of 5 is", factorial(5))

local_var = "I am local"
global_var = "I am global"

def scope_test():
    local_var = "Changed locally"
    print("Inside function:", local_var)

scope_test()
print("Outside function:", local_var)


# 9. Dictionaries + List Comprehension + If-Else
def label_salaries(salaries):
    return {name: ('High' if salary > 100000 else 'Low') for name, salary in salaries.items()}

salaries = {"Smita": 120000, "Mamali": 80000, "Puspa": 105000}
print("9:", label_salaries(salaries))


# 10. Lambda + Filter + Map + Reduce
from functools import reduce

def process_numbers(nums):
    odds = filter(lambda x: x % 2 == 1, nums)
    squares = map(lambda x: x ** 2, odds)
    total = reduce(lambda x, y: x + y, squares)
    return total

print("10:", process_numbers([1, 2, 3, 4, 5]))
