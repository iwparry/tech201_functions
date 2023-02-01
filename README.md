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
### Default Arguments
Recall how we can create a function in Python that uses arguments, well we can actually set default arguments for our function. What this means is we can create our function with an argument that has a default value set.
```python
def addition(int1=2, int2=2):      # we have assigned default values to our arguments
    return int1 + int2

print(addition())    # will run because we have set default values, will print 4 by default
print(addition(1, 2)) # will run but with 1 and 2 as overwritten argument, will print 3
```
As seen in the above code our function `addition` has been created with arguments `int1` and `int2`, both of which have been assigned a value `2`. Assigning default arguments can be useful because Python does not require us to call these functions with arguments, in fact we can still do so, all Python does is overwrite the default arguments with any arguments we insert when calling our function.
### Multiple Arguments
What's great with functions in Python is that we can create functions with multiple argument, but of course there may be times when we need our function to have a lot of arguments.
Maybe we need to call our function with 8 arguments on one line and with 5 on another, fortunately Python provides a way for us to do this.
```python
def multi_args(*multiargs):    # * allows us to input as many arguments as we wish
    print(type(multiargs))     # The arguments should be put into a tuple

    for arg in multiargs:      # Iterates over every argument we've put in the function
        print(arg)             # Prints each individual argument
```
What we want to note here is `*`, this is what allows us to create a function that will take any number of arguments we wish to give it at any time.
So when we call
```python
multi_args(1 , 2, 3, 4, 5, 6) # prints every argument (1-6) to our console
multi_args(7, 8, 9, 10)  # prints every argument (7-10)
```
The program still runs even though we have called the function twice with a different number of arguments.
### Type Hints
A very useful tool we have for functions in Python are type hints. They are exactly as advertised, they provide hints on what types of values should be used as arguments for any particular function.
```python
def greeting(name: str):     # This allows Python to give a stronger hint that something is wrong
    print("Hello my name is " + name)

greeting(2)    # returns a TypeError, can only concatenate a string - we can see a hint that something is wrong
```
The above shows an example of using a type hint for a function.
We have used the type hint to indicate that this function should only be given a string as an argument.

The type hint can be very useful because when are writing code it isn't always obvious that there may be an issue in our code due to the data types we are using, and if there is an error, we will not know until Python runs the program.

It should be remembered that we only give Python a **hint**, this does not stop the program from being run if an incorrect data type is entered as an argument.
```python
def division(num1: int = 5, num2: int = 2) -> float:      # we can still introduce default values for arguments
    return num1 / num2

print(division(4, 53)) # prints 0.07547169811320754
print(type(division(4, 54)))  # prints <class 'float'>
print(division()) # prints 2.5 because we've set default arguments
```
As we can see here we can still create functions using default arguments and still be able to insert type hints.

### Functions best practices
- Name functions clearly using lower case letters and underscores for spaces
- All arguments should be clear in their need and where possible include their expected type
- Remember the return statement - else functions will return 'None'
- Keep functions small - for readability and keep things simple
- Use comments in your functions/methods to give instructions on how to use them
- Consider using type hints to avoid TypeErrors when you run your code