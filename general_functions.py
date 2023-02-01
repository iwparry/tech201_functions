# Functions

# D R Y - Don't Repeat Yourself
# Keep it simple

# Creating a Function

def print_something():    # arguments aren't completely necessary
    print("Something has been printed")    # what we want our function to do

print_something()   # we call our print_something function

# Creating a Function with an Argument

def print_string(my_string):     # We have defined a function with an argument my_string
    print(my_string)

print_string("This is my string!")   # Will print the string we used as an argument here
print_string("This is my second string!")    # Will print the string we used as an argument here

# In Java:
# public void print_string(String_text)

def greetings(name):
    print(f"Hello my name is {name}")
greetings("Iwan")
greetings("Luke")
greetings("Flo")
greetings("Belal")  # all will print the string embedded in our greetings function but with the names entered as arguments

# The Return statement

def addition(int1, int2):
    return int1 + int2      # must tell Python to return the logic otherwise it doesn't know what to do and we would get None printed to our console

print(addition(1, 2))   # need to print to have it printed to our console

# Default arguments

def addition(int1=2, int2=2):      # we have assigned default values to our arguments
    return int1 + int2

print(addition())    # will run because we have set default values, will print 4 by default
print(addition(1, 2)) # will run but with 1 and 2 as overwritten argument, will print 3
print(addition()) # will print 4

# Multiple Arguments

def multi_args(*multiargs):    # * allows us to input as many arguments as we wish
    print(type(multiargs))     # The arguments should be put into a tuple

    for arg in multiargs:      # Iterates over every argument we've put in the function
        print(arg)             # Prints each individual argument

multi_args(1 , 2, "Three", [1, 2, "Three"], 4, 5, 6)

# Type Hints

def greeting(name: str):     # This allows Python to give a stronger hint that something is wrong
    print("Hello my name is " + name)

greeting(2)    # returns a TypeError, can only concatenate a string - we can see a hint that something is wrong

def division(num1: int = 5, num2: int = 2) -> float:      # we can still introduce default values for arguments
    return num1 / num2

print(division(4, 53)) # prints 0.07547169811320754
print(type(division(4, 54)))  # prints <class 'float'>
print(division()) # prints 2.5 because we've set default arguments

# Functions best practices

## Name functions clearly using lower case and '_' for spaces
## All arguments should be clear in their need and where possible include their expected type
## Remember the return statement - else functions will return 'None'
## Keep functions small - for readability and keep things simple
## Use comments in your functions/methods to give instructions on how to use them
## Consider using type hints to avoid TypeErrors when you run your code.