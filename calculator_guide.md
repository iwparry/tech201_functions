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
Now that all our operation functions have been created we now move on to creating the main body of our calculator.
We want to make our calculator in a way so that it may accept user input, and to keep it simple we will only ask the user for two numbers, and an operation to be performed as shown here
```python
def calc():
    num1 = input("Pick a number: ")
    num2 = input("Pick a second number: ")
    operation = input("Hello! What would you like to do? (+, -, *, /): ")
```
But we want to ensure that  appropriate values are entered at each prompt. So we add a while loop to our function to repeat the prompt until an appropriate value is provided for each prompt.
```python
def calc():      # includes a while loop that will continue to loop if the user doesn't input appropriate values
    while True:
        num1 = input("Pick a whole number: ") 
        if num1.isdigit():
            num2 = input("Pick a second whole number: ") 
            if num2.isdigit():
                operator = input("Please choose an operation to perform (+, -, *, /): ")
```

So when we first call our calculator the user should receive the 3 prompts shown above, and note in the operation prompt we show the available options to the user to avoid any confusion. What follows is a simple control flow of `if`, `elif` and `else` statements as shown in our full calculator body here
```python
def calc():      # includes a while loop that will continue to loop if the user doesn't input appropriate values
    while True:
        num1 = input("Pick a whole number: ")   
        if num1.isdigit():
            num2 = input("Pick a second whole number: ")   
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
```
When our program is run now the user will be faced with the prompts we mentioned a little earlier, and once the user has provided their input the program will run through the conditions of the `if`, `elif` and `else` statements as required, and will execute the appropriate function (one of the functions we defined earlier), assuming the user has provided an appropriate value for `num1`, `num2` and `operation`.
As we can see we have included several `else` statements to restart the loop in any case the user enters a value we don't want.