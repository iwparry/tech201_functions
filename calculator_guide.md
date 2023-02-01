# Tech 201 Calculator Task Guide

### Tasks
Create simple functions for arithmetic operations on a calculator

### Creating the Functions for our Arithmetic Operators
We start by defining our first function which we'll call `add`.
```python
def add(num1, num2) -> int:   # currently works only for integers
    return int(num1) + int(num2)
print(add(2, 3)) # prints 5
```
What I want this function to do is to take two integer numbers `num1` and `num2`, which will be given as arguments, and add them together and return the result.
When I run the function for 2 and 3, for example, 5 is printed to our console.

I have done the same for all the other operations

Subtract
```python
def subtract(num1, num2) -> int:
    return int(num1) - int(num2)
print(subtract(4, 2)) # prints 2
```
Multiply
```python
def multiply(num1, num2) -> int:
    return int(num1) * int(num2)
print(multiply(3, 4)) # prints 12
```
And Divide
```python
def divide(num1, num2) -> float:
    if int(num2) == 0:
        return "Cannot divide by 0"
    else:
        return int(num1) / int(num2)
print(divide(6, 2)) # prints 3.0
```
Note with `divide` that I have included an if statement for the case that `num2` is 0, we cannot divide by 0, thus I've instructed Python to run the code as above in the case that our `divide` function is called with 0 as our second number in its arguments.
### Adding the main body of our Calculator
Now that all our operation functions have been created we now move on to creating the main body of our calculator. We want to make our calculator in a way so that it may accept user input, and to keep it simple we will only ask the user for two numbers, and an operation to be performed as shown here
```python
def calculator():
    num1 = input("Pick a number: ")
    num2 = input("Pick a second number: ")
    operation = input("Hello! What would you like to do? (+, -, *, /): ")
```
So when we first call our calculator the user should receive the 3 prompts shown above, and note in the operation prompt we show the available options to the user to avoid any confusion. What follows is a simple control flow of `if`, `elif` and `else` statements as shown in our full calculator body here
```python
def calculator():
    num1 = input("Pick a number: ")
    num2 = input("Pick a second number: ")
    operation = input("Hello! What would you like to do? (+, -, *, /): ")
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        return "You have not selected a valid arithmetic operator. Please try again."

print(calculator())
```
When our program is run now the user will be faced with the prompts we mentioned a little earlier, and once the user has provided their input the program will run through the conditions of the `if`, `elif` and `else` statements as required, and will execute the appropriate function (one of the functions we defined earlier), assuming the user has provided an appropriate value for `operation`.