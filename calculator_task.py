# Functions - Calculator Task

# Add

def add(num1, num2) -> int:   # currently works only for integers
    return int(num1) + int(num2)
# print(add(2, 3)) # prints 5

# Subtract

def subtract(num1, num2) -> int:
    return int(num1) - int(num2)
# print(subtract(4, 2)) # prints 2

# Multiply

def multiply(num1, num2) -> int:
    return int(num1) * int(num2)
# print(multiply(3, 4)) # prints 12

# Divide

def divide(num1, num2) -> float:
    if int(num2) == 0:
        return "Cannot divide by 0"
    else:
        return int(num1) / int(num2)
# print(divide(6, 2)) # prints 3.0

# Main calculator body
# def calculator():
#     num1 = input("Pick a number: ")
#     num2 = input("Pick a second number: ")
#     operation = input("Hello! What would you like to do? (+, -, *, /): ")
#     if operation == '+':
#         return add(num1, num2)
#     elif operation == '-':
#         return subtract(num1, num2)
#     elif operation == '*':
#         return multiply(num1, num2)
#     elif operation == '/':
#         return divide(num1, num2)
#     else:
#         return "You have not selected a valid arithmetic operator. Please try again."
#
# print(calculator())

def calc():      # includes a while loop that will continue to loop if the user doesn't input appropriate values
    while True:
        num1 = input("Pick a whole number: ")   # because the calculater only works for int data types at the moment
        if num1.isdigit():
            num2 = input("Pick a second whole number: ")   # because the calculator only works for int data types at the moment
            if num2.isdigit():
                operator = input("Please choose an operation to perform (+, -, *, /): ")
                if operator == '+':            # user must choose operator as instructed in the prompt
                    return add(num1, num2)     # if, elif statements determine if a valid operator is selected
                elif operator == '-':          # then calls corresponding function
                    return subtract(num1, num2)
                elif operator == '*':
                    return multiply(num1, num2)
                elif operator == '/':
                    return divide(num1, num2)
                else:
                    print("Please select a valid operator")  # restart the loop
            else:
                print("The value you've entered is invalid, please try again.") # restart the loop
        else:
            print("The value you entered is invalid, please try again.")   # restart the loop
print(calc())