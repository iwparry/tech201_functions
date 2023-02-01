# Tech 201 Calculator Task Guide

### Tasks
Create simple functions for arithmetic operations on a calculator

#### Creating the Functions
We start by defining our first function which we'll call `add`.
```python
def add(num1: int, num2: int) -> int:
    return num1 + num2
print(add(2, 3)) # prints 5
```
What I want this function to do is to take two integer numbers `num1` and `num2`, which will be given as arguments, and add them together and return the result.
When I run the function for 2 and 3, for example, 5 is printed to our console.

I have done the same for all the other operations

Subtract
```python
def subtract(num1: int, num2: int) -> int:
    return num1 - num2
print(subtract(4, 2)) # prints 2
```
Multiply
```python
def multiply(num1: int, num2: int) -> int:
    return num1 * num2
print(multiply(3, 4)) # prints 12
```
And Divide
```python
def divide(num1: int, num2: int) -> float:
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        return num1 / num2
print(divide(6, 2)) # prints 3.0
```
Note with `divide` that I have included an if statement for the case that `num2` is 0, we cannot divide by 0, thus I've instructed Python to run the code as above in the case that our `divide` function is called with 0 as our second number in its arguments.