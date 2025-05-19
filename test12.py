# inheritance  and polymorphism iterators

import math
from abc import ABC, abstractmethod

# 1. Employee Hierarchy

class Employee:
    def calculate_bonus(self):
        return 0

class Manager(Employee):
    def calculate_bonus(self):
        return 800

class Developer(Employee):
    def calculate_bonus(self):
        return 500

class Intern(Employee):
    def calculate_bonus(self):
        return 200

print("1. Employee Hierarchy")
employees = [Manager(), Developer(), Intern()]
for emp in employees:
    print(f"{emp.__class__.__name__} Bonus: {emp.calculate_bonus()}")
print("\n")

# 2. Vehicle Fleet

class Vehicle:
    def get_max_speed(self):
        return 0

    def print_info(self):
        print(f"{self.__class__.__name__} max speed: {super().get_max_speed()} km/h")

class Car(Vehicle):
    def get_max_speed(self):
        return 180

class Truck(Vehicle):
    def get_max_speed(self):
        return 120

class Motorcycle(Vehicle):
    def get_max_speed(self):
        return 160

print("2. Vehicle Fleet")
vehicles = [Car(), Truck(), Motorcycle()]
for v in vehicles:
    print(f"{v.__class__.__name__} max speed: {v.get_max_speed()}")
print("\n")

# 3. Shape Area Calculator

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

print("3. Shape Area Calculator")
shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
print("\n")

# 4. Notification System

class Notification:
    def send_notification(self):
        raise NotImplementedError

class EmailNotification(Notification):
    def send_notification(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send_notification(self):
        print("Sending SMS Notification")

class PushNotification(Notification):
    def send_notification(self):
        print("Sending Push Notification")

def notify_all(notifications):
    for n in notifications:
        n.send_notification()

print("4. Notification System")
notify_all([EmailNotification(), SMSNotification(), PushNotification()])
print("\n")

# 5. Payment Gateway

class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} via PayPal.")

class CryptoCurrency(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in CryptoCurrency.")

def checkout(payment_method, amount):
    payment_method.pay(amount)

print("5. Payment Gateway")
checkout(PayPal(), 100)
checkout(CreditCard(), 200)
checkout(CryptoCurrency(), 150)
print("\n")

# 6. Zoo Animal Sounds

class Animal:
    def make_sound(self):
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

print("6. Zoo Animal Sounds")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
print("\n")

# 7. Custom Range Generator

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

print("7. Custom Range Generator")
for i in MyRange(1, 5):
    print(i)
print("\n")

# 8. Fibonacci Sequence Iterator

class Fibonacci:
    def __init__(self, limit):
        self.a, self.b = 0, 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

print("8. Fibonacci Sequence Iterator")
for num in Fibonacci(50):
    print(num)
print("\n")


# 9. Reverse String Iterator

class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.text[self.index]

print("9. Reverse String Iterator")
for ch in ReverseString("hello"):
    print(ch)
print("\n")

