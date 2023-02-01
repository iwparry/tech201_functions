# Functions - Calculator Task

# Add

def add(num1: int, num2: int) -> int:
    return num1 + num2
print(add(2, 3)) # prints 5

# Subtract

def subtract(num1: int, num2: int) -> int:
    return num1 - num2
print(subtract(4, 2)) # prints 2

# Multiply

def multiply(num1: int, num2: int) -> int:
    return num1 * num2
print(multiply(3, 4)) # prints 12

# Divide

def divide(num1: int, num2: int) -> float:
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        return num1 / num2
print(divide(6, 2)) # prints 3.0

