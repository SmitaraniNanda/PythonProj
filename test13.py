import importlib
import types

print("\n 1. Custom Module (math_utils) ")


class math_utils:
    def add(a, b): return a + b
    def sub(a, b): return a - b
    def mul(a, b): return a * b
    def div(a, b): return a / b

print("add:", math_utils.add(3, 4))
print("sub:", math_utils.sub(10, 5))
print("mul:", math_utils.mul(2, 3))
print("div:", math_utils.div(8, 2))


print("\n 2. Package basics with __init__.py ")

def area_circle(radius):
    return 3.14 * radius * radius

def area_rectangle(w, h):
    return w * h

from __main__ import area_circle
print("area_circle:", area_circle(5))


print("\n 3. __name__ == '__main__' demo ")

def cli_main():
    import sys
    if len(sys.argv) == 4:
        a, b, op = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
        operations = {
            'add': math_utils.add,
            'sub': math_utils.sub,
            'mul': math_utils.mul,
            'div': math_utils.div
        }
        if op in operations:
            print("CLI Result:", operations[op](a, b))
        else:
            print("Invalid operation")

# Uncomment to enable CLI behavior
# if __name__ == "__main__":
#     cli_main()


print("\n 4. Module-level vs Function-level Scope ")

# Global list
my_list = [1, 2, 3]

def mutate_list():
    my_list.append(4)
    print("Inside function (list):", my_list)

mutate_list()
print("Outside function (list):", my_list)

# Global int
count = 0

def mutate_count():
    global count
    count += 1
    print("Inside function (count):", count)

mutate_count()
print("Outside function (count):", count)


print("\n 5. nonlocal keyword practice")

def outer():
    x = "original"
    def inner():
        nonlocal x
        print("Before change:", x)
        x = "modified"
        print("After change:", x)
    inner()
    print("In outer after inner:", x)

outer()


print("\n 6. Circular Import Pitfall (Simulated) ")

# Simulate circular import issue (commented out to prevent crash)
# module_a.py
# from module_b import func_b
# def func_a(): func_b()

# module_b.py
# from module_a import func_a
# def func_b(): func_a()

print("Circular imports cause ImportError if both are run on import. Fix by delaying imports or restructuring.")

print("\n 7. Dynamic Imports with importlib ")

# Simulate dynamic module
module_name = 'math_utils'
module = types.SimpleNamespace()
setattr(module, 'known_function', lambda: "I am loaded dynamically!")
print("Dynamically loaded:", module.known_function())


print("\n 8. Private vs Public Names ")

def _helper():
    return "I am private"

def public():
    return "I am public"

__all__ = ['public']

print("from module import * exposes:", __all__)
print("public():", public())
print("_helper():", _helper())


print("\n 9. Reloading a Module  ")

fake_module = types.SimpleNamespace(msg="Old Value")
print("Before reload:", fake_module.msg)
fake_module.msg = "New Value"
# importlib.reload(fake_module)  # would reload in real script
print("After 'reload':", fake_module.msg)


print("\n10. Package-wide state with Singleton pattern ")

class Logger:
    _instance = None


    def __new__(cls, level='INFO'):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.level = level
        return cls._instance

# Shared state
logger1 = Logger()
logger2 = Logger()
logger1.level = "DEBUG"
print("Logger1 Level:", logger1.level)
print("Logger2 Level (same instance):", logger2.level)


