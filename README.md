# Tech 201 Functions

Functions in Python are a great way for us to write and execute more complex code easier.

### Creating a Function
```Python
def print_something():    # Creates our function
    print("Something has been printed")    # what we want our function to do
```
We create our functions via the keyword `def` which means to define a function, following which we write our function name with a pair of parentheses at the end and a colon.
Similarly to for loops and if statements etc. functions require indentation, in which we write what we want our function to do.
Now that we've defined our function we call our function which is simply.
```python
print_something()   # "Something has been printed" will be printed to our console
```
### Create a Function with Arguments
We can call the function as much as we want, in this case we can have the string `"Something has been printed"` printed into our console anytime we call the function. Although currently there isn't much going on with the function at the moment, the way we've written it, the function is hard coded to simply print the same string over and over for every time its called. Fortunately Python allows us to create functions with arguments!
```python
def print_string(my_string):     # We have defined a function with an argument my_string
    print(my_string)              # To be executed when we call the function 

print_string("This is my string!")   # Will print the string we used as an argument here
print_string("This is my second string!")    # Will print the string we used as an argument here
```
### The Return Statement
The return statement is an important keyword in Python  when using functions, lets look at an example where we make a function without the return statement.
```python
def addition(int1, int2):
     int1 + int2     # what we want our function to do

print(addition(2, 3))
```
This wouldn't work, we would get `None` printed to our console, the reason being that Python doesn't know what to do with `int1 + int2` therefore does nothing with that line of code. For our code to be executed we need to use the return statement as follows
```python
def addition(int1, int2):
     return int1 + int2     # what we want our function to do

print(addition(2, 3))       # prints 5 to our console
```
Note that we still need to use the built-in function `print()` for our results to be printed to the console, with functions we usually call our function inside our print statement.