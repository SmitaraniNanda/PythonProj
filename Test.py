# Global variable
a = 10
b = 20

def add_numbers():
    # Local variables
    x = 5
    y = 15
    sum_local = x + y
    sum_global = a + b

    print("Sum of local variables:", sum_local)
    print("Sum of global variables:", sum_global)

# Calling the function
add_numbers()
